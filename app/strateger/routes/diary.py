from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.siteground.database import get_db_diary
from app.strateger.crud.diary import get_diary_entry, get_diary_entries, crud_create_diary_entry, crud_update_diary_entry, crud_delete_diary_entry
from app.strateger.schemas.diary import DiaryEntryCreate, DiaryEntryUpdate, DiaryEntry
import shutil
import os
from app.config import settings

router = APIRouter()

if not os.path.exists(settings.UPLOAD_DIRECTORY):
    os.makedirs(settings.UPLOAD_DIRECTORY)

@router.get("/get/{entry_id}", response_model=DiaryEntry)
async def read_diary_entry(entry_id: str, db: AsyncSession = Depends(get_db_diary)):
    db_entry = await get_diary_entry(db, entry_id)
    if db_entry is None:
        raise HTTPException(status_code=404, detail="Entry not found")
    return db_entry

@router.get("/list", response_model=list[DiaryEntry])
async def read_diary_entries(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db_diary)):
    return await get_diary_entries(db, skip=skip, limit=limit)

@router.post("/upload_image")
async def upload_image(file: UploadFile = File(...)):
    try:
        file_location = f"{settings.UPLOAD_DIRECTORY}/{file.filename}"
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        return {"file_url": f"/static/{file.filename}"}
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))

@router.post("/insert", response_model=DiaryEntry)
async def create_diary_entry(entry: DiaryEntryCreate, db: AsyncSession = Depends(get_db_diary)):
    return await crud_create_diary_entry(db, entry)

@router.put("/update/{entry_id}", response_model=DiaryEntry)
async def update_diary_entry(entry_id: str, entry: DiaryEntryUpdate, db: AsyncSession = Depends(get_db_diary)):
    db_entry = await get_diary_entry(db, entry_id)
    if db_entry is None:
        raise HTTPException(status_code=404, detail="Entry not found")
    return await crud_update_diary_entry(db, entry_id, entry)

@router.delete("/delete/{entry_id}", response_model=DiaryEntry)
async def delete_diary_entry(entry_id: str, db: AsyncSession = Depends(get_db_diary)):
    db_entry = await get_diary_entry(db, entry_id)
    if db_entry is None:
        raise HTTPException(status_code=404, detail="Entry not found")
    return await crud_delete_diary_entry(db, entry_id)
