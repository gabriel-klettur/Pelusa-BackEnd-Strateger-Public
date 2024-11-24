#Path: app/utils/ip_check.py

from fastapi import HTTPException
from loguru import logger
from app.config import settings

async def is_ip_allowed(client_ip: str) -> bool:
    if client_ip in settings.BLOCKED_IPS:
        logger.warning(f"Blocked IP {client_ip} attempted to access the service")
        raise HTTPException(status_code=403, detail="Access forbidden")
    
    if settings.ALLOWED_IPS and client_ip not in settings.ALLOWED_IPS:
        logger.warning(f"Unauthorized IP {client_ip} attempted to access the service")
        raise HTTPException(status_code=403, detail="Access forbidden")
    
    return True
