# Path: app/strateger/models/accounts.py

from sqlalchemy import Column, String, Float, DateTime, Integer
from app.siteground.base import BaseAccounts  # O la base de tu modelo, si tiene otro nombre

class Account(BaseAccounts):
    __tablename__ = 'tbl_bingx_account'

    id = Column(Integer, primary_key=True, index=True)
    accountName = Column(String(50), nullable=False)
    accountType = Column(String(50), nullable=False)
    asset = Column(String(50), nullable=False)
    balance = Column(Float, nullable=False)
    equity = Column(Float, nullable=True)
    unrealizedProfit = Column(Float, nullable=True)
    realizedProfit = Column(Float, nullable=True)
    dateTime = Column(DateTime, nullable=False)
    availableMargin = Column(Float, nullable=True)
    usedMargin = Column(Float, nullable=True)
