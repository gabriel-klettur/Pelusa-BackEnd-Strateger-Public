# Path: app/bingx/routes/coinm.py

from fastapi import APIRouter, Request, Body
from typing import Optional

from app.bingx.controllers.coinm import (
    make_order_coinm_controller,                #TODO 1. Place Order
    query_commission_rate_controller,           #TODO 2. Query Commission Rate
    query_leverage_controller,                  #TODO 3. Query Leverage
    modify_leverage_controller,                 #TODO 4. Modify Leverage
    cancel_all_open_orders_controller,          #TODO 5. Cancel All Open Orders
    close_all_positions_coinm_controller,       #TODO 6. Close All Positions
    get_positions_perp_coinm_controller,        #TODO 7. Query warehouse
    get_balance_controller,                     #TODO 8. Query Account Assets    
    query_force_orders_controller,              #TODO 9. Query Force Orders
    query_historical_orders_controller,         #TODO 10. Query Order Trade Detail by Id
    cancel_order_controller,                    #TODO 11. Cancel Order
    query_all_open_orders_controller,           #TODO 12. Query All Open Orders
    query_order_controller,                     #TODO 13. Query Order
    query_history_orders_controller,            #TODO 14. Query History Orders                 IN: 'Orders'
    query_margin_type_controller,               #TODO 15. Query Margin Type
    set_margin_type_controller,                 #TODO 16. Set Margin Type
    adjust_isolated_position_margin_controller  #TODO 17. Adjust Isolated Position Margin
)

router = APIRouter()

#TODO 1. Place Order
@router.post('/make-order-coinm')
async def make_order_endpoint(
    request: Request, 
    leverage: int = Body(...), 
    symbol: str = Body(...), 
    side: str = Body(...), 
    positionSide: str = Body(...), 
    order_type: str = Body(...), 
    quantity: int = Body(...)       #IMPORTANT: Quantity is an integer, its the number of items to buy/sell
):
    """
    Place an order in the Coin-M Perp Futures market.
    """
    client_ip = request.client.host
    return await make_order_coinm_controller(leverage, symbol, side, positionSide, order_type, quantity, client_ip)


#TODO 2. Query Commission Rate
@router.get('/query-commission-rate')
async def query_commission_rate_endpoint(request: Request):
    """
    Get the commission rate for the current user in Coin-M futures.
    """
    client_ip = request.client.host
    return await query_commission_rate_controller(client_ip)

#TODO 3. Query Leverage
@router.get('/query-leverage')
async def query_leverage_endpoint(request: Request, symbol: str):
    """
    Get the leverage for the current user in Coin-M futures.
    """
    client_ip = request.client.host
    return await query_leverage_controller(client_ip, symbol)

#TODO 4. Modify Leverage
@router.post('/modify-leverage')
async def modify_leverage_endpoint(
    request: Request, 
    symbol: str = Body(...), 
    side: str = Body(...), 
    leverage: int = Body(...)
):
    """
    Modify the leverage for the current user in Coin-M futures.
    """
    client_ip = request.client.host
    return await modify_leverage_controller(client_ip, symbol, side, leverage)

#TODO 5. Cancel All Open Orders
@router.post('/cancel-all-open-orders')
async def cancel_all_open_orders_endpoint(request: Request, symbol: str):
    """
    Cancel all open orders for the current user in Coin-M futures.
    """
    client_ip = request.client.host
    return await cancel_all_open_orders_controller(symbol, client_ip)

#TODO 6. Close All Positions in Bulk
@router.post('/close-all-positions-bulk-coinm')
async def close_all_positions_coinm_endpoint(request: Request, symbol: str):
    """
    Close all positions in bulk for the current user in Coin-M futures.
    """
    client_ip = request.client.host
    return await close_all_positions_coinm_controller(symbol, client_ip)    

#TODO 7. Query warehouse
@router.get('/get-positions-coinm')
async def get_positions_endpoint(request: Request):
    """
    Get user's coin-m account positions information.
    """
    client_ip = request.client.host
    return await get_positions_perp_coinm_controller(client_ip)

#TODO 8. Query Account Assets
@router.get('/get-balance-perp-coinm')
async def get_balance_endpoint(request: Request):
    """
    Get asset information of user‘s PERP COIN-M Account.
    """
    client_ip = request.client.host
    return await get_balance_controller(client_ip)

#TODO 9. Query Force Orders
@router.get('/query-force-orders')
async def query_force_orders_endpoint(request: Request, symbol: str, startTime: Optional[int], endTime: int, limit: int):
    """
    Query force orders for the current user in Coin-M futures.
    """
    client_ip = request.client.host
    return await query_force_orders_controller(symbol, startTime, endTime, limit, client_ip)

#TODO 10. Query Order Trade Detail by Id
@router.get('/query-historical-orders')
async def query_historical_orders_endpoint(request: Request, orderId: str, pageIndex: Optional[int], pageSize: Optional[int]):
    """
    Query historical orders for the current user in Coin-M futures.
    """
    client_ip = request.client.host
    return await query_historical_orders_controller(client_ip, orderId, pageIndex, pageSize)

#TODO 11. Cancel Order
@router.delete('/cancel-order')
async def cancel_order_endpoint(request: Request, orderId: str, symbol: str):
    """
    Cancel an order for the current user in Coin-M futures.
    """
    client_ip = request.client.host
    return await cancel_order_controller(orderId, symbol, client_ip)

#TODO 12. Query All Open Orders
@router.get('/query-all-open-orders')
async def query_all_open_orders_endpoint(request: Request, symbol: str):
    """
    Query all open orders for the current user in Coin-M futures.
    """
    client_ip = request.client.host
    return await query_all_open_orders_controller(client_ip, symbol)

#TODO 13. Query Order
@router.get('/query-order')
async def query_order_endpoint(request: Request, orderId: str, symbol: str):
    """
    Query an order for the current user in Coin-M futures.
    """
    client_ip = request.client.host
    return await query_order_controller(orderId, symbol, client_ip)


# TODO 14. Query History Orders
@router.get('/query-history-orders')
async def query_history_orders_endpoint(
    request: Request, 
    symbol: Optional[str] = None, 
    orderId: Optional[int] = None, 
    startTime: Optional[int] = None, 
    endTime: Optional[int] = None, 
    limit: int = 500  # Valor predeterminado para `limit`
):
    """
    Query historical orders for the current user in Coin-M futures.
    """    
    client_ip = request.client.host
    return await query_history_orders_controller(client_ip, symbol, orderId, startTime, endTime, limit)

#TODO 15. Query Margin Type
@router.get('/query-margin-type')
async def query_margin_type_endpoint(request: Request, symbol: str):
    """
    Query the margin type for the current user in Coin-M futures.
    """
    client_ip = request.client.host
    return await query_margin_type_controller(symbol, client_ip)

#TODO 16. Set Margin Type
@router.post('/set-margin-type')
async def set_margin_type_endpoint(request: Request, symbol: str, marginType: str):
    """
    Set the margin type for the current user in Coin-M futures.
    """
    client_ip = request.client.host
    return await set_margin_type_controller(symbol, marginType, client_ip)

#TODO 17. Adjust Isolated Position Margin
@router.post('/adjust-isolated-position-margin')
async def adjust_isolated_position_margin_endpoint(request: Request, symbol: str, positionSide: str, amount: float):
    """
    Adjust the isolated position margin for the current user in Coin-M futures.
    """
    client_ip = request.client.host
    return await adjust_isolated_position_margin_controller(symbol, positionSide, amount, client_ip)

