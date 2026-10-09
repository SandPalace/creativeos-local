---
name: gsap-motion
description: Receta para hacer un video de motion graphics como página HTML + SVG + GSAP (opcional: fluidos en WebGL2), renderizada cuadro por cuadro a MP4 (de AI Studios). Cubre usar una plantilla existente (poster-kinetic, mascot-explainer, cartoon-lyric, myth-fluid) o crear una nueva: personajes SVG articulados, caricaturas cortadas al ritmo, fluidos acoplados a la animación. Úsalo para pósters animados, explicadores con personaje, caricaturas o piezas de muestra.
---

Read `knowledge/craft/motion-graphics.md` first: it holds the rules, and this skill holds the
steps. The stack and the render commands are in the `motion-video` skill. The page contract is in
`render/gsap/README.md`.

## A. A spot from an existing template

1. **Folder.** Make a new spot folder: `<unit>/motion-vN/`. Never reuse an earlier version's folder.
2. **`props.json`.** Copy a sibling's `props.json`. In the exported kit, the examples are in `render/gsap/examples/` and `kinetic-offer/example.props.json`. Then:
   - change the copy, palette, times and scenes;
   - make every client fact trace to the brief, and list it in `claims[]`;
   - keep times on the music grid (120 BPM gives a 0.5 s grid).
3. **Stills.** Run `node render.mjs … --frames <8–14 times>`.
   - Read the layout check the renderer prints, and fix every line it reports.
   - Make a contact sheet and look at it. Crop to full size wherever the small view can mislead.
4. **Full render.** Run the full render: add `--gpu --jpeg --crf 17` for fluid templates.
   - Then make a contact sheet, a waveform, and measure duration, LUFS and dBTP.
5. **Deliver.** Write `review.md` and publish (see `motion-video` §4).

## B. A new template

Start from the closest template and keep its skeleton:
- fonts loaded in `__ready`;
- `const LEAD`, `T(x)`, `tl = gsap.timeline({paused: true})`;
- scene functions that add to `tl`;
- `__seek`, `__meta` and `__check`.

Then add a row to the catalog in `render/gsap/README.md`.

### Patterns that work

- **Text reveal:** wrap characters in spans, keeping each word `nowrap` so it never breaks mid-word.
  Animate `tl.from(chars, {opacity: 0, y: 34, filter: "blur(10px)", stagger: ≤0.035})`, and play
  the exit as `opacity: 0, y: -18, blur` 0.45 s before the next beat.
- **Draw-on geometry:** `DrawSVGPlugin` with a stagger computed per element. For example, a maze
  wall by its radius draws the maze from the centre outward.
- **Drive state through proxies.** Tween plain objects (`ICA = {x, y, s, flap…}`), then write SVG
  attributes from them in one `draw(t)` function called by `__seek`. One place sets every
  transform, and procedural motion (`sin` flaps, waves) composes cleanly with tweens.
- **3D tilt of a flat drawing:** put the SVG in a div with CSS `perspective`, then tween
  `rotationX`. The screenshot renders it.
- **Seeded generation:** a mulberry32 RNG from `props.seed`. Mazes (recursive backtracker on a
  polar grid), scatter positions and particle offsets then come out identical every render.

### Characters (`mascot-explainer`, `cartoon-lyric`)

- **Rig hierarchy:** root, body (squash and stretch, with the origin at the feet), head, eyes
  (pupils for gaze; swap eye shapes for states), mouth set, arms rotating at the shoulder with
  `svgOrigin`, and props.
- **Idle:** breathing scale ±1.5 %, a blink every 2–4 s from the seeded RNG, and pupils that drift.
- **Limited animation for cartoons:** hold a pose and snap to the next one on the beat. Add line
  boil with an `feTurbulence` + `feDisplacementMap` filter whose `seed` steps every 2–3 frames.
- **Effects:**
  - sunburst: N wedges rotating behind the pose;
  - bubble letters: per-letter `scale 0 → 1.25 → 1` with rotation jitter;
  - iris-out: an animated circle mask;
  - shake: a seeded offset on the camera group.

### Fluids (`myth-fluid`, `lib/fluid.js`)

```js
const F = window.Fluid(canvas, {simRes: 192, dyeRes: 720});   // canvas 1080×1920
F.splat(x, y, vx, vy, [r, g, b], radiusPx);   // px, px/s, linear-light colour
F.step(1 / __fps, {curl, velDiss, dyeDiss, iters: 24, wind: [0, wy], noise: [amp, scale, speed], buoy: [0, by], time});
F.render({top, bottom, exposure, grain, vignette, frame, relief});
F.reset();
```

- **`__seek(t)` steps the simulation** from its current frame up to `round(t·fps)`. For each step
  it sets the timeline to that frame, calls `draw`, then `emit` (splats), then `F.step`. Seeking
  backwards calls `reset()` and steps again from 0.
- **Emitters read timeline state:** tweened intensities (`EM.smoke`, `EM.heat`…) and positions.
  Give each frame its own RNG seed (`rng(1000 + frame)`).
- **Couple real motion.** Read a tip's position with `el.getCTM()` and take its difference from
  the previous frame as velocity. That velocity becomes a splat's force.
- **Colours:** convert to linear light for `splat` and for the background. The display shader
  applies gamma.
- **Avoid a uniform `wind`:** inside a closed box, the pressure solve cancels it. Use velocity on
  the splats and curl noise instead.
- **Render with `--gpu`**, and use `--jpeg` because grain makes PNG captures slow.

### Analytic physics

For falling or bouncing objects, use closed forms instead of integrating step by step. Then any
`t` can be evaluated directly. Example, a feather released at `td`:

```
τ = t − td
y = vt·(τ − (1 − e^(−kτ))/k)
x = drift·(1 − e^(−kτ)) + A·sin(ωτ + φ)·(1 − e^(−2τ))
rot = B·sin(ωτ + φ)
```

To start from the wing's pose, capture the element's `getCTM()` once at `td` while building, and
prepend it to the transform.

## C. Sound

Each template either:
- sets `__meta.music.script` (its own `score.py`) and passes `events`, or
- uses the stock bed plus procedural SFX cues.

See `sound-design`.

## Do not

- Return anything from `__seek`, use CSS transitions, `Math.random()` or `Date.now()`.
- Animate an SVG child with CSS `transform-origin`; use `svgOrigin`.
- Put a rendered image of the design in place of live SVG, or reuse a reference's characters.
