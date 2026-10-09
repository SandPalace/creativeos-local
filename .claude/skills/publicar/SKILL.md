---
name: publicar
description: Publica en las plataformas un creativo que el dueño ya firmó — Instagram y Facebook (orgánico y anuncios de Meta), TikTok, YouTube Shorts — siguiendo la estrategia de contenido, y prepara lo de Google Ads. Arma el paquete de publicación, sube sólo con el permiso del dueño en cada envío, todo anuncio nace pausado, y cuando se topa con algo (falta conexión, permiso, error, auditoría) se detiene y le pide ayuda al dueño. Úsalo para "publica", "súbelo a TikTok/Instagram/YouTube", "programa", "pautalo", "boost", o cuando un creativo pase a aprobada.
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
---

# Publicar

Publicar es **la única parte del ciclo que sale de tu computadora**: lo que se sube lo ven personas
reales, y un anuncio gasta dinero real. Por eso este skill tiene tres reglas que no se negocian:

1. **Sólo se publica un creativo firmado** (`estado: aprobada` y `aprobado_por` lleno) de una pieza
   firmada. El texto que se sube es **el de la pieza, palabra por palabra**: si hay que cambiar algo,
   se vuelve a firmar.
2. **Cada envío pasa por la ventana de permiso** (`ask` en `.claude/settings.json`). Esa ventana es la
   firma del dueño para *ese* envío. Si no hay ventana porque el modo de permisos lo saltó, no
   publiques: pídele que vuelva a modo **Manual**.
3. **Todo anuncio nace pausado.** Activarlo, subir presupuesto o cambiar a quién se muestra es del
   dueño, en el Administrador de anuncios.

## Cuando te topas con algo: pide ayuda, no improvises

Te vas a topar con cosas: una plataforma sin conectar, un token vencido, un permiso que falta, una
app que no ha pasado la auditoría, un error que no entiendes, un archivo que la plataforma rechaza.
**En cuanto pase, te detienes y le pides ayuda al dueño.** Así:

> [!question] Necesito tu ayuda para publicar P01 en TikTok
> **Qué pasó:** TikTok respondió que la app no tiene permiso para publicar (`scope_not_authorized`).
> **Qué significa:** falta que autorices la app con tu cuenta de TikTok.
> **Qué necesito que hagas:** 1. … 2. … 3. … (pasos con clics, como en `Conectores para después`)
> **Mientras tanto:** te dejo el paquete listo para que lo subas a mano (abajo).

- **Nunca** busques otra ruta para "lograrlo de todos modos": otra API, otra cuenta, una herramienta de
  terceros, reintentar en bucle, publicar con otro texto o con otra privacidad.
- **Nunca** leas ni imprimas tokens, ni le pidas al dueño que te los pegue en el chat: van en `.env`
  (ver `Conectores para después.md`), y tú sólo los usas como variables de entorno.
- Ofrece siempre **el plan B manual**: el paquete de publicación, para que el dueño lo suba desde la app.

## Orden de operaciones

0. **Revisa firmas y estrategia.** El creativo y su pieza firmados; lee `Estrategia de contenido.md`
   (ritmo elegido, qué va a orgánico primero y qué se pauta sólo si ganó).
1. **Arma el paquete de publicación** en la nota del creativo, sección `## Publicación`: plataforma,
   archivo exacto, texto (copia literal del pie de foto firmado), palabra clave, fecha y hora
   (`fecha` de la pieza), y **cómo se mide** (`se_mide`). Esto se hace siempre, haya conexión o no.
2. **Revisa qué está conectado** (tabla de abajo). Si la plataforma no está conectada → el dueño la
   sube a mano con el paquete, o le explicas cómo conectarla (`Conectores para después.md`).
3. **Pide permiso y sube** — un envío a la vez, diciendo antes qué vas a subir, a dónde y con qué
   privacidad.
4. **Comprueba** que quedó (estado de la publicación, enlace) y anótalo en la pieza: `enlace:` y una
   línea en `## Publicación`. **No escribas `publicada`:** dile al dueño que la mueva a la columna
   morada cuando la vea en su cuenta.
5. Si algo falla en cualquier paso → **"Cuando te topas con algo"**, arriba.

## Por plataforma

| Plataforma | Cómo se conecta | Qué puedes hacer | Qué es del dueño |
|---|---|---|---|
| **Anuncios de Meta** (Facebook + Instagram) | MCP oficial `https://mcp.facebook.com/ads` (OAuth de Meta) | Leer resultados; crear campaña, conjunto y anuncio **en pausa**; promocionar una publicación de Instagram (`ads_boost_ig_post`) **en pausa** | Activar, presupuesto, públicos |
| **Instagram orgánico** (feed, reels, historias, carrusel) | API de Instagram con inicio de sesión de Instagram; token en `.env` | Crear el contenedor y publicarlo | Firmar; mover a *publicada* |
| **TikTok** | Content Posting API; token en `.env` | **Mandar a borradores** (`video.upload`): el dueño lo termina y publica desde la app | Publicar desde la app |
| **YouTube Shorts** | YouTube Data API (`videos.insert`); OAuth en `.env` | Subir el video **como privado o no listado** | Hacerlo público desde YouTube Studio |
| **Google Ads** | MCP oficial `googleads/google-ads-mcp` — **sólo lectura** | Leer campañas y métricas | Crear y editar anuncios en Google Ads (tú le dejas el texto listo) |

### Anuncios de Meta (MCP oficial)

- Crea todo con `status: PAUSED`. Crear, editar, activar y promocionar están en `ask`: cada uno te
  abre la ventana de permiso.
- Lo que se pauta sale de la estrategia: **el ganador en orgánico**, no un video que no funcionó.
- Cuenta, moneda y meta (costo por conversación) salen de `hechos.md`; si no están confirmadas, te topaste.

### Instagram orgánico (API de Instagram)

- Requiere cuenta **profesional** de Instagram. Permisos: `instagram_business_basic` e
  `instagram_business_content_publish`.
- Flujo: `POST /<IG_ID>/media` (contenedor; reels con `media_type=REELS` y `video_url`) → revisa
  `status_code` una vez por minuto, máximo 5 minutos → `POST /<IG_ID>/media_publish` con `creation_id`.
- **El archivo tiene que estar en una URL pública** en el momento de publicar. Si el creativo sólo
  existe en tu computadora, te topaste: pídele al dueño dónde alojarlo o que lo suba a mano.
- Límite: 100 publicaciones por API en 24 horas (los carruseles cuentan como una); consúltalo en
  `GET /<IG_ID>/content_publishing_limit`.

### TikTok (Content Posting API)

- **Usa borradores** (`/v2/post/publish/inbox/video/init/`, permiso `video.upload`): el video llega a la
  bandeja del dueño y él lo publica desde la app. Así su firma queda en TikTok mismo.
- Publicar directo (`video.publish`) necesita que TikTok **audite** la app; sin auditoría, todo sale
  **privado**. No lo uses sin que el dueño lo pida y sepa esto.
- Archivo local: `source: FILE_UPLOAD` (se sube por partes al `upload_url`). Desde URL: sólo dominios
  verificados.

### YouTube Shorts (YouTube Data API)

- `videos.insert` con el permiso `youtube.upload`. **No hay "endpoint de Shorts":** YouTube lo vuelve
  Short si es **vertical o cuadrado y dura 3 minutos o menos**.
- Sube con `privacyStatus: private` (o `unlisted`) y que el dueño lo publique en YouTube Studio.
- Cuota: 100 subidas al día por proyecto.

### Google Ads

- El MCP oficial es **sólo lectura**: no crea ni pausa anuncios. Prepara en la nota los textos
  (títulos y descripciones con sus límites de caracteres) y el dueño los crea en Google Ads.

## Fuentes (léelas si algo no coincide: las plataformas cambian)

- Instagram, publicación de contenido: developers.facebook.com/documentation/instagram-platform/content-publishing
- TikTok, Content Posting API: developers.tiktok.com/doc/content-posting-api-get-started y …-upload-content
- YouTube, `videos.insert`: developers.google.com/youtube/v3/docs/videos/insert
- Google Ads MCP: developers.google.com/google-ads/api/docs/developer-toolkit/mcp-server
- Meta, conectores de IA para anuncios (beta abierta desde abril de 2026): `https://mcp.facebook.com/ads`

Revisado el 2026-10-08. Si una plataforma responde distinto a lo que dice aquí, **te topaste**: dilo
y pide ayuda, no adivines.
