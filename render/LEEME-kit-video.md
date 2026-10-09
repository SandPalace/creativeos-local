# Video Studio Kit (AI Studios)

This kit lets Claude Code **make and edit short vertical videos in code**. It packages an agent,
the skills, the craft knowledge, the templates and the tools behind AI Studios' first pieces:

| Piece | What it is | Template / tool |
|---|---|---|
| Kinetic offer | Type-only offer spot; the brand can reopen and edit it | `render/tesseract/templates/kinetic-offer` (Tesseract) |
| Animated poster | Swiss poster in four scenes: a self-drawing glyph, a split-flap board, a giant numeral, ring text | `render/gsap/templates/poster-kinetic` |
| Character explainer | An original rigged SVG mascot that acts out the message | `render/gsap/templates/mascot-explainer` |
| Beat-cut cartoon | A 2D lyric cartoon: an original cast, line boil, sunbursts, bubble letters, a horror beat, an iris-out | `render/gsap/templates/cartoon-lyric` |
| Myth over fluids | Ícaro: a seeded maze, feather wings, wing trails taken from a WebGL2 fluid simulation, analytic physics, a procedural score | `render/gsap/templates/myth-fluid` + `render/gsap/lib/fluid.js` |
| Talking-head edit | Silences cut from the audio, a camera driven by voice loudness and checked against the transcript, outlined captions, brand graphics with the person cut out in front, verified SFX | `render/tesseract/talking-head/` |

Paths match the AI Studios repository. **Unpack the kit at the root of your project** and every
path the agent and the skills cite will resolve.

## Start

1. Ask Claude Code to use the **`motion-editor`** agent, or just describe the video you want. The
   `motion-video` skill picks the format and engine.
2. Read `knowledge/craft/motion-graphics.md`. It holds the rules learned on real pieces; the first
   one is "más póster, menos flyer".
3. Try an example (stills first, then the video):
   ```bash
   cd render/gsap && npm install
   node render.mjs --gpu --page templates/myth-fluid/index.html --props examples/myth-fluid.icaro.props.json \
     --out ../../out/icaro/icaro.mp4 --frames 3,13,27,35,45,50
   node render.mjs --gpu --jpeg --crf 17 --page templates/myth-fluid/index.html \
     --props examples/myth-fluid.icaro.props.json --out ../../out/icaro/icaro.mp4
   ```

## Install

| Need | Install | Used for |
|---|---|---|
| Node 20+ | nodejs.org or `brew install node` | renderer |
| GSAP 3.13, Playwright 1.55 | `cd render/gsap && npm install` | timelines, frame capture |
| Headless Chrome | `npx playwright install chromium-headless-shell`, or set `CHROME_PATH` | rendering pages |
| Python 3.11+ with numpy and scipy | `python3 -m pip install numpy scipy` | scores, voice analysis, SFX pack |
| ffmpeg 7+ | `brew install ffmpeg` | encoding, loudness, contact sheets |
| Tesseract app (`tsrct` 0.3.1) | tesseract app, macOS | kinetic-offer, talking-head, editable `.tsrct` |
| Tesseract skills | **`tesseract-motion` ya viene en `.claude/skills/`** (su `tesseract_sound.py` hace los efectos; sólo Python). Los demás: `npx skills add mirage-hq/Tesseract` | efectos de sonido · plantillas Tesseract |
| Xcode command line tools | `xcode-select --install` | person matte (Swift + Apple Vision) for talking-head cutouts |
| Remotion (optional) | `npx skills add remotion-dev/skills` | flyers and clip assembly; not part of this kit |

The fluid template needs `--gpu`, which uses Metal through ANGLE on macOS. On other systems, try
without it (SwiftShader, slow) or with your platform's ANGLE backend.

## What is AI Studios–specific

- **`publish.py`** (upload to AI Studios' S3 and dashboard) was removed from this copy. Here the
  video is delivered in Obsidian: `clientes/<cliente>/creativos/` (see `motion-editor`).
- **`render/tesseract/talking-head/kits/ejemplo.json`** shows the brand-kit format (its values are
  an example, not your brand). Write `kits/<your-brand>.json` from your own brand's source of truth.
- **Statics (flyers)** use AI Studios' Remotion and plate-generation pipeline. The craft is in
  `knowledge/ads/static-flyer.md`; the pipeline is not in this kit.
- The SFX pack sits at `productions/campaigns/claude-emprendedoras/sfx-library/`, which is where
  the skills look for it. **Use `v2/`.**

## Licences

- **Studio code** (templates, `fluid.js`, tools, scores, skills, knowledge): AI Studios. Share it
  inside the organisation.
- **GSAP:** free for commercial use, including plugins, since 3.13 under GreenSock's standard
  no-charge licence. It forbids use in a tool that competes with Webflow's visual animation
  builder; producing videos is fine.
- **Fonts:** SIL Open Font License; each family's licence file is in its folder.
- **SFX:** CC0 1.0 originals from Freesound (`raw/`, with source and author in `manifest.json`),
  rebuilt into `v2/` by `build_pack.py`.
- **Scores:** synthesised with numpy, with no samples.
- **The fluid solver** follows Stam's stable fluids and GPU Gems ch. 38, with vorticity confinement
  after Pavel Dobryakov's WebGL-Fluid-Simulation (MIT).
- **Remotion** requires a company licence for organisations with more than 3 people. **Tesseract**
  is a separate app with its own terms.

## Rules the agent follows

- Never invent a client fact.
- No piece leaves without the owner's `APPROVE`.
- Every version is a new file.
- Take techniques from a reference, never its characters, lyrics or music.
- Say what was measured and what nobody listened to.
