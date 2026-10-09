---
name: motion-video
description: La puerta de entrada para hacer o editar un video vertical en código (de AI Studios). Elige el formato y la plantilla (póster animado, personaje, caricatura, fluidos, oferta Tesseract, persona a cámara) y cubre instalación, render, revisión de cuadros y entrega. Úsalo para "haz un video", "motion graphics", "póster animado", "caricatura", "personaje animado", "reel", "video sin cara", "edita este video", o para instalar el estudio de video.
---

This skill is the router and the stack sheet. Read the craft rules before making anything:

- `knowledge/craft/motion-graphics.md`: faceless video made in code.
- `knowledge/craft/talking-head-editing.md`: editing real footage of a person.
- `knowledge/ads/static-flyer.md`: still flyers.

## 1. Pick the format

| The ask | Format | Engine and template | Procedure |
|---|---|---|---|
| Offer or promo, editable by the brand afterwards | Kinetic type spot | Tesseract, `render/tesseract/templates/kinetic-offer` | Its README, then the `tesseract-motion` skill |
| Ad that should look like design, "más poster" | Animated poster | GSAP, `render/gsap/templates/poster-kinetic` | `gsap-motion` |
| Explainer with a cute character | Mascot explainer | GSAP, `mascot-explainer` | `gsap-motion` (§ characters) |
| Music-driven cartoon, lyric video, meme format | Beat-cut cartoon | GSAP, `cartoon-lyric` | `gsap-motion` + `sound-design` |
| Story, myth, brand film, showcase | Geometry over a fluid sim | GSAP + WebGL2, `myth-fluid` | `gsap-motion` (§ fluids) + `sound-design` |
| A person talking to camera (raw takes) | Talking-head edit | Tesseract tools, `render/tesseract/talking-head` | `talking-head-edit` |
| A still flyer or poster | Static | Remotion still, with a generated or client photo plate | `static-flyer` |
| Clips to assemble, generated shots | Spot assembly | Remotion (`render/`) | `edit-clips-remotion`, `generate-spot` |

When an existing template fits, write a new `props.json` for it. Build a new template only for a
new format, then add it to the catalog table in `render/gsap/README.md`.

## 2. The stack

| Piece | What | Version tested |
|---|---|---|
| Languages | HTML/CSS/SVG + JavaScript (pages and renderer), GLSL ES 3.00 (fluid shaders), Python 3.11+ (audio, tools), Swift (person matte, macOS only) | |
| GSAP | Timeline engine. All plugins are free since 3.13; we use SplitText, DrawSVG, MorphSVG and CustomEase | gsap 3.13.0 |
| Renderer | `render/gsap/render.mjs`: Playwright drives a headless Chrome, seeks the timeline frame by frame, and pipes screenshots into ffmpeg | playwright-core 1.55.1, Node 20+ (tested 24) |
| Browser | chrome-headless-shell. It looks for Remotion's copy in `render/node_modules/.remotion/`; set `CHROME_PATH`, or run `npx playwright install chromium-headless-shell` | |
| GPU | `--gpu` renders WebGL on Metal through ANGLE (needed for the fluid templates); without it you get SwiftShader on the CPU | |
| Fluids | `render/gsap/lib/fluid.js`: WebGL2 stable fluids (Stam; GPU Gems ch. 38; vorticity after Dobryakov, MIT) | |
| Audio | numpy (+ scipy for `cartoon-lyric`) synthesis: `score.py` per template, `render/tesseract/templates/kinetic-offer/music.py`; ffmpeg two-pass loudnorm | numpy 2.x, scipy 1.17 |
| Video | ffmpeg (libx264, AAC 192k), ffprobe | ffmpeg 7+ (tested 9.0) |
| Editable projects | Tesseract CLI `tsrct` (macOS app), `.tsrct` documents; read `knowledge/tools/tesseract.md` first | tsrct 0.3.1 |
| Person cutouts | Apple Vision person matte (`render/tesseract/talking-head/personmatte.swift`) → ProRes 4444 | macOS 14+ |
| Flyers, assemblies | Remotion | remotion 4.0.x |
| Fonts | OFL, in `render/tesseract/fonts/` with their licences: Inter, DM Sans, Space Grotesk, Space Mono, Instrument Serif, Luckiest Guy | |
| SFX | CC0 Freesound pack, rebuilt and verified, in `productions/campaigns/claude-emprendedoras/sfx-library/v2/` | |

Install:

```bash
cd render/gsap && npm install          # gsap + playwright-core
python3 -m pip install numpy scipy     # audio synthesis
brew install ffmpeg                    # or your platform's package
# optional: Tesseract app (tsrct), Xcode command line tools (swiftc), aws CLI (publishing)
```

## 3. The render contract (GSAP)

A template is one HTML page that builds **one paused timeline** and exposes `__ready`,
`__seek(t)` (returns nothing), `__meta` and `__check()`. The full contract and the determinism
rules (no `Math.random`, no wall clock, a seeded RNG, the `LEAD` offset, `svgOrigin`) are in
`render/gsap/README.md`.

```bash
cd render/gsap
node render.mjs --page templates/<t>/index.html --props <spot>/props.json --out <spot>/<name>.mp4 \
  --frames 0,2.5,7,…          # stills only, into <spot>/frames/: iterate on these
node render.mjs … [--gpu] [--jpeg] [--crf 17] [--fps 60]    # the full video with audio
node render.mjs … --audio-only                               # remix onto the frames already rendered
```

## 4. Quality control and delivery

1. **Stills.** Render stills, tile them into a contact sheet, and look at them before the full render:
   ```bash
   ffmpeg -pattern_type glob -i 'frames/t*.png' -vf "scale=270:480,tile=7x2" sheet.png
   ```
2. **Full render.** Then a contact sheet from the MP4 (`-vf fps=0.4,scale=180:320,tile=11x2`)
   and a waveform (`showwavespic`).
3. **Measure.** Check duration with `ffprobe`, and loudness and peak with `ebur128=peak=true`.
   The target is −15 LUFS and ≤ −1.5 dBTP; if the peak is over, add `alimiter`.
4. **Delivery encode.** When the master is very large, encode a delivery version at CRF 21.
5. **Write `review.md`.** Say what changed and what was measured. Say plainly what nobody listened
   to or watched on a phone. The owner answers `APPROVE` or `CHANGES:`.
6. **Never overwrite** a render someone has seen. Use a new letter and slug for each version
   (`9x16_b-v2-<slug>.mp4`).

In AI Studios they publish with `publish.py` (not included here), or the same `upload` and
`set_thumb` helpers. They upload to S3 (no overwrite, checksum verified), register the piece in
the dashboard's Demos, and set the thumbnail frame. Elsewhere, deliver the MP4 and `review.md`.

## Do not

- Invent client facts, or reuse a reference's characters, lyrics or music.
- Use point text inside a zoomed Tesseract group (tsrct 0.3.1 wraps it).
- Ship a template without `__check()`, or a piece nobody has looked at as stills.
