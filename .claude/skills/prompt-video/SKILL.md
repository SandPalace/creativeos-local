---
name: prompt-video
description: Escribe prompts de generación de video (Seedance, Veo, Sora, Kling, Hailuo, Runway…) para una pieza aprobada — una toma por generación, con cámara, movimiento y duración, sin texto en cuadro. Úsalo cuando pidan "prompt de video", "reel", "clip", "anuncio en video" o un storyboard.
allowed-tools: Read, Write
---

# Prompt de video

## Orden de operaciones

0. **Sólo piezas en la columna verde del Flujo** (`estado: aprobada` **y** `aprobado_por` lleno).
   Si falta la firma, no empieces: dile al director que la firme.
1. **Lee la nota de la pieza** en `piezas/` (debe decir `estado: aprobada`; formato, duración,
   canal) y la marca (`brief.md`).
2. **Guion primero:** corre `guion-de-contenido` (gancho → enganche → bloques → re-gancho →
   llamada a la acción). Las tomas salen de ese guion.
2b. **Storyboard:** parte el video en tomas de 3–8 segundos. Una pieza de 15 s = 3–4 tomas.
   **Una toma = una generación.** Un prompt que pide tres escenas produce una mezcla de las tres.
3. **Gancho en la toma 1.** El primer segundo decide si alguien se queda: movimiento, contraste o
   algo inesperado — no un logo.
4. **Por cada toma, el prompt con 6 partes**, en inglés:

| # | parte | ejemplo |
|---|---|---|
| 1 | Sujeto + acción | hands snap the last wire into a small robot, its LEDs light up |
| 2 | Escena | classroom desk, laptops and a 3D printer in the background |
| 3 | Cámara | close-up, slow push-in, eye level |
| 4 | Movimiento y ritmo | the robot rolls forward a few centimeters, playful pace |
| 5 | Luz y estilo | bright natural light, clean, shallow depth of field |
| 6 | Técnico | 5 seconds, 9:16 vertical, no text on screen, no logos |

5. **Rostros:** mejor manos, espaldas, producto. Una persona generada reconocible en un anuncio es
   un riesgo legal y de confianza; menores, nunca.
6. **El texto y la voz van después**, en el editor (CapCut, Canva, Premiere). Escribe el copy en
   pantalla y el guion de voz aparte, por toma.
7. **Guarda** una nota en `clientes/<cliente>/creativos/<pieza>_v1.md` con el mismo frontmatter que
   `prompt-imagen` (`tipo: creativo`, `pieza: "[[P02]]"`, `version`, `modelo`, `aspecto: "9:16"`,
   `estado: propuesta-sin-revisar`) más `duracion`. En el cuerpo: storyboard, cada prompt verbatim
   por toma, copy en pantalla y guion de voz por toma. Los clips generados se guardan junto a la nota
   y se embeben con `![[P02_v1_toma1.mp4]]` — Obsidian los reproduce. Nunca sobrescribas: `_v2`.

## Dato que vale saber

En nuestra agencia, con datos de 225 días: el video de persona hablando a cámara costó **12.1 MXN**
por conversación; el video cinematográfico generado con IA, **44.4**. Que se vea caro no significa
que venda. Propón al director probar ambos cuando el presupuesto lo permita.
