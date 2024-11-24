#Path: app/strateger/strateger.py

from fastapi import APIRouter
from app.strateger.routes import strategies , orders, diary, backtesting, positions, accounts

router = APIRouter()

router.include_router(strategies.router, prefix="/strategies", tags=["strategies"])
router.include_router(orders.router, prefix="/orders", tags=["orders"])
router.include_router(diary.router, prefix="/diary", tags=["diary"])
router.include_router(backtesting.router, prefix="/backtesting", tags=["backtesting"])
router.include_router(positions.router, prefix="/positions", tags=["positions"])
router.include_router(accounts.router, prefix="/accounts", tags=["accounts"])
