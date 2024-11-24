from fastapi import APIRouter, Request
from typing import Optional

from app.bingx.controllers.standard import (
    query_all_positions_controller,                 #TODO 1. Query All Positions
    query_historical_orders_controller,             #TODO 2. Query Historical Orders
    query_standard_contract_balance_controller      #TODO 3. Query Standard Contract Balance
)

router = APIRouter()

#TODO 1. Query All Positions
@router.get('/query-all-positions')
async def query_all_positions_endpoint(request: Request):
    """
    Queries all positions for standard contracts.
    """
    client_ip = request.client.host
    return await query_all_positions_controller(client_ip)

#TODO 2. Query Historical Orders
@router.get('/query-historical-orders')
async def query_historical_orders_endpoint(
    request: Request, 
    symbol: str = 'BTC-USDT', 
    orderId: Optional[int] = None, 
    startTime: Optional[int] = None, 
    endTime: Optional[int]= None, 
    limit: Optional[int] = None
):
    """
    Queries historical orders for a specific symbol in standard contracts.
    """
    client_ip = request.client.host
    return await query_historical_orders_controller(client_ip, symbol, orderId, startTime, endTime, limit)

#TODO 3. Query Standard Contract Balance
@router.get('/query-standard-contract-balance')
async def query_standard_contract_balance_endpoint(request: Request):
    """
    Queries the balance for standard contracts.
    """
    client_ip = request.client.host
    return await query_standard_contract_balance_controller(client_ip)
