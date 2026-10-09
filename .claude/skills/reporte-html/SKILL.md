---
name: reporte-html
description: Produce un reporte HTML de un solo archivo, sin dependencias, a partir de plantillas/reporte.html — plan del periodo, resultados, o investigación. Úsalo cuando pidan "reporte", "presentación para el cliente", "resumen visual", "dashboard" o "algo que pueda mandar".
allowed-tools: Read, Write, Bash
---

# Reporte HTML

El reporte HTML reemplaza al tablero: un archivo que abre en cualquier navegador, sin internet, y
que se puede mandar o publicar como artifact.

## Orden de operaciones

1. **Decide el tipo:** `plan` (calendario + objetivos), `resultados` (métricas del periodo) o
   `investigacion`.
2. **Junta las fuentes:** `brief.md`, `hechos.md`, las notas de `piezas/` (lee sus propiedades),
   `investigacion.md`, CSVs o `datos/agencia.db`. Anota de qué archivo sale cada número.
3. **Copia la plantilla** `plantillas/reporte.html` y llena sus secciones. Respeta las variables de
   color (`--marca`, `--acento`) con los hex de la marca del cliente.
4. **Cada número lleva su fuente** en un `<small class="fuente">`. Sin dato → la palabra
   **"sin dato"**, nunca 0 ni un estimado.
5. **Gráficas:** SVG en línea o barras con CSS (la plantilla trae un ejemplo). Nada de librerías
   externas: el archivo debe funcionar sin internet.
6. **Orden de lo importante:** arriba la conclusión en una frase y las 3 cifras clave; abajo el
   detalle. Ordena piezas por **costo por resultado**, nunca por CTR.
7. **Guarda** en `clientes/<cliente>/reportes/<YYYY-MM-DD>_<tipo>.html` (el reporte de `resultados`
   del cierre de periodo es lo que lee el brief del siguiente) y ábrelo en el navegador
   (`open <archivo>` en macOS) para revisarlo. Obsidian no previsualiza HTML: el tablero del día a
   día es Obsidian (Inicio, Flujo, Calendario); el reporte HTML es lo que se le entrega al cliente.
8. Revisa: abre en ancho de teléfono (sin scroll horizontal) y en modo oscuro.

## Nunca

- Inventar una cifra para que la gráfica "se vea completa".
- Promediar tasas diarias (CTR, costo) — se calculan de los totales.
- Mandar el reporte al cliente: eso lo decide el director.
