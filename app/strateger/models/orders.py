#Path: app/strateger/models/orders.py
# Descripción: SQLAlchemy models para las órdenes en la base de datos de Siteground

from sqlalchemy import Column, Integer, String
from app.siteground.base import BaseOrders

class Order(BaseOrders):
    __tablename__ = 'tbl_orders'

    id = Column(Integer, primary_key=True, index=True)
    side = Column(String(50))
    order_type = Column(String(50))
    position_side = Column(String(50))
    reduce_only = Column(String(50))
    quantity = Column(String(50))
    price = Column(String(50))
    average_price = Column(String(50))
    status = Column(String(50))
    profit = Column(String(50))
    commision = Column(String(50))
    stop_price = Column(String(50))
    working_type = Column(String(50))
    order_time = Column(String(50))
    update_time = Column(String(50))