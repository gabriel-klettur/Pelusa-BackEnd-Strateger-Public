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
