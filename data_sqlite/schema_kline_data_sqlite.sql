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
