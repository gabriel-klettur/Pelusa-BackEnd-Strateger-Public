#Path: app/strateger/routes/backtesting.py

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.siteground.database import get_db_estrategias
from app.strateger.schemas.backtesting import BacktestCreate, BacktestUpdate, Backtest
from app.strateger.crud import backtesting as crud_backtesting
from app.klinedata.schemas import Interval
from app.klinedata.services import get_kline_data
from app.siteground.database import get_db_kline_data
from loguru import logger

import pandas as pd
import ta
import numpy as np

router = APIRouter()

@router.post("/create_backtest", response_model=Backtest)
async def create_backtest(backtest: BacktestCreate, db: AsyncSession = Depends(get_db_estrategias)):
    return await crud_backtesting.create_backtest(db, backtest)

def crossover(series1, series2):
    return (series1.shift(1) < series2.shift(1)) & (series1 > series2)

def crossunder(series1, series2):
    return (series1.shift(1) > series2.shift(1)) & (series1 < series2)

@router.get("/stochastic-ta-v1", response_model=dict)
async def get_kline_data_endpoint(
    symbol: str, 
    intervals: Interval, 
    start_date: str,
    end_date: str,
    initial_balance: float = Query(default=10000),
    enable_long: bool = Query(default=True),  
    enable_short: bool = Query(default=True), 
    db: AsyncSession = Depends(get_db_kline_data), 
    limit: int = Query(default=10000, ge=1)
):
    """
    Retrieve kline data for a given symbol and perform stochastic technical analysis.
    
    Parameters:
    - symbol (str): The symbol for which to retrieve kline data.
    - intervals (Interval): The interval of the kline data.
    - start_date (str): The start date of the kline data.
    - end_date (str): The end date of the kline data.
    - db (AsyncSession): The database session to use for retrieving kline data.
    - initial_balance (float): The initial balance for backtesting.
    - enable_long (bool): Whether to enable long operations.
    - enable_short (bool): Whether to enable short operations.
    - limit (int): The maximum number of kline data points to retrieve.
    
    Returns:
    - result (dict): A dictionary containing the results of the backtesting, including various metrics and data.
    """
    try:                
        
        kline_data = await get_kline_data(db, symbol, intervals.value, start_date, end_date, limit)
        
        if not kline_data:
            raise HTTPException(status_code=404, detail="No data found")

        # Convertir los datos a un DataFrame de pandas
        df = pd.DataFrame([data.__dict__ for data in kline_data])                

        # Calcular el indicador estocástico
        df['stoch_k'] = ta.momentum.stoch(df['high'], df['low'], df['close'], window=14, smooth_window=3)
        df['stoch_d'] = ta.momentum.stoch_signal(df['high'], df['low'], df['close'], window=14, smooth_window=3)

        # Inicializa variables para niveles de sobrecompra y sobrevendido
        overbought_level = 79
        oversold_level = 30

        # Condiciones para entrar y salir de una operación
        df['enter_long'] = enable_long and crossover(df['stoch_k'], df['stoch_d']) & (df['stoch_k'] < oversold_level)
        df['exit_long'] = enable_long and crossunder(df['stoch_k'], df['stoch_d']) & (df['stoch_k'] > overbought_level)
        df['enter_short'] = enable_short and crossunder(df['stoch_k'], df['stoch_d']) & (df['stoch_k'] > overbought_level)
        df['exit_short'] = enable_short and crossover(df['stoch_k'], df['stoch_d']) & (df['stoch_k'] < oversold_level)

        # Simular las operaciones
        position = 0        
        balance = initial_balance
        balances = []
        positions = []
        returns = []
        for i in range(0, len(df)):
            if df['enter_long'][i] and position == 0:
                # Enter long position
                position = 1
                entry_price = df['close'][i]
                positions.append(('Long', int(df['time'][i]), float(entry_price)))
                balances.append((balance, int(df['time'][i])))                  
            elif df['exit_long'][i] and position == 1:
                # Exit long position
                position = 0
                exit_price = df['close'][i]
                profit = (exit_price - entry_price) * (balance / entry_price)
                balance += profit
                returns.append(profit / initial_balance)
                balances.append((balance, int(df['time'][i])))                  
                positions.append(('Close Long', int(df['time'][i]), float(exit_price), float(profit)))
            elif df['enter_short'][i] and position == 0:
                # Enter short position
                position = -1
                entry_price = df['close'][i]
                positions.append(('Short', int(df['time'][i]), float(entry_price)))
                balances.append((balance, int(df['time'][i])))                  
            elif df['exit_short'][i] and position == -1:
                # Exit short position
                position = 0
                exit_price = df['close'][i]
                profit = (entry_price - exit_price) * (balance / entry_price)
                balance += profit
                returns.append(profit / initial_balance)
                balances.append((balance, int(df['time'][i])))                  
                positions.append(('Close Short', int(df['time'][i]), float(exit_price), float(profit)))
            else:
                balances.append((balance, int(df['time'][i])))                  

        # Calcular el rendimiento acumulativo de la estrategia
        cumulative_returns = (balance - initial_balance) / initial_balance

        # Calcular métricas adicionales
        balances_array = np.array(balances)
        returns_array = np.array(returns)
        max_drawdown = (np.max(balances_array) - np.min(balances_array)) / np.max(balances_array)
        volatility = np.std(returns_array)
        downside_risk = np.std(returns_array[returns_array < 0])
        sharpe_ratio = np.mean(returns_array) / volatility if volatility != 0 else 0
        sortino_ratio = np.mean(returns_array) / downside_risk if downside_risk != 0 else 0
        win_rate = len([r for r in returns if r > 0]) / len(returns) if len(returns) > 0 else 0
        avg_gain = np.mean([r for r in returns if r > 0]) if len([r for r in returns if r > 0]) > 0 else 0
        avg_loss = np.mean([r for r in returns if r < 0]) if len([r for r in returns if r < 0]) > 0 else 0
        gain_to_loss_ratio = avg_gain / -avg_loss if avg_loss != 0 else 0

        # Convertir todos los valores a tipos serializables por JSON
        positions_serializable = [
            {
                "action": pos[0],
                "time": pos[1],
                "price": pos[2],
                "profit": pos[3] if len(pos) == 4 else None
            } for pos in positions
        ]
        
        balances_serializable = [
            {
                "balance": bal[0],
                "time": bal[1]
            } for bal in balances
        ]

        kline_data_serializable = [
            {
                "symbol": data.symbol,
                "intervals": data.intervals,
                "open": data.open,
                "close": data.close,
                "high": data.high,
                "low": data.low,
                "volume": data.volume,
                "time": data.time,
            } for data in kline_data
        ]

        # Retornar los resultados del backtesting
        result = {
            "initial_balance": initial_balance,
            "final_balance": balance,
            "cumulative_returns": cumulative_returns,            
            "max_drawdown": max_drawdown,
            "volatility": volatility,
            "downside_risk": downside_risk,
            "sharpe_ratio": sharpe_ratio,
            "sortino_ratio": sortino_ratio,
            "win_rate": win_rate,
            "gain_to_loss_ratio": gain_to_loss_ratio,
            "size_kline_data": len(kline_data),
            "balances": balances_serializable,
            "signals": df[['stoch_k', 'stoch_d', 'enter_long', 'exit_long', 'enter_short', 'exit_short', 'time']].to_dict('records'),
            "positions": positions_serializable,
            "kline_data": kline_data_serializable,                                   
        }
        
        return result

    except HTTPException as e:
        logger.error(f"HTTP error fetching kline data: {e.detail}")
        raise
    except Exception as e:
        logger.error(f"Error fetching kline data: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

