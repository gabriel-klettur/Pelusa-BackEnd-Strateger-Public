#Path: app/strateger/schemas/backtesting.py

from pydantic import BaseModel, ConfigDict
from typing import Optional

class BacktestBase(BaseModel):
    backtest_id: int
    strategy_id: int
    ticker: str
    start_date: str
    end_date: str
    results: str

class BacktestCreate(BacktestBase):
    pass

class BacktestUpdate(BacktestBase):
    pass

class BacktestInDBBase(BacktestBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

class Backtest(BacktestInDBBase):
    pass

class BacktestInDB(BacktestInDBBase):
    pass
