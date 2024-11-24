# Path: app/strateger/utils/tasks.py
import asyncio
from app.bingx.services.api_usdtm import get_positions as get_positions_usdtm, get_balance_perp as get_balance_perp_usdtm
from app.bingx.services.api_coinm import get_positions_perp_coinm, get_balance_perp_coinm
from app.bingx.services.api_spot import get_balance_spot
from app.siteground.database import get_db_positions, get_db_accounts
from app.strateger.models.positions import Position
from app.strateger.models.accounts import Account
from sqlalchemy.ext.asyncio import AsyncSession
from loguru import logger
import json
from datetime import datetime
import os

def get_fecha_hora_actual():
    """Retorna la fecha y hora actual en formato MM:HH DD/MM/YYYY"""
    ahora = datetime.now()
    return ahora.strftime("%H:%M %d/%m/%Y")

async def fetch_and_save_positions(db: AsyncSession, get_positions_func, account_name: str, account_type: str):
    try:
        response = await get_positions_func()
        response_json = json.loads(response)
        positions_data = response_json.get('data', [])

        for position in positions_data:
            db_position = Position(
                account_name=account_name,
                account_type=account_type,
                symbol=position['symbol'],
                positionId=position['positionId'],
                positionSide=position['positionSide'],
                isolated=position['isolated'],
                positionAmt=position['positionAmt'],
                availableAmt=position['availableAmt'],
                unrealizedProfit=position['unrealizedProfit'],
                realisedProfit=position.get('realisedProfit', '0.0'),  # Valor por defecto
                initialMargin=position['initialMargin'],
                margin=position.get('margin', '0.0'),  # Valor por defecto
                avgPrice=position['avgPrice'],
                liquidationPrice=position['liquidationPrice'],
                leverage=position['leverage'],
                positionValue=position.get('positionValue', '0.0'),  # Valor por defecto
                markPrice=position['markPrice'],
                riskRate=position['riskRate'],
                maxMarginReduction=position['maxMarginReduction'],
                pnlRatio=position.get('pnlRatio', '0.0'),  # Valor por defecto
                updateTime=position['updateTime'],
                dateTime=get_fecha_hora_actual()  # Nueva columna con la fecha y hora actual
            )
            async with db.begin():
                db.add(db_position)
        await db.commit()
        logger.info(f"Successfully fetched and saved {account_type} positions.")
    except json.JSONDecodeError as e:
        logger.error(f"JSON decode error: {e}")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")

async def fetch_and_save_balance(db: AsyncSession, get_balance_func, account_name: str, account_type: str):
    try:
        response = await get_balance_func()
        logger.debug(f"Response: {response}")
        response_json = json.loads(response)
        logger.debug(f"Parsed JSON: {response_json}")

        # Diferenciar entre los tipos de respuestas
        if account_type == "Perp USDT-M":
            balances_data = [response_json['data']['balance']]
        elif account_type == "Perp COIN-M":
            balances_data = response_json['data']
        elif account_type == "Spot":
            balances_data = response_json['data']['balances']
        else:
            logger.error(f"Unknown account type: {account_type}")
            return

        for balance in balances_data:
            if account_type == "Spot":
                balance_amount = float(balance['free'])
            else:
                balance_amount = float(balance['balance'])

            # Ignorar balances de 0
            if balance_amount == 0:
                continue

            db_balance = Account(
                accountName=account_name,
                accountType=account_type,
                asset=balance['asset'],
                balance=balance_amount,
                equity=float(balance.get('equity', 0.0)),
                unrealizedProfit=float(balance.get('unrealizedProfit', 0.0)),
                realizedProfit=float(balance.get('realizedProfit', 0.0)),
                dateTime=datetime.utcnow(),
                availableMargin=float(balance.get('availableMargin', 0.0)),
                usedMargin=float(balance.get('usedMargin', 0.0)),
            )
            async with db.begin():
                db.add(db_balance)
        await db.commit()
        logger.info(f"Successfully fetched and saved {account_type} balance.")
    except json.JSONDecodeError as e:
        logger.error(f"JSON decode error: {e}")
    except KeyError as e:
        logger.error(f"Key error: {e}")
    except TypeError as e:
        logger.error(f"Type error: {e}")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")

async def background_tasks():
    interval = int(os.getenv('FETCH_INTERVAL', 3600))  # Fetch interval in seconds, default is 1 hour
    while True:
        try:
            async for db in get_db_positions():
                await fetch_and_save_positions(db, get_positions_usdtm, "Main Account", "Perp USDT-M")
                await fetch_and_save_positions(db, get_positions_perp_coinm, "Main Account", "Perp COIN-M")
            async for db in get_db_accounts():
                await fetch_and_save_balance(db, get_balance_perp_usdtm, "Main Account", "Perp USDT-M")
                await fetch_and_save_balance(db, get_balance_perp_coinm, "Main Account", "Perp COIN-M")
                await fetch_and_save_balance(db, get_balance_spot, "Main Account", "Spot")
            logger.info("Sleeping for {} seconds.".format(interval))
            await asyncio.sleep(interval)
        except Exception as e:
            logger.error(f"Unexpected error in background_tasks: {e}")
