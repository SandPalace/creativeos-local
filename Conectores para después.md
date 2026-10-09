# Conectores para después

Hoy todo es local y gratis: Obsidian + archivos + Claude Desktop. No necesitas ningún conector para
que tus agentes lean y escriban tu bóveda: **son archivos, Claude ya los ve.**

Cuando la agencia crezca, éstos son los conectores que suman, en el orden en que suelen hacer falta.
Revisa el precio y los permisos de cada uno antes de conectarlo; varios requieren plan de pago o
una cuenta de negocio.

| Cuando necesites… | Conector | Tipo | Ojo con |
|---|---|---|---|
| Ver la web como un humano (perfiles, páginas que bloquean búsqueda) | **Navegador de Claude Desktop** o **Playwright** | Integrado / MCP local | Desktop ya trae navegador. Playwright (`.mcp.example.json`) necesita Node |
| Leer métricas reales de tus anuncios | **Meta Ads MCP oficial** (`mcp.facebook.com/ads`) | MCP remoto, OAuth | Ver *Publicar en tus plataformas*, abajo |
| Compartir documentos con el cliente | **Google Drive / Docs** | Conector de claude.ai | El cliente ve lo que subas: nada sin aprobar |
| Mandar reportes por correo | **Gmail** | Conector de claude.ai | Enviar es publicar: que el agente deje **borrador**, tú envías |
| Agendar publicaciones y juntas | **Google Calendar** | Conector de claude.ai | — |
| Diseño con plantillas de marca | **Canva** | Conector de claude.ai | Componer el texto encima de la imagen generada vive bien aquí |
| Wiki de equipo compartida | **Notion** | MCP / conector | Cuando más de una persona edite a la vez; mientras tanto, Obsidian |
| Avisos al equipo | **Slack** | Conector de claude.ai | Un pedido hecho sólo en un canal se olvida: los pendientes van en una nota o ticket |
| Generar imagen/video desde el agente | APIs de modelos (OpenRouter, Gemini, etc.) | API con llave | Cuesta por generación: pon un tope de gasto antes |

## Publicar en tus plataformas

Cuando ya firmaste el calendario y los creativos, el skill **`publicar`** sube lo firmado siguiendo la
**Estrategia de contenido**. Cada envío te pide permiso (es tu firma), todo anuncio nace pausado, y
**si el agente se topa con algo, se detiene y te pide ayuda** con los pasos para resolverlo.

Sin conectar nada, el agente igual te deja en cada creativo un **paquete de publicación** (archivo,
texto exacto, palabra clave, fecha) para que tú lo subas desde la app. Conecta una plataforma a la vez,
empezando por la que más usas.

| Plataforma | Dificultad | Qué hace el agente | Qué te queda a ti |
|---|---|---|---|
| **Anuncios de Meta** | Fácil: iniciar sesión | Crea anuncios **pausados**, lee resultados | Activar y presupuesto |
| **Instagram orgánico** | Media: app de Meta + token | Publica reels, posts, carruseles, historias | Firmar antes |
| **TikTok** | Media: app de TikTok + token | Lo manda a **borradores** | Publicarlo desde la app |
| **YouTube Shorts** | Media: proyecto de Google + OAuth | Lo sube **privado** | Hacerlo público en YouTube Studio |
| **Google Ads** | Alta: Python + proyecto de Google | **Sólo lee** métricas | Crear los anuncios |

### 1 · Anuncios de Meta — MCP oficial

Meta abrió en abril de 2026 sus conectores de IA para anuncios (beta abierta). Es un MCP remoto en
`https://mcp.facebook.com/ads`: no necesitas app de desarrollador ni token, sólo iniciar sesión.

1. Copia `.mcp.example.json` como `.mcp.json` (ya trae `meta-ads`). Con ese nombre, las reglas `ask` de
   `.claude/settings.json` ya cubren crear, editar, activar y promocionar.
2. Reinicia la conversación en Claude Desktop (pestaña **Code**). La primera vez que el agente use
   Meta se abre la ventana de Meta: inicia sesión y **elige sólo el portafolio de tu negocio**.
3. Prueba sólo lectura: *"¿cuánto gasté la semana pasada y a cuánto me salió cada conversación?"*.

> [!warning] Escribe en tu cuenta real
> Este conector puede crear y cambiar anuncios de verdad. Lo que lo frena son las reglas `ask`: cada
> creación, cambio o activación te abre la ventana de permiso. Si lo conectas desde *Ajustes → Conectores* de Claude en vez
> de `.mcp.json`, las herramientas tienen otro nombre: agrega esas reglas `ask` tú mismo.

### 2 · Instagram orgánico — API de Instagram

Necesitas una cuenta de Instagram **profesional** (de empresa o creador).

1. En developers.facebook.com crea una app y agrega el producto **Instagram** → *API con inicio de
   sesión de Instagram*.
2. Pide los permisos `instagram_business_basic` e `instagram_business_content_publish`, agrega tu
   cuenta de Instagram y genera un **token**.
3. En tu carpeta crea `.env` (nunca se sube a git) con:
   ```
   IG_USER_ID=…
   IG_TOKEN=…
   ```
4. Ojo: Instagram **descarga** el archivo desde una URL pública. Si tus creativos sólo están en tu
   computadora, el agente se va a topar ahí y te va a preguntar dónde alojarlos.

### 3 · TikTok — Content Posting API

1. En developers.tiktok.com crea una app y agrega **Content Posting API**.
2. Pide el permiso **`video.upload`** (manda a borradores). `video.publish` publica directo, pero
   mientras TikTok no audite tu app **todo sale privado**.
3. Autoriza la app con tu cuenta de TikTok y guarda en `.env`: `TIKTOK_TOKEN=…`
4. Cuando el agente suba algo, te llega una notificación en TikTok: ábrela, revisa y publica.

### 4 · YouTube Shorts — YouTube Data API

1. En console.cloud.google.com crea un proyecto y activa **YouTube Data API v3**.
2. Crea credenciales **OAuth** (app de escritorio) con el permiso `youtube.upload` y autoriza tu canal.
3. Guarda en `.env`: `YT_CLIENT_ID=…`, `YT_CLIENT_SECRET=…`, `YT_REFRESH_TOKEN=…`
4. YouTube lo vuelve **Short** solo si el video es vertical o cuadrado y dura 3 minutos o menos. El
   agente lo sube privado; tú lo haces público en YouTube Studio. Límite: 100 subidas al día.

### 5 · Google Ads — MCP oficial (sólo lectura)

Lee campañas y métricas; **no crea ni pausa anuncios**. Necesita Python (`pipx`) y un proyecto de
Google Cloud con acceso a la API de Google Ads (`gcloud auth application-default login`). Ya viene en
`.mcp.example.json` como `google-ads`; cambia `TU_PROYECTO`. Los anuncios los creas tú en Google
Ads con los textos que te deje el agente.

> [!info] Fuentes oficiales (revisadas el 8-oct-2026; las plataformas cambian)
> [Instagram: publicar contenido](https://developers.facebook.com/documentation/instagram-platform/content-publishing) ·
> [TikTok: Content Posting API](https://developers.tiktok.com/doc/content-posting-api-get-started) ·
> [TikTok: subir a borradores](https://developers.tiktok.com/doc/content-posting-api-get-started-upload-content) ·
> [YouTube: videos.insert](https://developers.google.com/youtube/v3/docs/videos/insert) ·
> [Google Ads MCP](https://developers.google.com/google-ads/api/docs/developer-toolkit/mcp-server)

## La regla al conectar cualquier cosa

Clasifica cada herramienta nueva antes de darle permiso:

| Si la herramienta… | Va en `.claude/settings.json` como |
|---|---|
| Sólo lee | `allow` |
| Escribe algo reversible (borrador, archivo local, anuncio pausado) | `ask` |
| Gasta dinero, publica o le escribe a una persona | `ask` — la ventana de permiso **es tu firma** |
| Nunca debería ni intentarlo (borrar todo, leer tus llaves) | `deny` |

Una regla escrita en un prompt no detiene a un agente. `ask` y `deny` sí. Ojo: `ask` necesita a
alguien frente a la pantalla — en una corrida automática sin humano, se bloquea.

## Lo que usan los sistemas que se ven en TikTok

Los "equipos de marketing agénticos" que se venden en redes (oct-2026) suelen montar, encima de
Claude: Semrush y SparkToro (investigación), Surfer (SEO), Canva y Midjourney (diseño),
ElevenLabs (voz), Metricool (programar publicaciones), ManyChat (responder DMs), HubSpot (CRM),
Klaviyo (correo), GA4 y Looker Studio (analítica). Casi todos son de pago. La arquitectura es la
misma que la de este kit — un orquestador, archivos de contexto compartidos y un humano que
aprueba —; lo que cambia es cuántas herramientas conecta. Empieza por las que leen, no por las
que publican.
