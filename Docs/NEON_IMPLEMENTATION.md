# Documentación de la Implementación de Neon en Pelusa-BackEnd-Strateger-Public

Este documento describe los pasos realizados para migrar el proyecto de SQLite/Turso a Neon PostgreSQL.

## 1. Estructura Inicial
- Varias bases de datos SQLite locales en `data_sqlite/`.
- Varias conexiones Turso en `app/turso/database.py`.
- Configuración condicionada en `app/config.py` usando `USE_TURSO`.

## 2. Configuración Unificada
1. Eliminadas todas las referencias a SQLite y Turso.
2. Renombrada carpeta `app/turso` a `app/db`.
3. `app/config.py`: eliminado `USE_TURSO`, dejado solo `DATABASE_URL`.
4. `.env`: añadido `DATABASE_URL` con la URL de Neon.

## 3. Base Declarativa
Archivo: `app/db/base.py`
```python
import sqlalchemy
from sqlalchemy.orm import declarative_base

# Declarative bases separados para cada grupo de tablas
metadata_alarmas = sqlalchemy.MetaData()
BaseAlarmas = declarative_base(metadata=metadata_alarmas)
# ... Bases para Estrategias, Diary, Positions, Accounts, KLineData, Orders
```

## 4. Engine y Sesión Únicos
Archivo: `app/db/database.py`
- Transformación de `postgres://` ➔ `postgresql+asyncpg://`.
- Remoción de `sslmode` de la URL.
- Creación de `ssl_context` y uso en `connect_args`.
- `create_async_engine` con `asyncpg`.
- `SessionLocal` con `AsyncSession`.
- Funciones:
  - `get_db()` (yield de sesión).
  - `init_db()` (crea todas las tablas con metadata múltiple).
  - `close_db()` (dispose del engine).

## 5. Actualización de Rutas
Se reemplazaron en **todas** las rutas y utilidades:
- `from app.turso.database import get_db_xxx` ➔ `from app.db.database import get_db`.
- `Depends(get_db_xxx)` ➔ `Depends(get_db)`.
- Archivos actualizados:
  - `app/alarms/routes.py`
  - `app/strateger/routes/*` (strategies, diary, accounts, orders, backtesting, positions)
  - `app/klinedata/routes.py`
  - `app/server/routes.py`
  - `app/strateger/utils/tasks.py`

## 6. Inicio de la App
En `app/main.py`, se importan `get_db`, `init_db`, `close_db`:
```python
@app.on_event("startup")
async def on_startup():
    await init_db()
@app.on_event("shutdown")
async def on_shutdown():
    await close_db()
```

## 7. Pruebas y Lanzamiento
- Instalación de dependencias: `pip install -r requirements.txt`.
- Levantar en desarrollo:
  ```bash
  python run.py  # o uvicorn app.main:app --reload
  ```
- Verificar endpoints y conexiones.

## 8. Eliminaciones
- Carpeta `data_sqlite/` y `app/turso/` renombrada.

### Conclusión
Todos los componentes del proyecto (routers, utilidades, cron-tasks) usan ahora un único Neon PostgreSQL, simplificando la arquitectura y eliminando código legado.
