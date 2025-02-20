#Path: app/bingx/routes/main.py

from fastapi import APIRouter, Request, WebSocket, WebSocketDisconnect
from app.bingx.controllers.main import get_ticker_controller, get_k_line_controller
import asyncio
import json

router = APIRouter()

active_connections = []

@router.get('/get-ticker')
async def get_ticker_endpoint(request: Request, symbol: str):
    """
    Get ticker information for a specific symbol.
    """
    client_ip = request.client.host    
    return await get_ticker_controller(client_ip, symbol)

@router.get('/get-k-line-data')
async def get_k_line_data_endpoint(request: Request, symbol: str, interval: str, limit: str, start_date: str, end_date: str):
    """
    Get K-Line data for a specific symbol.
    """
    client_ip = request.client.host    
    return await get_k_line_controller(client_ip, symbol, interval, limit, start_date, end_date)

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()  # Acepta la conexión del cliente
    
    # Extrae la IP del cliente
    client_ip = websocket.client.host
    
    while True:
        try:
            data = await websocket.receive_text()  # Recibe el mensaje del cliente
            # Convierte el mensaje JSON en un diccionario de Python
            params = json.loads(data)
            print("Datos recibidos:", params)
            
            # Extrae los parámetros enviados por el cliente
            symbol = params.get("symbol")
            interval = params.get("interval")
            limit = params.get("limit")
            start_date = params.get("start_date")
            end_date = params.get("end_date")
            
            # Llama a la función get_k_line_controller con los parámetros extraídos
            response = await get_k_line_controller(client_ip, symbol, interval, limit, start_date, end_date)
            
            # Envía una respuesta de confirmación al cliente
            await websocket.send_json({"mensaje": "Datos recibidos", "datos": response})
        except Exception as e:
            print("Error o desconexión:", e)
            break

