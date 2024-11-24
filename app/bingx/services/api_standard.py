# Path: app/bingx/api/api_standard.py

# Description: Standard Futures Contract functions for BingX exchange
import time
from .api_utils import send_request, parse_param

#!--------------------------------------  Standard Contract Endpoints  ---------------------------------------!#

#TODO 1. Query All Positions
async def query_all_positions():
    """
    Queries all positions for standard contracts.
    """
    path = '/openApi/contract/v1/allPosition'
    method = "GET"
    paramsMap = {
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})


#TODO 2. Query Historical Orders
async def query_historical_orders(symbol="BTC-USDT", orderId=None, startTime=None, endTime=None, limit=100):
    """
    Queries historical orders for a specific symbol in standard contracts.
    """
    path = '/openApi/contract/v1/allOrders'
    method = "GET"
    paramsMap = {   
        "symbol": symbol,    
        "timestamp": str(int(time.time() * 1000))
    }    
    if orderId:
        paramsMap["orderId"] = orderId
    if startTime:
        paramsMap["startTime"] = startTime
    if endTime:
        paramsMap["endTime"] = endTime
    if limit:
        paramsMap["limit"] = str(limit)
    
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})


#TODO 3. Query Standard Contract Balance
async def query_standard_contract_balance():
    """
    Queries the balance for standard contracts.
    """
    path = '/openApi/contract/v1/balance'
    method = "GET"
    paramsMap = {
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})

