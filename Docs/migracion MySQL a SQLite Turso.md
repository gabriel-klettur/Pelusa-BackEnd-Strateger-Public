# Migración de MySQL a SQLite en Turso (Desde cero)

Este documento describe paso a paso cómo crear nuevas bases de datos SQLite locales para cada servicio del proyecto (alarms, estrategias, diary, positions, accounts, kline\_data, orders) y luego cómo subirlas a Turso, de modo que el backend FastAPI funcione sin necesidad de acceder a datos previos de SiteGround (que se perdieron).

---

## 1. Introducción

A raíz de la pérdida de la información original en SiteGround, partiremos de cero diseñando los esquemas de base de datos en SQLite para cada componente del proyecto. Una vez definidas y creadas localmente, subiremos esas bases a Turso (SQLite distribuido) para que el backend en producción pueda consumirlas.

Se asume que:

* No hay backups de datos previos; se recrearán los esquemas según especificaciones actuales de la aplicación.
* El proyecto backend está basado en FastAPI y utiliza SQLAlchemy en modo asíncrono.
* Se usarán siete bases de datos independientes:

  1. `alarms`
  2. `estrategias`
  3. `diary`
  4. `positions`
  5. `accounts`
  6. `kline_data`
  7. `orders`

El flujo general será:

1. Definir y escribir el DDL (CREATE TABLE) de cada base en SQLite.
2. Crear archivos `.sqlite` vacíos localmente e importar (si hubiera datos) o simplemente dejarlos listos.
3. Ajustar el proyecto FastAPI para que, en desarrollo, use esas bases locales.
4. Instalar y configurar Turso CLI.
5. Crear instancias en Turso para cada base.
6. Importar los archivos SQLite a Turso.
7. Modificar variables de entorno y `config.py` para producción, apuntando a Turso.
8. Desplegar y validar.

---

## 2. Requisitos previos

Antes de comenzar, asegúrate de tener instaladas las siguientes herramientas:

1. **Python 3.8+** (idéntica versión al entorno del proyecto).
2. **FastAPI**, **SQLAlchemy 1.4+**, **aiosqlite**: en tu entorno virtual (`venv` o similar) debe instalarse:

   ```bash
   pip install fastapi "sqlalchemy>=1.4" aiosqlite uvicorn loguru python-dotenv
   ```
3. **SQLite3** (cliente de línea de comandos) para crear y verificar bases locales.
4. **Turso CLI** instalado y autenticado:

   * Sigue las instrucciones oficiales: [https://turso.sh/docs/getting-started/installation](https://turso.sh/docs/getting-started/installation)
   * Luego, ejecuta:

     ```bash
     turso login
     ```

     para iniciar sesión en tu cuenta Turso.
5. Un editor de texto o IDE para trabajar en los archivos SQL y en el código de FastAPI.

También, prepara un directorio local donde estarán tus archivos SQLite, por ejemplo:

```bash
mkdir -p ./data_sqlite
```

---

## 3. Diseño de esquemas en SQLite (desde cero)

A continuación se muestran ejemplos de cómo podrían quedar las tablas en SQLite. Ajusta nombres y columnas según tu lógica de negocio. (Si en el futuro se agregan nuevos campos, usarás Alembic u otro sistema de migraciones, pero en esta primera fase escribirás el DDL “a mano”).

### 3.1. Esquema para `alarms` (alarms.sqlite)

```sql
-- Archivo: schema_alarms_sqlite.sql

PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS alarms (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    alarm_name TEXT NOT NULL,
    ticker TEXT NOT NULL,
    variables TEXT,          -- JSON o texto con variables de la alarma
    time_created DATETIME    -- Fecha y hora en que se generó la alarma (UTC)
);

-- Índice para buscar por nombre de alarma rápidamente
CREATE UNIQUE INDEX IF NOT EXISTS idx_alarms_alarm_name ON alarms(alarm_name);
```

> **Nota:** En el ejemplo original de MySQL quizá había columnas como `strategy`, `entry_indicator`, etc. Si las necesitas, agrégalas aquí con su tipo (`TEXT`, `INTEGER`, etc.).

### 3.2. Esquema para `estrategias` (estrategias.sqlite)

```sql
-- Archivo: schema_estrategias_sqlite.sql

PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS strategies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    alarmName TEXT NOT NULL,
    isOn INTEGER DEFAULT 1,
    account_name TEXT,
    account_type TEXT,
    ticker TEXT,
    resultadoAcc TEXT,
    description TEXT,
    onStartDate DATETIME,
    offEndDate DATETIME,
    longEntryOrder TEXT,
    longCloseOrder TEXT,
    longEntryIndicator TEXT,
    longCloseIndicator TEXT,
    longPyramiding INTEGER,
    longLeverage REAL,
    longQuantity REAL,
    longTPPerOrder REAL,
    longTPGeneral REAL,
    longSLPerOrder REAL,
    longSLGeneral REAL,
    shortEntryOrder TEXT,
    shortCloseOrder TEXT,
    shortEntryIndicator TEXT,
    shortCloseIndicator TEXT,
    shortPyramiding INTEGER,
    shortLeverage REAL,
    shortQuantity REAL,
    shortTPPerOrder REAL,
    shortTPGeneral REAL,
    shortSLPerOrder REAL,
    shortSLGeneral REAL
);

-- Índice para búsqueda por alarmName + ticker
CREATE INDEX IF NOT EXISTS idx_strategies_alarm_ticker ON strategies(alarmName, ticker);
```

### 3.3. Esquema para `diary` (diary.sqlite)

```sql
-- Archivo: schema_diary_sqlite.sql

PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS diary_entries (
    id TEXT PRIMARY KEY,      -- Podría ser UUID, p.ej. Generado en la app
    date DATETIME NOT NULL,
    titleName TEXT,
    text TEXT,
    photos TEXT,             -- JSON array de URLs o rutas relativas
    references TEXT          -- JSON array de referencias externas
);

-- Índice en la fecha para consultas cronológicas
CREATE INDEX IF NOT EXISTS idx_diary_date ON diary_entries(date);
```

### 3.4. Esquema para `positions` (positions.sqlite)

```sql
-- Archivo: schema_positions_sqlite.sql

PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS positions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    account_name TEXT,
    account_type TEXT,
    symbol TEXT,
    positionId TEXT,
    positionSide TEXT,
    isolated INTEGER,
    positionAmt TEXT,
    availableAmt TEXT,
    unrealizedProfit TEXT,
    realisedProfit TEXT,
    initialMargin TEXT,
    margin TEXT,
    avgPrice TEXT,
    liquidationPrice REAL,
    leverage INTEGER,
    positionValue TEXT,
    markPrice TEXT,
    riskRate TEXT,
    maxMarginReduction TEXT,
    pnlRatio TEXT,
    updateTime INTEGER,
    dateTime TEXT            -- Fecha y hora (string) en formato "HH:MM DD/MM/YYYY"
);

-- Índice para buscar posiciones por símbolo
CREATE INDEX IF NOT EXISTS idx_positions_symbol ON positions(symbol);
```

### 3.5. Esquema para `accounts` (accounts.sqlite)

```sql
-- Archivo: schema_accounts_sqlite.sql

PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS accounts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    accountName TEXT,
    accountType TEXT,
    asset TEXT,
    balance REAL,
    equity REAL,
    unrealizedProfit REAL,
    realizedProfit REAL,
    dateTime DATETIME,
    availableMargin REAL,
    usedMargin REAL
);

-- Índice por accountName + accountType
CREATE INDEX IF NOT EXISTS idx_accounts_name_type ON accounts(accountName, accountType);
```

### 3.6. Esquema para `kline_data` (kline\_data.sqlite)

```sql
-- Archivo: schema_kline_data_sqlite.sql

PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS kline_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    symbol TEXT,
    intervals TEXT,
    open REAL,
    close REAL,
    high REAL,
    low REAL,
    volume REAL,
    time INTEGER
);

-- Índice para búsqueda por símbolo + intervalo
CREATE INDEX IF NOT EXISTS idx_kline_symbol_interval ON kline_data(symbol, intervals);
```

### 3.7. Esquema para `orders` (orders.sqlite)

```sql
-- Archivo: schema_orders_sqlite.sql

PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    symbol TEXT,
    side TEXT,
    order_type TEXT,
    position_side TEXT,
    reduce_only INTEGER,
    quantity TEXT,
    price TEXT,
    average_price TEXT,
    status TEXT,
    profit TEXT,
    commision TEXT,
    stop_price TEXT,
    working_type TEXT,
    order_time TEXT,
    update_time TEXT
);

-- Índice para buscar órdenes por símbolo + estado
CREATE INDEX IF NOT EXISTS idx_orders_symbol_status ON orders(symbol, status);
```

---

## 4. Crear bases de datos SQLite locales

Con los siete archivos `schema_*.sql` listos, crea los archivos `.sqlite` en el directorio `./data_sqlite`:

```bash
# Desde la raíz del proyecto
sqlite3 ./data_sqlite/alarms.sqlite   < schema_alarms_sqlite.sql
sqlite3 ./data_sqlite/estrategias.sqlite < schema_estrategias_sqlite.sql
sqlite3 ./data_sqlite/diary.sqlite    < schema_diary_sqlite.sql
sqlite3 ./data_sqlite/positions.sqlite  < schema_positions_sqlite.sql
sqlite3 ./data_sqlite/accounts.sqlite  < schema_accounts_sqlite.sql
sqlite3 ./data_sqlite/kline_data.sqlite < schema_kline_data_sqlite.sql
sqlite3 ./data_sqlite/orders.sqlite    < schema_orders_sqlite.sql
```

Estos comandos crean siete ficheros vacíos con las tablas definidas. Si en el futuro quisieras poblarlos con datos anteriores, usarías algún script de importación; pero como partimos de cero, bastará con la estructura.

---

## 5. Configurar FastAPI para SQLite local

### 5.1. Instalar el driver asincrónico de SQLite

Si aún no lo tienes:

```bash
pip install aiosqlite
```

### 5.2. Ajustar `config.py`

En lugar de apuntar a MySQL, define variables que señalen a los archivos `.sqlite`:

```python
# app/config.py
import os
from dotenv import load_dotenv
load_dotenv()

class Settings:
    # Directorio donde están los .sqlite
    SQLITE_DIR = os.getenv("SQLITE_DIR", "./data_sqlite")
    if not os.path.isdir(SQLITE_DIR):
        os.makedirs(SQLITE_DIR, exist_ok=True)

    # URLs de SQLite locales (modo desarrollo)
    DATABASE_URL_DESARROLLO_ALARMAS     = f"sqlite+aiosqlite:///{SQLITE_DIR}/alarms.sqlite"
    DATABASE_URL_DESARROLLO_ESTRATEGIAS = f"sqlite+aiosqlite:///{SQLITE_DIR}/estrategias.sqlite"
    DATABASE_URL_DESARROLLO_DIARY       = f"sqlite+aiosqlite:///{SQLITE_DIR}/diary.sqlite"
    DATABASE_URL_DESARROLLO_POSITIONS   = f"sqlite+aiosqlite:///{SQLITE_DIR}/positions.sqlite"
    DATABASE_URL_DESARROLLO_ACCOUNTS    = f"sqlite+aiosqlite:///{SQLITE_DIR}/accounts.sqlite"
    DATABASE_URL_DESARROLLO_KLINE_DATA  = f"sqlite+aiosqlite:///{SQLITE_DIR}/kline_data.sqlite"
    DATABASE_URL_DESARROLLO_ORDERS      = f"sqlite+aiosqlite:///{SQLITE_DIR}/orders.sqlite"

    # En producción, usaremos Turso (ver sección 7). Por ahora dejamos en blanco:
    DATABASE_URL_PROD_ALARMAS     = os.getenv("TURSO_URL_ALARMAS", "")
    DATABASE_URL_PROD_ESTRATEGIAS = os.getenv("TURSO_URL_ESTRATEGIAS", "")
    DATABASE_URL_PROD_DIARY       = os.getenv("TURSO_URL_DIARY", "")
    DATABASE_URL_PROD_POSITIONS   = os.getenv("TURSO_URL_POSITIONS", "")
    DATABASE_URL_PROD_ACCOUNTS    = os.getenv("TURSO_URL_ACCOUNTS", "")
    DATABASE_URL_PROD_KLINE_DATA  = os.getenv("TURSO_URL_KLINE_DATA", "")
    DATABASE_URL_PROD_ORDERS      = os.getenv("TURSO_URL_ORDERS", "")

    # Flag para determinar si usamos Turso o SQLite local
    USE_TURSO = os.getenv("USE_TURSO", "false").lower() in ["true", "1", "yes", "on"]

    # Propiedades que devuelven la URL adecuada según el modo
    @property
    def DATABASE_URL_ALARMAS(self):
        return self.DATABASE_URL_PROD_ALARMAS if self.USE_TURSO else self.DATABASE_URL_DESARROLLO_ALARMAS

    @property
    def DATABASE_URL_ESTRATEGIAS(self):
        return self.DATABASE_URL_PROD_ESTRATEGIAS if self.USE_TURSO else self.DATABASE_URL_DESARROLLO_ESTRATEGIAS

    @property
    def DATABASE_URL_DIARY(self):
        return self.DATABASE_URL_PROD_DIARY if self.USE_TURSO else self.DATABASE_URL_DESARROLLO_DIARY

    @property
    def DATABASE_URL_POSITIONS(self):
        return self.DATABASE_URL_PROD_POSITIONS if self.USE_TURSO else self.DATABASE_URL_DESARROLLO_POSITIONS

    @property
    def DATABASE_URL_ACCOUNTS(self):
        return self.DATABASE_URL_PROD_ACCOUNTS if self.USE_TURSO else self.DATABASE_URL_DESARROLLO_ACCOUNTS

    @property
    def DATABASE_URL_KLINE_DATA(self):
        return self.DATABASE_URL_PROD_KLINE_DATA if self.USE_TURSO else self.DATABASE_URL_DESARROLLO_KLINE_DATA

    @property
    def DATABASE_URL_ORDERS(self):
        return self.DATABASE_URL_PROD_ORDERS if self.USE_TURSO else self.DATABASE_URL_DESARROLLO_ORDERS

settings = Settings()
```

### 5.3. Ajustar `app/siteground/database.py`

Reemplaza las antiguas conexiones MySQL por conexiones SQLite asíncronas:

```python
# app/siteground/database.py
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.config import settings
from sqlalchemy import event

# --------------------------------------
# Alarmas
async_engine_alarmas = create_async_engine(settings.DATABASE_URL_ALARMAS, echo=False)
async_session_alarmas = sessionmaker(async_engine_alarmas, class_=AsyncSession, expire_on_commit=False)

# Habilitar validación de foreign keys en SQLite
@event.listens_for(async_engine_alarmas.sync_engine, "connect")
def _enable_fk_alarmas(dbapi_connection, connection_record):
    dbapi_connection.execute("PRAGMA foreign_keys=ON")

def get_db_alarmas():
    async def _get():
        async with async_session_alarmas() as session:
            yield session
    return _get

# --------------------------------------
# Estrategias
async_engine_estrategias = create_async_engine(settings.DATABASE_URL_ESTRATEGIAS, echo=False)
async_session_estrategias = sessionmaker(async_engine_estrategias, class_=AsyncSession, expire_on_commit=False)

@event.listens_for(async_engine_estrategias.sync_engine, "connect")
def _enable_fk_estrategias(dbapi_connection, connection_record):
    dbapi_connection.execute("PRAGMA foreign_keys=ON")

def get_db_estrategias():
    async def _get():
        async with async_session_estrategias() as session:
            yield session
    return _get

# --------------------------------------
# Diary
async_engine_diary = create_async_engine(settings.DATABASE_URL_DIARY, echo=False)
async_session_diary = sessionmaker(async_engine_diary, class_=AsyncSession, expire_on_commit=False)

@event.listens_for(async_engine_diary.sync_engine, "connect")
def _enable_fk_diary(dbapi_connection, connection_record):
    dbapi_connection.execute("PRAGMA foreign_keys=ON")

def get_db_diary():
    async def _get():
        async with async_session_diary() as session:
            yield session
    return _get

# --------------------------------------
# Positions
async_engine_positions = create_async_engine(settings.DATABASE_URL_POSITIONS, echo=False)
async_session_positions = sessionmaker(async_engine_positions, class_=AsyncSession, expire_on_commit=False)

@event.listens_for(async_engine_positions.sync_engine, "connect")
def _enable_fk_positions(dbapi_connection, connection_record):
    dbapi_connection.execute("PRAGMA foreign_keys=ON")

def get_db_positions():
    async def _get():
        async with async_session_positions() as session:
            yield session
    return _get

# --------------------------------------
# Accounts
async_engine_accounts = create_async_engine(settings.DATABASE_URL_ACCOUNTS, echo=False)
async_session_accounts = sessionmaker(async_engine_accounts, class_=AsyncSession, expire_on_commit=False)

@event.listens_for(async_engine_accounts.sync_engine, "connect")
def _enable_fk_accounts(dbapi_connection, connection_record):
    dbapi_connection.execute("PRAGMA foreign_keys=ON")

def get_db_accounts():
    async def _get():
        async with async_session_accounts() as session:
            yield session
    return _get

# --------------------------------------
# Kline Data
async_engine_kline = create_async_engine(settings.DATABASE_URL_KLINE_DATA, echo=False)
async_session_kline = sessionmaker(async_engine_kline, class_=AsyncSession, expire_on_commit=False)

@event.listens_for(async_engine_kline.sync_engine, "connect")
def _enable_fk_kline(dbapi_connection, connection_record):
    dbapi_connection.execute("PRAGMA foreign_keys=ON")

def get_db_kline_data():
    async def _get():
        async with async_session_kline() as session:
            yield session
    return _get

# --------------------------------------
# Orders
async_engine_orders = create_async_engine(settings.DATABASE_URL_ORDERS, echo=False)
async_session_orders = sessionmaker(async_engine_orders, class_=AsyncSession, expire_on_commit=False)

@event.listens_for(async_engine_orders.sync_engine, "connect")
def _enable_fk_orders(dbapi_connection, connection_record):
    dbapi_connection.execute("PRAGMA foreign_keys=ON")

def get_db_orders():
    async def _get():
        async with async_session_orders() as session:
            yield session
    return _get

# --------------------------------------
async def close_db_connections():
    await async_engine_alarmas.dispose()
    await async_engine_estrategias.dispose()
    await async_engine_diary.dispose()
    await async_engine_positions.dispose()
    await async_engine_accounts.dispose()
    await async_engine_kline.dispose()
    await async_engine_orders.dispose()
```

*Con esto, tu proyecto ya estaría apuntando a los archivos locales `./data_sqlite/*.sqlite`.*

## 6. Probar localmente

1. Lanza el servidor en modo desarrollo:

   ```bash
   uvicorn app.main:app --reload
   ```

2. Abre `http://127.0.0.1:8000/docs` en tu navegador y prueba:

   * Rutas de `alarms` (`GET /alarms/alarms`, `POST /alarms/…`).
   * Rutas de `estrategias` (`GET /strateger/strategies/list`, etc.).
   * `GET /diary/list`, `POST /diary/insert`, etc.
   * `POST /positions/` (crear), `GET /positions/` (si implementaste), etc.
   * `GET /accounts`, `GET /kline_data`, `GET /orders/list`.

3. Verifica que las tablas locales se llenan:

   ```bash
   sqlite3 ./data_sqlite/alarms.sqlite "SELECT * FROM alarms;"
   sqlite3 ./data_sqlite/diary.sqlite "SELECT count(*) FROM diary_entries;"
   # etc.
   ```

Si todo funciona —puedes leer y escribir datos—, entonces la parte local está lista.

---

## 7. Crear bases de datos en Turso

### 7.1. Instalar y autenticar Turso (si no está hecho)

```bash
# Si no lo instalaste aún:
# macOS: brew install turso
# Linux: sigue instrucciones en https://turso.sh/docs/getting-started/installation

turso login
```

### 7.2. Crear cada base en Turso

Ejecuta uno a uno estos comandos, reemplazando `--password` por una contraseña segura que uses para acceder:

```bash
turso db create alarmas-db   --region wlt1 --password TuPassFuerte
turso db create estrategias-db --region wlt1 --password TuPassFuerte
turso db create diary-db      --region wlt1 --password TuPassFuerte
turso db create positions-db  --region wlt1 --password TuPassFuerte
turso db create accounts-db   --region wlt1 --password TuPassFuerte
turso db create kline-data-db --region wlt1 --password TuPassFuerte
turso db create orders-db     --region wlt1 --password TuPassFuerte
```

Al final de cada comando, Turso muestra algo parecido a:

```
✔ Created database alarmas-db
  region: wlt1
  url:    turso://alarmas-db.wlt1.turso.io
  username: <username_turso>
  password: TuPassFuerte
```

Guarda las URLs que Turso te indica, porque las necesitarás en el siguiente paso.

---

## 8. Importar archivos SQLite a Turso

Con los archivos `alarms.sqlite`, `estrategias.sqlite`, … creados localmente, sube cada uno a su respectiva base en Turso:

```bash
turso db import ./data_sqlite/alarms.sqlite   --db alarmas-db
turso db import ./data_sqlite/estrategias.sqlite --db estrategias-db
turso db import ./data_sqlite/diary.sqlite    --db diary-db
turso db import ./data_sqlite/positions.sqlite  --db positions-db
turso db import ./data_sqlite/accounts.sqlite  --db accounts-db
turso db import ./data_sqlite/kline_data.sqlite --db kline-data-db
turso db import ./data_sqlite/orders.sqlite    --db orders-db
```

Cada comando subirá la base local a Turso. Al finalizar, Turso confirma algo como:

```
✔ Imported database alarms.sqlite into alarmas-db
```

---

## 9. Configurar producción: variables de entorno y `config.py`

### 9.1. Obtener los DSN (URIs) de Turso

Para cada base, Turso CLI te permite “conectarte” o ver la cadena de conexión. Por ejemplo:

```bash
turso db connect alarmas-db
```

Te devolverá un URI del estilo:

```
sqlite://@/alarmas-db.wlt1.turso.io/alarms.sqlite?authToken=TuPassFuerte
```

O, en versiones más recientes:

```
turso://<username_turso>:TuPassFuerte@alarmas-db.wlt1.turso.io/alarms-db
```

**Copia exactamente** la línea que Turso te muestre. Haz lo mismo para cada base:

* `estrategias-db`
* `diary-db`
* `positions-db`
* `accounts-db`
* `kline-data-db`
* `orders-db`

### 9.2. Definir variables de entorno en producción

En tu servidor (o en el contenedor donde ejecutes la app), exporta:

```ini
# .env o variables de entorno en el despliegue
USE_TURSO=true
TURSO_URL_ALARMAS="sqlite://@/alarmas-db.wlt1.turso.io/alarms.sqlite?authToken=TuPassFuerte"
TURSO_URL_ESTRATEGIAS="sqlite://@/estrategias-db.wlt1.turso.io/estrategias.sqlite?authToken=TuPassFuerte"
TURSO_URL_DIARY="sqlite://@/diary-db.wlt1.turso.io/diary.sqlite?authToken=TuPassFuerte"
TURSO_URL_POSITIONS="sqlite://@/positions-db.wlt1.turso.io/positions.sqlite?authToken=TuPassFuerte"
TURSO_URL_ACCOUNTS="sqlite://@/accounts-db.wlt1.turso.io/accounts.sqlite?authToken=TuPassFuerte"
TURSO_URL_KLINE_DATA="sqlite://@/kline-data-db.wlt1.turso.io/kline_data.sqlite?authToken=TuPassFuerte"
TURSO_URL_ORDERS="sqlite://@/orders-db.wlt1.turso.io/orders.sqlite?authToken=TuPassFuerte"

# Mantén también:
MODE_DEVELOPING=false
# Y el resto de variables: APIKEY, SECRETKEY, CORS, etc.
```

### 9.3. Validar `config.py` en producción

Asegúrate de que `app/config.py` esté leyendo esas variables:

```python
# app/config.py
import os
from dotenv import load_dotenv
load_dotenv()

class Settings:
    # Mismos atributos que antes...
    USE_TURSO = os.getenv("USE_TURSO", "false").lower() in ["true","1","yes","on"]

    # Rutas locales (desarrollo)
    SQLITE_DIR = os.getenv("SQLITE_DIR", "./data_sqlite")
    DATABASE_URL_DESARROLLO_ALARMAS     = f"sqlite+aiosqlite:///{SQLITE_DIR}/alarms.sqlite"
    DATABASE_URL_DESARROLLO_ESTRATEGIAS = f"sqlite+aiosqlite:///{SQLITE_DIR}/estrategias.sqlite"
    DATABASE_URL_DESARROLLO_DIARY       = f"sqlite+aiosqlite:///{SQLITE_DIR}/diary.sqlite"
    DATABASE_URL_DESARROLLO_POSITIONS   = f"sqlite+aiosqlite:///{SQLITE_DIR}/positions.sqlite"
    DATABASE_URL_DESARROLLO_ACCOUNTS    = f"sqlite+aiosqlite:///{SQLITE_DIR}/accounts.sqlite"
    DATABASE_URL_DESARROLLO_KLINE_DATA  = f"sqlite+aiosqlite:///{SQLITE_DIR}/kline_data.sqlite"
    DATABASE_URL_DESARROLLO_ORDERS      = f"sqlite+aiosqlite:///{SQLITE_DIR}/orders.sqlite"

    # Rutas Turso (producción)
    DATABASE_URL_PROD_ALARMAS     = os.getenv("TURSO_URL_ALARMAS", "")
    DATABASE_URL_PROD_ESTRATEGIAS = os.getenv("TURSO_URL_ESTRATEGIAS", "")
    DATABASE_URL_PROD_DIARY       = os.getenv("TURSO_URL_DIARY", "")
    DATABASE_URL_PROD_POSITIONS   = os.getenv("TURSO_URL_POSITIONS", "")
    DATABASE_URL_PROD_ACCOUNTS    = os.getenv("TURSO_URL_ACCOUNTS", "")
    DATABASE_URL_PROD_KLINE_DATA  = os.getenv("TURSO_URL_KLINE_DATA", "")
    DATABASE_URL_PROD_ORDERS      = os.getenv("TURSO_URL_ORDERS", "")

    @property
    def DATABASE_URL_ALARMAS(self):
        return self.DATABASE_URL_PROD_ALARMAS if self.USE_TURSO else self.DATABASE_URL_DESARROLLO_ALARMAS

    @property
    def DATABASE_URL_ESTRATEGIAS(self):
        return self.DATABASE_URL_PROD_ESTRATEGIAS if self.USE_TURSO else self.DATABASE_URL_DESARROLLO_ESTRATEGIAS

    @property
    def DATABASE_URL_DIARY(self):
        return self.DATABASE_URL_PROD_DIARY if self.USE_TURSO else self.DATABASE_URL_DESARROLLO_DIARY

    @property
    def DATABASE_URL_POSITIONS(self):
        return self.DATABASE_URL_PROD_POSITIONS if self.USE_TURSO else self.DATABASE_URL_DESARROLLO_POSITIONS

    @property
    def DATABASE_URL_ACCOUNTS(self):
        return self.DATABASE_URL_PROD_ACCOUNTS if self.USE_TURSO else self.DATABASE_URL_DESARROLLO_ACCOUNTS

    @property
    def DATABASE_URL_KLINE_DATA(self):
        return self.DATABASE_URL_PROD_KLINE_DATA if self.USE_TURSO else self.DATABASE_URL_DESARROLLO_KLINE_DATA

    @property
    def DATABASE_URL_ORDERS(self):
        return self.DATABASE_URL_PROD_ORDERS if self.USE_TURSO else self.DATABASE_URL_DESARROLLO_ORDERS

settings = Settings()
```

---

## 10. Despliegue y validación en producción

1. **Instala dependencias en el servidor** (idéntico al entorno local):

   ```bash
   pip install fastapi "sqlalchemy>=1.4" aiosqlite uvicorn loguru python-dotenv
   ```

2. **Coloca el `.env` con variables** (ver apartado 9.2).

3. **Inicia la aplicación**:

   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```

   (O bien, usa `supervisor`, `systemd` o `pm2` para mantenerla en segundo plano).

4. **Pruebas básicas**:

   * Desde Postman o CURL, lanza `GET /alarms/alarms?limit=10&offset=0`. Deberías obtener datos (vacío o con registros si insertaste local antes de importar).
   * Inserta una alarma nueva (`POST /alarms/alarms`). Luego, abre la shell de Turso para verificar:

     ```bash
     turso db shell alarmas-db
     sqlite> SELECT * FROM alarms;
     ```
   * Haz lo mismo con `/diary/insert`, `GET /diary/list`, etc., y verifica en Turso.
   * Para `/positions/`, comprueba que al hacer `POST /positions/` se grabe en la tabla `positions` de Turso.

5. **Monitoreo de errores**:

   * Encripta los logs con `loguru` y revisa fallos de conexión (“database is locked” o problemas de concurrencia). Turso maneja concurrencia mejor que SQLite local, pero si tu app hace escrituras intensas deberás controlar transacciones.
   * Verifica que las claves foráneas funcionen: en la shell de Turso ejecuta:

     ```sql
     PRAGMA foreign_keys;
     PRAGMA foreign_key_list(positions);
     ```

     para asegurarte de que las FKs existen.

---

## 11. Notas adicionales y recomendaciones

* **Migraciones futuras**: si planeas evolucionar el esquema (agregar o quitar columnas), te recomendamos incorporar una solución de migraciones como Alembic, aunque hay que tener cuidado porque no todas las operaciones de Alembic (ej.: cambiar tipo de columna) funcionan igual en SQLite.

* **Backups en Turso**: configura snapshots automáticos o exportaciones periódicas si quieres tener respaldo adicional. Consulta la documentación oficial: [https://turso.sh/docs/](https://turso.sh/docs/).

* **Concurrente vs. SQLite local**: SQLite en disco sólo permite una escritura a la vez; Turso abstráneamente lo maneja a nivel de red, pero sigue respetando locking. Si tu aplicación hace muchos writes simultáneos, considera agrupar operaciones en transacciones o revisar estrategias de reintento.

* **Tipos de datos**: SQLite es flexible (tipos dinámicos), pero conviene ser consistente:

  * `INTEGER PRIMARY KEY` → autoincrement
  * `TEXT` para cadenas y JSON simples
  * `REAL` para floats
  * `DATETIME` o `TEXT` (ISO 8601) para timestamps. Siempre usar UTC.

* **Configuración de CORS y seguridad**: asegúrate de no exponer directamente el endpoint de Turso (normalmente tu backend será el único cliente). Las variables `ALLOWED_IPS`, `BLOCKED_IPS` y la configuración de CORS en `main.py` deben proteger tus rutas.

* **Optimización de índices**: según volumen de datos, agrega índices adicionales (p.ej., sobre `time_created` en `alarms`, sobre `date` en `diary`, etc.). Puedes ejecutar `CREATE INDEX IF NOT EXISTS ...` en la shell de Turso si lo necesitas.

* **Pruebas end-to-end**: una vez todo funcione, crea pruebas automáticas (pytest) que comprueben que leer/insertar datos en producción (Turso) retorna valores esperados.

---

¡Con esto dispones de un plan completo para recrear las bases de datos desde cero en SQLite, levantar el proyecto localmente, y luego subir esas bases a Turso para producción! Posteriormente, cada vez que agregues o modifiques tablas, sigue el flujo:

1. Edita los archivos `schema_*.sql` o usa Alembic.
2. Aplica localmente (sqlite3 o SQLAlchemy).
3. Si necesitas llevar esos cambios a Turso, las opciones son:

   * Usar `turso db import` de nuevo (reemplaza la DB completa).
   * O aplicar `turso db shell <db> "ALTER TABLE …"` manualmente.

¡Éxito en tu migración!
