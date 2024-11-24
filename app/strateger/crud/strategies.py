# Path: app/strateger/crud/strategies.py

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.strateger.models.strategies import Strategy
from app.strateger.schemas.strategies import StrategyCreate, StrategyUpdate

async def crud_create_strategy(db: AsyncSession, strategy: StrategyCreate):
    db_strategy = Strategy(**strategy.dict())
    db.add(db_strategy)
    await db.commit()
    await db.refresh(db_strategy)
    return db_strategy

async def get_strategy(db: AsyncSession, strategy_id: int):
    result = await db.execute(select(Strategy).where(Strategy.id == strategy_id))
    return result.scalars().first()

async def get_strategies(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(Strategy).offset(skip).limit(limit))
    return result.scalars().all()

async def crud_update_strategy(db: AsyncSession, strategy_id: int, strategy: StrategyUpdate):
    db_strategy = await get_strategy(db, strategy_id)
    if db_strategy:
        for key, value in strategy.dict(exclude_unset=True).items():
            setattr(db_strategy, key, value)
        await db.commit()
        await db.refresh(db_strategy)
    return db_strategy

async def crud_delete_strategy(db: AsyncSession, strategy_id: int):
    db_strategy = await get_strategy(db, strategy_id)
    if db_strategy:
        await db.delete(db_strategy)
        await db.commit()
    return db_strategy

async def get_strategy_by_name_and_ticker(db: AsyncSession, strategy_name: str, ticker: str):
    result = await db.execute(
        select(Strategy).where(Strategy.alarmName == strategy_name).where(Strategy.ticker == ticker)
    )
    return result.scalars().all()
