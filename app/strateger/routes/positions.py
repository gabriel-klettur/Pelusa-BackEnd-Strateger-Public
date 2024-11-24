# Path: app/strateger/routes/positions.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.siteground.database import get_db_positions
from app.strateger.schemas.positions import PositionCreate, PositionResponse
from app.strateger.models.positions import Position

router = APIRouter()

@router.post("/", response_model=PositionResponse)
async def create_position(position: PositionCreate, db: AsyncSession = Depends(get_db_positions)):
    db_position = Position(**position.dict())
    db.add(db_position)
    await db.commit()
    await db.refresh(db_position)
    return db_position

# Puedes agregar más rutas para obtener, actualizar y eliminar posiciones.
