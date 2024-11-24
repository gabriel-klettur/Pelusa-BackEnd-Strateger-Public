# Path: app/bingx/api/api_coinm.py

# Description: Coin-M Perp Futures functions for BingX exchange
import time
from .api_utils import send_request, parse_param

#!--------------------------------------  Coin-M Trade Endpoints  ---------------------------------------!#

#TODO 1. Place Order
async def make_order_coinm(leverage, symbol, side, positionSide, order_type, quantity):
    payload = {}
    path = '/openApi/cswap/v1/trade/order'
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
    return send_request(method, path, paramsStr, payload)

#TODO 2. Query Commission Rate
async def query_commission_rate():
    """
    Queries the commission rate for the current user in Coin-M futures.
    """
    path = '/openApi/cswap/v1/user/commissionRate'
    method = "GET"
    paramsMap = {
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})

#TODO 3. Query Leverage
async def query_leverage(symbol):
    """
    Queries the leverage for the specified symbol in Coin-M futures.
    """
    path = '/openApi/cswap/v1/trade/leverage'
    method = "GET"
    paramsMap = {
        "symbol": symbol,
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})


#TODO 4. Modify Leverage
async def modify_leverage(symbol, side, leverage):
    """
    Modifies the leverage for a specific symbol in Coin-M futures.
    """
    path = '/openApi/cswap/v1/trade/leverage'
    method = "POST"
    paramsMap = {
        "symbol": symbol,
        "side": side,
        "leverage": leverage,
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})

#TODO 5. Cancel all orders
async def cancel_all_open_orders(symbol):
    """
    Cancels all open orders for a specific symbol in Coin-M futures.
    """
    path = '/openApi/cswap/v1/trade/allOpenOrders'
    method = "POST"
    paramsMap = {
        "symbol": symbol,
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})

#TODO 6. Close All Positions in Bulk
async def close_all_positions_coinm(symbol):
    payload = {}
    path = '/openApi/cswap/v1/trade/closeAllPositions'
    method = "POST"
    paramsMap = {
        "symbol": symbol,
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, payload)

#TODO 7. Query warehouse
async def get_positions_perp_coinm():   
    payload = {}
    path = '/openApi/cswap/v1/user/positions'
    method = "GET"
    paramsMap = {
        "timestamp": str(int(time.time() * 1000)),
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, payload)


#TODO 8. Query Account Assets
async def get_balance_perp_coinm():    
    payload = {}
    path = '/openApi/cswap/v1/user/balance'
    method = "GET"
    paramsMap = {
        "timestamp": str(int(time.time() * 1000)),
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, payload)

#TODO 9. Query Force Orders
async def query_force_orders(symbol=None, startTime=None, endTime=None, limit=100):
    """
    Queries forced liquidation orders in Coin-M futures.
    """
    path = '/openApi/cswap/v1/trade/forceOrders'
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

#TODO 10. Query Order Trade Detail
async def query_historical_orders(orderId, pageIndex=None, pageSize=None):
    """
    Queries historical transaction orders for a specific symbol in Coin-M futures.
    """
    path = '/openApi/cswap/v1/trade/allFillOrders'
    method = "GET"
    paramsMap = {
        "orderId": orderId,
        "timestamp": str(int(time.time() * 1000))
    }

    if pageIndex:
        paramsMap["pageIndex"] = str(pageIndex)
    if pageSize:
        paramsMap["pageSize"] = str(pageSize)

    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})

#TODO 11. Cancel an Order
async def cancel_order(orderId, symbol):
    """
    Cancels a specific order in Coin-M futures.
    """
    path = '/openApi/cswap/v1/trade/cancelOrder'
    method = "DELETE"
    paramsMap = {
        "orderId": str(orderId),
        "symbol": symbol,
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})

#TODO 12. Query all current pending orders
async def query_all_open_orders(symbol=None):
    """
    Queries all open orders for a specific symbol in Coin-M futures.
    """
    path = '/openApi/cswap/v1/trade/openOrders'
    method = "GET"
    paramsMap = {
        "symbol": symbol,
        "timestamp": str(int(time.time() * 1000))
    }



    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})

#TODO 13. Query Order
async def query_order(orderId, symbol):
    """
    Queries a specific order by order ID in Coin-M futures.
    """
    path = '/openApi/cswap/v1/trade/orderDetail'
    method = "GET"
    paramsMap = {
        "orderId": str(orderId),
        "symbol": symbol,
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})

#TODO 14. Query User's History Orders
async def query_history_orders(symbol: str, orderId: int, startTime: int, endTime: int, limit: int):
    """
    Queries the user's historical orders in Coin-M futures.
    """
    path = '/openApi/cswap/v1/trade/orderHistory'
    method = "GET"
    paramsMap = {
        "limit": str(limit),
        "timestamp": str(int(time.time() * 1000))
    }

    if symbol:
        paramsMap["symbol"] = symbol
    if orderId:
        paramsMap["orderId"] = str(orderId)
    if startTime:
        paramsMap["startTime"] = str(startTime)
    if endTime:
        paramsMap["endTime"] = str(endTime)    

    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})


#TODO 15. Query Margin Type
async def query_margin_type(symbol):
    """
    Queries the margin type for a specific symbol in Coin-M futures.
    """
    path = '/openApi/cswap/v1/trade/marginType'
    method = "GET"
    paramsMap = {
        "symbol": symbol,
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})

#TODO 16. Set Margin Type
async def set_margin_type(symbol, marginType):
    """
    Sets the margin type for a specific symbol in Coin-M futures.
    """
    path = '/openApi/cswap/v1/trade/marginType'
    method = "POST"
    paramsMap = {
        "symbol": symbol,
        "marginType": marginType,
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})

#TODO 17. Adjust Isolated Margin
async def adjust_isolated_position_margin(symbol, amount, positionSide, type):
    """
    Modifies the isolated margin for a position in Coin-M futures.
    """
    path = '/openApi/cswap/v1/trade/positionMargin'
    method = "POST"
    paramsMap = {
        "symbol": symbol,
        "amount": str(amount),
        "positionSide": positionSide,
        "type": type,
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})

