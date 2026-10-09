# Kit · Mi agencia de marketing agéntica

Una carpeta que es tu agencia. **Claude Desktop** (modo Code) es donde trabaja tu CMO y su equipo de
agentes; **Obsidian** es donde tú contestas, revisas y firmas. Los dos abren la misma carpeta. Todo
es local: nada sale de tu computadora.

## Instalación (una sola vez)

| Programa | Para qué | Cómo |
|---|---|---|
| **Claude Desktop** | Donde trabajan los agentes (pestaña **Code**) | claude.ai/download · plan **Pro o superior** · inicia sesión |
| **Obsidian 1.14+** | Donde diriges y firmas | obsidian.md · gratis · si ya lo tienes: Ajustes → General → *Buscar actualizaciones* **y reinicia** |
| **git** | Para clonar este repo | Mac: abre Terminal y escribe `git --version`; si te ofrece instalar las *herramientas de desarrollador*, acepta. Windows: git-scm.com |

**Para el taller no necesitas** Node, Python ni nada más. (`sqlite3`, opcional, ya viene en macOS.)

**Opcional · el estudio de video** (agente `motion-editor`, de AI Studios): para que el equipo te
entregue el video terminado de una pieza, no sólo su guion y sus prompts.

```bash
brew install node ffmpeg                 # Node 20+ y ffmpeg 7+
python3 -m pip install numpy scipy       # la música se sintetiza en Python
cd render/gsap && npm install            # GSAP + el renderer
npx playwright install chromium-headless-shell
# los efectos de sonido ya vienen (skill tesseract-motion); la app Tesseract es opcional
```

Detalle, plantillas y licencias: `render/LEEME-kit-video.md`.

## Arranque

1. **Clona el repo** (Terminal):
   ```bash
   git clone https://github.com/SandPalace/creativeos-local.git ~/mi-agencia
   ```
   Sin git: descomprime `mi-agencia.zip` en `~/mi-agencia`.
2. **Obsidian** → *Abrir carpeta como bóveda* → `~/mi-agencia`. Cuando pregunte, elige **confiar en
   el autor y activar plugins**. Abre **Inicio**.
3. **Claude Desktop** → pestaña **Code** → elige la carpeta `~/mi-agencia` → modo de permisos
   **Manual** (así ves cada cosa que el agente pide hacer).
4. **Deja tus documentos** en la carpeta `documentos/`: copias de tu lista de precios, brochure,
   logo, manual de marca, capturas de tus redes (PDF, imagen, Word o CSV). El CMO los lee primero y
   sólo te pregunta lo que no encuentre. Qué meter y qué no: `documentos/LEEME.md`.
5. Escribe:
   > *"Hola, soy el dueño de <tu negocio>. Te dejé mis documentos."*

El CMO revisa qué hay en la bóveda y te entrevista para llenar lo que falta. **Pon las dos ventanas
lado a lado** y mira cómo se llena Obsidian mientras contestas.

## Qué trae la bóveda

- **Pantallas** (en *Marcadores*, en orden): Inicio → Flujo → Calendario → Equipo → Presentación →
  Conectores.
- **El equipo** vive en `.claude/` y lo ves en **Equipo**: 5 agentes (cmo, investigador, creativo,
  analista, motion-editor) y 18 skills. En Claude Desktop, escribe `/` para ver los skills.
- **Dos plugins de la comunidad** ya instalados en `.obsidian/plugins/`: *Calendar Bases* (la
  cuadrícula del mes) y *Unhidden* (muestra la carpeta `.claude` —y sólo ésa— para la página
  Equipo). Por eso Obsidian pide confiar al abrir.
- **La presentación del taller**: abre `Presentación.md` → ⌘P → *Start presentation*.

## Cómo apruebas

En **Flujo**, arrastra la tarjeta a *aprobada* y escribe tu nombre en `aprobado_por`. Ningún agente
puede hacerlo: es tu firma. Si falta el nombre, la tarjeta dice ⚠ *falta firma*.

## Si algo no se ve

| Ves | Haz |
|---|---|
| "unknown view type: kanban" | Actualiza Obsidian a 1.14+ **y reinicia** |
| Inicio sin colores | Reinicia Obsidian; o Ajustes → Apariencia → Fragmentos CSS → activa `agencia` |
| Calendario o Equipo vacíos | Ajustes → Plugins de la comunidad → desactiva *Modo restringido* → enciende los dos plugins |

Lee `CLAUDE.md`: ahí está quién aprueba qué. Los conectores para cuando crezcas, en
`Conectores para después.md`. `datos/ejemplo-exporte.csv` trae métricas **ficticias** para practicar
`metricas-sqlite` (opcional): P03 tiene el CTR más alto y es la pieza más cara por resultado.
