-- Archivo: schema_diary_sqlite.sql
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS diary_entries (
    id TEXT PRIMARY KEY,      -- Podría ser UUID, p.ej. Generado en la app
    date DATETIME NOT NULL,
    titleName TEXT,
    text TEXT,
    photos TEXT,             -- JSON array de URLs o rutas relativas
    "references" TEXT          -- JSON array de referencias externas
);

-- Índice en la fecha para consultas cronológicas
CREATE INDEX IF NOT EXISTS idx_diary_date ON diary_entries(date);
