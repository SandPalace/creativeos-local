---
name: evaluar-boveda
description: Revisa si la bóveda ya tiene lo necesario para trabajar las campañas de un negocio — brief, hechos confirmados, periodo y calendario — y dice exactamente qué falta y cuál es el siguiente paso. Úsalo al empezar cualquier sesión, cuando digan "hola", "arranquemos", "¿en qué vamos?", "¿qué sigue?", o antes de planear, producir o reportar.
allowed-tools: Read, Glob, Grep, Bash
---

# Evaluar la bóveda

Antes de trabajar, mira qué hay. Nunca supongas que algo existe porque se habló en el chat: si no
está en un archivo, no existe.

## Orden de operaciones

0. **¿Hay documentos nuevos?** `ls documentos/`. Si hay archivos (además de `LEEME.md`) que no
   aparecen en `clientes/<cliente>/documentos.md`, el siguiente paso es **`leer-documentos`** —
   antes del onboarding: leer primero ahorra preguntas.
1. **¿Hay negocio?** Lista `clientes/*/`. Ninguno → paso a `onboarding` (negocio nuevo). Más de
   uno → pregunta con cuál trabajamos hoy.
2. **¿Hay brief?** Lee `clientes/<cliente>/brief.md`. No existe → `onboarding`. Existe pero no dice
   `estado: aprobada` (o `aprobado`) con un nombre en `aprobado_por` → pide al dueño que lo revise y firme en Obsidian.
3. **¿Están los hechos mínimos?** Revisa `hechos.md` contra la lista de abajo. Cuenta cuántos están
   `confirmado`, cuántos `inferido` y cuántos `falta` (o no aparecen).
4. **¿Hay periodo y calendario?** `periodo_inicio` / `periodo_fin` en el brief y notas en
   `piezas/`. Lee el estado de las piezas:
   `grep -h "^estado:" clientes/<cliente>/piezas/*.md | sort | uniq -c`
5. **Entrega el diagnóstico** con el formato de abajo y **el siguiente paso** — uno solo.

## Hechos mínimos para trabajar campañas

| clave | qué es | sin esto no se puede… |
|---|---|---|
| `negocio` | qué vende, en una frase | nada |
| `oferta` | productos/servicios del periodo, con sus nombres reales | escribir copy |
| `precios` | precio de lo que se anuncia (o "no se publica precio") | anunciar oferta |
| `ubicacion` | dirección o zona que atiende | anuncios locales |
| `horarios` | cuándo atiende / fechas de eventos | invitar a ir o a escribir |
| `publico` | quién compra y quién decide (p. ej. papás vs. alumnos) | segmentar y escribir |
| `canales` | redes que tiene y a dónde llega el cliente (WhatsApp, web) | planear el calendario |
| `marca` | colores (hex), tono, lo que **nunca** se dice | prompts y copy |
| `objetivo` | objetivo #1, #2, #3 del periodo, ordenados | priorizar |
| `medicion` | qué cuenta como resultado y cuánto vale uno | medir y reportar |
| `periodo` | fechas de inicio y fin (2–4 semanas) y fechas clave | el calendario |
| `restricciones` | lo que no se puede prometer, permisos (menores, licencias) | publicar sin riesgo |

## Formato del diagnóstico

```markdown
**<Negocio> — estado de la bóveda**

- Brief: aprobado ✅ / propuesta (falta tu firma) / no existe
- Documentos: 3 leídos · 1 nuevo sin leer (catalogo.pdf)
- Hechos: 9 confirmados · 2 inferidos (precios, horarios) · 1 falta (medicion)
- Periodo: 13–31 oct · Calendario: 6 piezas (3 propuesta, 1 bloqueada, 2 aprobadas)

**Siguiente paso:** <uno solo, concreto — p. ej. "5 preguntas para terminar el onboarding">
```

## Reglas

- Un hecho `inferido` cuenta como **faltante** para escribir copy.
- No arregles nada en este skill: sólo diagnosticas. Llenar es trabajo de `onboarding`.
- Si todo está completo, el siguiente paso sale del ciclo en `boveda-obsidian` (sección 4).
