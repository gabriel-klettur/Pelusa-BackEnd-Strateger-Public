#Path: app/alarms/services.py

from sqlalchemy.orm import Session
from fastapi import HTTPException
from loguru import logger
from app.alarms.repositories import get_alarms
from app.alarms.schemas import AlarmResponse                            #Schemas   


async def fetch_alarms(limit: int, offset: int, latest: bool, db: Session):
    """
    Fetch alarms from the database with given parameters.

    Args:
        limit (int): The maximum number of alarms to fetch.
        offset (int): The number of alarms to skip before starting to fetch.
        latest (bool): If True, the alarms will be ordered by their ID in descending order.
        db (Session): The database session to use for fetching alarms.

    Returns:
        List[AlarmResponse]: A list of validated alarm responses.

    Raises:
        HTTPException: If there is an error fetching the alarms.
    """
    try:
        alarms = await get_alarms(db, limit=limit, offset=offset, latest=latest)
        return [AlarmResponse.model_validate(alarm) for alarm in alarms]
    except Exception as e:
        logger.error(f"Error fetching alarms: {e}")
        raise HTTPException(status_code=500, detail="There was an error fetching the alarms")