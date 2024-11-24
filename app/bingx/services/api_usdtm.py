#Path: app/bingx/api/api_usdtm.py

# Description: USDT-M Perp Futures functions for BingX exchange
import time
from .api_utils import send_request, parse_param

#!--------------------------------------  Account Endpoints  ---------------------------------------!#

#! 1. Query account data
async def get_balance_perp():
    """
    Retrieves the balance for the USDTM perpetual contract.
    """
    path = '/openApi/swap/v3/user/balance'
    method = "GET"
    paramsMap = {
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})

#! 2. Query position data
async def get_positions():
    """
    Fetches the user's positions for USDT-M perpetual futures.
    """
    path = '/openApi/swap/v2/user/positions'
    method = "GET"
    paramsMap = {
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})

#! 3. Get Account Profit and Loss Fund Flow
async def get_income_acc():
    path = '/openApi/swap/v2/user/income'
    method = "GET"
    paramsMap = {
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})

#! 4. Export Fund Flow
async def export_fund_flow(symbol=None, incomeType=None, startTime=None, endTime=None, limit=200):
    """
    Exports the fund flow of the perpetual account. The response will be an Excel file.
    """
    path = '/openApi/swap/v2/user/income/export'
    method = "GET"
    paramsMap = {
        "symbol": symbol,
        "incomeType": incomeType,
        "startTime": startTime,
        "endTime": endTime,
        "limit": str(limit),        
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})

#! 5. Query Trading Commission Rate
async def query_trading_commission_rate():
    """
    Obtains the trading commission rate for the current user.
    """
    path = '/openApi/swap/v2/user/commissionRate'
    method = "GET"
    paramsMap = {        
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})

#TODO -------------------------------------  Trades Endpoints  -------------------------------------------!#

#TODO 1. Test Order
async def test_order(symbol, side, positionSide, order_type, quantity, price=None, stopPrice=None):
    """
    Tests an order. This order will not be placed in the real market, only test results will be returned.
    """
    path = '/openApi/swap/v2/trade/order/test'
    method = "POST"
    paramsMap = {
        "symbol": symbol,
        "side": side,
        "positionSide": positionSide,
        "type": order_type,
        "quantity": quantity,
        "timestamp": str(int(time.time() * 1000))
    }

    if price:
        paramsMap["price"] = price
    if stopPrice:
        paramsMap["stopPrice"] = stopPrice

    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})

#TODO 2. Place order
async def make_order(leverage, symbol, side, positionSide, order_type, quantity):
    path = '/openApi/swap/v2/trade/order'
    method = "POST"
    paramsMap = {
        "leverage": leverage,
        "symbol": symbol,
        "side": side,
        "positionSide": positionSide,
        "type": order_type,
        "quantity": quantity,
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})

#TODO 3. Place order in demo trading
async def place_demo_order(symbol, side, positionSide, order_type, quantity, price=None, stopPrice=None):
    """
    Places a demo order on the specified symbol contract.
    """
    path = '/openApi/swap/v2/trade/order/test'
    method = "POST"
    paramsMap = {
        "symbol": symbol,
        "side": side,
        "positionSide": positionSide,
        "type": order_type,
        "quantity": quantity,
        "timestamp": str(int(time.time() * 1000))
    }
    
    # Add price fields if required
    if price:
        paramsMap["price"] = price
    if stopPrice:
        paramsMap["stopPrice"] = stopPrice

    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})


#TODO 4. Place multiple orders
async def place_multiple_orders(batchOrders):
    """
    Places multiple orders simultaneously.
    """
    path = '/openApi/swap/v2/trade/batchOrders'
    method = "POST"
    paramsMap = {
        "batchOrders": batchOrders,
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})

#TODO 5. Close All Positions
async def close_all_positions(symbol):
    path = '/openApi/swap/v2/trade/closeAllPositions'
    method = "POST"
    paramsMap = {
        "symbol": symbol,
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})

#TODO 6. Cancel Order
async def cancel_order(orderId, symbol):
    """
    Cancels a specific order.
    """
    path = '/openApi/swap/v2/trade/order'
    method = "DELETE"
    paramsMap = {
        "orderId": str(orderId),
        "symbol": symbol,
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})

#TODO 7. Cancel multiple orders
async def cancel_multiple_orders(orderIdList, symbol):
    """
    Cancels multiple orders.
    """
    path = '/openApi/swap/v2/trade/batchOrders'
    method = "DELETE"
    paramsMap = {
        "orderIdList": orderIdList,
        "symbol": symbol,
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})

#TODO 8. Cancel All Open Orders
async def cancel_all_open_orders(symbol):
    """
    Cancels all open orders for a specific symbol.
    """
    path = '/openApi/swap/v2/trade/allOpenOrders'
    method = "DELETE"
    paramsMap = {
        "symbol": symbol,
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})

#TODO 9. Current All Open Orders
async def query_all_open_orders(symbol):
    """
    Queries all open orders for a specific symbol.
    """
    path = '/openApi/swap/v2/trade/openOrders'
    method = "GET"
    paramsMap = {
        "symbol": symbol,
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})

#TODO 10. Query pending order status
async def query_pending_order_status(orderId, symbol):
    """
    Queries the details of a specific order.
    """
    path = '/openApi/swap/v2/trade/openOrder'
    method = "GET"
    paramsMap = {
        "orderId": str(orderId),
        "symbol": symbol,
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})

#TODO 11. Query Order details
async def query_order_details(orderId, symbol):
    """
    Queries the details of a specific order.
    """
    path = '/openApi/swap/v2/trade/order'
    method = "GET"
    paramsMap = {
        "orderId": str(orderId),
        "symbol": symbol,
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})

#TODO 12. Query Margin Type
async def query_margin_type(symbol):
    """
    Queries the margin type (isolated or cross) for the specified symbol.
    """
    path = '/openApi/swap/v2/trade/marginType'
    method = "GET"
    paramsMap = {
        "symbol": symbol,
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})

#TODO 13. Change Margin Type
async def change_margin_type(symbol, marginType):
    """
    Changes the margin type (isolated or cross) for the specified symbol.
    """
    path = '/openApi/swap/v2/trade/marginType'
    method = "POST"
    paramsMap = {
        "symbol": symbol,
        "marginType": marginType,
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})

#TODO 14. Query Leverage
async def query_leverage(symbol):
    """
    Queries the leverage for the specified symbol.
    """
    path = '/openApi/swap/v2/trade/leverage'
    method = "GET"
    paramsMap = {
        "symbol": symbol,
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})

#TODO 15. Set Leverage
async def set_leverage(symbol, side, leverage):
    """
    Sets the leverage for a specific symbol in a long/short position.
    """
    path = '/openApi/swap/v2/trade/leverage'
    method = "POST"
    paramsMap = {
        "symbol": symbol,
        "side": side,
        "leverage": str(leverage),
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})

#TODO 16. User's Force Orders
async def query_force_orders(symbol=None, startTime=None, endTime=None, limit=100):
    """
    Queries forced liquidation orders for the user.
    """
    path = '/openApi/swap/v2/trade/forceOrders'
    method = "GET"
    paramsMap = {
        "symbol": symbol,
        "startTime": startTime,
        "endTime": endTime,
        "limit": str(limit),
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})

#TODO 17. Query Order history
async def get_all_orders(limit: int, offset: int):
    path = '/openApi/swap/v2/trade/allOrders'
    method = "GET"
    end_time = str(int(time.time() * 1000))
    start_time = str(int(time.time() * 1000) - 24 * 60 * 60 * 1000 * (offset + 1))
    paramsMap = {
        "limit": str(limit),
        "startTime": start_time,
        "endTime": end_time,
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})

#TODO 18. Modify Isolated Position Margin
async def modify_isolated_position_margin(symbol, amount, positionSide):
    """
    Modifies the isolated margin for a position.
    """
    path = '/openApi/swap/v2/trade/positionMargin'
    method = "POST"
    paramsMap = {
        "symbol": symbol,
        "amount": str(amount),
        "positionSide": positionSide,
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})

#TODO 19. Query historical transaction orders
async def query_historical_orders(symbol, startTime, endTime, limit=500):
    """
    Queries historical transaction orders for a specific symbol.
    """
    path = '/openApi/swap/v2/trade/allFillOrders'
    method = "GET"
    paramsMap = {
        "symbol": symbol,
        "startTime": startTime,
        "endTime": endTime,
        "limit": str(limit),
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})

#TODO 20. Set Position Mode
async def set_position_mode(dualSidePosition):
    """
    Sets the position mode (dual or single).
    """
    path = '/openApi/swap/v1/positionSide/dual'
    method = "POST"
    paramsMap = {
        "dualSidePosition": str(dualSidePosition).lower(),  # "true" for dual, "false" for single
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})

#TODO 21. Query Position Mode
async def query_position_mode():
    """
    Queries the current position mode (dual or single).
    """
    path = '/openApi/swap/v1/positionSide/dual'
    method = "GET"
    paramsMap = {
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})

#TODO 22. Cancel an Existing Order and Send a New Orde
async def cancel_and_replace_order(cancelOrderId, symbol, side, positionSide, order_type, quantity, price=None):
    """
    Cancels an existing order and places a new one on the same symbol.
    """
    path = '/openApi/swap/v1/trade/cancelReplace'
    method = "POST"
    paramsMap = {
        "cancelOrderId": str(cancelOrderId),
        "cancelReplaceMode": "STOP_ON_FAILURE",
        "symbol": symbol,
        "side": side,
        "positionSide": positionSide,
        "type": order_type,
        "quantity": quantity,
        "timestamp": str(int(time.time() * 1000))
    }

    if price:
        paramsMap["price"] = price

    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})

#TODO 23. Cancel orders in batches and place orders in batches
async def batch_cancel_and_replace_orders(batchOrders):
    """
    Cancels and places new orders in batches.
    """
    path = '/openApi/swap/v1/trade/batchCancelReplace'
    method = "POST"
    paramsMap = {
        "batchOrders": batchOrders,
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})

#TODO 24. Cancel All After
async def cancel_all_after(timeout):
    """
    Cancels all open orders after a specified timeout.
    """
    path = '/openApi/swap/v2/trade/cancelAllAfter'
    method = "POST"
    paramsMap = {
        "timeOut": str(timeout),
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})

#TODO 25. Close position by position ID
async def close_position_by_id(positionId):
    """
    Closes the position by position ID.
    """
    path = '/openApi/swap/v1/trade/closePosition'
    method = "POST"
    paramsMap = {
        "positionId": str(positionId),
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})

#TODO 26. All Orders
async def get_full_all_orders(limit: int):
    path = '/openApi/swap/v1/trade/fullOrder'
    method = "GET"
    end_time = str(int(time.time() * 1000))
    paramsMap = {
        "limit": str(limit),
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})

#TODO 27. Position and Maintenance Margin Ratio
async def get_position_margin_ratio(symbol):
    """
    Retrieves the position and maintenance margin ratio for a given symbol.
    """
    path = '/openApi/swap/v1/maintMarginRatio'
    method = "GET"
    paramsMap = {
        "symbol": symbol,
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})

#TODO 28. Query historical transaction details
async def query_historical_transaction_details(symbol, startTime, endTime, limit=100):
    """
    Queries the detailed historical transaction orders for a specific symbol.
    """
    path = '/openApi/swap/v1/trade/fillHistory'
    method = "GET"
    paramsMap = {
        "symbol": symbol,
        "startTime": startTime,
        "endTime": endTime,
        "limit": str(limit),
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})

#TODO 29. Query Position History
async def query_position_history(symbol, startTime, endTime, limit=20):
    """
    Queries the position history for a given symbol.
    """
    path = '/openApi/swap/v1/trade/positionHistory'
    method = "GET"
    paramsMap = {
        "symbol": symbol,
        "startTime": startTime,
        "endTime": endTime,
        "limit": str(limit),
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})












