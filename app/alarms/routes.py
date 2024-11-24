# Path: app/alarms/routes.py

from fastapi import APIRouter, Depends, HTTPException, Request, Query       #FastAPI           
from sqlalchemy.ext.asyncio import AsyncSession                             #Base de datos        
from app.siteground.database import get_db_alarmas, get_db_estrategias      #Base de datos

from app.alarms.schemas import AlarmCreate, AlarmResponse                   #Schemas   
from app.alarms.repositories import get_alarms                          #Base de datos

from app.utils.ip_check import is_ip_allowed                                #Seguridad
from app.alarms.utils import convierte_temporalidad                         #Utilidades

from loguru import logger                                                   #Logging
from typing import List                                                     #Tipado         
from app.strateger.utils.orders import crear_operacion                      #Operaciones                        

router = APIRouter()

@router.get("/alarms", response_model=List[AlarmResponse])
async def get_alarms_endpoint(
    request: Request,
    db: AsyncSession = Depends(get_db_alarmas),
    limit: int = Query(default=10, ge=1),  # Limit para el número de resultados por página
    offset: int = Query(default=0, ge=0),   # Offset para el desplazamiento
    latest: bool = Query(default=False)     # Parámetro para obtener las últimas alarmas
):
    client_ip = request.client.host
    # Verificar si la IP está permitida
    logger.info(f"Fetching alarms from {client_ip}")
    await is_ip_allowed(client_ip)
    
    try:
        alarms = await get_alarms(db, limit=limit, offset=offset, latest=latest)
        return [AlarmResponse.from_orm(alarm) for alarm in alarms]
    except Exception as e:
        logger.error(f"Error fetching alarms: {e}")
        raise HTTPException(status_code=500, detail="There was an error fetching the alarms")