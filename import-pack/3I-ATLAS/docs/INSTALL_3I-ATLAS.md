# 3I/ATLAS — Import Pack (v0.1)

This folder gives you **ready-to-use templates** and **scripts** to push 3I/ATLAS into apps that accept **MPC-format orbital elements**. It also documents what’s currently *possible* (and *not possible*) in each app.

> **TL;DR**
> - **Stellarium**: use `templates/stellarium/3I_ATLAS_mpc_elements.txt` via *Solar System Editor → Import elements in MPC format*.
> - **KStars**: convert your MPC 1‑line to a KStars `comets.dat` entry (see `tools/3i_elements_to_formats.py`); then replace/append in your local `comets.dat` (backup first!).
> - **SkySafari**: no manual import; use *Settings → Solar System → Update Orbit Data* (Plus/Pro). We include a 1‑line file for reference.
> - **Solar Fire**: uses `extras.dat` (Other Bodies). We include guidance and a placeholder, but **the exact line format is version‑specific**; back up first.
> - **Astro Gold (macOS/iOS)** and **TimePassages (macOS/Windows)**: no supported workflow to import a *new moving body* from a file. You can toggle built‑ins and add fixed “Custom Points,” but not supply MPC/ephemerides.

## What’s inside
- `templates/stellarium/3I_ATLAS_mpc_elements.txt` — one MPC 1‑line comet element (or add yours).
- `templates/skysafari/3I_ATLAS_mpc_1line.txt` — same one‑line for archival/reference.
- `templates/kstars/3I_ATLAS_comets_dat_snippet.txt` — ready‑to‑paste KStars `comets.dat` single line.
- `templates/solar_fire/3I_ATLAS_extras_dat_PLACEHOLDER.txt` — noted skeleton for Solar Fire.
- `tools/3i_elements_to_formats.py` — paste a **single MPC 1‑line**; writes the templates and prints a KStars line.

> This pack **does not** estimate orbital elements from ephemerides. Use MPC/JPL/COBS as the source of truth.

## Quick start
1) Get a single **MPC 1‑line** for `3I/ATLAS` (aka `C/2025 N1 (ATLAS)`).
2) Run:
```bash
python tools/3i_elements_to_formats.py --paste
# or:
python tools/3i_elements_to_formats.py --line "C/2025 N1 (ATLAS) …"
```
3) Follow the per‑app steps in `docs/WORKFLOWS.md`.

### Caveats

* **Solar Fire `extras.dat`**: field order varies with version; check in‑app help before editing.
* **SkySafari**: rely on *Update Orbit Data*; no manual import.
* **Astro Gold / TimePassages**: no import for new moving bodies; only built‑ins/fixed points.
