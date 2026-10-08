---
name: brief-de-cliente
description: Arranca un cliente nuevo o un periodo nuevo — entrevista al director con preguntas concretas y deja clientes/<cliente>/brief.md y hechos.md. Úsalo cuando digan "nuevo cliente", "arranquemos con X", "hazme el brief" o antes de planear un periodo sin brief.
allowed-tools: Read, Write, Glob, Bash
---

# Brief de cliente

## Orden de operaciones

1. **Busca lo que ya existe.** Si hay `clientes/<cliente>/brief.md` o `hechos.md`, léelos y
   pregunta sólo lo que falta. No repitas preguntas ya contestadas.
2. **Pregunta en un solo bloque, máximo 12 preguntas**, agrupadas:
   - **Negocio:** qué vende, precio(s), dónde, horarios, qué lo hace distinto.
   - **Cliente ideal:** quién compra, por qué, qué objeción tiene.
   - **Periodo:** fechas exactas de inicio y fin, objetivo #1, #2, #3 (ordenados), presupuesto.
   - **Canales:** cuáles tiene (IG, TikTok, FB, WhatsApp, web) y dónde cae el cliente que escribe.
   - **Medición:** qué cuenta como éxito (mensajes, reservas, ventas) y cuánto vale uno.
   - **Marca:** colores (hex si los hay), tono, lo que **nunca** se dice.
3. **Para.** Espera respuestas. No rellenes huecos con suposiciones.
4. **Escribe `hechos.md`**: una fila por dato con su fuente (ver formato abajo). Lo que no se
   contestó entra con estado `falta`.
5. **Escribe `brief.md`**: resumen de una página que cite los hechos, no los repita con otras
   palabras. Empieza con este frontmatter (Obsidian lo muestra como propiedades):

   ```yaml
   ---
   tipo: brief
   cliente: cafe-norte
   periodo_inicio: 2026-10-13
   periodo_fin: 2026-10-31
   estado: propuesta
   aprobado_por:
   ---
   ```
6. **Calcula los días de la semana** de las fechas del periodo con `date`; no los escribas de
   memoria.
7. Pide al director que lo apruebe **en Obsidian**, cambiando `estado` a `aprobada`. Tú nunca
   escribes `aprobada`.

## Formato de `hechos.md`

```markdown
| dato | valor | fuente | estado |
|---|---|---|---|
| precio_cafe_americano | $45 MXN | dueño, taller 2026-10-08 | confirmado |
| horario_sabado | — | — | falta |
| promo_octubre | 2x1 martes | inferido de su Instagram | inferido |
```

Estados: `confirmado` (lo dijo el cliente o un documento suyo), `inferido` (lo dedujimos —
**nunca sirve para copy**), `falta`.

## Por qué

Un agente inventó un rango de edad "plausible" para un anuncio y quedó publicado. El dato real era
otro. Un valor que suena bien es más peligroso que un hueco, porque nadie lo cuestiona.
