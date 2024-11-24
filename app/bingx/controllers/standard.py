#Path: app/bingx/controllers/standard.py

from app.utils.ip_check import is_ip_allowed
from fastapi import HTTPException
from loguru import logger

from app.bingx.services.api_standard import (
    query_all_positions,                #TODO 1. Query All Positions
    query_historical_orders,            #TODO 2. Query Historical Orders
    query_standard_contract_balance      #TODO 3. Query Standard Contract Balance
)

#TODO 1. Query All Positions
async def query_all_positions_controller(client_ip: str):
    """
    Queries all positions for standard contracts.
    """

    logger.info(f"Fetching all positions from {client_ip}")

    # Verificar si la IP está permitida
    await is_ip_allowed(client_ip)
    
    try:
        result = await query_all_positions()
        return result
    except Exception as e:
        logger.error(f"Error fetching all positions: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

#TODO 2. Query Historical Orders
async def query_historical_orders_controller(
    client_ip: str, 
    symbol: str = 'BTC-USDT', 
    orderId: int = None, 
    startTime: int = None, 
    endTime: int = None, 
    limit: int = None):
    """
    Queries historical orders for a specific symbol in standard contracts.
    """

    logger.info(f"Fetching historical orders from {client_ip}")

    # Verificar si la IP está permitida
    await is_ip_allowed(client_ip)
    
    try:
        result = await query_historical_orders(symbol, orderId, startTime, endTime, limit)
        return result
    except Exception as e:
        logger.error(f"Error fetching historical orders: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    
#TODO 3. Query Standard Contract Balance
async def query_standard_contract_balance_controller(client_ip: str):
    """
    Queries the balance for standard contracts.
    """

    logger.info(f"Fetching standard contract balance from {client_ip}")

    # Verificar si la IP está permitida
    await is_ip_allowed(client_ip)
    
    try:
        result = await query_standard_contract_balance()
        return result
    except Exception as e:
        logger.error(f"Error fetching standard contract balance: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e) )