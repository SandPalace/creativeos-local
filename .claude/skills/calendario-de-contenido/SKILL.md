---
name: calendario-de-contenido
description: Arma el calendario de las próximas 2–4 semanas como una nota de Obsidian por pieza — fecha, canal, formato, objetivo, copy propuesto, a dónde llega el cliente y cómo se mide. Úsalo cuando digan "calendario", "plan de contenido", "qué publicamos", "arma el periodo/el mes".
allowed-tools: Read, Write, Edit, Glob, Bash
---

# Calendario de contenido

## Orden de operaciones

1. **Requiere brief aprobado.** Si el frontmatter de `brief.md` no dice `estado: aprobada` (o
   `aprobado`) con un nombre en `aprobado_por`, para y pídele al dueño que lo firme en Obsidian.
2. **Lee** `brief.md`, `hechos.md` e `investigacion.md` (si no hay investigación, sugiere correr
   `investigar-mercado` primero).
3. **Ritmo.** Lee `Estrategia de contenido.md` y pregúntale al dueño: *"¿Ritmo lento (3–5
   publicaciones a la semana) o rápido (1–2 clips diarios)?"* — explícale la diferencia en una
   frase. Reparte las piezas según esa tabla (cuántas por semana, qué días, qué formatos) y anota el
   ritmo en el brief si no está.
3b. **Objetivos ordenados.** Toma del brief el objetivo #1, #2, #3. Cada pieza sirve a uno.
4. **Fechas calculadas.** El día de la semana sale de `date` (`date -j -f "%Y-%m-%d" <fecha> "+%A"`
   en macOS), nunca de memoria.
5. **Una nota por pieza** (propiedades y canales válidos: skill `boveda-obsidian`, sección 2) en `clientes/<cliente>/piezas/P01.md`, `P02.md`… con el formato de abajo.
   Si un campo depende de un dato que falta o es `inferido` en `hechos.md`, la pieza va con
   `estado: bloqueada` y la pregunta exacta en `pregunta`.
6. **Graba una vez, publica muchas:** si el ritmo es rápido, propón una sesión de grabación y
   reparte sus clips en varias piezas (sección *Graba una vez* de la estrategia).
6b. **Mezcla de formatos:** al menos dos familias (estático/carrusel y video). Dato real de nuestra
   agencia: el estático de oferta y el video de persona hablando a cámara suelen costar menos por
   resultado que el video "cinematográfico" — no supongas que lo más producido rinde más.
7. **No sobrescribas** una pieza que ya existe. Si hay que rehacerla y no está aprobada, edítala; si
   está `aprobada`, no la toques y avisa.
8. **Revisa que aparezcan:** cada nota empieza con `---`, `tipo: pieza`, `fecha` ISO y un `canal` de
   la lista. Si falta uno, la pieza no sale en el Flujo ni en el Calendario.
9. Dile al director: *"Hay N piezas en la columna propuesta del Flujo y M bloqueadas."*

## Formato de la nota de pieza

```markdown
---
tipo: pieza
cliente: algolab
id: P01
fecha: 2026-10-14
dia: miércoles
canal: Instagram feed
formato: carrusel 4:5, 5 láminas
objetivo: "#1 mensajes por WhatsApp"
datos: [oferta, publico, canales]
llega_a: WhatsApp con la palabra "CLASES"
se_mide: mensajes que traen la palabra CLASES
exito: ">= 10 mensajes"
estado: propuesta
pregunta:
aprobado_por:
---

## Idea / gancho
4 cosas que tu hijo puede construir este mes (una por curso)

## Copy propuesto
…

## Notas
```

Estados que puedes escribir: `propuesta`, `bloqueada` (y `bloqueada` → `propuesta` cuando el dato ya
quedó `confirmado` en `hechos.md`; vacía `pregunta`). **Nunca** `aprobada` ni `aprobado_por`: eso
es la firma del director.

## Por qué

Un mensaje en un chat se lee, se aprueba y se olvida. Una nota con `llega_a` y `se_mide` es la
única forma de saber después qué pieza trajo clientes — y como es una propiedad, el tablero la
muestra sin que nadie la busque.
