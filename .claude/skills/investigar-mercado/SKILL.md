---
name: investigar-mercado
description: Panorama de competidores, formatos y tendencias del giro de un cliente, con fuentes. Úsalo antes de planear un periodo, cuando pregunten "qué hace la competencia", "qué está funcionando en TikTok/IG para X", o para buscar ganchos e ideas.
allowed-tools: Read, Write, WebSearch, WebFetch
---

# Investigar mercado

## Orden de operaciones

1. **Lee el brief** (`clientes/<cliente>/brief.md`): giro, ciudad, cliente ideal.
2. **Competidores (3–5):** búsqueda web por giro + ciudad. Por cada uno: nombre, URL o cuenta,
   qué publica, frecuencia aproximada, su oferta visible. Fuente y fecha de consulta en cada fila.
3. **Formatos y ganchos (5+):** qué tipos de pieza aparecen con más interacción visible (carrusel,
   reel con voz, antes/después, lista, detrás de cámaras). Por cada uno: el patrón en una línea +
   el ejemplo con su enlace. **Patrón, no texto copiado.**
4. **Tendencias:** sólo con fecha. Una tendencia de hace 6 meses se marca `vieja`. Dos fuentes
   gratuitas, sin cuenta: **Google Trends** (`trends.google.com`, qué busca la gente en la ciudad)
   y la **Biblioteca de anuncios de Meta** (`facebook.com/ads/library`, qué anuncios tiene activos
   cada competidor). Las dos cargan con JavaScript: si la búsqueda web no alcanza, ábrelas con el
   navegador de Claude Desktop.
5. **Huecos:** qué nadie del giro está haciendo bien.
6. **3 oportunidades** para el CMO, cada una con la evidencia que la sostiene.
7. Escribe `clientes/<cliente>/investigacion.md`.

## Reglas

- Cifras de seguidores o vistas: sólo si las viste, con fecha. Si no, "sin dato".
- Lo que es tu opinión se marca **(opinión)**.
- Si una página bloquea la búsqueda, usa el navegador de Claude Desktop; si tampoco, dilo.

## Salida

```markdown
# Investigación — <cliente> — <fecha>
## Competidores
| nombre | dónde | qué publica | oferta visible | fuente (fecha) |
## Formatos y ganchos observados
- **<patrón>** — ejemplo: <url>
## Tendencias (fechadas)
## Huecos
## 3 oportunidades
```
