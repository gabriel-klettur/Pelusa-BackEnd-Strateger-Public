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

async def get_latest_alarm_with_entry(db: AsyncSession, strategy_name: str, ticker: str, entry_order: str, temporalidad: str):
    result = await db.execute(
        select(Alarm)
        .where(Alarm.Strategy == strategy_name)
        .where(Alarm.Ticker == ticker)
        .where(Alarm.Order == entry_order)
        .where(Alarm.Temporalidad == temporalidad)
        .order_by(Alarm.id.desc())
        .limit(1)
    )
    return result.scalars().first()
