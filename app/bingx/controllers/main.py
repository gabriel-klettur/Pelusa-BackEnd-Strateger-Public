#Path: app/bingx/controllers/main_controller.py

from fastapi import HTTPException
from app.bingx.services.api_main import get_ticker, get_k_line_data
from app.utils.ip_check import is_ip_allowed
from loguru import logger

async def get_ticker_controller(client_ip: str, symbol: str):
    logger.info(f"Getting data for {symbol} from {client_ip}")

    await is_ip_allowed(client_ip)
    try:
        result = await get_ticker(symbol)
        return result
    except Exception as e:
        logger.error(f"Error fetching ticker information: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

async def get_k_line_controller(client_ip: str, symbol: str, interval: str, limit: str, start_date: str, end_date: str):
    logger.info(f"Fetching K-Line data for {symbol} from {client_ip}")

    await is_ip_allowed(client_ip)
    try:       
        data = await get_k_line_data(symbol, interval, limit, start_date, end_date)
        return data
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
