#Path: app/strateger/models/strategies.py

from sqlalchemy import Column, Integer, String, Boolean, Float, Text
from app.siteground.base import BaseEstrategias

class Strategy(BaseEstrategias):
    __tablename__ = 'tbl_strategies'

    id = Column(Integer, primary_key=True, index=True)
    alarmName = Column(String(100), nullable=True)
    isOn = Column(Boolean, nullable=True)
    account_name = Column(String(255), nullable=True)
    account_type = Column(String(255), nullable=True)
    ticker = Column(String(10), nullable=True)
    resultadoAcc = Column(String(100), nullable=True)
    description = Column(String(500), nullable=True)
    onStartDate = Column(String(50), nullable=True)
    offEndDate = Column(String(50), nullable=True)
    longEntryOrder = Column(String(100), nullable=True)
    longCloseOrder = Column(String(100), nullable=True)
    longEntryIndicator = Column(String(100), nullable=True)
    longCloseIndicator = Column(String(100), nullable=True)
    longPyramiding = Column(Integer, nullable=True)
    longLeverage = Column(Float, nullable=True)
    longQuantity = Column(Float, nullable=True)
    longTPPerOrder = Column(Float, nullable=True)
    longTPGeneral = Column(Float, nullable=True)
    longSLPerOrder = Column(Float, nullable=True)
    longSLGeneral = Column(Float, nullable=True)
    shortEntryOrder = Column(String(100), nullable=True)
    shortCloseOrder = Column(String(100), nullable=True)
    shortEntryIndicator = Column(String(100), nullable=True)
    shortCloseIndicator = Column(String(100), nullable=True)
    shortPyramiding = Column(Integer, nullable=True)
    shortLeverage = Column(Float, nullable=True)
    shortQuantity = Column(Float, nullable=True)
    shortTPPerOrder = Column(Float, nullable=True)
    shortTPGeneral = Column(Float, nullable=True)
    shortSLPerOrder = Column(Float, nullable=True)
    shortSLGeneral = Column(Float, nullable=True)
