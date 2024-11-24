from fastapi import APIRouter, Depends, HTTPException, Request, Query
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.siteground.database import get_db_kline_data
from app.klinedata.schemas import KlineDataCreate, Interval
from app.klinedata.services import save_kline_data, get_kline_data
from app.utils.ip_check import is_ip_allowed
from loguru import logger

from app.bingx.services.api_main import get_k_line_data
from datetime import datetime, timedelta

from typing import List, Dict, Any

import json

router = APIRouter()

@router.post("/create_kline_data", response_model=KlineDataCreate)
async def create_kline_data(kline_data: KlineDataCreate, db: AsyncSession = Depends(get_db_kline_data)):
    try:
        saved_kline_data = await save_kline_data(db, kline_data)
        return saved_kline_data
    except HTTPException as e:
        logger.error(f"HTTP error saving kline data: {e.detail}")
        raise
    except Exception as e:
        logger.error(f"Error saving kline data: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get('/fill-kline-data-historical')
async def fill_kline_data_historical(
    request: Request,
    symbol: str,
    interval: str,
    start_date: str,
    end_date: str,
    db: AsyncSession = Depends(get_db_kline_data)
):
    client_ip = request.client.host
    
    logger.debug(f"Fetching historical K-Line data for {symbol} from {client_ip}")

    await is_ip_allowed(client_ip)
    
    try:
        start_time = datetime.strptime(start_date, '%Y-%m-%d')
        end_time = datetime.strptime(end_date, '%Y-%m-%d')

        total_units = calculate_units_between_dates(start_date, end_date, interval)
        logger.debug(f"Total units between {start_date} and {end_date}: {total_units}")

        max_units_per_request = 1000
        unit_mapping = {
            '1m': timedelta(minutes=1),
            '5m': timedelta(minutes=5),
            '15m': timedelta(minutes=15),
            '30m': timedelta(minutes=30),
            '1h': timedelta(hours=1),
            '4h': timedelta(hours=4),
            'D': timedelta(days=1),
            'W': timedelta(weeks=1),
            'M': timedelta(days=30),  # Aproximación de un mes
        }
        
        if interval not in unit_mapping:
            raise HTTPException(status_code=400, detail="Invalid interval")

        current_start_time = start_time
        while current_start_time < end_time:
            logger.debug(f"Fetching data from {current_start_time} to {current_start_time + unit_mapping[interval] * max_units_per_request}")
            current_end_time = current_start_time + unit_mapping[interval] * max_units_per_request
            if current_end_time > end_time:
                current_end_time = end_time

            kline_data = await get_k_line_data(
                symbol, interval, max_units_per_request, str(current_start_time), str(current_end_time)
            )

            if isinstance(kline_data, str):
                try:
                    kline_data = json.loads(kline_data)
                except json.JSONDecodeError as e:
                    logger.error(f"Error decoding JSON: {e}")
                    raise HTTPException(status_code=400, detail="Invalid JSON response")

            if 'data' not in kline_data or not isinstance(kline_data['data'], list):
                raise HTTPException(status_code=400, detail="Invalid response structure")

            for data in kline_data['data']:
                logger.debug(f"Processing data: {data}")
                kline_record = KlineDataCreate(
                    symbol=symbol,
                    open=float(data.get('open', 0)),
                    close=float(data.get('close', 0)),
                    high=float(data.get('high', 0)),
                    low=float(data.get('low', 0)),
                    volume=float(data.get('volume', 0)),
                    time=int(data.get('time', 0)),
                    intervals=interval
                )
                saved_data = await save_kline_data(db, kline_record)
                if saved_data is None:
                    logger.debug(f"Duplicate data found, skipping insertion: {kline_record}")
                else:
                    logger.debug(f"Saving K-Line data: {kline_record}")

            current_start_time = current_end_time

        return {"message": "Historical K-Line data saved successfully."}
    except Exception as e:
        logger.error(f"Error fetching or saving historical K-Line data: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

def calculate_units_between_dates(start_date: str, end_date: str, interval: str) -> int:
    start_datetime = datetime.strptime(start_date, '%Y-%m-%d')
    end_datetime = datetime.strptime(end_date, '%Y-%m-%d')
    time_difference = end_datetime - start_datetime

    interval_mapping = {
        '1m': 1,
        '5m': 5,
        '15m': 15,
        '30m': 30,
        '1h': 60,
        '4h': 240,
        'D': 1440,
        'W': 10080,
        'M': 43200,
    }

    if interval not in interval_mapping:
        raise ValueError("Invalid interval")

    minutes_per_unit = interval_mapping[interval]
    total_minutes = time_difference.days * 24 * 60 + time_difference.seconds // 60
    return total_minutes // minutes_per_unit



@router.get("/get-kline-data", response_model=List[Dict[str, Any]])
async def get_kline_data_endpoint(
    symbol: str, 
    intervals: Interval, 
    start_date: str,
    end_date: str,
    db: AsyncSession = Depends(get_db_kline_data), 
    limit: int = Query(default=10000, ge=1)
):
    try:
        kline_data = await get_kline_data(db, symbol, intervals.value, start_date, end_date, limit)
        
        if not kline_data:
            raise HTTPException(status_code=404, detail="No data found")
        
        # Convertir cada instancia de kline_data a un diccionario
        kline_data_serializable = [data.__dict__ for data in kline_data]

        # Eliminar la clave '_sa_instance_state' que añade SQLAlchemy
        for data in kline_data_serializable:
            data.pop('_sa_instance_state', None)
        
        return kline_data_serializable

    except HTTPException as e:
        logger.error(f"HTTP error fetching kline data: {e.detail}")
        raise
    except Exception as e:
        logger.error(f"Error fetching kline data: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
