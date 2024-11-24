#Path: app/bingx/routes/spot.py

from fastapi import APIRouter, Request
from typing import Optional
from app.utils.ip_check import is_ip_allowed
from app.bingx.controllers.spot import (
    #!------------------------------------------ Spot Market Data Endpoints ------------------------------------------!#
    get_spot_symbols_controller,                #TODO 1. Query Symbols
    get_recent_trades_controller,               #TODO 2. Query Recent Trades
    get_order_book_controller,                  #TODO 3. Query Order Book
    get_kline_data_controller,                  #TODO 4. Query Kline Data
    get_24hr_ticker_controller,                 #TODO 5. Query 24hr Ticker Price Change Statistics
    get_order_book_aggregation_controller,      #TODO 6. Query Order Book Aggregated
    get_symbol_price_controller,                #TODO 7. Query Symbol Price
    get_order_book_ticker_controller,           #TODO 8. Query Order Book Ticker
    get_historical_kline_controller,            #TODO 9. Query Historical Kline
    get_old_trades_controller,                  #TODO 10. Query Old Trades

    #!----------------------------------- Wallet Deposits and Withdrawals Endpoints -----------------------------------!#
    get_spot_deposit_records_controller,            #TODO 1. Deposit Records
    get_withdraw_records_controller,                #TODO 2. Withdraw Records
    get_currency_info_controller,                   #TODO 3. Query Currency Information
    withdraw_controller,                            #TODO 4. Withdraw
    get_deposit_address_controller,                 #TODO 5. Query Deposit Address
    get_deposit_risk_control_records_controller,    #TODO 6. Query Deposit Risk Control Records

    #!----------------------------------------- Fund Account Endpoints -----------------------------------------------!#
    get_balance_spot_controller,                    #TODO 1. Query Assets
    transfer_asset_controller,                      #TODO 2. Asset Transfer
    get_transfer_records_controller,                #TODO 3. Asset Transfer Records
    main_account_internal_transfer_controller,      #TODO 4. Main Account Internal Transfer
    get_internal_transfer_records_controller,       #TODO 5. Main Account Internal Transfer Records

    #!------------------------------------------- Spot Trades Endpoints -----------------------------------------------!#
    place_order_controller,                         #TODO 1. Place Order
    place_multiple_orders_controller,               #TODO 2. Place Multiple Orders
    cancel_order_controller,                        #TODO 3. Cancel Order
    cancel_multiple_orders_controller,              #TODO 4. Cancel Multiple Orders
    cancel_all_open_orders_controller,              #TODO 5. Cancel All Open Orders
    cancel_and_replace_order_controller,            #TODO 6. Cancel an Existing Order and Send a New Order
    query_order_details_controller,                 #TODO 7. Query Order Details
    get_open_orders_controller,                     #TODO 8. Query Open Orders
    get_order_history_controller,                   #TODO 9. Query Order History
    get_transaction_details_controller,             #TODO 10. Query Transaction Details
    get_trading_commission_rate_controller,         #TODO 11. Query Trading Commission Rate
    cancel_all_after_controller,                    #TODO 12. Cancel All After
    create_oco_order_controller,                    #TODO 13. Create OCO Order
    cancel_oco_order_controller,                    #TODO 14. Cancel OCO Order
    query_oco_order_list_controller,                #TODO 15. Query OCO Order List
    query_all_open_oco_orders_controller,           #TODO 16. Query All Open OCO Orders
    query_oco_history_controller                    #TODO 17. Query OCO History
)

router = APIRouter()

#!-----------------------------------------------------------------------------------------------------------!#
#!--------------------------------------  Spot Market Data Endpoints  ---------------------------------------!#
#!-----------------------------------------------------------------------------------------------------------!#

#TODO 1. Query Symbols
@router.get('/get-spot-symbols')
async def get_spot_symbols_endpoint(request: Request):
    client_ip = request.client.host
    await is_ip_allowed(client_ip)
    return await get_spot_symbols_controller(client_ip)

#TODO 2. Query Recent Trades
@router.get('/get-recent-trades')
async def get_recent_trades_endpoint(request: Request, symbol: str, limit: int = 100):
    client_ip = request.client.host
    await is_ip_allowed(client_ip)
    return await get_recent_trades_controller(client_ip, symbol, limit)

#TODO 3. Query Order Book
@router.get('/get-order-book')
async def get_order_book_endpoint(request: Request, symbol: str, limit: int = 100):
    client_ip = request.client.host
    await is_ip_allowed(client_ip)
    return await get_order_book_controller(client_ip, symbol, limit)

#TODO 4. Query Kline Data
@router.get('/get-kline-data')
async def get_kline_data_endpoint(request: Request, symbol: str, interval: str, limit: int = 500, startTime: int = None, endTime: int = None):
    client_ip = request.client.host
    await is_ip_allowed(client_ip)
    return await get_kline_data_controller(client_ip, symbol, interval, limit, startTime, endTime)

#TODO 5. Query 24hr Ticker Price Change Statistics
@router.get('/get-24hr-ticker')
async def get_24hr_ticker_endpoint(request: Request, symbol: str):
    client_ip = request.client.host
    await is_ip_allowed(client_ip)
    return await get_24hr_ticker_controller(client_ip, symbol)

#TODO 6. Query Order Book Aggregated
@router.get('/get-order-book-aggregation')
async def get_order_book_aggregation_endpoint(request: Request, symbol: str, depth: int, order_type: str):
    client_ip = request.client.host
    await is_ip_allowed(client_ip)
    return await get_order_book_aggregation_controller(client_ip, depth, order_type, symbol)

#TODO 7. Query Symbol Price
@router.get('/get-symbol-price')
async def get_symbol_price_endpoint(request: Request, symbol: str):
    client_ip = request.client.host
    await is_ip_allowed(client_ip)
    return await get_symbol_price_controller(client_ip, symbol)

#TODO 8. Query Order Book Ticker
@router.get('/get-order-book-ticker')
async def get_order_book_ticker_endpoint(request: Request, symbol: str):
    client_ip = request.client.host
    await is_ip_allowed(client_ip)
    return await get_order_book_ticker_controller(client_ip, symbol)

#TODO 9. Query Historical Kline
@router.get('/get-historical-kline')
async def get_historical_kline_endpoint(request: Request, symbol: str, interval: str, startTime: int, endTime: int, limit: int = 500):
    client_ip = request.client.host
    await is_ip_allowed(client_ip)
    return await get_historical_kline_controller(client_ip, symbol, interval, startTime, endTime, limit)

#TODO 10. Query Old Trades
@router.get('/get-old-trades')
async def get_old_trades_endpoint(request: Request, symbol: str, limit: int = 100, fromId: int = None):
    client_ip = request.client.host
    await is_ip_allowed(client_ip)
    return await get_old_trades_controller(client_ip, symbol, limit, fromId)

#!-----------------------------------------------------------------------------------------------------------!#
#!-------------------------------- Wallet Deposits and Withdrawals Endpoints --------------------------------!#
#!-----------------------------------------------------------------------------------------------------------!#

#TODO 1. Deposit Records
@router.get('/get-spot-deposit-records')
async def get_spot_deposit_records_endpoint(request: Request):
    client_ip = request.client.host
    await is_ip_allowed(client_ip)
    return await get_spot_deposit_records_controller(client_ip)

#TODO 2. Withdraw Records
@router.get('/get-withdraw-records')
async def get_withdraw_records_endpoint(request: Request, coin: str, withdrawOrderId: str, status: int, startTime: int, endTime: int, limit: int = 100):
    client_ip = request.client.host
    await is_ip_allowed(client_ip)
    return await get_withdraw_records_controller(client_ip, coin, withdrawOrderId, status, startTime, endTime, limit)

#TODO 3. Query Currency Information
@router.get('/get-currency-info')
async def get_currency_info_endpoint(request: Request):
    client_ip = request.client.host
    await is_ip_allowed(client_ip)
    return await get_currency_info_controller(client_ip)

#TODO 4. Withdraw
@router.post('/withdraw')
async def withdraw_endpoint(request: Request, coin: str, amount: float, address: str, network: str, addressTag: str = None, walletType: str = None, withdrawOrderId: str = None):
    client_ip = request.client.host
    await is_ip_allowed(client_ip)
    return await withdraw_controller(client_ip, coin, amount, address, network, addressTag, walletType, withdrawOrderId)

#TODO 5. Query Deposit Address
@router.get('/get-deposit-address')
async def get_deposit_address_endpoint(request: Request, coin: str, offset: int = 0, limit: int = 1000):
    client_ip = request.client.host
    await is_ip_allowed(client_ip)
    return await get_deposit_address_controller(client_ip, coin, offset, limit)

#TODO 6. Query Deposit Risk Control Records
@router.get('/get-deposit-risk-control-records')
async def get_deposit_risk_control_records_endpoint(request: Request):
    client_ip = request.client.host
    await is_ip_allowed(client_ip)
    return await get_deposit_risk_control_records_controller(client_ip)

#!-----------------------------------------------------------------------------------------------------------!#
#!------------------------------------------ Fund Account Endpoints -----------------------------------------!#
#!-----------------------------------------------------------------------------------------------------------!#

#TODO 1. Query Assets
@router.get('/get-balance-spot')
async def get_balance_spot_endpoint(request: Request):
    client_ip = request.client.host
    await is_ip_allowed(client_ip)
    return await get_balance_spot_controller(client_ip)

#TODO 2. Asset Transfer
@router.post('/transfer-asset')
async def transfer_asset_endpoint(request: Request, asset: str, amount: float, transfer_type: int):
    client_ip = request.client.host
    await is_ip_allowed(client_ip)
    return await transfer_asset_controller(client_ip, asset, amount, transfer_type)

#TODO 3. Asset Transfer Records
@router.get('/get-transfer-records')
async def get_transfer_records_endpoint(request: Request, transfer_type: int, startTime: int, endTime: int, tranId: int = None, size: int = 10):
    client_ip = request.client.host
    await is_ip_allowed(client_ip)
    return await get_transfer_records_controller(client_ip, transfer_type, startTime, endTime, tranId, size)

#TODO 4. Main Account Internal Transfer
@router.post('/main-account-internal-transfer')
async def main_account_internal_transfer_endpoint(request: Request, coin: str, amount: float, userAccountType: int, walletType: int, callingCode: str = None, transferClientId: str = None):
    client_ip = request.client.host
    await is_ip_allowed(client_ip)
    return await main_account_internal_transfer_controller(client_ip, coin, amount, userAccountType, walletType, callingCode, transferClientId)

#TODO 5. Main Account Internal Transfer Records
@router.get('/get-internal-transfer-records')
async def get_internal_transfer_records_endpoint(request: Request, coin: str, startTime: int, endTime: int, transferClientId: str = None, offset: int = 0, limit: int = 100):
    client_ip = request.client.host
    await is_ip_allowed(client_ip)
    return await get_internal_transfer_records_controller(client_ip, coin, startTime, endTime, transferClientId, offset, limit)

#!-----------------------------------------------------------------------------------------------------------!#
#!------------------------------------------- Spot Trades Endpoints -----------------------------------------!#
#!-----------------------------------------------------------------------------------------------------------!#

#TODO 1. Place Order
@router.post('/place-order')
async def place_order_endpoint(request: Request, symbol: str, side: str, order_type: str, quantity: float, price: float = None, stopPrice: float = None, quoteOrderQty: float = None, newClientOrderId: str = None, timeInForce: str = None):
    client_ip = request.client.host
    await is_ip_allowed(client_ip)
    return await place_order_controller(client_ip, symbol, side, order_type, quantity, price, stopPrice, quoteOrderQty, newClientOrderId, timeInForce)

#TODO 2. Place Multiple Orders
@router.post('/place-multiple-orders')
async def place_multiple_orders_endpoint(request: Request, orders_data: list):
    client_ip = request.client.host
    await is_ip_allowed(client_ip)
    return await place_multiple_orders_controller(client_ip, orders_data)

#TODO 3. Cancel Order
@router.post('/cancel-order')
async def cancel_order_endpoint(request: Request, symbol: str, clientOrderId: str):
    client_ip = request.client.host
    await is_ip_allowed(client_ip)
    return await cancel_order_controller(client_ip, symbol, clientOrderId)

#TODO 4. Cancel Multiple Orders
@router.post('/cancel-multiple-orders')
async def cancel_multiple_orders_endpoint(request: Request, symbol: str, orderIds: list, clientOrderId: str = None):
    client_ip = request.client.host
    await is_ip_allowed(client_ip)
    return await cancel_multiple_orders_controller(client_ip, symbol, orderIds, clientOrderId)

#TODO 5. Cancel All Open Orders
@router.post('/cancel-all-open-orders')
async def cancel_all_open_orders_endpoint(request: Request, symbol: str):
    client_ip = request.client.host
    await is_ip_allowed(client_ip)
    return await cancel_all_open_orders_controller(client_ip, symbol)

#TODO 6. Cancel an Existing Order and Send a New Order
@router.post('/cancel-and-replace-order')
async def cancel_and_replace_order_endpoint(request: Request, symbol: str, cancelOrderId: str, cancelReplaceMode: int, side: str, order_type: str, quantity: float, price: float = None):
    client_ip = request.client.host
    await is_ip_allowed(client_ip)
    return await cancel_and_replace_order_controller(client_ip, symbol, cancelOrderId, cancelReplaceMode, side, order_type, quantity, price)

#TODO 7. Query Order Details
@router.get('/query-order-details')
async def query_order_details_endpoint(request: Request, symbol: str, clientOrderId: str):
    client_ip = request.client.host
    await is_ip_allowed(client_ip)
    return await query_order_details_controller(client_ip, symbol, clientOrderId)

#TODO 8. Query Open Orders
@router.get('/get-open-orders')
async def get_open_orders_endpoint(request: Request, symbol: str):
    client_ip = request.client.host
    await is_ip_allowed(client_ip)
    return await get_open_orders_controller(client_ip, symbol)

#TODO 9. Query Order History
@router.get('/get-order-history')
async def get_order_history_endpoint(
    request: Request, 
    symbol: Optional[str] = None, 
    startTime: Optional[int] = None, 
    endTime: Optional[int] = None, 
    pageIndex: Optional[int] = None, 
    pageSize: Optional[int] = None, 
    orderId: Optional[int] = None, 
    status: Optional[str] = None, 
    type: Optional[str] = None
):
    client_ip = request.client.host
    await is_ip_allowed(client_ip)
    return await get_order_history_controller(client_ip, symbol, startTime, endTime, pageIndex, pageSize, orderId, status, type)

#TODO 10. Query Transaction Details
@router.get('/get-transaction-details')
async def get_transaction_details_endpoint(request: Request, symbol: str, orderId: int, startTime: int, endTime: int, fromId: int = None, limit: int = 500):
    client_ip = request.client.host
    await is_ip_allowed(client_ip)
    return await get_transaction_details_controller(client_ip, symbol, orderId, startTime, endTime, fromId, limit)

#TODO 11. Query Trading Commission Rate
@router.get('/get-trading-commission-rate')
async def get_trading_commission_rate_endpoint(request: Request, symbol: str):
    client_ip = request.client.host
    await is_ip_allowed(client_ip)
    return await get_trading_commission_rate_controller(client_ip, symbol)

#TODO 12. Cancel All After
@router.post('/cancel-all-after')
async def cancel_all_after_endpoint(request: Request, type: str, timeOut: int):
    client_ip = request.client.host
    await is_ip_allowed(client_ip)
    return await cancel_all_after_controller(client_ip, type, timeOut)

#TODO 13. Create OCO Order
@router.post('/create-oco-order')
async def create_oco_order_endpoint(request: Request, symbol: str, side: str, quantity: float, limitPrice: float, orderPrice: float, triggerPrice: float, listClientOrderId: str = None, aboveClientOrderId: str = None, belowClientOrderId: str = None):
    client_ip = request.client.host
    await is_ip_allowed(client_ip)
    return await create_oco_order_controller(client_ip, symbol, side, quantity, limitPrice, orderPrice, triggerPrice, listClientOrderId, aboveClientOrderId, belowClientOrderId)

#TODO 14. Cancel OCO Order
@router.post('/cancel-oco-order')
async def cancel_oco_order_endpoint(request: Request, symbol: str, orderId: int, clientOrderId: str = None):
    client_ip = request.client.host
    await is_ip_allowed(client_ip)
    return await cancel_oco_order_controller(client_ip, symbol, orderId, clientOrderId)

#TODO 15. Query OCO Order List
@router.get('/query-oco-order-list')
async def query_oco_order_list_endpoint(request: Request, orderListId: int, clientOrderId: str = None):
    client_ip = request.client.host
    await is_ip_allowed(client_ip)
    return await query_oco_order_list_controller(client_ip, orderListId, clientOrderId)

#TODO 16. Query All Open OCO Orders
@router.get('/query-all-open-oco-orders')
async def query_all_open_oco_orders_endpoint(request: Request):
    client_ip = request.client.host
    await is_ip_allowed(client_ip)
    return await query_all_open_oco_orders_controller(client_ip)

#TODO 17. Query OCO History
@router.get('/query-oco-history')
async def query_oco_history_endpoint(request: Request, startTime: int, endTime: int, pageIndex: int = 1, pageSize: int = 100):
    client_ip = request.client.host
    await is_ip_allowed(client_ip)
    return await query_oco_history_controller(client_ip, startTime, endTime, pageIndex, pageSize)
