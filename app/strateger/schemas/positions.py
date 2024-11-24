from pydantic import BaseModel
from typing import List

class PositionBase(BaseModel):
    account_name: str
    account_type: str
    symbol: str
    positionId: str
    positionSide: str
    isolated: bool
    positionAmt: str
    availableAmt: str
    unrealizedProfit: str
    realisedProfit: str
    initialMargin: str
    margin: str
    avgPrice: str
    liquidationPrice: float
    leverage: int
    positionValue: str
    markPrice: str
    riskRate: str
    maxMarginReduction: str
    pnlRatio: str
    updateTime: int
    dateTime: str  # Nueva columna para fecha y hora

class PositionCreate(PositionBase):
    pass

class PositionUpdate(PositionBase):
    pass

class PositionInDB(PositionBase):
    id: int

    class Config:
        from_attributes = True

class PositionResponse(BaseModel):
    code: int
    msg: str
    timestamp: int
    data: List[PositionInDB]

    class Config:
        from_attributes = True
