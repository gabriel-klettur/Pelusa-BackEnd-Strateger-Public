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
