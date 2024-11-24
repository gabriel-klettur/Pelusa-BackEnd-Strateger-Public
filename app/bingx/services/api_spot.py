#Path: app/bingx/api/api_spot.py

# Description: Spot account functions for BingX exchange
import time
from .api_utils import send_request, parse_param

#!-----------------------------------------------------------------------------------------------------------!#
#!--------------------------------------  Spot Market Data Endpoints  ---------------------------------------!#
#!-----------------------------------------------------------------------------------------------------------!#

#TODO 1. Spot Trading Symbols
async def get_spot_symbols():
    """
    Retrieves the list of all spot trading symbols.
    """
    path = '/openApi/spot/v1/common/symbols'
    method = "GET"
    paramsMap = {
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})


#TODO 2. Recent Trades List
async def get_recent_trades(symbol, limit=100):
    """
    Retrieves the list of recent trades for a specific symbol in the spot market.
    """
    path = '/openApi/spot/v1/market/trades'
    method = "GET"
    paramsMap = {
        "symbol": symbol,
        "limit": limit,
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})


#TODO 3. Order Book
async def get_order_book(symbol, limit=20):
    """
    Retrieves the order book for a specific symbol in the spot market.
    """
    path = '/openApi/spot/v1/market/depth'
    method = "GET"
    paramsMap = {
        "symbol": symbol,
        "limit": limit,
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})


#TODO 4. Kline/Candlestick Data
async def get_kline_data(symbol, interval, limit=500, startTime=None, endTime=None):
    """
    Retrieves Kline/candlestick data for a specific symbol.
    """
    path = '/openApi/spot/v2/market/kline'
    method = "GET"
    paramsMap = {
        "symbol": symbol,
        "interval": interval,
        "limit": str(limit),
        "timestamp": str(int(time.time() * 1000))
    }
    
    if startTime:
        paramsMap["startTime"] = str(startTime)
    if endTime:
        paramsMap["endTime"] = str(endTime)
    
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})


#TODO 5. 24hr Ticker Price Change Statistics
async def get_24hr_ticker(symbol):
    """
    Retrieves the 24-hour ticker price change statistics for a specific symbol.
    """
    path = '/openApi/spot/v1/ticker/24hr'
    method = "GET"
    paramsMap = {
        "symbol": symbol,
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})


#TODO 6. Order Book Aggregation
async def get_order_book_aggregation(symbol, depth, order_type):
    """
    Retrieves aggregated order book data for a specific symbol.
    """
    path = '/openApi/spot/v2/market/depth'
    method = "GET"
    paramsMap = {
        "symbol": symbol,
        "depth": str(depth),
        "type": order_type,
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})


#TODO 7. Symbol Price Ticker
async def get_symbol_price(symbol):
    """
    Retrieves the latest price for a specific symbol.
    """
    path = '/openApi/spot/v1/ticker/price'
    method = "GET"
    paramsMap = {
        "symbol": symbol,
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})


#TODO 8. Symbol Order Book Ticker
async def get_order_book_ticker(symbol):
    """
    Retrieves the best price and quantity on the order book for a specific symbol.
    """
    path = '/openApi/spot/v1/ticker/bookTicker'
    method = "GET"
    paramsMap = {
        "symbol": symbol,
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})


#TODO 9. Historical K-line Data
async def get_historical_kline(symbol, interval, limit=500, startTime=None, endTime=None):
    """
    Retrieves historical K-line data for a specific symbol.
    """
    path = '/openApi/market/his/v1/kline'
    method = "GET"
    paramsMap = {
        "symbol": symbol,
        "interval": interval,
        "limit": str(limit),
        "timestamp": str(int(time.time() * 1000))
    }
    
    if startTime:
        paramsMap["startTime"] = str(startTime)
    if endTime:
        paramsMap["endTime"] = str(endTime)
    
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})


#TODO 10. Old Trade Lookup
async def get_old_trades(symbol, limit=100, fromId=None):
    """
    Retrieves historical trade data for a specific symbol.
    args:
        limit(max 500)
    """
    path = '/openApi/market/his/v1/trade'
    method = "GET"
    paramsMap = {
        "symbol": symbol,
        "limit": str(limit),
        "timestamp": str(int(time.time() * 1000))
    }
    
    if fromId:
        paramsMap["fromId"] = fromId
    
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})

#!--------------------------------------------------------------------------------------------------------------------------!#
#!--------------------------------------  Wallet Deposits and Withdrawals Endpoints  ---------------------------------------!#
#!--------------------------------------------------------------------------------------------------------------------------!#

#TODO 1. Deposit Records
async def get_spot_deposit_records(coin=None, status=None, startTime=None, endTime=None, offset=0, limit=1000):
    """
    Retrieves the deposit records.
    """
    path = '/openApi/api/v3/capital/deposit/hisrec'
    method = "GET"
    paramsMap = {
        "offset": str(offset),
        "limit": str(limit),
        "timestamp": str(int(time.time() * 1000))
    }
    
    if coin:
        paramsMap["coin"] = coin
    if status:
        paramsMap["status"] = str(status)
    if startTime:
        paramsMap["startTime"] = str(startTime)
    if endTime:
        paramsMap["endTime"] = str(endTime)
    
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})


#TODO 2. Withdraw Records
async def get_withdraw_records(coin=None, withdrawOrderId=None, status=None, startTime=None, endTime=None, offset=0, limit=1000):
    """
    Retrieves the withdraw records.
    """
    path = '/openApi/api/v3/capital/withdraw/history'
    method = "GET"
    paramsMap = {
        "offset": str(offset),
        "limit": str(limit),
        "timestamp": str(int(time.time() * 1000))
    }

    if coin:
        paramsMap["coin"] = coin
    if withdrawOrderId:
        paramsMap["withdrawOrderId"] = withdrawOrderId
    if status:
        paramsMap["status"] = str(status)
    if startTime:
        paramsMap["startTime"] = str(startTime)
    if endTime:
        paramsMap["endTime"] = str(endTime)
    
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})


#TODO 3. Query Currency Deposit and Withdrawal Data
async def get_currency_info():
    """
    Retrieves currency deposit and withdrawal data.
    """
    path = '/openApi/wallets/v1/capital/config/getall'
    method = "GET"
    paramsMap = {
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})


#TODO 4. Withdraw
async def withdraw(coin, address, amount, network=None, addressTag=None, walletType=1, withdrawOrderId=None):
    """
    Initiates a withdrawal request.
    """
    path = '/openApi/wallets/v1/capital/withdraw/apply'
    method = "POST"
    paramsMap = {
        "coin": coin,
        "address": address,
        "amount": str(amount),
        "walletType": str(walletType),
        "timestamp": str(int(time.time() * 1000))
    }

    if network:
        paramsMap["network"] = network
    if addressTag:
        paramsMap["addressTag"] = addressTag
    if withdrawOrderId:
        paramsMap["withdrawOrderId"] = withdrawOrderId

    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})


#TODO 5. Main Account Deposit Address
async def get_deposit_address(coin, offset=0, limit=1000):
    """
    Retrieves the deposit address for the main account.
    """
    path = '/openApi/wallets/v1/capital/deposit/address'
    method = "GET"
    paramsMap = {
        "coin": coin,
        "offset": str(offset),
        "limit": str(limit),
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})


#TODO 6. Deposit Risk Control Records
async def get_deposit_risk_control_records():
    """
    Retrieves the deposit risk control records for users and sub-accounts.
    """
    path = '/openApi/wallets/v1/capital/deposit/riskRecords'
    method = "GET"
    paramsMap = {
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})


#!--------------------------------------------------------------------------------------------------------------------!#
#!----------------------------------------------  Fund Account Endpoints  --------------------------------------------!#
#!--------------------------------------------------------------------------------------------------------------------!#

#TODO 1. Query Assets
async def get_balance_spot():
    """
    Retrieves the balance for the spot account.
    """
    payload = {}
    path = '/openApi/spot/v1/account/balance'
    method = "GET"
    paramsMap = {
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, payload)


#TODO 2. Asset Transfer
async def transfer_asset(asset, amount, transfer_type):
    """
    Transfers assets within the BingX platform (e.g., from spot to futures).

    Args:
        transfer_type:
            FUND_SFUTURES            
            SFUTURES_FUND
            FUND_PFUTURES
            PFUTURES_FUND
            SFUTURES_PFUTURES
            PFUTURES_SFUTURES            
    """
    path = '/openApi/api/v3/post/asset/transfer'
    method = "POST"
    paramsMap = {
        "asset": asset,
        "amount": str(amount),
        "type": transfer_type,
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})


#TODO 3. Asset Transfer Records
async def get_transfer_records(transfer_type, startTime=None, endTime=None, tranId=None, current=1, size=10):
    """
    Retrieves records of asset transfers within the platform.

    Args:
        transfer_type:        
            FUND_SFUTURES            
            SFUTURES_FUND            
            FUND_PFUTURES            
            PFUTURES_FUND    
            SFUTURES_PFUTURES
            PFUTURES_SFUTURES
            FUND_STRADING
            STRADING_FUND
            FUND_CTRADING
            SFUTURES_CTRADING            
            PFUTURES_CTRADING            
            CTRADING_FUND            
            CTRADING_SFUTURES        
            CTRADING_PFUTURES
    """
    path = '/openApi/api/v3/asset/transfer'
    method = "GET"
    paramsMap = {
        "type": transfer_type,
        "current": str(current),
        "size": str(size),
        "timestamp": str(int(time.time() * 1000))
    }

    if startTime:
        paramsMap["startTime"] = str(startTime)
    if endTime:
        paramsMap["endTime"] = str(endTime)
    if tranId:
        paramsMap["tranId"] = str(tranId)

    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})


#TODO 4. Main Account Internal Transfer
async def main_account_internal_transfer(coin, amount, userAccount, userAccountType=1, walletType=1, callingCode=None, transferClientId=None):
    """
    Transfers funds between main accounts or from main account to sub-accounts.
    """
    path = '/openApi/wallets/v1/capital/innerTransfer/apply'
    method = "POST"
    paramsMap = {
        "coin": coin,
        "amount": str(amount),
        "userAccount": userAccount,
        "userAccountType": str(userAccountType),
        "walletType": str(walletType),
        "timestamp": str(int(time.time() * 1000))
    }

    if callingCode:
        paramsMap["callingCode"] = callingCode
    if transferClientId:
        paramsMap["transferClientId"] = transferClientId

    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})


#TODO 5. Main Account Internal Transfer Records
async def get_internal_transfer_records(coin, startTime=None, endTime=None, transferClientId=None, offset=0, limit=100):
    """
    Retrieves internal transfer records for the main account.
    """
    path = '/openApi/wallets/v1/capital/innerTransfer/records'
    method = "GET"
    paramsMap = {
        "coin": coin,
        "offset": str(offset),
        "limit": str(limit),
        "timestamp": str(int(time.time() * 1000))
    }

    if startTime:
        paramsMap["startTime"] = str(startTime)
    if endTime:
        paramsMap["endTime"] = str(endTime)
    if transferClientId:
        paramsMap["transferClientId"] = transferClientId

    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})



#!------------------------------------------------------------------------------------------------------------------!#
#!---------------------------------------------  Spot Trades Endpoints  --------------------------------------------!#
#!------------------------------------------------------------------------------------------------------------------!#

#TODO 1. Place order
async def place_order(symbol, side, order_type, quantity=None, price=None, stopPrice=None, quoteOrderQty=None, newClientOrderId=None, timeInForce=None):
    """
    Places a new order on the spot market.
    """
    path = '/openApi/spot/v1/trade/order'
    method = "POST"
    paramsMap = {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "timestamp": str(int(time.time() * 1000))
    }

    if quantity:
        paramsMap["quantity"] = str(quantity)
    if price:
        paramsMap["price"] = str(price)
    if stopPrice:
        paramsMap["stopPrice"] = str(stopPrice)
    if quoteOrderQty:
        paramsMap["quoteOrderQty"] = str(quoteOrderQty)
    if newClientOrderId:
        paramsMap["newClientOrderId"] = newClientOrderId
    if timeInForce:
        paramsMap["timeInForce"] = timeInForce

    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})


#TODO 2. Place multiple orders
async def place_multiple_orders(orders_data):
    """
    Places multiple orders at once. Limited to 5 orders.
    """
    path = '/openApi/spot/v1/trade/batchOrders'
    method = "POST"
    paramsMap = {
        "data": orders_data,
        "timestamp": str(int(time.time() * 1000))
    }

    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})


#TODO 3. Cancel Order
async def cancel_order(symbol, orderId=None, clientOrderId=None):
    """
    Cancels an existing order on the spot market.
    """
    path = '/openApi/spot/v1/trade/cancel'
    method = "POST"
    paramsMap = {
        "symbol": symbol,
        "timestamp": str(int(time.time() * 1000))
    }

    if orderId:
        paramsMap["orderId"] = str(orderId)
    if clientOrderId:
        paramsMap["clientOrderId"] = clientOrderId

    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})


#TODO 4. Cancel multiple orders
async def cancel_multiple_orders(symbol, orderIds, clientOrderIds=None):
    """
    Cancels multiple orders at once for a specific symbol.
    """
    path = '/openApi/spot/v1/trade/cancelOrders'
    method = "POST"
    paramsMap = {
        "symbol": symbol,
        "orderIds": orderIds,
        "timestamp": str(int(time.time() * 1000))
    }

    if clientOrderIds:
        paramsMap["clientOrderIds"] = clientOrderIds

    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})


#TODO 5. Cancel all Open Orders on a Symbol
async def cancel_all_open_orders(symbol):
    """
    Cancels all open orders for a specific symbol.
    """
    path = '/openApi/spot/v1/trade/cancelOpenOrders'
    method = "POST"
    paramsMap = {
        "symbol": symbol,
        "timestamp": str(int(time.time() * 1000))
    }

    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})


#TODO 6. Cancel an Existing Order and Send a New Order
async def cancel_and_replace_order(symbol, cancelOrderId, cancelReplaceMode, side, order_type, quantity=None, price=None):
    """
    Cancels an existing order and replaces it with a new one.
    """
    path = '/openApi/spot/v1/trade/order/cancelReplace'
    method = "POST"
    paramsMap = {
        "symbol": symbol,
        "cancelOrderId": cancelOrderId,
        "cancelReplaceMode": cancelReplaceMode,
        "side": side,
        "type": order_type,
        "timestamp": str(int(time.time() * 1000))
    }

    if quantity:
        paramsMap["quantity"] = str(quantity)
    if price:
        paramsMap["price"] = str(price)

    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})


#TODO 7. Query Order details
async def query_order_details(symbol, orderId=None, clientOrderId=None):
    """
    Queries the details of an order by its ID or client order ID.
    """
    path = '/openApi/spot/v1/trade/query'
    method = "GET"
    paramsMap = {
        "symbol": symbol,
        "timestamp": str(int(time.time() * 1000))
    }

    if orderId:
        paramsMap["orderId"] = str(orderId)
    if clientOrderId:
        paramsMap["clientOrderId"] = clientOrderId

    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})


#TODO 8. Current Open Orders
async def get_open_orders(symbol=None):
    """
    Retrieves all current open orders.
    """
    path = '/openApi/spot/v1/trade/openOrders'
    method = "GET"
    paramsMap = {
        "timestamp": str(int(time.time() * 1000))
    }

    if symbol:
        paramsMap["symbol"] = symbol

    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})


#TODO 9. Query Order history
async def get_order_history(
    symbol: str = None,
    startTime: int = None,
    endTime: int = None,
    pageIndex: int = None,
    pageSize: int = None,
    orderId: int = None,
    status: str = None,
    type: str = None,
):
    """
    Retrieves the history of orders for a specific symbol.
    """
    path = '/openApi/spot/v1/trade/historyOrders'
    method = "GET"
    paramsMap = {    
        "timestamp": str(int(time.time() * 1000))
    }

    if symbol:
        paramsMap["symbol"] = symbol
    if startTime:
        paramsMap["startTime"] = str(startTime)
    if endTime:
        paramsMap["endTime"] = str(endTime)
    if pageIndex:
        paramsMap["pageIndex"] = str(pageIndex)
    if pageSize:
        paramsMap["pageSize"] = str(pageSize)
    if orderId:
        paramsMap["orderId"] = str(orderId)
    if status:
        paramsMap["status"] = status
    if type:
        paramsMap["type"] = type

    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})

#TODO 10. Query transaction details
async def get_transaction_details(symbol, orderId, startTime=None, endTime=None, fromId=None, limit=500):
    """
    Queries transaction details within the last 24 hours for a symbol.
    """
    path = '/openApi/spot/v1/trade/myTrades'
    method = "GET"
    paramsMap = {
        "symbol": symbol,
        "orderId": str(orderId),
        "limit": str(limit),
        "timestamp": str(int(time.time() * 1000))
    }

    if startTime:
        paramsMap["startTime"] = str(startTime)
    if endTime:
        paramsMap["endTime"] = str(endTime)
    if fromId:
        paramsMap["fromId"] = str(fromId)

    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {}) 


#TODO 11. Query Trading Commission Rate
async def get_trading_commission_rate(symbol):
    """
    Queries the current trading commission rate for a specific trading pair.
    """
    path = '/openApi/spot/v1/user/commissionRate'
    method = "GET"
    paramsMap = {
        "symbol": symbol,
        "timestamp": str(int(time.time() * 1000))
    }

    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})


#TODO 12. Cancel All After
async def cancel_all_after(type, timeOut):
    """
    Cancels all open orders after a specified countdown time.
    """
    path = '/openApi/spot/v1/trade/cancelAllAfter'
    method = "POST"
    paramsMap = {
        "type": type,
        "timeOut": str(timeOut),
        "timestamp": str(int(time.time() * 1000))
    }

    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})


#TODO 13. Create an OCO Order
async def create_oco_order(symbol, side, quantity, limitPrice, orderPrice, triggerPrice, listClientOrderId=None, aboveClientOrderId=None, belowClientOrderId=None):
    """
    Creates a One-Cancels-the-Other (OCO) order.
    """
    path = '/openApi/spot/v1/oco/order'
    method = "POST"
    paramsMap = {
        "symbol": symbol,
        "side": side,
        "quantity": str(quantity),
        "limitPrice": str(limitPrice),
        "orderPrice": str(orderPrice),
        "triggerPrice": str(triggerPrice),
        "timestamp": str(int(time.time() * 1000))
    }

    if listClientOrderId:
        paramsMap["listClientOrderId"] = listClientOrderId
    if aboveClientOrderId:
        paramsMap["aboveClientOrderId"] = aboveClientOrderId
    if belowClientOrderId:
        paramsMap["belowClientOrderId"] = belowClientOrderId

    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})


#TODO 14. Cancel an OCO Order List
async def cancel_oco_order(symbol, orderId=None, clientOrderId=None):
    """
    Cancels an OCO order.
    """
    path = '/openApi/spot/v1/oco/cancel'
    method = "POST"
    paramsMap = {
        "symbol": symbol,
        "timestamp": str(int(time.time() * 1000))
    }

    if orderId:
        paramsMap["orderId"] = str(orderId)
    if clientOrderId:
        paramsMap["clientOrderId"] = clientOrderId

    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})


#TODO 15. Query an OCO Order List
async def query_oco_order_list(orderListId=None, clientOrderId=None):
    """
    Queries an OCO order list by ID or client order ID.
    """
    path = '/openApi/spot/v1/oco/orderList'
    method = "GET"
    paramsMap = {
        "timestamp": str(int(time.time() * 1000))
    }

    if orderListId:
        paramsMap["orderListId"] = orderListId
    if clientOrderId:
        paramsMap["clientOrderId"] = clientOrderId

    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})


#TODO 16. Query All Open OCO Orders
async def query_all_open_oco_orders(pageIndex=1, pageSize=100):
    """
    Queries all open OCO orders.
    """
    path = '/openApi/spot/v1/oco/openOrderList'
    method = "GET"
    paramsMap = {
        "pageIndex": str(pageIndex),
        "pageSize": str(pageSize),
        "timestamp": str(int(time.time() * 1000))
    }

    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})


#TODO 17. Query OCO Historical Order List
async def query_oco_history(startTime=None, endTime=None, pageIndex=1, pageSize=100):
    """
    Queries the historical OCO orders.
    """
    path = '/openApi/spot/v1/oco/historyOrderList'
    method = "GET"
    paramsMap = {
        "pageIndex": str(pageIndex),
        "pageSize": str(pageSize),
        "timestamp": str(int(time.time() * 1000))
    }

    if startTime:
        paramsMap["startTime"] = str(startTime)
    if endTime:
        paramsMap["endTime"] = str(endTime)

    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})






