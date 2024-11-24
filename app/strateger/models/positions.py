from sqlalchemy import Column, String, Boolean, Integer, Float, BigInteger
from app.siteground.base import BasePositions

class Position(BasePositions):
    __tablename__ = 'tbl_positions'

    id = Column(Integer, primary_key=True, index=True)
    account_name = Column(String(50), nullable=False)  # Puede ser: Main, Subaccount, etc.
    account_type = Column(String(50), nullable=False)  # Del tipo: 'Perp USDT-M', 'Perp COIN-M', 'Spot'
    symbol = Column(String(50), nullable=True)
    positionId = Column(String(50), nullable=True)
    positionSide = Column(String(50), nullable=True)
    isolated = Column(Boolean, nullable=True)
    positionAmt = Column(String(50), nullable=True)
    availableAmt = Column(String(50), nullable=True)
    unrealizedProfit = Column(String(50), nullable=True)
    realisedProfit = Column(String(50), nullable=True)  # Campo adicional
    initialMargin = Column(String(50), nullable=True)
    margin = Column(String(50), nullable=True)  # Campo adicional
    avgPrice = Column(String(50), nullable=True)
    liquidationPrice = Column(Float, nullable=True)
    leverage = Column(Integer, nullable=True)
    positionValue = Column(String(50), nullable=True)  # Campo adicional
    markPrice = Column(String(50), nullable=True)
    riskRate = Column(String(50), nullable=True)
    maxMarginReduction = Column(String(50), nullable=True)
    pnlRatio = Column(String(50), nullable=True)  # Campo adicional
    updateTime = Column(BigInteger, nullable=True)
    dateTime = Column(String(50), nullable=True)  # Nueva columna para fecha y hora
