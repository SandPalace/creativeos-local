---
name: talking-head-edit
description: Receta para editar tomas crudas de una persona hablando a cámara hasta un reel o anuncio vertical (de AI Studios): corta silencios por el audio, hace zooms guiados por el volumen de la voz y validados contra la transcripción, agrega gráficos de marca con la persona recortada al frente y normaliza el volumen. Requiere la app Tesseract. Úsalo para "edita el video de la maestra/el fundador", "corta silencios", "zoom de énfasis", videos a cámara o de creador.
---

This skill is the procedure. The rules live in the KB and the tools do the work:

- `knowledge/craft/talking-head-editing.md`: what to cut, the camera system, and how to validate emphasis. Read it in full first.
- `knowledge/tools/tesseract.md`: the Tesseract caveats. Read it before touching a `.tsrct`.
- `render/tesseract/talking-head/README.md`: the tool reference and the `edit.json` format.

In the steps below, `T` = `render/tesseract/talking-head`.

Stack: Python 3.11 + numpy and ffmpeg (voice analysis, loudness, seams), the Tesseract CLI `tsrct`
0.3.1 (the editable project and its export), Swift + Apple Vision (person cutouts, macOS), and the
`kits/<brand>.json` brand kit. Install and versions: `motion-video` skill §2.

## Preconditions

- **Footage:** the takes are local, and every take has a word-level transcript (`{"NN": [[word, s, e], …]}`).
  The CLI does not transcribe. Use the platform's existing transcripts; never invent words.
- **Brand kit:** `T/kits/ejemplo.json` shows the format. For the client, write `T/kits/<cliente>.json` from
  `hechos.md` (`marca_colores`, fonts): only `confirmado` values; otherwise say the palette is provisional.
- **Client facts:** every on-screen claim traces to the brief (non-negotiable 8). New copy goes to client review.
- **Versioning:** each version gets a new `work` folder and a new `name`. Never overwrite an earlier version's `.tsrct`.

## Procedure

1. **Write `edit.json`** in a new `<edit-root>/.tesseract-work/vN/` (copy the Lucy 002 v7 one).
   - Choose the shot order and source ranges from the transcript.
   - Give each shot `head`/`cx`. Read them off the person matte: the first white row, and the face centre.
   - Give each shot a single kit `path` colour.
   - Add graphics only where they carry a word the viewer must keep.
2. **Cutouts.** If any shot has `behind` graphics, run `python3 T/cutouts.py --edit E`.
   Check one cutout over a contrasting background.
3. **Analyse the voice.** Run `python3 T/voice.py analyze --edit E`, then read `analysis.md`:
   - Are the trims and pause cuts sensible?
   - Does a pause carry meaning? If so, keep it, by raising `min_pause` or excluding it.
4. **Plan the camera.** Run `python3 T/voice.py propose --edit E` to get `emphasis.draft.json`.
   Then **validate every super zoom against its sentence** (KB §3):
   - Move it to the word that carries the meaning.
   - Reject function words and repeated words.
   - Fill in `why`.
   - Prune `sections` to real clause starts.
   - Set `tail_override` when the CTA would be shorter than 2.5 s.

   Save the result as `emphasis.json`. Never build from the draft unread.
5. **Build.** Run `python3 T/build.py --edit E`, adding `--no-import` while you iterate.
   Then check a filmstrip at every super zoom, at every snap and at the hero moments:
   ```
   "$HOME/Library/Application Support/Tesseract/bin/tsrct" filmstrip --project <root>/<name>.tsrct \
     --timestamps-ms <t1> <t2> … --tile-width 216 --tile-height 384 --items-per-row 9 --output <root>/Previews/<name>-strip.png
   ```
   Times are in `<work>/edit-map.json` (`snaps_s`, `super_s`). Look at the image. Fix any word
   hidden by the head, any label or chip over the face (check it at the super-zoom moments too),
   any wrap or collision, and any zoom that lands off the face.
5b. **Sound.** Point `sfx.dir` at a folder of **verified** files: the `sound-design` skill §1,
   or the pack's `v2/`. Write `roles.json` (gain, `lead_ms` and `dur_ms` per role). Then:
   - add per-shot cues (`"sfx": [{"role", "at"}]`) for a swell into the CTA or a closing ding;
   - alternate repeated accents with `sfx_variants`;
   - turn off pops that a bigger sound masks (`"pop": false` on a chip, `"sfx": null` on a pill).

   After `finish`, measure each effect against the previous version (`sound-design` §3).
6. **Finish.** Run `python3 T/finish.py --edit E`. It produces the export, a loudness of −15 LUFS /
   ≤ −1 dBTP, and a seam click check. Any flagged seam must be fixed before you deliver.
7. **Deliver in the vault** (this kit has no `publish.py`): copy the export to
   `clientes/<cliente>/creativos/<pieza>_v<n>_video.mp4` and write the creativo note as `motion-editor`
   describes ("En esta bóveda").
   - Choose a thumbnail frame with the face expressive and a hero block visible → `_portada.png`.
   - Use a new version for each change; never overwrite one the owner saw.
8. **Write `README-vN.md`** in the edit root:
   - what changed;
   - the measured duration and loudness;
   - the emphasis table with its reasons;
   - any deliberate departures from the kit;
   - what was **not** checked, e.g. "not listened at speed".

   Then commit the scripts and configs. Media live in S3, not git.

## Do not

- Find pauses from transcript timestamps (they hide them), or cut every breath.
- Zoom the graphics with the shot, or use point text inside a zoomed group (tsrct 0.3.1 wraps it).
- Pick emphasis by loudness alone.
- Claim the mix sounds right without listening. Say what was measured instead.
