# Path: app/alarms/crud.py

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.alarms.models import Alarm

async def get_alarms(db: AsyncSession, limit: int = 10, offset: int = 0, latest: bool = False):
    query = select(Alarm).offset(offset).limit(limit)
    if latest:
        query = query.order_by(Alarm.id.desc())
    result = await db.execute(query)
    return result.scalars().all()

