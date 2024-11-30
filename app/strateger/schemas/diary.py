# Path: app/strateger/schemas/diary.py
from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import datetime

class DiaryEntryBase(BaseModel):
    date: datetime
    titleName: str
    text: str
    photos: Optional[List[str]] = []
    references: Optional[List[str]] = []

class DiaryEntryCreate(DiaryEntryBase):
    pass

class DiaryEntryUpdate(DiaryEntryBase):
    pass

class DiaryEntry(DiaryEntryBase):
    id: str

    model_config = ConfigDict(from_attributes=True)
