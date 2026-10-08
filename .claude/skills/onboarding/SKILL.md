---
name: onboarding
description: Entrevista al dueño del negocio en rondas cortas para llenar la bóveda — qué vende, oferta, precios, público, canales, marca, objetivos, medición y el periodo de las próximas semanas — y escribe cada respuesta al momento en hechos.md y brief.md. Úsalo con un negocio nuevo, cuando evaluar-boveda encuentre huecos, o cuando digan "hazme el brief", "empecemos", "te cuento de mi negocio".
allowed-tools: Read, Write, Edit, Glob, Bash
---

# Onboarding: llenar la bóveda con el dueño

El dueño del negocio es la única fuente de los datos de su negocio. Tu trabajo es preguntarle bien,
escribir exactamente lo que dice y que **vea cómo se llena la bóveda mientras contesta**.

## Antes de preguntar

1. Corre (o lee el resultado de) `evaluar-boveda`. Si hay documentos sin leer, corre antes
   `leer-documentos`. **Pregunta sólo lo que falta.**
2. Si es un negocio nuevo, crea la carpeta `clientes/<cliente>/` (kebab-case: `algolab`,
   `estudio-yoga-sur`) copiando **`plantillas/hechos.md`** → `hechos.md` y **`plantillas/brief.md`**
   → `brief.md` (`estado: propuesta`) — así aparece en Obsidian desde el primer minuto.

## Ronda 0 · Lo que salió de tus documentos (si hay)

Si `leer-documentos` dejó datos `inferido` con fuente `documentos/…`, empieza confirmándolos **en
bloque**, en una tabla: *"Esto saqué de tus documentos. ¿Sigue vigente? Dime cuál cambió."* Lo que
el dueño confirme pasa a `confirmado` (fuente: `documentos/<archivo>, confirmado por el dueño
<fecha>`); lo que corrija, con sus palabras. Después, las rondas sólo preguntan lo que siga faltando.

## Las rondas (máximo 4 preguntas por ronda)

| Ronda | Pregunta por | Claves en `hechos.md` |
|---|---|---|
| 1 · El negocio | qué vende · a quién y **qué lo frena para comprar** · dónde · cuándo atiende | `negocio`, `publico` (con la objeción), `ubicacion`, `horarios` |
| 2 · La oferta | qué se vende este periodo, precios, qué lo hace distinto, restricciones | `oferta`, `precios`, `diferenciador`, `restricciones` |
| 3 · Los canales y la marca | redes, a dónde llega el cliente, colores, tono, lo que nunca se dice | `canales`, `marca` |
| 4 · El periodo | fechas de inicio y fin, fechas clave (eventos, inicios de curso), objetivos #1–#3, qué es un resultado y cuánto vale | `periodo`, `objetivo`, `medicion` |

**Después de cada ronda:**
1. Escribe las respuestas en `hechos.md` **antes** de hacer la siguiente pregunta.
2. Dile en una línea qué quedó: *"Listo: 4 datos confirmados en hechos.md. Míralos en Obsidian →
   clientes/algolab/hechos."*
3. Sigue con la ronda siguiente.

Las rondas cubren **todas las secciones de `plantillas/brief.md`**: si agregas una pregunta, que sea
para llenar una sección de la plantilla. Pregunta concreto, con un ejemplo de respuesta: no *"¿cuál es tu público?"* sino *"¿quién decide la
compra: los papás o el alumno? ¿De qué edades?"*.

## Formato de `hechos.md`

```markdown
| dato | valor | fuente | estado |
|---|---|---|---|
| publico | papás de niños de 8 a 15 años | dueño, onboarding 2026-10-08 | confirmado |
| horarios | sábados 9:00–14:00 | "creo que así", dueño | inferido |
| precios | — | — | falta |
```

- `confirmado`: el dueño lo dijo con seguridad o lo leyó de un documento suyo.
- `inferido`: lo dijo con duda ("creo", "más o menos"), o lo dedujiste tú. **Nunca sirve para copy.**
- `falta`: no lo sabe todavía. Anota a quién hay que preguntarle.

**Escribe sus palabras, no tu interpretación.** Si dice "como 900 pesos", el valor es "como 900
pesos" y el estado `inferido`.

## Cierra con el brief

Con las 4 rondas, llena `brief.md` **sección por sección de `plantillas/brief.md`**: cada línea cita
su clave de `hechos.md` (no la reescribe con otras palabras); lo `inferido` o en `falta` va en
cursiva y a la tabla *Lo que todavía bloquea piezas*. No agregues ni quites secciones: así todos
los briefs se leen igual. Si el dueño ya editó el brief en Obsidian, **conserva sus cambios**.

```yaml
---
tipo: brief
cliente: algolab
periodo_inicio: 2026-10-13
periodo_fin: 2026-10-31
estado: propuesta
aprobado_por:
---
```

Calcula los días de la semana de las fechas con `date`, nunca de memoria. Termina explicando la
firma como si fuera la primera vez:

> [!tip] Tu primera firma: el brief
> 1. En Obsidian, columna izquierda: **clientes → <cliente> → brief**.
> 2. Léelo. Lo amarillo es lo que no confirmaste; lo rojo, lo que frena alguna pieza.
> 3. Arriba, en **Propiedades**, haz clic en el valor de **estado** y escribe `aprobada`.
> 4. En **aprobado_por** escribe tu nombre. Listo: eso es tu firma.
>
> Después investigo a tu competencia y armo el calendario de las próximas semanas.

## Cierre de periodo

Para un periodo nuevo del mismo negocio: lee el último reporte en `reportes/`, revisa que los hechos
sigan vigentes (precios y horarios caducan) y escribe el brief nuevo con *Lo que aprendimos*.

## Por qué

Un agente inventó un rango de edad "plausible" para un anuncio y quedó publicado: decía 7 a 17 años
y el real era 8 a 15. Un valor que suena bien es más peligroso que un hueco, porque nadie lo
cuestiona. Por eso cada dato lleva su fuente, y por eso el dueño ve cada uno en cuanto se escribe.
