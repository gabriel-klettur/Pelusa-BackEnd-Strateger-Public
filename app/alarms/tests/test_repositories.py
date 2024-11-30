#Path: app/alarms/tests/test_repositories.py

from unittest.mock import AsyncMock, MagicMock
import pytest
from sqlalchemy.ext.asyncio import AsyncSession
from app.alarms.repositories import get_alarms
from app.alarms.models import Alarm
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException

MOCK_ALARMS = [
    Alarm(
        id=7,
        Ticker="BTCUSDT.PS",
        Temporalidad="1m",
        Quantity=0.01,
        Entry_Price_Alert=67813.17,
        Exit_Price_Alert=None,
        Time_Alert="2024-05-24 14:46:00",
        Order="open long",
        Strategy="Stochastic_v1",
        raw_data='{"Ticker":"BTCUSDT.PS","Temporalidad":"1","Quantity":"0.01","Entry_Price_Alert":"67813.17","Exit_Price_Alert":null,"Time_Alert":"14:46:00_24/5/2024","Order":"open long","Strategy":"Stochastic_v1"}'
    ),
    Alarm(
        id=8,
        Ticker="BTCUSDT.PS",
        Temporalidad="1m",
        Quantity=0.0073318072,
        Entry_Price_Alert=68196.01,
        Exit_Price_Alert=None,
        Time_Alert="2024-05-24 15:45:00",
        Order="open long",
        Strategy="Stochastic_v1",
        raw_data='{"Ticker":"BTCUSDT.PS","Temporalidad":"1","Quantity":"0.0073318072","Entry_Price_Alert":"68196.01","Exit_Price_Alert":null,"Time_Alert":"15:45:00_24/5/2024","Order":"open long","Strategy":"Stochastic_v1"}'
    )
]

@pytest.mark.asyncio
async def test_get_alarms_success():
    """
    Test that get_alarms returns a valid list of alarms.
    """
    db_mock = AsyncMock(spec=AsyncSession)

    # Configurar el mock para scalars().all()
    mock_result = MagicMock()
    mock_scalars = MagicMock()
    mock_scalars.all.return_value = MOCK_ALARMS
    mock_result.scalars.return_value = mock_scalars
    db_mock.execute.return_value = mock_result

    # Llamar a la función
    result = await get_alarms(db=db_mock, limit=10, offset=0, latest=False)

    # Verificar resultados
    assert isinstance(result, list)
    assert len(result) == len(MOCK_ALARMS)
    assert result == MOCK_ALARMS

@pytest.mark.asyncio
async def test_get_alarms_empty_result():
    """
    Test that get_alarms returns an empty list when no alarms are found.
    """
    db_mock = AsyncMock(spec=AsyncSession)

    # Configurar el mock para devolver una lista vacía
    mock_result = MagicMock()
    mock_scalars = MagicMock()
    mock_scalars.all.return_value = []
    mock_result.scalars.return_value = mock_scalars
    db_mock.execute.return_value = mock_result

    # Llamar a la función
    result = await get_alarms(db=db_mock, limit=10, offset=0, latest=False)

    # Verificar resultados
    assert isinstance(result, list)
    assert len(result) == 0


@pytest.mark.asyncio
async def test_get_alarms_sqlalchemy_error():
    """
    Test that get_alarms raises an HTTPException when a SQLAlchemyError occurs.
    """
    db_mock = AsyncMock(spec=AsyncSession)

    # Configurar el mock para lanzar un error de SQLAlchemy
    db_mock.execute.side_effect = SQLAlchemyError("Database error")

    # Llamar a la función y verificar que lanza una excepción
    with pytest.raises(HTTPException) as exc_info:
        await get_alarms(db=db_mock, limit=10, offset=0, latest=False)

    assert exc_info.value.status_code == 500
    assert exc_info.value.detail == "Database query failed"

@pytest.mark.asyncio
async def test_get_alarms_general_error():
    """
    Test that get_alarms raises an HTTPException when a general error occurs.
    """
    db_mock = AsyncMock(spec=AsyncSession)

    # Configurar el mock para lanzar un error genérico
    db_mock.execute.side_effect = Exception("General error")

    # Llamar a la función y verificar que lanza una excepción
    with pytest.raises(HTTPException) as exc_info:
        await get_alarms(db=db_mock, limit=10, offset=0, latest=False)

    assert exc_info.value.status_code == 500
    assert exc_info.value.detail == "Unexpected error occurred while fetching alarms"