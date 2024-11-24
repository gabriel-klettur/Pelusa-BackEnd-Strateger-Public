#Path: app/strateger/crud/orders.py

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.strateger.models.orders import Order

async def save_order(db: AsyncSession, variables: dict):
    db_order = Order(
        side=variables.get('side'),
        order_type=variables.get('order_type'),
        position_side=variables.get('position_side'),
        reduce_only=variables.get('reduce_only'),
        quantity=variables.get('quantity'),
        price=variables.get('price'),
        average_price=variables.get('average_price'),
        status=variables.get('status'),
        profit=variables.get('profit'),
        commision=variables.get('commision'),
        stop_price=variables.get('stop_price'),
        working_type=variables.get('working_type'),
        order_time=variables.get('order_time'),
        update_time=variables.get('update_time')
    )
    db.add(db_order)
    await db.commit()
    await db.refresh(db_order)
    return db_order

async def get_orders(db: AsyncSession, limit: int = 10, offset: int = 0, latest: bool = False):
    query = select(Order).offset(offset).limit(limit)
    if latest:
        query = query.order_by(Order.id.desc())
    result = await db.execute(query)
    return result.scalars().all()