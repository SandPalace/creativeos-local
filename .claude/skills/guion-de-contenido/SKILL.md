---
name: guion-de-contenido
description: Escribe el guion de un video corto (reel, TikTok, Short) o la estructura de un carrusel con la estructura que retiene — gancho, zona de enganche, bloques, re-gancho y llamada a la acción con palabra clave — y propone variantes de gancho para probar. Úsalo cuando pidan "guion", "hook", "gancho", "qué digo en el video", "CTA", "llamada a la acción", o antes de los prompts de video de una pieza aprobada.
allowed-tools: Read, Write, Edit, Grep, Bash
---

# Guion de contenido

Un video corto se pierde en el primer segundo o a la mitad. Esta estructura existe para que no pase
ninguna de las dos, y para que al final la persona **haga una sola cosa** que se pueda medir.

## Orden de operaciones

0. **Sólo para piezas firmadas** (`estado: aprobada` y `aprobado_por` lleno) y con
   `verificar-hechos` corrido sobre el copy: el guion no puede afirmar nada que no esté `confirmado`
   en `hechos.md`.
1. **Lee la pieza** (objetivo, canal, formato, `llega_a`, `se_mide`) y `Estrategia de contenido.md`.
2. **Escribe el guion con los 8 pasos** (abajo), con su tiempo aproximado.
3. **Propón 3 ganchos distintos** para el mismo cuerpo — uno de cada tipo de la tabla de ganchos.
   Son las variantes que se prueban en orgánico (*graba una vez, publica muchas*).
4. **Guarda** en la nota del creativo (`creativos/<pieza>_v1.md`), sección `## Guion`, antes de los
   prompts. Si ya hay `_v1` revisada, `_v2`.

## La estructura (8 pasos)

| # | Paso | Qué hace | Duración |
|---|---|---|---|
| 1 | **Gancho** | Para el scroll: una tensión, una promesa o un dolor concreto | 0–2 s |
| 2 | **Zona de enganche** | Confirma que vale la pena quedarse: qué va a obtener y por qué tú | 2–5 s |
| 3 | **Bloque 1** | La primera idea, con una prueba visual | ~8 s |
| 4 | **Re-gancho** | Reabre la curiosidad antes de que se vaya: *"pero lo que nadie hace es…"* | 1–2 s |
| 5 | **Bloque 2** | La segunda idea | ~8 s |
| 6 | **Bloque 3** *(opcional)* | Sólo si suma; si no, se corta | ~8 s |
| 7 | **Re-gancho** | Prepara la acción: *"y si quieres…"* | 1–2 s |
| 8 | **Llamada a la acción** | **Una** acción con **palabra clave**: *"escribe CLASES por WhatsApp"* | 2–3 s |

**Carrusel:** lámina 1 = gancho · lámina 2 = zona de enganche · una lámina por bloque · última
lámina = llamada a la acción con palabra clave.

## Tipos de gancho (elige 3 distintos para probar)

| Tipo | Forma | Ejemplo (rellénalo con datos confirmados) |
|---|---|---|
| **Dolor** | *"La razón por la que [problema] es que te enfocas en lo equivocado."* | "Tu hijo no se aburre de la tecnología: se aburre de sólo verla." |
| **Contrario** | *"[Lo que todos creen] no es [lo que parece]."* | "Más horas de pantalla no es el problema; el problema es qué hace en ella." |
| **Promesa con número** | *"[N] cosas que [resultado] — la última nadie la hace."* | "4 cosas que tu hijo puede construir este mes." |
| **Novedad** | *"Ahora ya puedes [nueva capacidad]."* | "Ahora tu hijo puede diseñar una pieza y llevársela impresa en 3D." |
| **Facilidad** | *"La forma más fácil de [resultado]. Se llama [nombre]."* | "La forma más fácil de que pruebe programación: la clase de prueba gratis." |

## Llamada a la acción

- **Una sola**, al final, con **palabra clave** que diga de qué pieza vino el mensaje: *CLASES*,
  *NEGOCIO*. Sin palabra clave no se puede medir.
- El patrón que más se repite en la base de @kallaway es *"comenta [PALABRA] y te mando [recurso]"*
  — un recurso gratis a cambio de una palabra. Adáptalo a WhatsApp: *"escribe CLASES y te mando los
  horarios de la clase de prueba"* — **sólo si ese recurso existe** (si no, no lo prometas).

## Reglas

- **Cada afirmación del guion sale de `hechos.md` confirmado.** El guion es copy: pasa por
  `verificar-hechos` como cualquier otro.
- **El texto en pantalla se compone en edición**, nunca dentro de una imagen o video generado.
- **Sin menores reconocibles** sin consentimiento firmado; sin personas generadas.
- El gancho que gane en orgánico (más % visto completo, guardados, compartidos) es el que se pauta;
  los otros se archivan. Ver `Estrategia de contenido.md`.

## De dónde sale

Base de conocimiento de @kallaway (`docs/knowledge-bases/`, 100 videos), en la agencia madre:
- Estructura de 8 pasos: video `7679804544657788191` — *"This is the ultimate scriptwriting format
  for short-form content."*
- Tipos de gancho: su *Hook Library* (videos `7641206959236009247`, `7646139653707336991`,
  `7651981914001231134`, `7657919247670152479`).
- Llamada a la acción con palabra clave: su patrón *Comment-to-DM Lead Magnet*, el más frecuente en
  la cuenta.

Es el método de un creador que funciona en su cuenta; nosotros lo medimos en la nuestra por costo
por conversación.
