#Path: app/bingx/controllers/usdtm.py

from fastapi import HTTPException
from app.bingx.services.api_usdtm import (
    get_balance_perp,                       #! 1. Query account data
    get_positions,                          #! 2. Query position data
    get_income_acc,                         #! 3. Get Account Profit and Loss Fund Flow
    query_trading_commission_rate,          #! 5. Query trading commission rate
    test_order,                             #TODO 1. Test Order
    make_order,                             #TODO 2. Place order
    place_multiple_orders,                  #TODO 4. Place multiple orders   
    close_all_positions,                    #TODO 5. Close All Positions
    cancel_order,                           #TODO 6. Cancel Order
    cancel_multiple_orders,                 #TODO 7. Cancel multiple orders
    cancel_all_open_orders,                 #TODO 8. Cancel All Open Orders
    query_all_open_orders,                  #TODO 9. Current All Open Orders 
    query_pending_order_status,             #TODO 10. Query pending order status
    query_order_details,                    #TODO 11. Query Order details
    query_margin_type,                      #TODO 12. Query Margin Type
    change_margin_type,                     #TODO 13. Change Margin Type
    query_leverage,                         #TODO 14. Query Leverage
    set_leverage,                           #TODO 15. Set Leverage  
    query_force_orders,                     #TODO 16. User's Force Orders  
    get_all_orders,                         #TODO 17. Query Order history 
    modify_isolated_position_margin,        #TODO 18. Modify Isolated Position Margin               
    query_historical_orders,                #TODO 19. Query historical transaction orders    
    set_position_mode,                      #TODO 20. Set Position Mode
    query_position_mode,                    #TODO 21. Query Position Mode
    cancel_and_replace_order,               #TODO 22. Cancel and Replace Order
    batch_cancel_and_replace_orders,        #TODO 23. Cancel orders in batches and place orders in batches   
    cancel_all_after,                       #TODO 24. Cancel All After
    close_position_by_id,                   #TODO 25. Close position by position ID
    get_full_all_orders,                    #TODO 26. All Orders        
    get_position_margin_ratio,              #TODO 27. Position and Maintenance Margin Ratio
    query_historical_transaction_details,   #TODO 28. Query historical transaction details
    query_position_history                  #TODO 29. Query Position History            
)
from loguru import logger
from app.utils.ip_check import is_ip_allowed

 #! 1. Query account data
async def get_balance_perp_controller(client_ip: str):
    logger.info(f"Fetching balance information from {client_ip}")
    await is_ip_allowed(client_ip)
    try:
        result = await get_balance_perp()
        return result
    except Exception as e:
        logger.error(f"Error fetching balance information: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

#! 2. Query position data
async def get_positions_controller(client_ip: str):
    logger.info(f"Fetching positions information from {client_ip}")
    await is_ip_allowed(client_ip)
    try:
        result = await get_positions()
        return result
    except Exception as e:
        logger.error(f"Error fetching positions: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

#! 3. Get Account Profit and Loss Fund Flow
async def get_income_acc_controller(client_ip: str):
    logger.info(f"Fetching income account information from {client_ip}")
    await is_ip_allowed(client_ip)
    try:
        result = await get_income_acc()
        return result
    except Exception as e:
        logger.error(f"Error fetching income account information: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

#! 5. Query trading commission rate
async def query_trading_commission_rate_controller(client_ip: str):
    logger.info(f"Fetching trading commission rate from {client_ip}")
    await is_ip_allowed(client_ip)
    try:
        result = await query_trading_commission_rate()
        return result
    except Exception as e:
        logger.error(f"Error fetching trading commission rate: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

#TODO 1. Test Order
async def test_order_controller(client_ip: str, symbol: str, side: str, positionSide: str, order_type: str, quantity: float, price: float = None, stopPrice: float = None):
    logger.info(f"Testing order for {symbol} from {client_ip}")
    await is_ip_allowed(client_ip)
    try:
        result = await test_order(symbol, side, positionSide, order_type, quantity, price, stopPrice)
        return result
    except Exception as e:
        logger.error(f"Error testing order: {str(e)}")
        raise HTTPException(status_code=400,  detail=str(e))

#TODO 2. Place order
async def make_order_usdtm_controller(client_ip: str, leverage: int, symbol: str, side: str, positionSide: str, order_type: str, quantity: float):
    logger.info(f"Making order request from {client_ip}")
    await is_ip_allowed(client_ip)
    try:
        result = await make_order(leverage, symbol, side, positionSide, order_type, quantity)
        return result
    except Exception as e:
        logger.error(f"Error making order: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    
#TODO 4. Place multiple orders 
async def place_multiple_orders_controller(client_ip: str, batchOrders: list):
    logger.info(f"Placing multiple orders from {client_ip}")
    await is_ip_allowed(client_ip)
    try:
        result = await place_multiple_orders(batchOrders)
        return result
    except Exception as e:
        logger.error(f"Error placing multiple orders: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    
#TODO 5. Close All Positions
async def close_all_positions_controller(client_ip: str, symbol: str):
    logger.info(f"Closing all positions for {symbol} from {client_ip}")
    await is_ip_allowed(client_ip)
    try:
        result = await close_all_positions(symbol)
        return result
    except Exception as e:
        logger.error(f"Error closing all positions: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

#TODO 6. Cancel Order
async def cancel_order_controller(client_ip: str, orderId: str, symbol: str):
    logger.info(f"Canceling order {orderId} for {symbol} from {client_ip}")
    await is_ip_allowed(client_ip)
    try:
        result = await cancel_order(orderId, symbol)
        return result
    except Exception as e:
        logger.error(f"Error canceling order: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    
#TODO 7. Cancel multiple orders
async def cancel_multiple_orders_controller(client_ip: str, orderIdList: list, symbol: str):
    logger.info(f"Canceling multiple orders for {symbol} from {client_ip}")
    await is_ip_allowed(client_ip)
    try:
        result = await cancel_multiple_orders(orderIdList, symbol)
        return result
    except Exception as e:
        logger.error(f"Error canceling multiple orders: {str(e)}")
        raise HTTPException(status_code=400,  detail=str(e))


#TODO 8. Cancel All Open Orders
async def cancel_all_open_orders_controller(client_ip: str, symbol: str):
    logger.info(f"Canceling all open orders for {symbol} from {client_ip}")
    await is_ip_allowed(client_ip)
    try:
        result = await cancel_all_open_orders(symbol)
        return result
    except Exception as e:
        logger.error(f"Error canceling all open orders: {str(e)}")
        raise HTTPException(status_code=400,  detail=str(e))

#TODO 9. Current All Open Orders 
async def query_all_open_orders_controller(client_ip: str, symbol: str):
    logger.info(f"Fetching all open orders for {symbol} from {client_ip}")
    await is_ip_allowed(client_ip)
    try:
        result = await query_all_open_orders(symbol)
        return result
    except Exception as e:
        logger.error(f"Error fetching all open orders: {str(e)}")
        raise HTTPException(status_code=400,  detail=str(e))

#TODO 10. Query pending order status
async def query_pending_order_status_controller(client_ip: str, orderId: str, symbol: str):
    logger.info(f"Fetching pending order status for {symbol} from {client_ip}")
    await is_ip_allowed(client_ip)
    try:
        result = await query_pending_order_status(orderId, symbol)
        return result
    except Exception as e:
        logger.error(f"Error fetching pending order status: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

#TODO 11. Query Order details
async def query_order_details_controller(client_ip: str, orderId: str, symbol: str):
    logger.info(f"Fetching order details for {symbol} from {client_ip}")
    await is_ip_allowed(client_ip)
    try:
        result = await query_order_details(orderId, symbol)
        return result
    except Exception as e:
        logger.error(f"Error fetching order details: {str(e)}")
        raise HTTPException(status_code=400,  detail=str(e))

#TODO 12. Query Margin Type
async def query_margin_type_controller(client_ip: str, symbol: str):
    logger.info(f"Fetching margin type for {symbol} from {client_ip}")
    await is_ip_allowed(client_ip)
    try:
        result = await query_margin_type(symbol)
        return result
    except Exception as e:
        logger.error(f"Error fetching margin type: {str(e)}")
        raise HTTPException(status_code=400,  detail=str(e))

#TODO 13. Change Margin Type
async def charge_margin_type_controller(client_ip: str, symbol: str, marginType: str):
    logger.info(f"Changing margin type for {symbol} from {client_ip}")
    await is_ip_allowed(client_ip)
    try:
        result = await change_margin_type(symbol, marginType)
        return result
    except Exception as e:
        logger.error(f"Error changing margin type: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

#TODO 14. Query Leverage
async def query_leverage_controller(client_ip: str, symbol: str):
    logger.info(f"Fetching leverage for {symbol} from {client_ip}")
    await is_ip_allowed(client_ip)
    try:
        result = await query_leverage(symbol)
        return result
    except Exception as e:
        logger.error(f"Error fetching leverage: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

#TODO 15. Set Leverage  
async def set_leverage_controller(client_ip: str, symbol: str, side: str, leverage: int):
    logger.info(f"Setting leverage for {symbol} from {client_ip}")
    await is_ip_allowed(client_ip)
    try:
        result = await set_leverage(symbol, side, leverage)
        return result
    except Exception as e:
        logger.error(f"Error setting leverage: {str(e)}")
        raise HTTPException(status_code=400,  detail=str(e))
    
#TODO 16. User's Force Orders 
async def query_force_orders_controller(client_ip: str, symbol: str = None, startTime: int = None, endTime: int = None, limit: int = 100):
    logger.info(f"Fetching forced liquidation orders for {symbol} from {client_ip}")
    await is_ip_allowed(client_ip)
    try:
        result = await query_force_orders(symbol, startTime, endTime, limit)
        return result
    except Exception as e:
        logger.error(f"Error fetching forced liquidation orders: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

#TODO 17. Query Order history 
async def get_all_orders_controller(client_ip: str, limit: int, offset: int):
    logger.info(f"Fetching historical orders information from {client_ip}")
    await is_ip_allowed(client_ip)
    try:
        result = await get_all_orders(limit, offset)
        logger.debug(f"result: {result}")
        return result
    except Exception as e:
        logger.error(f"Error fetching all orders: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

#TODO 18. Modify Isolated Position Margin
async def modify_isolated_position_margin_controller(client_ip: str, symbol: str, amount: float, positionSide: str):
    logger.info(f"Modifying isolated position margin for {symbol} from {client_ip}")
    await is_ip_allowed(client_ip)
    try:
        result = await modify_isolated_position_margin(symbol, amount, positionSide)
        return result
    except Exception as e:
        logger.error(f"Error modifying isolated position margin: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

#TODO 19. Query historical transaction orders 
async def query_historical_orders_controller(client_ip: str, symbol: str, startTime: int, endTime: int, limit: int):
    logger.info(f"Fetching historical orders for {symbol} from {client_ip}")
    await is_ip_allowed(client_ip)
    try:
        result = await query_historical_orders(symbol, startTime, endTime, limit)
        return result
    except Exception as e:
        logger.error(f"Error fetching historical orders: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

    
#TODO 20. Set Position Mode
async def set_position_mode_controller(client_ip: str, dualSidePosition: bool):
    logger.info(f"Setting position mode from {client_ip}")
    await is_ip_allowed(client_ip)
    try:
        result = await set_position_mode(dualSidePosition)
        return result
    except Exception as e:
        logger.error(f"Error setting position mode: {str(e)}")
        raise HTTPException(status_code=400,  detail=str(e))

 #TODO 21. Query Position Mode
async def query_position_mode_controller(client_ip: str):
    logger.info(f"Fetching position mode from {client_ip}")
    await is_ip_allowed(client_ip)
    try:
        result = await query_position_mode()
        return result
    except Exception as e:
        logger.error(f"Error fetching position mode: {str(e)}")
        raise HTTPException(status_code=400,  detail=str(e))

#TODO 22. Cancel and Replace Order
async def cancel_and_replace_order_controller(client_ip: str, cancelOrderId: str, symbol: str, side: str, positionSide: str, order_type: str, quantity: float, price: float = None):
    logger.info(f"Canceling and replacing order {cancelOrderId} for {symbol} from {client_ip}")
    await is_ip_allowed(client_ip)
    try:
        result = await cancel_and_replace_order(cancelOrderId, symbol, side, positionSide, order_type, quantity, price)
        return result
    except Exception as e:
        logger.error(f"Error canceling and replacing order: {str(e)}")
        raise HTTPException(status_code=400,  detail=str(e))

#TODO 23. Cancel orders in batches and place orders in batches 
async def batch_cancel_and_replace_orders_controller(client_ip: str, batchOrders: list):
    logger.info(f"Batch canceling and replacing orders from {client_ip}")
    await is_ip_allowed(client_ip)
    try:
        result = await batch_cancel_and_replace_orders(batchOrders)
        return result
    except Exception as e:
        logger.error(f"Error batch canceling and replacing orders: {str(e)}")
        raise HTTPException(status_code=400,  detail=str(e))

#TODO 24. Cancel All After
async def cancel_all_after_controller(client_ip: str, timeout: int):
    logger.info(f"Canceling all orders after {timeout}ms from {client_ip}")
    await is_ip_allowed(client_ip)
    try:
        result = await cancel_all_after(timeout)
        return result
    except Exception as e:
        logger.error(f"Error canceling all orders after timeout: {str(e)}")
        raise HTTPException(status_code=400,  detail=str(e))

#TODO 25. Close position by position ID
async def close_position_by_id_controller(client_ip: str, positionId: str):
    logger.info(f"Closing position by ID {positionId} from {client_ip}")
    await is_ip_allowed(client_ip)
    try:
        result = await close_position_by_id(positionId)
        return result
    except Exception as e:
        logger.error(f"Error closing position by ID: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

#TODO 26. All Orders        
async def get_full_all_orders_controller(client_ip: str, limit: int):
    logger.info(f"Fetching historical orders information from {client_ip}")
    await is_ip_allowed(client_ip)
    try:
        result = await get_full_all_orders(limit)
        logger.debug(f"result: {result}")
        return result
    except Exception as e:
        logger.error(f"Error fetching historical orders: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

#TODO 27. Position and Maintenance Margin Ratio
async def get_position_margin_ratio_controller(client_ip: str, symbol: str):
    logger.info(f"Fetching position margin ratio for {symbol} from {client_ip}")
    await is_ip_allowed(client_ip)
    try:
        result = await get_position_margin_ratio(symbol)
        return result
    except Exception as e:
        logger.error(f"Error fetching position margin ratio: {str(e)}")
        raise HTTPException(status_code=400,  detail=str(e))

#TODO 28. Query historical transaction details
async def query_historical_transaction_details_controller(client_ip: str, symbol: str, startTime: int, endTime: int, limit: int = 100):
    logger.info(f"Fetching historical transaction details for {symbol} from {client_ip}")
    await is_ip_allowed(client_ip)
    try:
        result = await query_historical_transaction_details(symbol, startTime, endTime, limit)
        return result
    except Exception as e:
        logger.error(f"Error fetching historical transaction details: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

#TODO 29. Query Position History
async def query_position_history_controller(client_ip: str, symbol: str, startTime: int, endTime: int, limit: int = 20):
    logger.info(f"Fetching position history for {symbol} from {client_ip}")
    await is_ip_allowed(client_ip)
    try:
        result = await query_position_history(symbol, startTime, endTime, limit)
        return result
    except Exception as e:
        logger.error(f"Error fetching position history: {str(e)}")
        raise HTTPException(status_code=400,  detail=str(e))


