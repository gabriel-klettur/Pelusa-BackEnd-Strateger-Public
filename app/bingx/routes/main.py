#Path: app/bingx/routes/main.py

from fastapi import APIRouter, Request
from app.bingx.controllers.main import get_ticker_controller, get_k_line_controller

router = APIRouter()

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
