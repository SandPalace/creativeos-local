# Conectores para después

Hoy todo es local y gratis: Obsidian + archivos + Claude Desktop. No necesitas ningún conector para
que tus agentes lean y escriban tu bóveda: **son archivos, Claude ya los ve.**

Cuando la agencia crezca, éstos son los conectores que suman, en el orden en que suelen hacer falta.
Revisa el precio y los permisos de cada uno antes de conectarlo; varios requieren plan de pago o
una cuenta de negocio.

| Cuando necesites… | Conector | Tipo | Ojo con |
|---|---|---|---|
| Ver la web como un humano (perfiles, páginas que bloquean búsqueda) | **Navegador de Claude Desktop** o **Playwright** | Integrado / MCP local | Desktop ya trae navegador. Playwright (`.mcp.example.json`) necesita Node |
| Leer métricas reales de tus anuncios | **Meta Ads MCP oficial** (`mcp.facebook.com/ads`) | MCP remoto, OAuth | Empieza **sólo lectura**. Las herramientas que crean, activan o editan van en `ask` |
| Compartir documentos con el cliente | **Google Drive / Docs** | Conector de claude.ai | El cliente ve lo que subas: nada sin aprobar |
| Mandar reportes por correo | **Gmail** | Conector de claude.ai | Enviar es publicar: que el agente deje **borrador**, tú envías |
| Agendar publicaciones y juntas | **Google Calendar** | Conector de claude.ai | — |
| Diseño con plantillas de marca | **Canva** | Conector de claude.ai | Componer el texto encima de la imagen generada vive bien aquí |
| Wiki de equipo compartida | **Notion** | MCP / conector | Cuando más de una persona edite a la vez; mientras tanto, Obsidian |
| Avisos al equipo | **Slack** | Conector de claude.ai | Un pedido hecho sólo en un canal se olvida: los pendientes van en una nota o ticket |
| Generar imagen/video desde el agente | APIs de modelos (OpenRouter, Gemini, etc.) | API con llave | Cuesta por generación: pon un tope de gasto antes |

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
