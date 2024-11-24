#Path: app/klinedata/crud.py

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from app.klinedata.models import KlineData
from app.klinedata.schemas import KlineDataCreate
from fastapi import HTTPException
from loguru import logger
import datetime
import time

async def save_kline_data(db: AsyncSession, kline_data: KlineDataCreate):
    try:
        db_kline_data = KlineData(**kline_data.model_dump())
        db.add(db_kline_data)
        await db.commit()
        await db.refresh(db_kline_data)
        return db_kline_data
    except IntegrityError:
        await db.rollback()
        logger.warning(f"K-line data already exists: {kline_data}")
        return None
    except SQLAlchemyError as e:
        await db.rollback()
        raise HTTPException(status_code=500, detail=f"Error saving K-line data: {str(e)}")



async def get_kline_data(db: AsyncSession, symbol: str, intervals: str, start_date: str, end_date: str, limit: int = 10000):
    MAX_LIMIT = 10000  # Limite máximo permitido
    try:
        # Convertir las fechas de 'YYYY-MM-DD HH:MM:SS' a timestamp en milisegundos
        start_timestamp = int(datetime.datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S').timestamp() * 1000)
        end_timestamp = int(datetime.datetime.strptime(end_date, '%Y-%m-%d %H:%M:%S').timestamp() * 1000)
        
        # Asegurarse de que el límite no sea mayor que el límite máximo permitido
        effective_limit = min(limit, MAX_LIMIT)
        
        query = (
            select(KlineData)
            .where(
                KlineData.symbol == symbol,
                KlineData.intervals == intervals,
                KlineData.time >= start_timestamp,
                KlineData.time <= end_timestamp
            )            
            .limit(effective_limit)
        )
        result = await db.execute(query)
        return result.scalars().all()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving K-line data: {str(e)}")
    

