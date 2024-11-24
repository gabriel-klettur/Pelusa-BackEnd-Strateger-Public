#Path: app/strateger/routes/orders.py


from fastapi import APIRouter, Depends, HTTPException, Request, Query       #FastAPI           
from sqlalchemy.ext.asyncio import AsyncSession                             #Base de datos        
from app.siteground.database import get_db_orders      #Base de datos

from app.strateger.schemas.orders import OrderCreate, OrderResponse                   #Schemas

from app.strateger.crud.orders import get_orders                            #Base de datos

from app.utils.ip_check import is_ip_allowed                                #Seguridad

from loguru import logger                                                   #Logging
from typing import List                                                     #Tipado 

router = APIRouter()

@router.get("/list", response_model=List[OrderResponse])
async def get_orders_endpoint(
    request: Request,
    db: AsyncSession = Depends(get_db_orders),
    limit: int = Query(default=10, ge=1),  # Limit para el número de resultados por página
    offset: int = Query(default=0, ge=0),   # Offset para el desplazamiento
    latest: bool = Query(default=False)     # Parámetro para obtener las últimas alarmas
):
    client_ip = request.client.host
    # Verificar si la IP está permitida
    logger.info(f"Fetching orders from {client_ip}")
    await is_ip_allowed(client_ip)

    try:
        orders = await get_orders(db, limit, offset=offset, latest=latest)
        return [OrderResponse.from_orm(order) for order in orders]
    except Exception as e:
        logger.error(f"Error fetching orders: {e}")
        raise HTTPException(status_code=500, detail="There was an error fetching orders")

