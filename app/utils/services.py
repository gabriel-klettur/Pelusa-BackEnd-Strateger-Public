#Path: app/utils/services.py
#Description: Functions for services

import requests

def enviar_data(data, webhook_url):
    headers = {
        'Content-Type': 'text/plain; charset=utf-8',
        'User-Agent': 'PRUEBAS_V1/1.0'
    }
    try:
        response = requests.post(webhook_url, headers=headers, data=data, allow_redirects=False)        
        response.raise_for_status()                
        print(f"Datos enviados al webhook: {webhook_url}")
        
    except requests.exceptions.RequestException as e:
        print(f"Error enviando datos al webhook externo: {e}")     