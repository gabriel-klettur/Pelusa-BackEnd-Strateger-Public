#Path: app/strateger/schemas/orders.py
#Descripción: Esquemas de Pydantic para las órdenes
from pydantic import BaseModel
from typing import Optional

class OrderCreate(BaseModel):    
    symbol: str # Ejemplo: 'BTCUSDT'
    side: str  # Ejemplo: 'buy' o 'sell'
    order_type: str  # Ejemplo: 'market' o 'limit'
    position_side: Optional[str] = None  # Ejemplo: 'long' o 'short'
    reduce_only: Optional[bool] = None
    quantity: Optional[str]
    price: Optional[str] = None
    average_price: Optional[str] = None
    status: Optional[str] = None
    profit: Optional[str] = None
    commision: Optional[str] = None    
    stop_price: Optional[str] = None
    working_type: Optional[str] = None  # Ejemplo: 'mark_price' o 'last_price'
    order_time: Optional[str] = None
    update_time: Optional[str] = None
    
    class Config:
        from_attributes = True

class OrderResponse(BaseModel):
    id: int
    symbol: str
    side: str
    order_type: str
    position_side: Optional[str] = None
    reduce_only: Optional[bool] = None
    quantity: Optional[str]
    price: Optional[str] = None
    average_price: Optional[str] = None
    status: Optional[str] = None
    profit: Optional[str] = None
    commision: Optional[str] = None
    stop_price: Optional[str] = None
    working_type: Optional[str] = None
    order_time: Optional[str] = None
    update_time: Optional[str] = None
    
    class Config:
        from_attributes = True

