"""Rebuild the SFX pack from the Freesound originals in raw/ into v2/.

  python3 build_pack.py

The first processed pack (the .wav/.mp3 files next to this script) is broken: every file keeps
only ~30 ms of sound followed by digital silence. It is left in place because Lucy 002 v4–v10
were built from it. v2/ is cut from raw/ with the segments below, read from each original's
loudness envelope, then given a 5 ms fade in, a fade out, and a peak of -3 dBFS.

Each row: name, start s, duration s, fade-out s, hit_ms (where the transient or the peak sits
inside the cut file, for lining the sound up with a picture cue).
"""
import json
import os
import subprocess

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SPEC = [
    ("boom-deep-01", 0.30, 3.40, 0.60, 120),
    ("hit-cinematic-01", 0.00, 4.10, 0.50, None),
    ("record-scratch-01", 0.08, 1.20, 0.25, 20),
    ("whoosh-fast-01", 0.05, 0.50, 0.15, 150),
    ("whoosh-fast-02", 0.05, 0.90, 0.30, 200),
    ("swoosh-swipe-01", 0.00, 0.66, 0.15, 150),
    ("pop-01", 0.00, 0.25, 0.08, 0),
    ("pop-02", 0.00, 0.15, 0.04, 0),
    ("ding-notification-01", 0.00, 1.80, 0.40, 0),
    ("cash-register-01", 0.90, 0.95, 0.25, 100),
    ("keyboard-typing-01", 0.00, 1.50, 0.30, None),
    ("mouse-click-01", 1.00, 0.10, 0.03, 0),
    ("camera-shutter-01", 3.20, 0.60, 0.10, 100),
    ("riser-01", 0.00, 2.18, 0.08, 1800),
    ("reverse-swell-01", 0.00, 3.06, 0.03, 3030),
    ("applause-01", 2.00, 2.50, 0.80, None),
    ("crowd-wow-01", 0.00, 3.00, 0.80, None),
    ("glitch-01", 0.00, 1.72, 0.10, 0),
    ("typewriter-ding-01", 0.08, 0.75, 0.20, 20),
]


def decode(path):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-ac", "1", "-ar", "48000", "-f", "s16le", "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.int16).astype(float) / 32768


def main():
    out = os.path.join(HERE, "v2")
    os.makedirs(out, exist_ok=True)
    report = []
    for name, start, dur, fade, hit in SPEC:
        src = os.path.join(HERE, "raw", f"{name}.mp3")
        dst = os.path.join(out, f"{name}.wav")
        x = decode(src)[int(start * 48000): int((start + dur) * 48000)]
        gain = -3.0 - 20 * np.log10(np.abs(x).max() + 1e-12)
        af = (f"afade=t=in:d=0.005,afade=t=out:st={max(0, dur - fade):.3f}:d={fade:.3f},volume={gain:.2f}dB")
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{start}", "-t", f"{dur}", "-i", src, "-af", af,
                        "-ar", "48000", "-ac", "2", "-c:a", "pcm_s16le", dst], check=True)
        y = decode(dst)
        win = 480
        n = len(y) // win
        e = 20 * np.log10(np.sqrt((y[: n * win].reshape(n, win) ** 2).mean(1)) + 1e-9)
        audible = int((e > e.max() - 40).sum() * 10)
        report.append({"file": f"v2/{name}.wav", "from": f"raw/{name}.mp3", "start_s": start, "duration_s": round(len(y) / 48000, 3),
                       "gain_db": round(gain, 1), "hit_ms": hit, "audible_ms": audible})
        print(f"{name:22s} {len(y) / 48000:5.2f}s  gain {gain:+5.1f} dB  audible {audible} ms")
    with open(os.path.join(out, "pack.json"), "w") as f:
        json.dump(report, f, indent=1)


if __name__ == "__main__":
    main()
