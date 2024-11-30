# Path: app/strateger/schemas/accounts.py

from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional, List

class AccountBase(BaseModel):
    accountName: str
    accountType: str
    asset: str
    balance: float
    equity: Optional[float] = None
    unrealizedProfit: Optional[float] = None
    realizedProfit: Optional[float] = None
    dateTime: datetime
    availableMargin: Optional[float] = None
    usedMargin: Optional[float] = None

class AccountInDB(AccountBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

class AccountListResponse(BaseModel):
    code: int
    msg: str
    timestamp: int
    data: List[AccountInDB]

    model_config = ConfigDict(from_attributes=True)
