# Path: app/strateger/models/diary.py

from sqlalchemy import Column, String, DateTime, JSON
from app.siteground.base import BaseDiary
import uuid

class DiaryEntry(BaseDiary):
    __tablename__ = 'tbl_diary'

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    titleName = Column(String(500), nullable=False)
    date = Column(DateTime, nullable=True)
    text = Column(String(5000), nullable=True)  # Especificar la longitud para la columna text
    photos = Column(JSON, nullable=True)  # Usar JSON en lugar de ARRAY
    references = Column(JSON, nullable=True)  # Usar JSON en lugar de ARRAY
