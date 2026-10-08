-- Opcional: el 20% de base de datos. Uso: sqlite3 datos/agencia.db < datos/esquema.sql

CREATE TABLE IF NOT EXISTS metricas_diarias (
  cliente      TEXT NOT NULL,
  pieza_id     TEXT NOT NULL,          -- el id del calendario (P01) o el nombre del anuncio
  fecha        TEXT NOT NULL,          -- YYYY-MM-DD
  canal        TEXT NOT NULL,          -- meta, tiktok, instagram-organico…
  impresiones  INTEGER DEFAULT 0,
  clics        INTEGER DEFAULT 0,
  resultados   INTEGER DEFAULT 0,      -- lo que cuenta como éxito: mensajes, reservas, ventas
  gasto        REAL    DEFAULT 0,
  moneda       TEXT NOT NULL DEFAULT 'MXN',
  importado_en TEXT NOT NULL DEFAULT (datetime('now','localtime')),
  PRIMARY KEY (cliente, pieza_id, fecha, canal)   -- re-importar un día lo reemplaza, no lo duplica
);

CREATE TABLE IF NOT EXISTS hechos (
  cliente TEXT NOT NULL,
  dato    TEXT NOT NULL,
  valor   TEXT,
  fuente  TEXT,
  estado  TEXT NOT NULL CHECK (estado IN ('confirmado','inferido','falta')),
  -- un dato inferido nunca puede marcarse confirmado sin fuente
  CHECK (estado <> 'confirmado' OR (fuente IS NOT NULL AND fuente <> '')),
  PRIMARY KEY (cliente, dato)
);
