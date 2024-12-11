# Path: app/alarms/schemas.py
# Descripción: Esquemas de Pydantic para las alarmas
from pydantic import BaseModel, ConfigDict
from typing import Optional

class AlarmResponse(BaseModel):
    id: int
    Ticker: str
    Interval: str
    Quantity: Optional[str] = None
    Price_Alert: Optional[str] = None    
    Time_Alert: str
    Order: str
    Strategy: Optional[str] = None
    
    model_config = ConfigDict(from_attributes=True)
