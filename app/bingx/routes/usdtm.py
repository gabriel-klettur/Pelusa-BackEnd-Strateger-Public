#Path: app/bingx/routes/usdtm.py

from fastapi import APIRouter, Request
from app.bingx.controllers.usdtm import (
    get_balance_perp_controller,                    #! 1. Query account data                
    get_positions_controller,                       #! 2. Query position data
    get_income_acc_controller,                      #! 3. Get Account Profit and Loss Fund Flow
    query_trading_commission_rate_controller,       #! 5. Query trading commission rate
    test_order_controller,                          #TODO 1. Test Order
    make_order_usdtm_controller,                    #TODO 2. Place order
    place_multiple_orders_controller,               #TODO 4. Place multiple orders
    close_all_positions_controller,                 #TODO 5. Close all positions
    cancel_order_controller,                        #TODO 6. Cancel order
    cancel_multiple_orders_controller,              #TODO 7. Cancel multiple orders
    cancel_all_open_orders_controller,              #TODO 8. Cancel all open orders
    query_all_open_orders_controller,               #TODO 9. Query Current all open orders
    query_pending_order_status_controller,          #TODO 10. Query pending order status
    query_order_details_controller,                 #TODO 11. Query order details
    query_margin_type_controller,                   #TODO 12. Query margin type
    charge_margin_type_controller,                  #TODO 13. Change margin type
    query_leverage_controller,                      #TODO 14. Query leverage
    set_leverage_controller,                        #TODO 15. Set leverage
    query_force_orders_controller,                  #TODO 16. Query force orders
    get_all_orders_controller,                      #TODO 17. Query order history 
    modify_isolated_position_margin_controller,     #TODO 18. Modify isolated position margin
    query_historical_orders_controller,             #TODO 19. Query historical transaction orders
    set_position_mode_controller,                   #TODO 20. Set position mode
    query_position_mode_controller,                 #TODO 21. Query position mode
    cancel_and_replace_order_controller,            #TODO 22. Cancel and replace order
    batch_cancel_and_replace_orders_controller,     #TODO 23. Cancel orders in batches and place orders in batches
    cancel_all_after_controller,                    #TODO 24. Cancel all after
    close_position_by_id_controller,                #TODO 25. Close position by position ID
    get_full_all_orders_controller,                 #TODO 26. All orders                                            IN: ORDERS
    get_position_margin_ratio_controller,           #TODO 27. Position and maintenance margin ratio
    query_historical_transaction_details_controller,    #TODO 28. Query historical transaction details
    query_position_history_controller               #TODO 29. Query position history
)

router = APIRouter()

#! 1. Query account data                
@router.get('/get-balance-perp-usdtm')
async def get_balance_perp_endpoint(request: Request):
    client_ip = request.client.host    
    return await get_balance_perp_controller(client_ip)

#! 2. Query position data
@router.get('/get-positions-usdtm')
async def get_positions_endpoint(request: Request):
    client_ip = request.client.host    
    return await get_positions_controller(client_ip)

#! 3. Get Account Profit and Loss Fund Flow
@router.get('/get-income-acc')
async def get_income_acc_endpoint(request: Request):
    client_ip = request.client.host    
    return await get_income_acc_controller(client_ip)

#! 5. Query trading commission rate
@router.get('/query-trading-commission-rate')
async def query_trading_commission_rate_endpoint(request: Request):
    client_ip = request.client.host    
    return await query_trading_commission_rate_controller(client_ip)

#TODO 1. Test Order
@router.post('/place-demo-order')
async def place_demo_order_endpoint(request: Request, symbol: str, side: str, positionSide: str, order_type: str, quantity: float, price: float = None, stopPrice: float = None):
    client_ip = request.client.host
    return await test_order_controller(client_ip, symbol, side, positionSide, order_type, quantity, price, stopPrice)

#TODO 2. Place order
@router.post('/make-order-usdtm')
async def make_order_usdtm_endpoint(request: Request, leverage: int, symbol: str, side: str, positionSide: str, order_type: str, quantity: float):
    client_ip = request.client.host    
    return await make_order_usdtm_controller(client_ip, leverage, symbol, side, positionSide, order_type, quantity)

#TODO 4. Place multiple orders
@router.post('/place-multiple-orders')
async def place_multiple_orders_endpoint(request: Request, batchOrders: list):
    client_ip = request.client.host
    return await place_multiple_orders_controller(client_ip, batchOrders)

#TODO 5. Close all positions
@router.post('/close-all-positions')
async def close_all_positions_endpoint(request: Request, symbol: str):
    client_ip = request.client.host
    return await close_all_positions_controller(client_ip, symbol)

#TODO 6. Cancel order
@router.delete('/cancel-order')
async def cancel_order_endpoint(request: Request, orderId: str, symbol: str):
    client_ip = request.client.host
    return await cancel_order_controller(client_ip, orderId, symbol)

#TODO 7. Cancel multiple orders
@router.delete('/cancel-multiple-orders')
async def cancel_multiple_orders_endpoint(request: Request, orderIdList: list, symbol: str):
    client_ip = request.client.host
    return await cancel_multiple_orders_controller(client_ip, orderIdList, symbol)

#TODO 8. Cancel all open orders
@router.delete('/cancel-all-open-orders')
async def cancel_all_open_orders_endpoint(request: Request, symbol: str):
    client_ip = request.client.host
    return await cancel_all_open_orders_controller(client_ip, symbol)

#TODO 9. Query Current all open orders
@router.get('/query-all-open-orders')
async def query_all_open_orders_endpoint(request: Request, symbol: str):
    client_ip = request.client.host
    return await query_all_open_orders_controller(client_ip, symbol)

#TODO 10. Query pending order status
@router.get('/query-pending-order-status')
async def query_pending_order_status_endpoint(request: Request, orderId: str, symbol: str):
    client_ip = request.client.host
    return await query_pending_order_status_controller(client_ip, orderId, symbol)

#TODO 11. Query order details
@router.get('/query-order-details')
async def query_order_details_endpoint(request: Request, orderId: str, symbol: str):
    client_ip = request.client.host
    return await query_order_details_controller(client_ip, orderId, symbol)

#TODO 12. Query margin type
@router.get('/query-margin-type')
async def query_margin_type_endpoint(request: Request, symbol: str):
    client_ip = request.client.host
    return await query_margin_type_controller(client_ip, symbol)

#TODO 13. Change margin type
@router.get('/change-margin-type')
async def change_margin_type_endpoint(request: Request, symbol: str, marginType: str):
    client_ip = request.client.host
    return await charge_margin_type_controller(client_ip, symbol, marginType)

#TODO 14. Query leverage
@router.get('/query-leverage')
async def query_leverage_endpoint(request: Request, symbol: str):
    client_ip = request.client.host
    return await query_leverage_controller(client_ip, symbol)

#TODO 15. Set leverage
@router.post('/set-leverage')
async def set_leverage_endpoint(request: Request, symbol: str, side: str, leverage: int):
    client_ip = request.client.host
    return await set_leverage_controller(client_ip, symbol, side, leverage)

#TODO 16. Query force orders
@router.get('/query-force-orders')
async def query_force_orders_endpoint(request: Request, symbol: str = None, startTime: int = None, endTime: int = None, limit: int = 100):
    client_ip = request.client.host
    return await query_force_orders_controller(client_ip, symbol, startTime, endTime, limit)

#TODO 17. Query order history
@router.get('/get-all-orders')
async def get_all_orders_endpoint(request: Request, limit: int = 500, offset: int = 0):
    client_ip = request.client.host    
    return await get_all_orders_controller(client_ip, limit, offset)

#TODO 18. Modify isolated position margin
@router.post('/modify-isolated-position-margin')
async def modify_isolated_position_margin_endpoint(request: Request, symbol: str, amount: float, positionSide: str):
    client_ip = request.client.host
    return await modify_isolated_position_margin_controller(client_ip, symbol, amount, positionSide)

#TODO 19. Query historical transaction orders
@router.get('/query-historical-orders')
async def query_historical_orders_endpoint(request: Request, symbol: str, startTime: int, endTime: int, limit: int = 500):
    client_ip = request.client.host
    return await query_historical_orders_controller(client_ip, symbol, startTime, endTime, limit)

#TODO 20. Set position mode
@router.post('/set-position-mode')
async def set_position_mode_endpoint(request: Request, dualSidePosition: bool):
    client_ip = request.client.host
    return await set_position_mode_controller(client_ip, dualSidePosition)

#TODO 21. Query position mode
@router.get('/query-position-mode')
async def query_position_mode_endpoint(request: Request):
    client_ip = request.client.host
    return await query_position_mode_controller(client_ip)

#TODO 22. Cancel and replace order
@router.get('/cancel-and-replace-order')
async def cancel_and_replace_order_endpoint(request: Request, orderId: str, symbol: str, side: str, positionSide: str, order_type: str, quantity: float, price: float = None, stopPrice: float = None):
    client_ip = request.client.host
    return await cancel_and_replace_order_controller(client_ip, orderId, symbol, side, positionSide, order_type, quantity, price, stopPrice)

#TODO 23. Cancel orders in batches and place orders in batches
@router.post('/batch-cancel-and-replace-orders')
async def batch_cancel_and_replace_orders_endpoint(request: Request, batchOrders: list):
    client_ip = request.client.host
    return await batch_cancel_and_replace_orders_controller(client_ip, batchOrders)

#TODO 24. Cancel all after
@router.post('/cancel-all-after')
async def cancel_all_after_endpoint(request: Request, timeout: int):
    client_ip = request.client.host
    return await cancel_all_after_controller(client_ip, timeout)

#TODO 25. Close position by position ID
@router.post('/close-position-by-id')
async def close_position_by_id_endpoint(request: Request, positionId: str):
    client_ip = request.client.host
    return await close_position_by_id_controller(client_ip, positionId)

#TODO 26. All orders
@router.get('/get-all-full-orders')
async def get_full_all_orders_endpoint(request: Request, limit: int = 500):
    client_ip = request.client.host    
    return await get_full_all_orders_controller(client_ip, limit)

#TODO 27. Position and maintenance margin ratio
@router.get('/query-position-margin-ratio')
async def query_position_margin_ratio_endpoint(request: Request, symbol: str):
    client_ip = request.client.host
    return await get_position_margin_ratio_controller(client_ip, symbol)

#TODO 28. Query historical transaction details
@router.get('/query-historical-transaction-details')
async def query_historical_transaction_details_endpoint(request: Request, symbol: str, startTime: int, endTime: int, limit: int = 100):
    client_ip = request.client.host
    return await query_historical_transaction_details_controller(client_ip, symbol, startTime, endTime, limit)

#TODO 29. Query position history
@router.get('/query-position-history')
async def query_position_history_endpoint(request: Request, symbol: str, startTime: int, endTime: int, limit: int = 20):
    client_ip = request.client.host
    return await query_position_history_controller(client_ip, symbol, startTime, endTime, limit)

