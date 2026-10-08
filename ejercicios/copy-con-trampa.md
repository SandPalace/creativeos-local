# Ejercicio · El copy con trampa

Un anuncio puede verse perfecto y traer un dato inventado. El titular de éste es **real**: lo
publicamos para AlgoLab en agosto de 2026 con un rango de edad que inventó un agente (el real es 8 a
15). El resto lo armamos para el ejercicio, con tres trampas:

> **VUELTA A CLASES · 7 A 17 AÑOS**
> Inscripción gratis todo octubre. Clases de Roblox, Python, robótica e IA.
> Empezamos el lunes 13 de octubre. ¡Escríbenos!

## Lo que haces

1. Termina antes el onboarding de tu negocio (el CMO te lo pide al abrir la carpeta).
2. **Escribe un anuncio de tu negocio con un dato que nunca le diste al CMO** — un precio, una
   promoción, un horario o una edad que no esté en tu `hechos.md`. Pégalo en el chat:
   > *"Revisa este anuncio antes de que lo publique: <tu anuncio>"*
3. El CMO debe correr `verificar-hechos` y contestarte con una tabla: cada dato del anuncio, qué dice
   tu `hechos.md`, y un ⛔ en el que no puede confirmar — **más la pregunta exacta para ti.**

## Cómo sabes que funcionó

- Bloqueó **ese** anuncio, no todo tu plan.
- No "corrigió" el dato con uno que le pareció probable: te lo preguntó.
- Si el anuncio trae una fecha con día de la semana, la comprobó con `date`.

Si el CMO deja pasar el dato inventado, algo falta en `hechos.md` o en el skill: ése es el hallazgo
más valioso del taller.
