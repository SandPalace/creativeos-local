---
name: metricas-sqlite
description: Opcional — guarda y consulta métricas de publicaciones y anuncios en una base SQLite local (datos/agencia.db). Úsalo cuando haya exportes CSV que se repiten cada semana, cuando pregunten "cuál pieza rindió mejor" sobre varios periodos, o para alimentar el reporte HTML con números consultables.
allowed-tools: Read, Write, Bash
---

# Métricas en SQLite (opcional)

Una sola base, un solo archivo: `datos/agencia.db`. Si dos reportes leen dos fuentes distintas,
tarde o temprano dan números distintos.

## Orden de operaciones

1. **Crea la base si no existe:** `sqlite3 datos/agencia.db < datos/esquema.sql`
2. **Importa el CSV** a una tabla temporal y de ahí a `metricas_diarias`, mapeando columnas. No
   borres datos previos: re-importar el mismo día **reemplaza** la fila (la llave primaria es
   `cliente + pieza + fecha`).

   ```bash
   sqlite3 datos/agencia.db <<'SQL'
   .mode csv
   -- import_tmp no existe todavía: la 1a fila del CSV se vuelve los nombres de columna
   .import exporte.csv import_tmp
   INSERT OR REPLACE INTO metricas_diarias (cliente, pieza_id, fecha, canal, impresiones, clics, resultados, gasto, moneda)
   SELECT 'cafe-norte', ad_name, date, 'meta', impressions, clicks, results, spend, 'MXN' FROM import_tmp;
   DROP TABLE import_tmp;
   SQL
   ```
3. **Consulta con tasas desde totales**, nunca `AVG()` de tasas:

   ```sql
   SELECT pieza_id,
          SUM(gasto) AS gasto,
          SUM(resultados) AS resultados,
          ROUND(SUM(gasto) / NULLIF(SUM(resultados), 0), 2) AS costo_por_resultado,
          ROUND(100.0 * SUM(clics) / NULLIF(SUM(impresiones), 0), 2) AS ctr
   FROM metricas_diarias
   WHERE cliente = 'cafe-norte' AND moneda = 'MXN'
   GROUP BY pieza_id
   ORDER BY costo_por_resultado IS NULL, costo_por_resultado;
   ```
4. **Cita la consulta** junto al número cuando lo uses en un reporte.
5. **Revisa la frescura:** `SELECT MAX(fecha) FROM metricas_diarias WHERE cliente=…`. Si el dato
   más nuevo tiene más de 2 días, dilo antes de recomendar nada.

## Reglas

- `NULLIF(...,0)` → un divisor en cero da `NULL` ("sin dato"), nunca 0.
- Una moneda por consulta. Nunca sumes MXN con USD.
- Un día sin filas puede ser un día sin entrega, no un hueco: confírmalo antes de "rellenarlo".
