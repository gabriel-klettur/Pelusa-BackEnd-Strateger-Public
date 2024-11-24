from sqlalchemy.ext.asyncio import AsyncSession
from app.strateger.models.diary import DiaryEntry
from app.strateger.schemas.diary import DiaryEntryCreate, DiaryEntryUpdate
from sqlalchemy.future import select
import uuid

async def get_diary_entry(db: AsyncSession, entry_id: str):
    result = await db.execute(select(DiaryEntry).filter(DiaryEntry.id == entry_id))
    return result.scalars().first()

async def get_diary_entries(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(DiaryEntry).offset(skip).limit(limit))
    return result.scalars().all()

async def crud_create_diary_entry(db: AsyncSession, entry: DiaryEntryCreate):
    db_entry = DiaryEntry(
        id=str(uuid.uuid4()),
        titleName=entry.titleName,
        date=entry.date,
        text=entry.text,
        photos=entry.photos,
        references=entry.references
    )
    db.add(db_entry)
    await db.commit()
    await db.refresh(db_entry)
    return db_entry

async def crud_update_diary_entry(db: AsyncSession, entry_id: str, entry: DiaryEntryUpdate):
    db_entry = await get_diary_entry(db, entry_id)
    if db_entry is None:
        return None
    for key, value in entry.dict().items():
        setattr(db_entry, key, value)
    await db.commit()
    await db.refresh(db_entry)
    return db_entry

async def crud_delete_diary_entry(db: AsyncSession, entry_id: str):
    db_entry = await get_diary_entry(db, entry_id)
    if db_entry:
        await db.delete(db_entry)
        await db.commit()
    return db_entry
