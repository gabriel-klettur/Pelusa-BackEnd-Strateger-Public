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
