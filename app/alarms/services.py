#Path: app/alarms/controllers.py

from sqlalchemy.orm import Session
from fastapi import HTTPException
from loguru import logger
from app.alarms.repositories import get_alarms
from app.alarms.schemas import AlarmResponse                            #Schemas   


async def fetch_alarms(limit: int, offset: int, latest: bool, db: Session):
    try:
        alarms = await get_alarms(db, limit=limit, offset=offset, latest=latest)
        return [AlarmResponse.model_validate(alarm) for alarm in alarms]
    except Exception as e:
        logger.error(f"Error fetching alarms: {e}")
        raise HTTPException(status_code=500, detail="There was an error fetching the alarms")