# Path: app/siteground/database.py

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.config import settings
from loguru import logger
from app.siteground.base import BaseAlarmas, BaseEstrategias, BaseDiary, BasePositions, BaseAccounts, BaseKLineData, BaseOrders

from app.alarms.models import Alarm
from app.strateger.models import accounts, backtesting, diary, orders, positions, strategies

# Configuración de las bases de datos
engine_alarmas = create_async_engine(settings.DATABASE_URL_DESARROLLO_ALARMAS, pool_recycle=3600, pool_pre_ping=True)
SessionLocalAlarmas = sessionmaker(autocommit=False, autoflush=False, bind=engine_alarmas, class_=AsyncSession)

engine_estrategias = create_async_engine(settings.DATABASE_URL_DESARROLLO_ESTRATEGIAS, pool_recycle=3600, pool_pre_ping=True)
SessionLocalEstrategias = sessionmaker(autocommit=False, autoflush=False, bind=engine_estrategias, class_=AsyncSession)

engine_diary = create_async_engine(settings.DATABASE_URL_DESARROLLO_DIARY, pool_recycle=3600, pool_pre_ping=True)
SessionLocalDiary = sessionmaker(autocommit=False, autoflush=False, bind=engine_diary, class_=AsyncSession)

engine_positions = create_async_engine(settings.DATABASE_URL_DESARROLLO_POSITIONS, pool_recycle=3600, pool_pre_ping=True)
SessionLocalPositions = sessionmaker(autocommit=False, autoflush=False, bind=engine_positions, class_=AsyncSession)

engine_accounts = create_async_engine(settings.DATABASE_URL_DESARROLLO_ACCOUNTS, pool_recycle=3600, pool_pre_ping=True)  
SessionLocalAccounts = sessionmaker(autocommit=False, autoflush=False, bind=engine_accounts, class_=AsyncSession) 

engine_kline_data = create_async_engine(settings.DATABASE_URL_DESARROLLO_KLINE_DATA, pool_recycle=3600, pool_pre_ping=True)
SessionLocalKLineData = sessionmaker(autocommit=False, autoflush=False, bind=engine_kline_data, class_=AsyncSession)

engine_orders = create_async_engine(settings.DATABASE_URL_DESARROLLO_ORDERS, pool_recycle=3600, pool_pre_ping=True)
SessionLocalOrders = sessionmaker(autocommit=False, autoflush=False, bind=engine_orders, class_=AsyncSession)

async def get_db_alarmas():
    async with SessionLocalAlarmas() as db:
        yield db

async def get_db_estrategias():
    async with SessionLocalEstrategias() as db:
        yield db
        
async def get_db_diary():
    async with SessionLocalDiary() as db:
        yield db

async def get_db_positions():
    async with SessionLocalPositions() as db:
        yield db

async def get_db_accounts():  
    async with SessionLocalAccounts() as db:
        yield db

async def get_db_kline_data():
    async with SessionLocalKLineData() as db:
        yield db

async def get_db_orders():
    async with SessionLocalOrders() as db:
        yield db

async def init_db_alarmas():
    async with engine_alarmas.begin() as conn:
        await conn.run_sync(BaseAlarmas.metadata.create_all)

async def init_db_estrategias():
    async with engine_estrategias.begin() as conn:
        await conn.run_sync(BaseEstrategias.metadata.create_all)

async def init_db_diary():
    async with engine_diary.begin() as conn:
        await conn.run_sync(BaseDiary.metadata.create_all)

async def init_db_positions():
    async with engine_positions.begin() as conn:        
        await conn.run_sync(BasePositions.metadata.create_all)

async def init_db_accounts():  
    async with engine_accounts.begin() as conn:
        await conn.run_sync(BaseAccounts.metadata.create_all)

async def init_db_kline_data():
    async with engine_kline_data.begin() as conn:
        await conn.run_sync(BaseKLineData.metadata.create_all)

async def init_db_orders():
    async with engine_orders.begin() as conn:
        await conn.run_sync(BaseOrders.metadata.create_all)

async def close_db_connections():
    await engine_alarmas.dispose()
    await engine_estrategias.dispose()
    await engine_diary.dispose()
    await engine_positions.dispose()
    await engine_accounts.dispose()  
    await engine_kline_data.dispose()
    await engine_orders.dispose()
