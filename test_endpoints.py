#!/usr/bin/env python3
"""
Script para probar todos los endpoints de la aplicación FastAPI.
Utiliza el OpenAPI spec en /openapi.json para descubrir rutas.
"""
import os
import requests

def main():
    base_url = os.getenv("BASE_URL", "http://localhost:8000")
    # Obtener spec OpenAPI
    spec = requests.get(f"{base_url}/openapi.json").json()
    paths = spec.get("paths", {})

    for path, methods in paths.items():
        for method, details in methods.items():
            url = base_url + path
            # Reemplazar parámetros de ruta con valores dummy
            for param in details.get("parameters", []):
                if param.get("in") == "path":
                    name = param["name"]
                    typ = param.get("schema", {}).get("type", "string")
                    val = "1" if typ == "integer" else "test"
                    url = url.replace(f"{{{name}}}", val)
            # Realizar petición
            try:
                if method.lower() in ("post", "put", "patch"):  # enviar JSON vacío
                    resp = getattr(requests, method)(url, json={})
                else:
                    resp = getattr(requests, method)(url)
                print(f"{method.upper()} {url} -> {resp.status_code}")
                try:
                    print(resp.json())
                except ValueError:
                    print(resp.text)
            except Exception as e:
                print(f"Error llamando {method.upper()} {url}: {e}")

if __name__ == "__main__":
    main()
