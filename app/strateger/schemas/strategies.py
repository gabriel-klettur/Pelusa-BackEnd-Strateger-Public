#Path: app/strateger/schemas/strategies.py

from pydantic import BaseModel
from typing import Optional

class StrategyBase(BaseModel):
    alarmName: str
    isOn: Optional[bool] = None
    account_name: Optional[str] = None
    account_type: Optional[str] = None
    ticker: Optional[str] = None
    resultadoAcc: Optional[str] = None
    description: Optional[str] = None
    onStartDate: Optional[str] = None  # Nuevo campo
    offEndDate: Optional[str] = None  # Nuevo campo
    longEntryOrder: Optional[str] = None
    longCloseOrder: Optional[str] = None
    longEntryIndicator: Optional[str] = None
    longCloseIndicator: Optional[str] = None
    longPyramiding: Optional[int] = None
    longLeverage: Optional[float] = None
    longQuantity: Optional[float] = None
    longTPPerOrder: Optional[float] = None
    longTPGeneral: Optional[float] = None
    longSLPerOrder: Optional[float] = None
    longSLGeneral: Optional[float] = None
    shortEntryOrder: Optional[str] = None
    shortCloseOrder: Optional[str] = None
    shortEntryIndicator: Optional[str] = None
    shortCloseIndicator: Optional[str] = None
    shortPyramiding: Optional[int] = None
    shortLeverage: Optional[float] = None
    shortQuantity: Optional[float] = None
    shortTPPerOrder: Optional[float] = None
    shortTPGeneral: Optional[float] = None
    shortSLPerOrder: Optional[float] = None
    shortSLGeneral: Optional[float] = None

class StrategyCreate(StrategyBase):
    pass

class StrategyUpdate(StrategyBase):
    pass

class StrategyInDBBase(StrategyBase):
    id: int

    class Config:
        from_attributes = True  # Asegúrate de usar 'from_attributes' en lugar de 'orm_mode'

class Strategy(StrategyInDBBase):
    pass

class StrategyInDB(StrategyInDBBase):
    pass
