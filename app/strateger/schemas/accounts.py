# Path: app/strateger/schemas/accounts.py

from pydantic import BaseModel
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

    class Config:
        from_attributes = True  # Use 'from_attributes' instead of 'orm_mode' in Pydantic V2

class AccountListResponse(BaseModel):
    code: int
    msg: str
    timestamp: int
    data: List[AccountInDB]

    class Config:
        from_attributes = True  # Use 'from_attributes' instead of 'orm_mode' in Pydantic V2
