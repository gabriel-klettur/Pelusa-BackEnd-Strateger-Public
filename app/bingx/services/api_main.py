#Path: app/bingx/api/api_main.py

# Description: Main functions generic for BingX exchange
import time
from .api_utils import send_request, parse_param, date_to_milliseconds

async def get_ticker(symbol: str):
    path = '/openApi/swap/v2/quote/ticker'
    method = "GET"
    paramsMap = {
        "symbol": symbol,
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})

async def get_k_line_data(symbol, interval, limit, start_time, end_time):
    """
    Retrieves K-line data for a given symbol within a specified time interval.

    Args:
        symbol (str): The symbol for which to retrieve K-line data.
        interval (str): The time interval for the K-line data (e.g., '1m', '5m', '1h', etc.).
        limit (int): The maximum number of K-line data points to retrieve.
        start_time (datetime): The start time of the K-line data range.
        end_time (datetime): The end time of the K-line data range.

    Returns:
        dict: A dictionary containing K-line data for the specified symbol and time interval.
            The dictionary includes the following keys:
            
            - "open" (float64): The opening price of the symbol at the beginning of the interval.
            - "close" (float64): The closing price of the symbol at the end of the interval.
            - "high" (float64): The highest price of the symbol during the interval.
            - "low" (float64): The lowest price of the symbol during the interval.
            - "volume" (float64): The transaction volume of the symbol during the interval.
            - "time" (int64): The timestamp of the K-line data, in milliseconds.
    """
    payload = {}
    path = '/openApi/swap/v3/quote/klines'
    method = "GET"
    paramsMap = {
        "symbol": symbol,
        "interval": interval,
        "limit": limit,
        "startTime": date_to_milliseconds(start_time),
        "endTime": date_to_milliseconds(end_time)
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, payload)

