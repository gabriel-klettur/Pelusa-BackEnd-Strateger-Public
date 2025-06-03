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
