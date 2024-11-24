# Path: app/klinedata/schemas.py

from pydantic import BaseModel, constr
from enum import Enum

class Interval(str, Enum):
    one_minute = '1m'
    five_minutes = '5m'
    fifteen_minutes = '15m'
    thirty_minutes = '30m'
    one_hour = '1h'
    four_hours = '4h'
    one_day = 'D'
    one_week = 'W'
    one_month = 'M'

class KlineDataCreate(BaseModel):
    symbol: str
    intervals: Interval
    open: float
    close: float
    high: float
    low: float
    volume: float
    time: int

    class Config:
        from_attributes = True
