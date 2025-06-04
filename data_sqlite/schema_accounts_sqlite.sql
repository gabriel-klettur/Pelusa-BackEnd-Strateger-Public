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
