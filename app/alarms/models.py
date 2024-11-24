# app/alarms/models.py
# Descripción: SQLAlchemy models para las alarmas en la base de datos de Siteground

from sqlalchemy import Column, Integer, String
from app.siteground.base import BaseAlarmas

class Alarm(BaseAlarmas):
    __tablename__ = 'tbl_alarms'
    
    id = Column(Integer, primary_key=True, index=True)
    Ticker = Column(String(50), index=True)
    Temporalidad = Column(String(50))
    Quantity = Column(String(50))
    Entry_Price_Alert = Column(String(50))
    Exit_Price_Alert = Column(String(50))
    Time_Alert = Column(String(50))  # Adjusted to string to match format
    Order = Column(String(50))
    Strategy = Column(String(50))
    raw_data = Column(String(500))
