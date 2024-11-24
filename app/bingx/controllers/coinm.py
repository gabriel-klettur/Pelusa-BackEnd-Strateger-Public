# Path: app/bingx/controllers/coinm_controller.py

from app.bingx.services.api_coinm import (
    make_order_coinm,               #TODO 1. Place Order
    query_commission_rate,          #TODO 2. Query Commission Rate
    query_leverage,                 #TODO 3. Query Leverage
    modify_leverage,                #TODO 4. Modify Leverage
    cancel_all_open_orders,         #TODO 5. Cancel All Open Orders
    close_all_positions_coinm,      #TODO 6. Close All Positions in Bulk
    get_positions_perp_coinm,       #TODO 7. Query warehouse
    get_balance_perp_coinm,         #TODO 8. Query Account Assets
    query_force_orders,             #TODO 9. Query Force Orders
    query_historical_orders,        #TODO 10. Query Order Trade Detail by Id
    cancel_order,                   #TODO 11. Cancel Order
    query_all_open_orders,          #TODO 12. Query All Open Orders
    query_order,                    #TODO 13. Query Order
    query_history_orders,           #TODO 14. Query History Orders
    query_margin_type,              #TODO 15. Query Margin Type
    set_margin_type,                #TODO 16. Set Margin Type
    adjust_isolated_position_margin #TODO 17. Adjust Isolated Position Margin    
)

from app.utils.ip_check import is_ip_allowed
from fastapi import HTTPException
from loguru import logger

#TODO 1.Place Order
async def make_order_coinm_controller(leverage, symbol, side, positionSide, order_type, quantity, client_ip: str):
    """
    Place an order in the Coin-M Perp Futures market.
    """

    logger.info(f"Placing order from {client_ip}")

    # Verificar si la IP está permitida
    await is_ip_allowed(client_ip)

    try:
        result = await make_order_coinm(leverage, symbol, side, positionSide, order_type, quantity)
        return result
    except Exception as e:
        logger.error(f"Error placing order: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

#TODO 2. Query Commission Rate
async def query_commission_rate_controller(client_ip: str):
    """
    Get the commission rate for the current user in Coin-M futures.
    """

    logger.info(f"Fetching commission rate from {client_ip}")

    # Verificar si la IP está permitida
    await is_ip_allowed(client_ip)
    
    try:
        result = await query_commission_rate()
        return result
    except Exception as e:
        logger.error(f"Error fetching commission rate: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

#TODO 3. Query Leverage
async def query_leverage_controller(client_ip: str, symbol: str):
    """
    Get the leverage for the current user in Coin-M futures.
    """

    logger.info(f"Fetching leverage from {client_ip}")

    # Verificar si la IP está permitida
    await is_ip_allowed(client_ip)
    
    try:
        result = await query_leverage(symbol)
        return result
    except Exception as e:
        logger.error(f"Error fetching leverage: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    
#TODO 4. Modify Leverage
async def modify_leverage_controller(client_ip: str, symbol: str, side: str, leverage: int):
    """
    Modify the leverage for the current user in Coin-M futures.
    """

    logger.info(f"Modifying leverage from {client_ip}")

    # Verificar si la IP está permitida
    await is_ip_allowed(client_ip)
    
    try:
        result = await modify_leverage(symbol, side, leverage)
        return result
    except Exception as e:
        logger.error(f"Error modifying leverage: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

#TODO 5. Cancel All Open Orders
async def cancel_all_open_orders_controller(client_ip: str, symbol: str):
    """
    Cancel all open orders for the current user in Coin-M futures.
    """

    logger.info(f"Canceling all open orders from {client_ip}")

    # Verificar si la IP está permitida
    await is_ip_allowed(client_ip)
    
    try:
        result = await cancel_all_open_orders(symbol)
        return result
    except Exception as e:
        logger.error(f"Error canceling all open orders: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

#TODO 6. Close All Positions in Bulk
async def close_all_positions_coinm_controller(client_ip: str, symbol: str):
    """
    Close all positions for the current user in Coin-M futures.
    """

    logger.info(f"Closing all positions from {client_ip}")

    # Verificar si la IP está permitida
    await is_ip_allowed(client_ip)
    
    try:
        result = await close_all_positions_coinm(symbol)
        return result
    except Exception as e:
        logger.error(f"Error closing all positions: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

#TODO 7. Query warehouse
async def get_positions_perp_coinm_controller(client_ip: str):
    """
    Get user's coin-m account positions information.
    """

    logger.info(f"Fetching positions from {client_ip}")

    # Verificar si la IP está permitida
    await is_ip_allowed(client_ip)
    
    try:
        result = await get_positions_perp_coinm()
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

#TODO 8. Query Account Assets
async def get_balance_controller(client_ip: str):
    """
    Get asset information of user‘s PERP COIN-M Account.
    """

    logger.info(f"Fetching balance from {client_ip}")

    # Verificar si la IP está permitida
    await is_ip_allowed(client_ip)
    
    try:
        result = await get_balance_perp_coinm()
        return result
    except Exception as e:
        logger.error(f"Error fetching PERP COIN-M balance: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

#TODO 9. Query Force Orders
async def query_force_orders_controller(client_ip: str, symbol: str, startTime: int, endTime: int, limit: int):
    """
    Get forced liquidation orders in Coin-M futures.
    """

    logger.info(f"Fetching force orders from {client_ip}")

    # Verificar si la IP está permitida
    await is_ip_allowed(client_ip)
    
    try:
        result = await query_force_orders(symbol, startTime, endTime, limit)
        return result
    except Exception as e:
        logger.error(f"Error fetching force orders: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

#TODO 10. Query Order Trade Detail
async def query_historical_orders_controller(client_ip: str, orderId: str, pageIndex: int, pageSize: int):
    """
    Get historical transaction orders for a specific symbol in Coin-M futures.
    """

    logger.info(f"Fetching historical orders from {client_ip}")

    # Verificar si la IP está permitida
    await is_ip_allowed(client_ip)
    
    try:
        result = await query_historical_orders(orderId, pageIndex, pageSize)
        return result
    except Exception as e:
        logger.error(f"Error fetching historical orders: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    
#TODO 11. Cancel Order
async def cancel_order_controller(client_ip: str, symbol: str, orderId: str):
    """
    Cancel an order in Coin-M futures.
    """

    logger.info(f"Canceling order from {client_ip}")

    # Verificar si la IP está permitida
    await is_ip_allowed(client_ip)
    
    try:
        result = await cancel_order(symbol, orderId)
        return result
    except Exception as e:
        logger.error(f"Error canceling order: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

#TODO 12. Query All Open Orders
async def query_all_open_orders_controller(client_ip: str, symbol: str):
    """
    Get all current pending orders for the current user in Coin-M futures.
    """

    logger.info(f"Fetching all open orders from {client_ip}")

    # Verificar si la IP está permitida
    await is_ip_allowed(client_ip)
    
    try:
        result = await query_all_open_orders(symbol)
        return result
    except Exception as e:
        logger.error(f"Error fetching all open orders: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

#TODO 13. Query Order
async def query_order_controller(client_ip: str, symbol: str, orderId: str):
    """
    Get a specific order for the current user in Coin-M futures.
    """

    logger.info(f"Fetching order from {client_ip}")

    # Verificar si la IP está permitida
    await is_ip_allowed(client_ip)
    
    try:
        result = await query_order(symbol, orderId)
        return result
    except Exception as e:
        logger.error(f"Error fetching order: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

#TODO 14. Query History Orders
async def query_history_orders_controller(client_ip: str, symbol: str, orderId: int, startTime: int, endTime: int, limit: int):
    """
    Get the user's historical orders in Coin-M futures.
    """

    logger.info(f"Fetching history orders from {client_ip}")

    # Verificar si la IP está permitida
    await is_ip_allowed(client_ip)
    
    try:
        result = await query_history_orders(symbol, orderId, startTime, endTime, limit)
        return result
    except Exception as e:
        logger.error(f"Error fetching history orders: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

#TODO 15. Query Margin Type
async def query_margin_type_controller(client_ip: str, symbol: str):
    """
    Get the margin type for a specific symbol in Coin-M futures.
    """

    logger.info(f"Fetching margin type from {client_ip}")

    # Verificar si la IP está permitida
    await is_ip_allowed(client_ip)
    
    try:
        result = await query_margin_type(symbol)
        return result
    except Exception as e:
        logger.error(f"Error fetching margin type: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

#TODO 16. Set Margin Type
async def set_margin_type_controller(client_ip: str, symbol: str, marginType: str):
    """
    Set the margin type for a specific symbol in Coin-M futures.
    """

    logger.info(f"Setting margin type from {client_ip}")

    # Verificar si la IP está permitida
    await is_ip_allowed(client_ip)
    
    try:
        result = await set_margin_type(symbol, marginType)
        return result
    except Exception as e:
        logger.error(f"Error setting margin type: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

#TODO 17. Adjust Isolated Position Margin
async def adjust_isolated_position_margin_controller(client_ip: str, symbol: str, positionSide: str, amount: float):
    """
    Adjust the isolated position margin for a specific symbol in Coin-M futures.
    """

    logger.info(f"Adjusting isolated position margin from {client_ip}")

    # Verificar si la IP está permitida
    await is_ip_allowed(client_ip)
    
    try:
        result = await adjust_isolated_position_margin(symbol, positionSide, amount)
        return result
    except Exception as e:
        logger.error(f"Error adjusting isolated position margin: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

