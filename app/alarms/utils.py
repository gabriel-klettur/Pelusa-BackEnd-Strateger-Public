# Path: app/alarms/utils.py

def convierte_temporalidad(temporalidad: str) -> str:
    conversiones = {
        '1': '1m',
        '5': '5m',
        '15': '15m',
        '30': '30m',
        '60': '1h',
        '240': '4h',
        '1440': 'D',
        '10080': 'W'
    }
    return conversiones.get(temporalidad, temporalidad)