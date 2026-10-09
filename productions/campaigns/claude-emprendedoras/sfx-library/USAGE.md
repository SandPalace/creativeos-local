# SFX Library — Lucy / "4 agentes de IA" spot

> **2026-10-08: usa `v2/`.** Los `.wav`/`.mp3` de esta carpeta están rotos: cada uno conserva ~30 ms
> de sonido y luego silencio digital. `v2/` se reconstruyó desde `raw/` con `build_pack.py`
> (segmentos, `hit_ms` y nivel por archivo en `v2/pack.json`). Lucy 002 v11 es la primera versión
> que suena con efectos reales.

Librería de efectos de sonido libres de derechos (commercial-safe) para el
spot de Lucy (lucy-002), con investigación de uso práctico en edición
short-form 2025-2026 y una tabla de colocación lista para aplicar en el
montaje.

**Licencia:** todos los archivos son CC0 (Creative Commons Zero) de
Freesound, verificado individualmente en la página de cada sonido antes de
descargar. Ver `manifest.json` para el link y autor de cada uno. CC0 permite
uso comercial sin atribución — seguro para este cliente.

## 1. Investigación: cómo se usan los SFX de meme/viral edit en 2025-2026

Resumen práctico, con fuentes:

- **El gancho (hook) es crítico en los primeros 1-1.5s.** TikTok usa esa
  ventana para predecir si alguien se queda a ver más, y los edits más
  densos apilan 5-7 efectos en los primeros 5 segundos: un golpe grave
  (bass hit) sobre la imagen del hook, whooshes en cada corte más rápido
  que 0.8s, y un riser hacia el punchline.
  ([sfxengine.com](https://sfxengine.com/blog/tiktok-sound-effects-tips))
- **Densidad para talking-head (nuestro caso):** 3-5 SFX en un video de
  30s es el punto dulce para contenido hablado a cámara; los edits
  cortados visualmente (jump-cut heavy) usan más.
  ([sfxengine.com](https://sfxengine.com/blog/tiktok-sound-effects-tips))
- **Arquetipo → momento:**
  - *Boom/sub impact o cinematic hit* → declaración fuerte, reveal, "esto
    te va a cambiar la vida".
  - *Record scratch* → objeción, "espera/no", giro cómico.
  - *Whoosh* → corte/zoom, especialmente en cortes <0.8s de distancia.
  - *Swoosh/swipe* → entrada de un ítem de lista (cada uno de los 4
    agentes).
  - *Pop/bubble pop* → aparición de texto en pantalla, captions.
  - *Ding/notificación* → mención de beneficio, "y lo mejor es que...".
  - *Cash register/coin* → dinero, ahorro, "cobranza", ingresos.
  - *Keyboard/click* → tecnología, "la IA está trabajando".
  - *Riser* → 1-2s antes de un reveal, debe terminar justo EN el corte.
  - *Reverse swell* → anticipación más suave que el riser, para reveals
    menos agresivos.
  - *Applause/crowd "wow"* → el payoff, después de mostrar el resultado.
  - *Glitch* → beat de error→solución, o la parte "tech/IA".
  - *Typewriter ding* → cierre de una idea/lista, como un "capítulo
    cerrado".
  ([sfxengine.com](https://sfxengine.com/blog/tiktok-sound-effects-tips),
  general 2025-2026 editing convention also described on
  [soundstripe.com](https://www.soundstripe.com/blogs/best-royalty-free-sound-effects-for-tik-tok))
- **Mezcla / niveles:** diálogo entre -6 y -12dB, música de fondo entre
  -20 y -30dB mientras alguien habla, y efectos de sonido entre -10 y
  -20dB por debajo de picos de diálogo. Mezclar en orden: diálogo primero,
  efectos después, música al final.
  ([mytasker.com](https://mytasker.com/blog/the-complete-guide-to-sound-design-for-video-creators))
- **Dings específicos:** mantener la ganancia del ding entre -8dB y -5dB
  y nunca por encima del diálogo; el "ka-ching" de caja registradora debe
  caer exactamente en el frame del momento de "dinero", no un beat
  después, o se siente despegado.
  ([sonilo.com](https://sonilo.com/ai-music/ding-sound-effect-guide),
  [sonilo.com](https://sonilo.com/ai-music/ding-sound-effect-guide))
- **Regla general de timing:** el efecto debe caer un poco antes o
  exactamente en el frame visual — la sincronización ajustada es lo que
  hace que un corte "se sienta" intencional; los risers deben *terminar*
  en el corte, nunca seguir sonando después.
  ([sfxengine.com](https://sfxengine.com/blog/tiktok-sound-effects-tips))

## 2. Tabla de colocación — spot Lucy ("4 agentes de IA")

| Momento del spot | Arquetipo | Archivo | Gain sugerido (dB bajo voz) | Tip de timing |
|---|---|---|---|---|
| Hook (0-1.5s), frase de impacto | Deep boom / cinematic hit | `boom-deep-01` o `hit-cinematic-01` | -6 a -8dB vs. pico de voz | Transiente exactamente ON el primer frame del hook; no antes. |
| Corte rápido / zoom dentro del hook | Fast whoosh | `whoosh-fast-01` / `whoosh-fast-02` (alternar) | -10dB | Alinear el "aire" del whoosh con el frame de inicio del corte, no con el final. |
| Entrada de cada agente de IA (marketing, ventas, cobranza, dirección) | Swoosh / swipe | `swoosh-swipe-01` | -10 a -12dB | Un swipe por cada entrada de ítem de lista; mismo gain en los 4 para que se sientan como una serie. |
| Texto en pantalla / caption pop-in | Pop / bubble pop | `pop-01` / `pop-02` (alternar) | -12dB | Dispara en el frame exacto donde el texto llega a su tamaño final, no al iniciar la animación. |
| Mención de beneficio ("te ahorra horas", "nunca pierdes un cliente") | Notification ding | `ding-notification-01` | -8 a -5dB | Ding en la palabra clave del beneficio, no en la pausa antes. |
| Mención de "cobranza" / dinero / ahorro | Cash register / coin | `cash-register-01` | -6dB | Debe caer en el frame exacto donde se dice "cobranza" o se muestra un número de dinero — no un beat después. |
| Beat de "la IA está trabajando" / tech | Keyboard typing | `keyboard-typing-01` | -14dB (cama, no acento) | Usar como textura de fondo breve (1-1.5s) bajo b-roll de pantalla/app, no como golpe aislado. |
| Click de UI / selección en pantalla | Mouse click | `mouse-click-01` | -12dB | Sincroniza exacto con el frame del click visual en la demo de producto. |
| 1-2s antes del reveal ("mira lo que puede hacer EQUIPO") | Riser | `riser-01` | sube de -20dB a -6dB | El riser debe **terminar** justo en el corte del reveal — nunca seguir sonando después del corte. |
| Alternativa de riser para un reveal más cálido/suave | Reverse swell | `reverse-swell-01` | sube de -20dB a -8dB | Igual que el riser: terminar en el corte, no encima de él. |
| Foto/demo de pantalla (screenshot, app) | Camera shutter | `camera-shutter-01` | -10dB | Dispara en el frame donde la imagen "se congela", como si fuera una captura. |
| Payoff — resultado mostrado (ej. antes/después, testimonio) | Applause corto | `applause-01` | -14dB, breve (no dejar sonar completo) | Entra justo cuando se revela el resultado, corta rápido para no tapar el VO que sigue. |
| Payoff alternativo con textura de "reacción" | Crowd "wow" | `crowd-wow-01` | -16dB, muy por debajo de la voz | Es una textura de ambiente, no un acento — úsalo como cama breve, no como golpe; si se siente genérico, omitir en favor de applause. |
| Beat de error→solución o "esto antes era un problema" | Glitch | `glitch-01` | -10dB | Alinear el inicio del glitch con el corte que muestra el "problema", se resuelve cuando entra la solución. |
| Cierre de una idea / fin de lista ("y eso es todo lo que hacen los 4 agentes") | Typewriter ding | `typewriter-ding-01` | -10dB | Dispara en la última palabra de la frase de cierre, como un punto final audible. |
| CTA final ("comenta EQUIPO") | Notification ding o cash register (reutilizar) | `ding-notification-01` | -6dB | Sincroniza con la aparición del texto de CTA en pantalla, no con el inicio del VO del CTA. |

## 3. Reglas de mezcla (resumen rápido)

1. Diálogo primero, efectos segundo, música al final — ese orden de mezcla.
2. Diálogo: -6 a -12dB. Música de fondo (si hay) bajo voz: -20 a -30dB.
   Efectos de acento: -10 a -20dB bajo el pico de la voz; los dings de
   beneficio pueden ir un poco más arriba (-8 a -5dB) porque son breves.
3. Nunca más de ~5-7 efectos en los primeros 5 segundos, y 3-5 en total
   en un spot de 15-30s para contenido talking-head — este no es un
   gaming meme edit, así que preferir menos y mejor colocados sobre
   saturar.
4. Todo riser / reverse swell debe **terminar exactamente en el corte**
   del reveal, nunca sonar después.
5. Todo "momento de dinero" (cash register, ding de beneficio) debe caer
   en el frame exacto del hecho, no un beat después — si se nota tarde,
   se siente pegado en postproducción en vez de parte de la edición.
6. Variar entre los dos whooshes / dos pops disponibles para que la
   repetición no se note en un spot corto con varios cortes.

## 4. Notas de calidad por archivo

Algunos previews HQ de Freesound llegan muy bajos de volumen (hasta
-65dB de pico). Se normalizaron todos a -3dBFS de pico para que sean
utilizables, pero los que requirieron +40dB o más de ganancia
(`hit-cinematic-01`, `camera-shutter-01`, `reverse-swell-01`,
`riser-01`, `swoosh-swipe-01`, `typewriter-ding-01`, `whoosh-fast-01`,
`whoosh-fast-02`, `cash-register-01`) pueden tener algo de ruido de
fondo audible a volumen alto — escuchar antes de usar en la mezcla
final y, si el ruido molesta, considerar un segundo pase de
`afftdn`/denoise o buscar un reemplazo con un preview más caliente.

`crowd-wow-01` es una textura de ambiente de restaurante (no un "wow"
aislado y limpio) — funciona como cama de reacción muy baja en el mix,
no como acento puntual; si se necesita un "wow" más claro, se puede
re-buscar en Freesound con el mismo filtro CC0.
