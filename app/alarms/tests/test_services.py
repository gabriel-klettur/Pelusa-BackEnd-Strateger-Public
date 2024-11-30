#Path: app/alarms/tests/test_services.py

from unittest.mock import AsyncMock, patch, MagicMock
import pytest
from fastapi import HTTPException
from app.alarms.services import fetch_alarms
from app.alarms.schemas import AlarmResponse

# Case 1: Repositories Error
@patch("app.alarms.repositories.get_alarms", new=AsyncMock(side_effect=Exception("Database error")))
@pytest.mark.asyncio
async def test_fetch_alarms_repository_error():
    """
    Test fetch_alarms raises HTTPException when get_alarms fails.
    """
    db_mock = AsyncMock()  # Simula la sesión de la base de datos

    with pytest.raises(HTTPException) as exc_info:
        await fetch_alarms(limit=2, offset=0, latest=True, db=db_mock)

    # Verifica que se lanza un HTTPException con código 500
    assert exc_info.value.status_code == 500
    assert exc_info.value.detail == "There was an error fetching the alarms"
