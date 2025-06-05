from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.config import settings
from loguru import logger
from app.db.base import (BaseAlarmas, BaseEstrategias, BaseDiary,
                         BasePositions, BaseAccounts, BaseKLineData,
                         BaseOrders)
import ssl

# Un único engine y session
db_url = settings.DATABASE_URL
if db_url.startswith("postgres://"):
    db_url = db_url.replace("postgres://", "postgresql+asyncpg://", 1)
# Remover sslmode del query string
if "?" in db_url:
    base_url, query = db_url.split("?", 1)
    params = [p for p in query.split("&") if not p.startswith("sslmode=")]
    db_url = f"{base_url}?{'&'.join(params)}" if params else base_url
# Crear contexto SSL
ssl_ctx = ssl.create_default_context()
engine = create_async_engine(
    db_url,
    pool_recycle=3600,
    pool_pre_ping=True,
    connect_args={"ssl": ssl_ctx}
)
SessionLocal = sessionmaker(autocommit=False,
                           autoflush=False,
                           bind=engine,
                           class_=AsyncSession)

async def get_db():
    async with SessionLocal() as db:
        yield db

async def init_db():
    async with engine.begin() as conn:
        # crear todas las tablas
        for Base in (BaseAlarmas, BaseEstrategias, BaseDiary,
                     BasePositions, BaseAccounts,
                     BaseKLineData, BaseOrders):
            await conn.run_sync(Base.metadata.create_all)

async def close_db():
    await engine.dispose()