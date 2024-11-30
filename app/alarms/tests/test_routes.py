#Path: app/alarms/tests/test_routes.py

from unittest.mock import patch, AsyncMock
from fastapi.testclient import TestClient
from fastapi import HTTPException
from app.main import app
from app.config import settings

client = TestClient(app)

# Case 1: Simple Success
# Right token, right IP, right parameters
@patch("app.alarms.routes.fetch_alarms", new=AsyncMock(return_value=[]))  # Mock vacío
@patch("app.alarms.routes.is_ip_allowed", new=AsyncMock(return_value=True))  # Simula que la IP está permitida
def test_get_alarms_endpoint_success():
    """
    Test the /alarms endpoint with valid parameters.
    """
    response = client.get(
        "/alarms/alarms",  # Ruta completa
        headers={
            "Authorization": "Bearer valid_token",
            "X-Forwarded-For": "127.0.0.1"  # IP permitida
        },
        params={"limit": 5, "offset": 0, "latest": "true"}
    )
    # Verificar estado 200
    assert response.status_code == 200

    # Verificar que la respuesta sea una lista
    assert isinstance(response.json(), list)

#!----------------------------- TOKEN ---------------------------------------------------

# Case 2: Unauthorized Access
@patch("app.alarms.routes.is_ip_allowed", new=AsyncMock(return_value=True)) 
def test_get_alarms_endpoint_unauthorized_missing_token():
    """
    Test the /alarms endpoint when the Authorization header is missing.
    """
    response = client.get(
        "/alarms/alarms",
        headers={
            "X-Forwarded-For": "127.0.0.1"  # IP permitida
        },
        params={"limit": 5, "offset": 0, "latest": "true"}
    )
    # Verificar estado 401
    assert response.status_code == 401
    
    assert response.json()["detail"] == "Invalid or missing authentication token."

# Case 3: Unauthorized Access
@patch("app.alarms.routes.is_ip_allowed", new=AsyncMock(return_value=True)) 
def test_get_alarms_endpoint_unauthorized_invalid_token():
    """
    Test the /alarms endpoint when the Authorization token is invalid.
    """
    response = client.get(
        "/alarms/alarms",
        headers={
            "Authorization": "InvalidToken",
            "X-Forwarded-For": "127.0.0.1"  
        },
        params={"limit": 5, "offset": 0, "latest": "true"}
    )    
    assert response.status_code == 401    
    assert response.json()["detail"] == "Invalid or missing authentication token."

#!----------------------------- IP ---------------------------------------------------
# Case 4: No IP provided
# Stoped by middleware out of endpoint
@patch("app.config.settings.ALLOWED_IPS", new=["127.0.0.1"])
def test_allowed_ips_middleware_missing_ip():
    """
    Test the middleware when the X-Forwarded-For header is missing.
    """
    response = client.get(
        "/alarms/alarms",
        headers={
            "Authorization": "Bearer valid_token"
        },
        params={"limit": 5, "offset": 0, "latest": "true"}
    )
    # Verificar estado 403
    assert response.status_code == 403

    # Verificar mensaje de error
    assert response.json()["detail"] == "Access forbidden: Your IP is not allowed"

# Caso 5: IP not allowed
# Stoped by middleware out of endpoint
@patch("app.config.settings.ALLOWED_IPS", new=["127.0.0.1"])
def test_allowed_ips_middleware_invalid_ip():
    """
    Test the middleware when the IP is not allowed.
    """
    response = client.get(
        "/alarms/alarms",
        headers={
            "Authorization": "Bearer valid_token",
            "X-Forwarded-For": "192.168.1.101"
        },
        params={"limit": 5, "offset": 0, "latest": "true"}
    )
    # Verificar estado 403
    assert response.status_code == 403

    # Verificar mensaje de error
    assert response.json()["detail"] == "Access forbidden: Your IP is not allowed"


#!------------------------------------------------------- INVALID RESPONSE DATA ----------------------------------------------

@patch("app.alarms.routes.is_ip_allowed", new=AsyncMock(return_value=True))  # IP permitida
@patch("app.alarms.routes.fetch_alarms", new=AsyncMock(return_value=[{"invalid_key": "value"}]))  # Datos malformados
def test_get_alarms_endpoint_invalid_response_data():
    """
    Test the /alarms endpoint when the server returns malformed or invalid data.
    """
    response = client.get(
        "/alarms/alarms",
        headers={
            "Authorization": "Bearer valid_token",
            "X-Forwarded-For": "127.0.0.1"  # IP permitida
        },
        params={"limit": 5, "offset": 0, "latest": "true"}
    )

    assert response.status_code == 400 #400 is the state code for invalid request data catched by fastapi when data is not alligned with the model


