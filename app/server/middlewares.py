# Path: app/server/middlewares.py

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response, JSONResponse
from starlette.types import ASGIApp
from app.config import settings
from loguru import logger

from datetime import datetime

import json

'''
class AllowedIPsMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Extraer la IP de la cabecera X-Forwarded-For, si existe
        forwarded_for = request.headers.get("X-Forwarded-For")
        client_ip = forwarded_for if forwarded_for else request.client.host

        # Verificar si la IP está en la lista permitida
        if client_ip not in settings.ALLOWED_IPS:
            logger.warning(f"Unauthorized IP {client_ip} attempted to access the service")
            return JSONResponse({"detail": "Access forbidden: Your IP is not allowed"}, status_code=403)

        response = await call_next(request)
        return response
'''

class InvalidRequestLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            response = await call_next(request)
            return response
        except Exception as exc:
            client_ip = request.client.host
            requested_url = str(request.url)
            user_agent = request.headers.get('user-agent', 'unknown')
            logger.warning(
                f"Invalid HTTP request received from IP: {client_ip}, URL: {requested_url}, "
                f"User-Agent: {user_agent}, Error: {exc}"
            )
            return JSONResponse(content={"detail": "Invalid request"}, status_code=400)

class LogResponseMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)

        # Log the response details
        client_ip = request.client.host
        method = request.method
        url = str(request.url)
        status_code = response.status_code

        #logger.info(f"Response to {client_ip} - {method} {url} - Status: {status_code}")
        #current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        #print(f"[{current_time}] Response to {client_ip} - {method} {url} - Status: {status_code}")

        return response
