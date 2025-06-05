#Path: app/server/routes.py

from fastapi import APIRouter, Request, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import text
from datetime import datetime
from app.utils.ip_check import is_ip_allowed
from app.db.database import get_db
from loguru import logger

router = APIRouter()


@router.get("/status-server", tags=["health"])
async def health_check(request: Request, db: AsyncSession = Depends(get_db)):
    
    client_ip = request.client.host
    logger.info(f"Alarm received from {client_ip}")

    # Verificar si la IP está permitida
    await is_ip_allowed(client_ip)
    
    try:
        # Verificar conexión con la base de datos de alarmas
        await db.execute(text("SELECT 1"))
        

        # Obtener la hora actual
        current_time = datetime.now()
        time_str = current_time.strftime("%Y-%m-%d %H:%M:%S")

        return JSONResponse(status_code=200, content={"status": "ok", "time": time_str})
    except Exception as e:
        logger.error(f"Health check failed: {e}")
        return JSONResponse(status_code=500, content={"status": "error", "detail": str(e)})