---
name: prompt-imagen
description: Escribe prompts de generación de imagen para una pieza aprobada — fórmula de 7 partes, con la paleta de la marca y espacio limpio para el copy, sin texto dentro de la imagen. Úsalo cuando pidan "prompt para imagen", "flyer", "post", "foto de producto", "fondo para el anuncio" o variantes de una imagen.
allowed-tools: Read, Write
---

# Prompt de imagen

## Orden de operaciones

0. **Sólo piezas en la columna verde del Flujo** (`estado: aprobada` **y** `aprobado_por` lleno).
   Si falta la firma, no empieces: dile al director que la firme.
1. **Lee la nota de la pieza** en `piezas/` (debe decir `estado: aprobada`; formato, aspecto, objetivo) y la marca en `brief.md`
   (colores en hex, tono).
2. **Decide dónde irá el copy** antes de escribir el prompt: arriba, abajo, un lado. El prompt
   reserva ese espacio.
3. **Escribe el prompt con las 7 partes**, en inglés (los modelos responden mejor), una oración o
   frase por parte:

| # | parte | ejemplo |
|---|---|---|
| 1 | Sujeto | a small robot kit with an ESP32 board on a classroom desk |
| 2 | Acción / estado | LEDs glowing, wires neatly connected, half-assembled |
| 3 | Entorno | bright makerspace, 3D printer and laptops blurred in the background |
| 4 | Composición | subject in lower third, **clean empty space in the upper 40% for text** |
| 5 | Luz | soft warm window light from the left, gentle shadows |
| 6 | Estilo / cámara | editorial product photography, 50mm, shallow depth of field |
| 7 | Paleta y formato | palette <los hex de `marca` en hechos.md>, aspect ratio 4:5 |

4. **Cierra con las restricciones** (siempre): `no text, no letters, no logos, no watermark, no
   people's faces`.
5. **Dos variantes, no diez:** cambia **una** variable entre ellas (luz, o encuadre, o fondo) para
   que se pueda saber qué cambió el resultado.
6. **Guarda** una nota en `clientes/<cliente>/creativos/<pieza>_v1.md`. Si ya existe `_v1`, crea
   `_v2` — nunca sobrescribas.

   ```markdown
   ---
   tipo: creativo
   cliente: algolab
   pieza: "[[P01]]"
   version: v1
   modelo: <el que se usará>
   aspecto: "4:5"
   estado: propuesta-sin-revisar
   imagen:
   aprobado_por:
   ---

   ## Prompt A (verbatim)
   ## Prompt B (verbatim) — cambia sólo: <la variable>
   ## Copy que va encima (se compone después)
   ## Resultado
   ![[P01_v1_A.png]]
   ## Defectos medidos
   ```
7. Cuando el director genere la imagen, guárdala **dentro de `creativos/`** con el nombre de la
   nota (`P01_v1_A.png`) para que se vea en Obsidian, llena `imagen: "[[P01_v1_A.png]]"` (así
   sale de portada en Tablero → Creativos), y anota los **defectos medidos** (manos raras,
   texto fantasma, color fuera de paleta). Honesto, no "quedó bien".
8. El director revisa en **Inicio → Creativos**: si cambia el estado a `rechazada`, crea `_v2`
   **desde el brief y la pieza**, no desde la v1, y anota qué cambió.

## Reglas que no se negocian

- **Cero texto en la imagen.** Un precio horneado en un pixel no se corrige sin regenerar todo. El
  copy se pone en Canva/Figma/HTML encima.
- **Sin personas generadas reconocibles, nunca menores**, sin logos o personajes de otras marcas.
- **Deriva del brief, no de otra imagen generada.** La copia de una copia deriva de la marca.
