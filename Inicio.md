# 🏠 Mi agencia

Esta bóveda **es** la agencia. Todo vive aquí, en archivos locales: Obsidian es donde tú lees y
apruebas; Claude Code es donde los agentes trabajan. Los dos ven los mismos archivos.

## Tu tablero

![[Tablero.base]]

Las vistas de arriba (Calendario, Por aprobar, Bloqueadas, Creativos por revisar) se llenan solas
con las notas que dejan los agentes.

## Cómo apruebas

Abre la nota de una pieza → en **Propiedades** cambia `estado` de `propuesta` a `aprobada` y
escribe tu nombre en `aprobado_por`. **Eso es la aprobación.** Ningún agente puede escribir
`aprobada`: es tu firma.

| estado | significa |
|---|---|
| `propuesta` | El agente la propone; te toca revisarla |
| `bloqueada` | Falta un dato del cliente; la pregunta está en `pregunta` |
| `aprobada` | Tú la aprobaste |
| `publicada` | Ya salió |

## El equipo

Viven en la carpeta oculta `.claude/` (Obsidian no muestra carpetas que empiezan con punto).
Para verlos o editarlos: en Claude Code escribe `/agents`, o pídele *"muéstrame al estratega"*.

| Agente | Úsalo para |
|---|---|
| estratega | Brief, periodo, calendario; coordina a los demás |
| investigador | Mercado, competidores, tendencias, con fuentes |
| creativo | Copy y prompts de imagen/video para piezas aprobadas |
| analista | Números y el reporte HTML |

## Clientes

- [[clientes/cafe-norte/copy-con-trampa|Café Norte — copy para revisar (ejercicio)]]

## Para después

- [[Conectores para después]]
