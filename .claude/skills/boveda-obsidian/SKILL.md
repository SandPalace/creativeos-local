---
name: boveda-obsidian
description: El mapa de la agencia — dónde va cada archivo, qué propiedades lleva cada tipo de nota, quién puede escribir cada estado, qué ve el director en Inicio / Flujo / Calendario, y el ciclo completo de gestión de marketing de un cliente (alta → plan → aprobación → producción → publicación → medición → cierre). Úsalo antes de crear o mover cualquier nota, cuando no sepas dónde va algo, cuando pregunten "¿cómo funciona la agencia?", "¿qué sigue?", "¿en qué va el cliente?" o al empezar una sesión.
allowed-tools: Read, Glob, Grep, Bash
---

# La bóveda: dónde va cada cosa y cómo se gestiona un cliente

Esta carpeta es **a la vez** la agencia y una bóveda de Obsidian. Tú escribes archivos; el director
los ve en Obsidian como tableros. **Si una nota no tiene las propiedades correctas, no aparece en
ningún tablero y para el director no existe.**

## 1 · El mapa

```
Inicio.md              ← dashboard del director (Flujo + Creativos + Calendario). No lo edites.
Flujo.md               ← kanban a pantalla completa: aquí aprueba arrastrando tarjetas.
Calendario.md          ← el mes en cuadrícula: las piezas en su fecha.
Equipo.md              ← agentes y skills (lee .claude/ con el plugin Unhidden).
Presentación.md        ← diapositivas del taller (plugin core Slides).
.obsidian/             ← apariencia y plugins del director. Nunca lo toques.
CLAUDE.md              ← reglas de la agencia.
Conectores para después.md
plantillas/            ← brief.md · hechos.md · reporte.html: se copian, nunca se editan.
datos/Tablero.base     ← las vistas de piezas y creativos (YAML). No lo edites sin que el director lo pida.
datos/Equipo.base      ← las vistas del equipo. Ídem.
datos/esquema.sql      ← opcional: datos/agencia.db (sqlite)
documentos/            ← copias de los PDFs, imágenes, Word, CSV del dueño. Nunca se borran ni mueven.
clientes/<cliente>/    ← <cliente> en kebab-case: algolab, estudio-yoga-sur
  brief.md             tipo: brief       — quién es, objetivos ordenados, periodo
  hechos.md            (tabla)           — LA fuente de verdad: dato · valor · fuente · estado
  documentos.md        (índice)          — qué se sacó de cada archivo de documentos/
  investigacion.md     tipo: investigacion
  piezas/P01.md        tipo: pieza       — una nota por publicación del periodo
  creativos/P01_v1.md  tipo: creativo    — copy + prompts de una pieza; imágenes y clips al lado
  creativos/P01_v1_A.png
  reportes/2026-10-31_resultados.html    — se abre en el navegador, no en Obsidian
```

**Nombres:** piezas `P01`, `P02`… (dos dígitos, sin saltarse números, nunca se reusan). Creativos
`<pieza>_v<n>`; los archivos generados `<pieza>_v<n>_<variante>.<ext>` (`P01_v1_A.png`,
`P02_v1_toma1.mp4`). Un archivo que el director ya vio **no se sobrescribe**: sube la versión.

## 2 · Qué propiedad mueve qué tablero

| Propiedad | La usa | Efecto en lo que ve el director |
|---|---|---|
| `tipo` | todas las vistas | `pieza` → Flujo, Calendario, Lista. `creativo` → Creativos. Otro valor → no aparece. |
| `estado` | Flujo (columna), colores | de izquierda a derecha: `bloqueada` rojo → `propuesta` azul → `aprobada` verde → `publicada` morado |
| `fecha` | Calendario | El día donde cae la tarjeta. **ISO `AAAA-MM-DD`**, sin comillas. |
| `canal` | la píldora de color | Texto corto y consistente (ver lista abajo). |
| `pregunta` | tarjeta bloqueada | Se ve en rojo con ❓. Una pregunta, cerrada, que el dueño pueda contestar. |
| `aprobado_por` | tarjeta aprobada | ✍ nombre. Vacío en una aprobada → **⚠ falta firma**. |
| `imagen` | Creativos (portada) | `"[[P01_v1_A.png]]"` — corchetes y comillas; el archivo dentro de la bóveda. |

**Canales** (escríbelos así, siempre igual): `Instagram feed`, `Instagram reels`,
`Instagram stories`, `TikTok`, `YouTube Shorts`, `Facebook`, `WhatsApp`, `Google`, `Web`, `Email`.

**Reglas de frontmatter:** va en los primeros bytes del archivo (nada antes del `---`); los enlaces
dentro del frontmatter entre comillas (`pieza: "[[P01]]"`); un campo vacío se deja vacío
(`pregunta:`), nunca `null`, `-` ni `N/A`.

## 2b · Estilo de las notas: íconos y colores

Las notas se leen en Obsidian; que sean agradables de leer. **Usa callouts** — cajas de color con
ícono, nativas de Obsidian — y **siempre con el mismo significado**, para que el color ya diga algo:

| Callout | Color · ícono | Úsalo para |
|---|---|---|
| `> [!success]` | verde · ✓ | lo confirmado, lo listo, lo aprobado |
| `> [!warning]` | amarillo · ⚠ | lo `inferido`, lo que falta confirmar |
| `> [!danger]` | rojo · ⚡ | lo que **bloquea** una pieza |
| `> [!question]` | naranja · ? | una pregunta para el dueño (cerrada, que pueda contestar) |
| `> [!tip]` | turquesa · 🔥 | el siguiente paso |
| `> [!info]` | azul · ℹ | contexto, de dónde sale un dato |
| `> [!example]` | morado · ☰ | ejemplos, borradores de copy, prompts |
| `> [!quote]` | gris · ❝ | las palabras textuales del dueño |

```markdown
> [!danger] Bloquea las piezas con precio
> Falta saber cada cuánto se paga el semestre (`precios`).

> [!question] Para ti
> ¿El semestre de $11,000 es del plan 1 o del plan 2?
```

Más reglas de estilo:
- **Títulos con `##` y `###`**: ya salen con color e ícono por el CSS de la bóveda; no les pongas emojis.
- `==resaltado==` para la cifra o la palabra clave de un párrafo (una por párrafo, no más).
- **Tablas** para datos que se comparan (precios, piezas, competidores); callouts para lo que hay que
  ver o decidir.
- Un callout plegado `> [!info]-` para el detalle largo que no todos necesitan leer.
- Nada de esto va dentro del **frontmatter** ni cambia los nombres de las propiedades.

## 2c · Llevar al dueño a la pantalla (puedes manejar Obsidian)

Puedes **abrir en Obsidian la nota o pantalla que quieres que vea**, en vez de describirle el camino:

```bash
open "obsidian://open?path=$PWD/clientes/algolab/brief.md"
open "obsidian://open?path=$PWD/Flujo.md"
open "obsidian://open?path=$PWD/Calendario.md"
```

- La ruta va completa (`$PWD/…`). Espacios → `%20`, acentos → su código
  (`Presentaci%C3%B3n.md`, `Conectores%20para%20despu%C3%A9s.md`).
- **Avísale antes de abrir:** *"Te abro el brief en Obsidian."* Al abrir, Obsidian toma el foco: si
  el dueño estaba escribiendo o dictando, su texto cae dentro de la nota. Si ves texto suelto que no
  escribiste tú, pregúntale antes de borrarlo.
- **La primera vez** Obsidian pregunta *"¿Ejecutar acción desde un enlace externo?"*: dile que marque
  **"No volver a preguntar"** y dé **Continuar**.
- Úsalo en los momentos clave: al terminar el onboarding (abre el brief), al pedir una firma (abre la
  nota o el Flujo), al terminar el calendario (abre Calendario), al entregar el reporte (`open` del
  HTML, que se ve en el navegador).
- Abrir no sustituye explicar: igual di en una frase qué es y qué tiene que hacer ahí.

## 3 · Quién escribe cada estado

| Nota | Estado | Lo escribe | Cuándo |
|---|---|---|---|
| brief | `propuesta` | agente | al empezar `onboarding` (se llena en vivo) |
| brief | `aprobada` + `aprobado_por` | **director** | en Obsidian |
| pieza | `propuesta` | agente | todos sus datos están `confirmado` |
| pieza | `bloqueada` + `pregunta` | agente | depende de un dato `inferido` o `falta` |
| pieza | `aprobada` + `aprobado_por` | **director** | arrastra la tarjeta a *aprobada* y firma |
| pieza | `publicada` | **director** | ya la vio en su cuenta (aunque la haya subido el agente) |
| creativo | `propuesta-sin-revisar` | agente | al guardar copy + prompts |
| creativo | `aprobada` + `aprobado_por` | **director** | revisó la imagen o el clip |
| creativo | `rechazada` | **director** | → el agente crea `_v2` desde el brief, no desde la v1 |

**La firma vale escrita `aprobada` o `aprobado`** (el brief es masculino; el dueño escribe como le sale) — siempre que `aprobado_por` tenga un nombre. No la corrijas.

**Nunca escribes `aprobada`, `publicada`, `rechazada` ni `aprobado_por`.** Si el director te dice en
el chat "apruébala", contéstale que lo haga él en el Flujo: la firma es suya.

**Sí puedes:** pasar una pieza `bloqueada` → `propuesta` cuando el dato que faltaba ya está
`confirmado` en `hechos.md` (y vaciar `pregunta`); y regresar una `aprobada` → `propuesta` **sólo**
si el director pidió un cambio de copy, avisándole que necesitará volver a firmar.

**`dia` se calcula de `fecha`.** El director puede mover una pieza en el Calendario y eso cambia
`fecha` pero no `dia`. Cada vez que leas o toques una pieza, comprueba
`date -j -f "%Y-%m-%d" <fecha> "+%A"` y, si no coincide, corrige `dia` y avísale.

## 4 · El ciclo de gestión de un cliente

Un **periodo** dura 2–4 semanas. Cada paso deja un archivo que el siguiente lee; ninguno vive sólo
en el chat.

| # | Paso | Quién | Skill | Deja | El director lo ve en | Compuerta |
|---|---|---|---|---|---|---|
| 0 | **Evaluar** | CMO | `evaluar-boveda` | — (diagnóstico en el chat) | — | — |
| 0a | **Leer documentos** | CMO | `leer-documentos` | filas `inferido` en `hechos.md` + `documentos.md` | hechos en amarillo | — |
| 0b | **Onboarding** | CMO + dueño | `onboarding` | `brief.md`, `hechos.md`, ronda por ronda | las notas del cliente, llenándose | firma el brief |
| 1 | **Investigar** | investigador (lo pide el CMO) | `investigar-mercado` | `investigacion.md` | la nota | — |
| 2 | **Planear** | CMO | `calendario-de-contenido` | `piezas/Pxx.md` | Flujo (propuesta / bloqueada) y Calendario | — |
| 3 | **Desbloquear** | CMO | `verificar-hechos` | fila `confirmado` en `hechos.md`; pieza → propuesta | la tarjeta roja pasa a azul | el dato lo da el dueño |
| 4 | **Aprobar** | **director** | — | `estado: aprobada`, `aprobado_por` | Flujo, columna verde | su firma |
| 5 | **Producir** | creativo (y `motion-editor` si pide el video terminado) | `verificar-hechos` → `guion-de-contenido` → `prompt-imagen` / `prompt-video`, o `motion-video` | `creativos/Pxx_v1.md` (+ archivos; el video: `Pxx_vN_video.mp4` + portada) | Creativos (amarillo) | revisa y aprueba o rechaza |
| 6 | **Publicar** | cmo (con permiso por envío) o el director a mano | `publicar` | `## Publicación` + `enlace:` en la pieza | Flujo: el director la mueve a morada | autoriza cada envío; marca `publicada` |
| 7 | **Medir** | analista | `metricas-sqlite` (opcional) | `datos/agencia.db` | — | — |
| 8 | **Reportar** | analista | `reporte-html` | `reportes/<fecha>_<tipo>.html` | lo abre en el navegador | decide si lo manda al cliente |
| 9 | **Cerrar** | CMO | `onboarding` | brief del siguiente periodo con lo aprendido | nuevo brief | aprueba el nuevo brief |

**Lo que no se salta:** sin brief aprobado no hay calendario; sin pieza aprobada no hay creativo;
sin `verificar-hechos` no hay copy; sin firma no hay publicación. **Un dato faltante bloquea esa
pieza, no el periodo:** las demás siguen.

## 5 · "¿En qué va el cliente?" — cómo contestarlo

Lee las propiedades, no la memoria del chat:

```bash
grep -h "^estado:" clientes/<cliente>/piezas/*.md | sort | uniq -c      # cuántas en cada columna
grep -H "^pregunta: ." clientes/<cliente>/piezas/*.md                   # qué está bloqueado y por qué
grep -H -e "^estado:" -e "^aprobado_por:" clientes/<cliente>/piezas/*.md  # aprobadas sin firma
```

Responde así: *"AlgoLab, periodo 13–31 oct: 1 propuesta, 1 bloqueada (¿horario del sábado?), 2 aprobadas
(1 sin firma), 1 publicada. Siguiente paso: …"* — y el siguiente paso sale de
la tabla del ciclo, no de una intuición.

## Por qué

Lo que el director no ve en su tablero no existe para él, y lo que sólo se dijo en el chat se
olvida. Por eso cada paso deja una nota con propiedades: el tablero es la memoria de la agencia.
