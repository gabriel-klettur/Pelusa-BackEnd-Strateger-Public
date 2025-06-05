# Neon PostgreSQL - Guía de Inicio

Este documento explica cómo configurar y utilizar Neon (una plataforma de PostgreSQL serverless) en un proyecto de Python.

## 1. Registro en Neon
1. Ve a https://neon.tech y crea una cuenta.
2. Crea un nuevo proyecto y un clúster de base de datos.

## 2. Obtención de la cadena de conexión
1. En el panel del clúster, selecciona **Connect**.
2. Copia la URL de conexión. Debe tener el formato:
   ```
   postgres://<usuario>:<password>@<host>:<puerto>/<database>?sslmode=require
   ```

## 3. Variables de entorno
Crea un archivo `.env` en la raíz de tu proyecto e incluye:
```ini
DATABASE_URL="postgres://<usuario>:<password>@<host>:<puerto>/<database>?sslmode=require"
```

## 4. Dependencias
Instala las siguientes librerías:
```bash
pip install sqlalchemy asyncpg python-dotenv
```

## 5. Configuración en Python
```python
import os
import ssl
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

# Cargar variables de .env
load_dotenv()

# Transformar URL para asyncpg
db_url = os.getenv("DATABASE_URL")
if db_url.startswith("postgres://"):
    db_url = db_url.replace("postgres://", "postgresql+asyncpg://", 1)
# Remover sslmode de la query
if "?" in db_url:
    base_url, query = db_url.split("?", 1)
    params = [p for p in query.split("&") if not p.startswith("sslmode=")]
    db_url = f"{base_url}?{'&'.join(params)}" if params else base_url

# Crear contexto SSL
essl_ctx = ssl.create_default_context()

engine = create_async_engine(
    db_url,
    pool_recycle=3600,
    pool_pre_ping=True,
    connect_args={"ssl": ssl_ctx}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession
)

async def get_db():
    async with SessionLocal() as db:
        yield db
```

## 6. Uso con FastAPI
```python
from fastapi import Depends, FastAPI
from sqlalchemy.ext.asyncio import AsyncSession
from .database import get_db

app = FastAPI()

@app.get("/items")
async def read_items(db: AsyncSession = Depends(get_db)):
    # realiza consultas...
    return []
```

## 7. Migrations (opcional)
Para manejar migraciones de esquema, puedes usar Alembic:
1. `alembic init alembic`
2. En `alembic.ini`, ajusta `sqlalchemy.url = <db_url>`.
3. Genera y aplica migraciones.

---

¡Listo! Ahora tu proyecto está conectado a Neon PostgreSQL.
