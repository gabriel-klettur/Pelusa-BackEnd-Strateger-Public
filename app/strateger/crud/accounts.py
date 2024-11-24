# Path: app/strateger/crud/accounts.py

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import SQLAlchemyError
from app.strateger.models.accounts import Account
from fastapi import HTTPException

async def get_all_data_bingx_accounts(db: AsyncSession):
    try:
        result = await db.execute(select(Account))
        return result.scalars().all()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e))
