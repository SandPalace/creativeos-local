---
name: sound-design
description: Receta para el sonido de un video corto (de AI Studios): música generada a partir de los eventos de la imagen, efectos elegidos de un paquete CC0 verificado, niveles contra la voz, normalización de volumen y la comprobación de que cada sonido se oye. Úsalo para "música", "efectos de sonido", "mezcla", "volumen", "suena raro", o antes de entregar cualquier video con audio.
---

Rules: §6 of `knowledge/craft/talking-head-editing.md` (SFX) and §6 of
`knowledge/craft/motion-graphics.md`. The tools are named below.

## 1. Verify the sound files first

A broken pack can ship unnoticed: Lucy 002 v4–v10 were mixed from files that each held about 30 ms
of sound followed by silence, and no step complained. Before using any SFX or music file, check
how long it stays within 40 dB of its peak:

```python
x = decode(file)                 # ffmpeg -ac 1 -ar 48000 -f s16le -
e = rms_db(x, window=10 ms)
audible_ms = (e > e.max() - 40).sum() * 10
```

If a 2 s whoosh is audible for 30 ms, the file is broken.

**The pack.** It is `productions/campaigns/claude-emprendedoras/sfx-library/`:
- **Use `v2/`.** It is rebuilt from the Freesound originals in `raw/` (all CC0) by
  `build_pack.py`.
- **Per-sound data** is in `v2/pack.json`: source, cut, gain, and `hit_ms` (where the transient
  or the peak sits).
- **Which sound for which moment** is in `USAGE.md` (whoosh on a cut, swoosh on a list item,
  cash register on money, typewriter ding to close a list, riser or swell into a reveal).

To add a sound:
1. download the CC0 original into `raw/`;
2. add a row to `SPEC`, with the cut read from its loudness envelope;
3. rebuild and check `audible_ms`.

## 2. Procedural score (motion pieces)

The picture emits events and the score is written to them, so the two cannot drift.

- **The page puts `music: {script: "score.py", events: [...]}` in `__meta`.** The renderer runs
  `python3 score.py --out --duration --events`.
- **Two scores exist as models:**
  - `render/gsap/templates/myth-fluid/score.py`: chord sections with pads and a drone, plus pluck,
    bell, tick, hit, swell, whoosh, riser, heartbeat, a fall (it ducks the mix before the impact),
    a splash and a fade;
  - `render/gsap/templates/cartoon-lyric/score.py`: 120 bpm modes `intro`, `groove`, `dark`,
    `build`, `drop`, `thin`, `silence`, `hit` and `end`.
- **Synthesis is numpy** (additive pads, decaying-harmonic plucks, FM bells, noise sweeps through a
  one-pole filter, FFT convolution reverb) from a fixed seed. There are no samples, so no licences.
- **Musical devices that worked:**
  - pitch tied to the image (shorter feather = higher note, like pan pipes);
  - a heartbeat that speeds up toward the climax;
  - near-silence 0.5 s before the impact;
  - a minor key that resolves to major in the epilogue.
- **For a plain bed under an offer**, use `render/tesseract/templates/kinetic-offer/music.py`
  (`--bpm --lift --drop`).

## 3. SFX on a talking-head or offer edit

- **Define roles in `roles.json`:** `{key, gain, lead_ms, dur_ms}`. `lead_ms` puts the sound's hit
  on the cue: a swell with `lead_ms` equal to its length ends exactly on the cut.
- **Set cues in `edit.json`** (talking-head tools):
  - behind words take `sfx`, chips `sfx`/`pop`, and pills `sfx`;
  - per shot, `"sfx": [{"role", "at": "start"|"end"|source_s}]`;
  - `sfx_variants` alternates variants of a role.
- **Density:** about 3–5 accents per 30 s of talking head. Remove a sound that lands within ~0.3 s
  of another, or that a bigger sound masks.
- **Levels:**
  - measure each effect alone: the difference between this build and the previous one at each cue;
  - accent peaks sit 3–14 dB under the voice peak, with ding and cash at the top of that range;
  - a long boom carries more energy than its peak suggests, so keep its gain low;
  - the voice level must not drop between versions.

## 4. Master

- **Two-pass `loudnorm` to I = −15 LUFS and TP −1.5**, `linear=true`, on the mix, then mux with
  `-c:v copy`.
- **If true peak stays above −1.5,** use `loudnorm=I=-15.5:TP=-2,alimiter=limit=0.8`.
- **Report** LUFS and dBTP from `ebur128=peak=true`, and for talking heads, the seam click check.
- **Say whether anyone listened at speed on a phone.** If not, write that in `review.md`.
