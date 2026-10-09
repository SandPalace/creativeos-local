---
name: verificar-hechos
description: La compuerta de datos — revisa un copy, un brief o un prompt, extrae cada dato del cliente (precio, fecha, horario, dirección, edad, oferta) y bloquea la pieza si alguno no está confirmado en hechos.md. Úsalo SIEMPRE antes de escribir o entregar copy, y cuando alguien pregunte "¿esto está bien?".
allowed-tools: Read, Grep, Bash
---

# Verificar hechos

## Orden de operaciones

1. **Extrae** del texto cada afirmación verificable: números, precios, fechas, días, horarios,
   direcciones, rangos de edad, nombres de producto, promociones, garantías.
2. **Busca cada una** en `clientes/<cliente>/hechos.md`.
3. **Calcula** lo calculable: cada fecha con día de la semana se comprueba con
   `date -j -f "%Y-%m-%d" <fecha> "+%A"` (macOS) o `date -d <fecha> +%A` (Linux).
4. **Clasifica** cada afirmación:
   - ✅ `confirmado` en hechos.md y el valor coincide **exacto**.
   - ⛔ `inferido`, `falta`, no aparece, o el valor difiere → **bloquea**.
5. **Entrega la tabla** y el veredicto:

```markdown
| afirmación en el copy | hechos.md | veredicto |
|---|---|---|
| "de 7 a 17 años" | publico: 8 a 15 años, confirmado | ⛔ no coincide: el rango es 8 a 15 |
| "inscripción gratis" | no aparece | ⛔ preguntar al dueño |
| "lunes 13 de octubre" | date → martes | ⛔ el 13 es martes |

VEREDICTO: BLOQUEADA — 1 dato distinto, 1 dato sin confirmar, 1 fecha incorrecta.
Pregunta para el dueño: "¿La inscripción es gratis en octubre? ¿Para todos los cursos?"
```

6. **Bloquea sólo esta pieza.** Las demás siguen. En la nota: `estado: bloqueada` y la pregunta
   exacta en `pregunta` — así sale en rojo en el Flujo.
7. **Desbloquea** cuando el director conteste: agrega o corrige la fila en `hechos.md` con
   `confirmado` y la fuente (`director, chat <fecha>`), pasa la pieza a `propuesta` y vacía
   `pregunta`. La tarjeta vuelve a la columna azul para que él la apruebe.
8. **Auditoría de fechas:** en cada pieza que toques, `dia` debe ser el de `date` sobre `fecha`
   (el director puede mover piezas en el Calendario). Si no coincide, corrígelo y avisa.

## Nunca

- Corregir el dato tú mismo con un valor "más probable".
- Aceptar `inferido` porque "seguro es así".
- Copiar un día de la semana de otro documento, aunque sea del cliente.

## Por qué

Un valor plausible y específico es el más peligroso: nadie lo cuestiona. Y una fe de erratas que
decía "miércoles 27" estaba mal — el 27 era jueves. Hasta las correcciones se verifican.
