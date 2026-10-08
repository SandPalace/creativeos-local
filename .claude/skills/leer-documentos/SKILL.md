---
name: leer-documentos
description: Lee los documentos que el dueño dejó en la carpeta documentos/ — PDFs, imágenes, Word, Excel/CSV, capturas — y propone hechos del negocio en hechos.md citando archivo y página, para que el onboarding sólo confirme y pregunte lo que falta. Úsalo cuando haya archivos nuevos en documentos/, antes del onboarding, o cuando digan "te dejé unos archivos", "lee mi lista de precios", "ahí está mi brochure".
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
---

# Leer documentos

El dueño ya tiene escrito mucho de su negocio: listas de precios, brochures, menús, manuales de
marca, exportes de anuncios. Leerlos primero ahorra preguntas — pero **un documento no es el dueño**:
puede estar viejo. Por eso todo lo que sale de un documento entra como `inferido` y el dueño lo
confirma en el onboarding.

## Orden de operaciones

1. **Lista lo nuevo:** `ls -la documentos/` (y subcarpetas). Compara contra
   `clientes/<cliente>/documentos.md`: sólo lee los archivos que no aparecen ahí. Si todavía no
   existe la carpeta del cliente, créala desde las plantillas (`plantillas/hechos.md`,
   `plantillas/brief.md`) — el nombre del negocio suele venir en los mismos documentos; si no, pregúntalo.
2. **Lee cada archivo según su tipo:**

   | Tipo | Cómo |
   |---|---|
   | `.pdf` | `Read` (por páginas si es largo) |
   | `.png` `.jpg` `.webp` `.heic` | `Read`: la imagen se ve. Logo → colores aproximados; foto del local → contexto, no datos |
   | `.md` `.txt` `.csv` | `Read` |
   | `.docx` `.doc` `.rtf` `.pages` | `textutil -convert txt -stdout "<archivo>"` |
   | `.xlsx` | Pide al dueño **guardarlo como CSV** (Archivo → Guardar como → CSV). Mientras: `unzip -p "<archivo>" xl/sharedStrings.xml` y `unzip -p "<archivo>" xl/worksheets/sheet1.xml` |
   | otro | Dile al dueño que no lo puedes leer y pídele un PDF o captura |

3. **Saca sólo hechos del negocio**, mapeados a las claves de `hechos.md` (`negocio`, `oferta`,
   `precios`, `horarios`, `ubicacion`, `publico`, `canales`, `marca`, `restricciones`…). Agrega
   filas nuevas si hace falta (`precios_semestre`, `menu_temporada`).
4. **Escribe en `hechos.md`**, una fila por dato:
   - `estado: inferido` — siempre. Lo confirma el dueño en el onboarding.
   - `fuente`: `documentos/<archivo>, p. <n> (fecha del archivo)` — la fecha con
     `ls -l` o la que diga el documento. Un documento de hace más de 6 meses: anótalo en la fuente.
   - **Nunca pises un dato `confirmado`.** Si el documento dice otra cosa, deja el confirmado y
     agrega una pregunta en `> [!question]`: *"Tu lista de precios de marzo dice $2,000; tú me
     dijiste $2,200. ¿Cuál vale?"*
   - Colores sacados de una imagen: *"aprox. #5C0F8B (de logo.png)"* — un hex leído de un pixel
     es aproximado.
5. **Escribe `clientes/<cliente>/documentos.md`** — el índice, para no releer y para que el dueño
   vea qué se sacó de cada archivo:

   ```markdown
   # Documentos — <Negocio>

   > [!info] Lo que salió de cada archivo entra a [[hechos]] como inferido hasta que lo confirmes.

   | archivo | fecha | qué saqué | claves |
   |---|---|---|---|
   | [[documentos/precios-2026.pdf]] | 2026-09-15 | 4 precios mensuales, semestre | `precios`, `oferta` |
   | [[documentos/logo.png]] | — | colores aprox. | `marca` |
   ```
6. **Entrega:** *"Leí N archivos y propuse M datos en hechos.md (en amarillo, como inferido). En
   el onboarding te los confirmo en bloque y sólo te pregunto lo que falte."*

## Reglas

- **No copies datos personales** (nombres, teléfonos o correos de clientes, credenciales, INE,
  datos bancarios). Si un documento los trae, sáltalos y avísale al dueño que no los usaste.
- **Nunca borres ni muevas** un archivo de `documentos/`: son del dueño.
- Lo que un documento **no** dice no lo deduces: queda en `falta` para el onboarding.
- Un exporte de anuncios (CSV de Meta) no es un hecho: es métrica. Pásalo al `analista`
  (`metricas-sqlite`) y anótalo en el índice.
