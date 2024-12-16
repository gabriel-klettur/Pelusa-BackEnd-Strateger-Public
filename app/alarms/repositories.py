# Path: app/alarms/crud.py

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.alarms.models import Alarm
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from loguru import logger

async def get_alarms(db: AsyncSession, limit: int = 10, offset: int = 0, latest: bool = False):
    """
    Fetches a list of alarms from the database.

    Args:
        db (AsyncSession): The database session to use for the query.
        limit (int, optional): The maximum number of alarms to return. Defaults to 10.
        offset (int, optional): The number of alarms to skip before starting to collect the result set. Defaults to 0.
        latest (bool, optional): If True, the alarms will be ordered by their ID in descending order. Defaults to False.

    Returns:
        List[Alarm]: A list of Alarm objects fetched from the database.

    Raises:
        HTTPException: If there is an error querying the database.
    """
    try:
        query = select(Alarm).offset(offset).limit(limit)
        if latest:
            query = query.order_by(Alarm.id.desc())

        # Ejecutar la consulta
        result = await db.execute(query)
        return result.scalars().all()
    
    except SQLAlchemyError as e:
        # Manejo de errores específicos de SQLAlchemy
        logger.error(f"Database query failed: {e}")
        raise HTTPException(status_code=520, detail="Database query failed")
    
    except Exception as e:
        # Manejo de errores generales
        logger.error(f"Unexpected error fetching alarms: {e}")
        raise HTTPException(status_code=530, detail="Unexpected error occurred while fetching alarms")

