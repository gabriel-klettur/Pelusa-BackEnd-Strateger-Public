import os
import csv
import asyncio
import sys
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text

# Añadir ruta del proyecto para importar app.config
sys.path.append(os.getcwd())
from app.config import settings

# Directorio de salida para CSV (por defecto data_csv en raíz)
CSV_DIR = os.getenv("CSV_DIR", os.path.join(os.getcwd(), "data_csv"))

# Mapeo: (atributo settings, nombre tabla SQLite, nombre archivo CSV)
MAPPINGS = [
    ("DATABASE_URL_DESARROLLO_ALARMAS", "alarms", "alarms.csv"),
    ("DATABASE_URL_DESARROLLO_ESTRATEGIAS", "strategies", "estrategias.csv"),
    ("DATABASE_URL_DESARROLLO_DIARY", "diary_entries", "diary.csv"),
    ("DATABASE_URL_DESARROLLO_POSITIONS", "positions", "positions.csv"),
    ("DATABASE_URL_DESARROLLO_ACCOUNTS", "accounts", "accounts.csv"),
    ("DATABASE_URL_DESARROLLO_KLINE_DATA", "kline_data", "kline_data.csv"),
    ("DATABASE_URL_DESARROLLO_ORDERS", "orders", "orders.csv"),
]

async def export_table(env_attr, table_name, filename):
    url = getattr(settings, env_attr)
    engine = create_async_engine(url)
    async with engine.connect() as conn:
        result = await conn.execute(text(f"SELECT * FROM {table_name}"))
        rows = result.fetchall()
        headers = result.keys()

    os.makedirs(CSV_DIR, exist_ok=True)
    output_path = os.path.join(CSV_DIR, filename)
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)
    print(f"[+] Exported {len(rows)} rows from {table_name} to {output_path}")

async def main():
    for env_attr, table_name, filename in MAPPINGS:
        await export_table(env_attr, table_name, filename)

if __name__ == "__main__":
    asyncio.run(main())
