#Path: app/bingx/controllers/spot_controller.py

from fastapi import HTTPException
from app.bingx.services.api_spot import (

    #!------------------------------------------ Spot Market Data Endpoints ------------------------------------------!#
    get_spot_symbols,                           #TODO 1. Query Symbols
    get_recent_trades,                          #TODO 2. Query Recent Trades
    get_order_book,                             #TODO 3. Query Order Book
    get_kline_data,                             #TODO 4. Query Kline Data
    get_24hr_ticker,                            #TODO 5. Query 24hr Ticker Price Change Statistics
    get_order_book_aggregation,                 #TODO 6. Query Order Book Aggregated
    get_symbol_price,                           #TODO 7. Query Symbol Price Ticker
    get_order_book_ticker,                      #TODO 8. Query Order Book Ticker
    get_historical_kline,                       #TODO 9. Query Historical Kline Data
    get_old_trades,                             #TODO 10. Query Old Trades

    #!----------------------------------- Wallet Deposits and Withdrawals Endpoints -----------------------------------!#
    get_spot_deposit_records,                   #TODO 1. Deposit Records
    get_withdraw_records,                       #TODO 2. Withdraw Records
    get_currency_info,                          #TODO 3. Query Currency Information
    withdraw,                                   #TODO 4. Withdraw
    get_deposit_address,                        #TODO 5. Query Deposit Address
    get_deposit_risk_control_records,           #TODO 6. Query Deposit Risk Control Records

    #!----------------------------------------- Fund Account Endpoints -----------------------------------------------!#
    get_balance_spot,                           #TODO 1. Query Assets
    transfer_asset,                             #TODO 2. Asset Transfer
    get_transfer_records,                       #TODO 3. Asset Transfer Records
    main_account_internal_transfer,             #TODO 4. Main Account Internal Transfer
    get_internal_transfer_records,              #TODO 5. Main Account Internal Transfer Records

    #!------------------------------------------- Spot Trades Endpoints -----------------------------------------------!#
    place_order,                                #TODO 1. Place Order
    place_multiple_orders,                      #TODO 2. Place Multiple Orders
    cancel_order,                               #TODO 3. Cancel Order
    cancel_multiple_orders,                     #TODO 4. Cancel Multiple Orders
    cancel_all_open_orders,                     #TODO 5. Cancel All Open Orders
    cancel_and_replace_order,                   #TODO 6. Cancel an Existing Order and Send a New Order
    query_order_details,                        #TODO 7. Query Order Details
    get_open_orders,                            #TODO 8. Query Open Orders
    get_order_history,                          #TODO 9. Query Order History
    get_transaction_details,                    #TODO 10. Query Transaction Details
    get_trading_commission_rate,                #TODO 11. Query Trading Commission Rate
    cancel_all_after,                           #TODO 12. Cancel All After
    create_oco_order,                           #TODO 13. Create OCO Order
    cancel_oco_order,                           #TODO 14. Cancel OCO Order
    query_oco_order_list,                       #TODO 15. Query OCO Order List
    query_all_open_oco_orders,                  #TODO 16. Query All Open OCO Orders
    query_oco_history                           #TODO 17. Query OCO History

)
from loguru import logger

#!-----------------------------------------------------------------------------------------------------------!#
#!--------------------------------------  Spot Market Data Endpoints  ---------------------------------------!#
#!-----------------------------------------------------------------------------------------------------------!#

#TODO 1. Query Symbols
async def get_spot_symbols_controller(client_ip: str):
    logger.info(f"Fetching spot symbols from {client_ip}")
    try:
        result = await get_spot_symbols()
        return result
    except Exception as e:
        logger.error(f"Error fetching spot symbols: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    
#TODO 2. Query Recent Trades
async def get_recent_trades_controller(client_ip: str, symbol: str, limit: int = 100):
    logger.info(f"Fetching recent trades for {symbol} from {client_ip}")
    try:
        result = await get_recent_trades(symbol, limit)
        return result
    except Exception as e:
        logger.error(f"Error fetching recent trades: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

#TODO 3. Query Order Book
async def get_order_book_controller(client_ip: str, symbol: str, limit: int = 100):
    logger.info(f"Fetching order book for {symbol} from {client_ip}")
    try:
        result = await get_order_book(symbol, limit)
        return result
    except Exception as e:
        logger.error(f"Error fetching order book: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

#TODO 4. Query Kline Data
async def get_kline_data_controller(client_ip: str, symbol: str, interval: str, limit: int = 500, startTime: int = None, endTime: int = None):
    logger.info(f"Fetching kline data for {symbol} from {client_ip}")
    try:
        result = await get_kline_data(symbol, interval, limit, startTime, endTime)
        return result
    except Exception as e:
        logger.error(f"Error fetching kline data: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

#TODO 5. Query 24hr Ticker Price Change Statistics
async def get_24hr_ticker_controller(client_ip: str, symbol: str):
    logger.info(f"Fetching 24hr ticker for {symbol} from {client_ip}")
    try:
        result = await get_24hr_ticker(symbol)
        return result
    except Exception as e:
        logger.error(f"Error fetching 24hr ticker: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

#TODO 6. Query Order Book Aggregated
async def get_order_book_aggregation_controller(client_ip: str, depth: int, order_type: str, symbol: str):
    logger.info(f"Fetching order book aggregation for {symbol} from {client_ip}")
    try:
        result = await get_order_book_aggregation(symbol, depth, order_type)
        return result
    except Exception as e:
        logger.error(f"Error fetching order book aggregation: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

#TODO 7. Query Symbol Price Ticker
async def get_symbol_price_controller(client_ip: str, symbol: str):
    logger.info(f"Fetching symbol price ticker for {symbol} from {client_ip}")
    try:
        result = await get_symbol_price(symbol)
        return result
    except Exception as e:
        logger.error(f"Error fetching symbol price ticker: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

#TODO 8. Query Order Book Ticker
async def get_order_book_ticker_controller(client_ip: str, symbol: str):
    logger.info(f"Fetching order book ticker for {symbol} from {client_ip}")
    try:
        result = await get_order_book_ticker(symbol)
        return result
    except Exception as e:
        logger.error(f"Error fetching order book ticker: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    
#TODO 9. Query Historical Kline Data
async def get_historical_kline_controller(client_ip: str, symbol: str, interval: str, startTime: int, endTime: int, limit: int = 500):
    logger.info(f"Fetching historical kline data for {symbol} from {client_ip}")
    try:
        result = await get_historical_kline(symbol, interval, startTime, endTime, limit)
        return result
    except Exception as e:
        logger.error(f"Error fetching historical kline data: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    
#TODO 10. Query Old Trades
async def get_old_trades_controller(client_ip: str, symbol: str, limit: int = 100, fromId: int = None):
    logger.info(f"Fetching old trades for {symbol} from {client_ip}")
    try:
        result = await get_old_trades(symbol, limit, fromId)
        return result
    except Exception as e:
        logger.error(f"Error fetching old trades: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))


#!--------------------------------------------------------------------------------------------------------------------------!#
#!--------------------------------------  Wallet Deposits and Withdrawals Endpoints  ---------------------------------------!#
#!--------------------------------------------------------------------------------------------------------------------------!#

#TODO 1. Deposit Records
async def get_spot_deposit_records_controller(client_ip: str):
    logger.info(f"Fetching spot deposit records from {client_ip}")
    try:
        result = await get_spot_deposit_records()
        return result
    except Exception as e:
        logger.error(f"Error fetching spot deposit records: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    
#TODO 2. Withdraw Records
async def get_withdraw_records_controller(client_ip: str, coin: str, withdrawOrderId: str, status: int, startTime: int, endTime: int, limit: int = 100):
    logger.info(f"Fetching withdraw records from {client_ip}")
    try:
        result = await get_withdraw_records(coin, withdrawOrderId, status, startTime, endTime, limit)
        return result
    except Exception as e:
        logger.error(f"Error fetching withdraw records: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    
#TODO 3. Query Currency Information
async def get_currency_info_controller(client_ip: str):
    logger.info(f"Fetching currency information from {client_ip}")
    try:
        result = await get_currency_info()
        return result
    except Exception as e:
        logger.error(f"Error fetching currency information: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    
#TODO 4. Withdraw
async def withdraw_controller(client_ip: str, coin: str, amount: float, address: str, network: str, addressTag: str = None, walletType: str = None, withdrawOrderId: str = None):
    logger.info(f"Withdrawing {amount} {coin} to {address} from {client_ip}")
    try:
        result = await withdraw(coin, amount, address, network, addressTag, walletType, withdrawOrderId)
        return result
    except Exception as e:
        logger.error(f"Error withdrawing: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    
#TODO 5. Query Deposit Address
async def get_deposit_address_controller(client_ip: str, coin: str, offset: int = 0, limit: int = 1000):
    logger.info(f"Fetching deposit address for {coin} from {client_ip}")
    try:
        result = await get_deposit_address(coin, offset, limit)
        return result
    except Exception as e:
        logger.error(f"Error fetching deposit address: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    
#TODO 6. Query Deposit Risk Control Records
async def get_deposit_risk_control_records_controller(client_ip: str):
    logger.info(f"Fetching deposit risk control records from {client_ip}")
    try:
        result = await get_deposit_risk_control_records()
        return result
    except Exception as e:
        logger.error(f"Error fetching deposit risk control records: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

#!--------------------------------------------------------------------------------------------------------------------!#
#!----------------------------------------------  Fund Account Endpoints  --------------------------------------------!#
#!--------------------------------------------------------------------------------------------------------------------!#

#TODO 1. Query Assets
async def get_balance_spot_controller(client_ip: str):
    logger.info(f"Fetching balance from {client_ip}")
    try:
        result = await get_balance_spot()
        return result
    except Exception as e:
        logger.error(f"Error fetching spot balance: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

#TODO 2. Asset Transfer
async def transfer_asset_controller(client_ip: str, asset: str, amount: float, transfer_type: int):
    logger.info(f"Transferring {amount} {asset} from {client_ip}")
    try:
        result = await transfer_asset(asset, amount, transfer_type)
        return result
    except Exception as e:
        logger.error(f"Error transferring asset: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    
#TODO 3. Asset Transfer Records
async def get_transfer_records_controller(client_ip: str, transfer_type: int, startTime: int, endTime: int, tranId = None, size = 10):
    logger.info(f"Fetching transfer records from {client_ip}")
    try:
        result = await get_transfer_records(transfer_type, startTime, endTime, tranId, size)
        return result
    except Exception as e:
        logger.error(f"Error fetching transfer records: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

#TODO 4. Main Account Internal Transfer
async def main_account_internal_transfer_controller(client_ip: str, coin: str, amount: float, userAccountType: int, walletType: int, callingCode = None, transferClientId = None):
    logger.info(f"Transferring {amount} from main account to spot account from {client_ip}")
    try:
        result = await main_account_internal_transfer(coin, amount, userAccountType, walletType, callingCode, transferClientId)
        return result
    except Exception as e:
        logger.error(f"Error transferring asset: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

    
#TODO 5. Main Account Internal Transfer Records
async def get_internal_transfer_records_controller(client_ip: str, coin: str, startTime: int, endTime: int, transferClientId: str = None, offset: int = 0, limit: int = 100):
    logger.info(f"Fetching internal transfer records from {client_ip}")
    try:
        result = await get_internal_transfer_records(coin, startTime, endTime, transferClientId, offset, limit)
        return result
    except Exception as e:
        logger.error(f"Error fetching internal transfer records: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

#!------------------------------------------------------------------------------------------------------------------!#
#!---------------------------------------------  Spot Trades Endpoints  --------------------------------------------!#
#!------------------------------------------------------------------------------------------------------------------!#

#TODO 1. Place Order
async def place_order_controller(client_ip: str, symbol: str, side: str, order_type: str, quantity: float, price: float = None, stopPrice: float = None, quoteOrderQty: float = None, newClientOrderId: str = None, timeInForce: str = None):
    logger.info(f"Placing order for {quantity} {symbol} from {client_ip}")
    try:
        result = await place_order(symbol, side, order_type, quantity, price)
        return result
    except Exception as e:
        logger.error(f"Error placing order: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    
#TODO 2. Place Multiple Orders
async def place_multiple_orders_controller(client_ip: str, orders_data: list):
    logger.info(f"Placing multiple orders from {client_ip}")
    try:
        result = await place_multiple_orders(orders_data)
        return result
    except Exception as e:
        logger.error(f"Error placing multiple orders: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    
#TODO 3. Cancel Order
async def cancel_order_controller(client_ip: str, symbol: str, clientOrderId: str):
    logger.info(f"Cancelling order {clientOrderId} for {symbol} from {client_ip}")
    try:
        result = await cancel_order(symbol, clientOrderId)
        return result
    except Exception as e:
        logger.error(f"Error cancelling order: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

#TODO 4. Cancel Multiple Orders
async def cancel_multiple_orders_controller(client_ip: str, symbol: str, orderIds: list, clientOrderId: str = None):
    logger.info(f"Cancelling multiple orders for {symbol} from {client_ip}")
    try:
        result = await cancel_multiple_orders(symbol, orderIds, clientOrderId)
        return result
    except Exception as e:
        logger.error(f"Error cancelling multiple orders: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    
#TODO 5. Cancel All Open Orders
async def cancel_all_open_orders_controller(client_ip: str, symbol: str):
    logger.info(f"Cancelling all open orders for {symbol} from {client_ip}")
    try:
        result = await cancel_all_open_orders(symbol)
        return result
    except Exception as e:
        logger.error(f"Error cancelling all open orders: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

#TODO 6. Cancel an Existing Order and Send a New Order
async def cancel_and_replace_order_controller(client_ip: str, symbol: str, cancelOrderId: str, cancelReplaceMode: int, side: str, order_type: str, quantity: float, price: float = None):
    logger.info(f"Cancelling order {cancelOrderId} and placing new order for {quantity} {symbol} from {client_ip}")
    try:
        result = await cancel_and_replace_order(symbol, cancelOrderId, cancelReplaceMode, side, order_type, quantity, price)
        return result
    except Exception as e:
        logger.error(f"Error cancelling and replacing order: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    
#TODO 7. Query Order Details
async def query_order_details_controller(client_ip: str, symbol: str, clientOrderId: str):
    logger.info(f"Fetching order details for {clientOrderId} from {client_ip}")
    try:
        result = await query_order_details(symbol, clientOrderId)
        return result
    except Exception as e:
        logger.error(f"Error fetching order details: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

#TODO 8. Query Open Orders
async def get_open_orders_controller(client_ip: str, symbol: str):
    logger.info(f"Fetching open orders for {symbol} from {client_ip}")
    try:
        result = await get_open_orders(symbol)
        return result
    except Exception as e:
        logger.error(f"Error fetching open orders: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    
#TODO 9. Query Order History
async def get_order_history_controller(
    client_ip: str,
    symbol: str = None,
    startTime: int = None,
    endTime: int = None,
    pageIndex: int = None,
    pageSize: int = None,
    orderId: int = None,
    status: str = None,
    type: str = None,
):
    logger.info(f"Fetching order history for {symbol} from {client_ip}")
    try:
        result = await get_order_history(symbol, startTime, endTime, pageIndex, pageSize, orderId, status, type)
        return result
    except Exception as e:
        logger.error(f"Error fetching order history: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

#TODO 10. Query Transaction Details
async def get_transaction_details_controller(client_ip: str, symbol: str, orderId: int, startTime: int, endTime: int, fromId: int = None, limit: int = 500):
    logger.info(f"Fetching transaction details for {orderId} from {client_ip}")
    try:
        result = await get_transaction_details(symbol, orderId, startTime, endTime, fromId, limit)
        return result
    except Exception as e:
        logger.error(f"Error fetching transaction details: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    
#TODO 11. Query Trading Commission Rate
async def get_trading_commission_rate_controller(client_ip: str, symbol: str):
    logger.info(f"Fetching trading commission rate from {client_ip}")
    try:
        result = await get_trading_commission_rate(symbol)
        return result
    except Exception as e:
        logger.error(f"Error fetching trading commission rate: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

#TODO 12. Cancel All After
async def cancel_all_after_controller(client_ip: str, type: str, timeOut: int):
    logger.info(f"Cancelling all orders after {timeOut} type {type} from {client_ip}")
    try:
        result = await cancel_all_after(type, timeOut)
        return result
    except Exception as e:
        logger.error(f"Error cancelling all after: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    
#TODO 13. Create OCO Order
async def create_oco_order_controller(client_ip: str, symbol: str, side: str, quantity: float, limitPrice: float, orderPrice: float, triggerPrice: float, listClientOrderId: str = None, aboveClientOrderId: str = None, belowClientOrderId: str = None):
    logger.info(f"Creating OCO order for {quantity} {symbol} from {client_ip}")
    try:
        result = await create_oco_order(symbol, side, quantity, limitPrice, orderPrice, triggerPrice, listClientOrderId, aboveClientOrderId, belowClientOrderId)
        return result
    except Exception as e:
        logger.error(f"Error creating OCO order: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    
#TODO 14. Cancel OCO Order
async def cancel_oco_order_controller(client_ip: str, symbol: str, orderId: int, clientOrderId: str = None):
    logger.info(f"Cancelling OCO order {orderId} from {client_ip}")
    try:
        result = await cancel_oco_order(symbol, orderId, clientOrderId)
        return result
    except Exception as e:
        logger.error(f"Error cancelling OCO order: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    
#TODO 15. Query OCO Order List
async def query_oco_order_list_controller(client_ip: str, orderListId: int, clientOrderId: str = None):
    logger.info(f"Fetching OCO order list from {client_ip}")
    try:
        result = await query_oco_order_list(orderListId, clientOrderId)
        return result
    except Exception as e:
        logger.error(f"Error fetching OCO order list: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

#TODO 16. Query All Open OCO Orders
async def query_all_open_oco_orders_controller(client_ip: str):
    logger.info(f"Fetching all open OCO orders from {client_ip}")
    try:
        result = await query_all_open_oco_orders()
        return result
    except Exception as e:
        logger.error(f"Error fetching all open OCO orders: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

#TODO 17. Query OCO History
async def query_oco_history_controller(client_ip: str, startTime: int, endTime: int, pageIndex: int = 1, pageSize: int = 100):
    logger.info(f"Fetching OCO history from {client_ip}")
    try:
        result = await query_oco_history(startTime, endTime, pageIndex, pageSize)
        return result
    except Exception as e:
        logger.error(f"Error fetching OCO history: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))