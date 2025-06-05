# Path: app/alarms/routes.py

from fastapi import APIRouter, Depends, Request, Query, HTTPException       # FastAPI           
from sqlalchemy.ext.asyncio import AsyncSession                             # async SQLAlchemy, necesary for async operations
from app.db.database import get_db                                # database session

from app.alarms.schemas import AlarmResponse                                # Schemas for alarms  
from typing import List                                                     # Typing necessary for response model        

from app.alarms.services import fetch_alarms                                # Services

#from app.utils.ip_check import is_ip_allowed                                # Security

from loguru import logger                                                   # Logging
from datetime import datetime

router = APIRouter()



@router.get("/alarms", 
            response_model=List[AlarmResponse],
            responses={
                500: {"description": "Unexpected server error."},
                520: {"description": "Database query failed."},
                530: {"description": "Unexpected error occurred while fetching alarms."}
            }
)
async def get_alarms_endpoint(    
    request: Request,
    db: AsyncSession = Depends(get_db),
    limit: int = Query(default=10, ge=1, description="The maximum number of alarms to return."),
    offset: int = Query(default=0, ge=0, description="The number of alarms to skip before starting to collect the result set."),
    latest: bool = Query(default=False, description="If True, the alarms will be ordered by their ID in descending order.")
):
    """
    Endpoint to fetch alarms with optional query parameters for pagination and filtering.
    - **Args**:
        - **request (Request)**: The request object containing client information.
        - **db (AsyncSession)**: Database session dependency.
        - **limit (int)**: The maximum number of alarms to return. Default is 10.
        - **offset (int)**: The number of alarms to skip before starting to collect the result set. Default is 0.
        - **latest (bool)**: The alarms will be ordered by their ID in descending order if True. Default is False.
    - **Returns**:
        - **List[AlarmResponse]**: A list of alarm responses.
    - **Raises**:
        - **HTTPException**:                         
            - **500 Internal Server Error**: If an unexpected error occurs while fetching alarms.
    """
    client_ip = request.client.host
    #logger.info(f"Fetching alarms from {client_ip}")
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{current_time}] Fetching alarms from {client_ip}")

    '''
    # **401 Unauthorized: Token missing or invalid**
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        logger.warning(f"Unauthorized access attempt from {client_ip}")
        raise HTTPException(status_code=401, detail="Invalid or missing authentication token.")
    '''

    '''
    # **403 Forbidden: IP not allowed (recheck)**    
    try:
        await is_ip_allowed(client_ip)  # Validación adicional de la IP
    except HTTPException:
        logger.warning(f"IP {client_ip} bypassed middleware but was blocked at endpoint validation.")
        raise HTTPException(status_code=403, detail="Access forbidden: Your IP is not allowed")
    '''


    # **200 OK or 500 Internal Server Error**
    try:
        alarms = await fetch_alarms(limit=limit, offset=offset, latest=latest, db=db)
        return alarms
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"Error fetching alarms: {e}")
        raise HTTPException(status_code=500, detail="Unexpected server error.")
    
