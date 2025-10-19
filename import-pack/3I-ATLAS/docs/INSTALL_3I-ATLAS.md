# 3I/ATLAS — Import Pack (v0.2)

Use this pack when you need **ready-to-use MPC orbital elements** or a
platform-specific helper to get 3I/ATLAS into astronomy software. Everything is
offline-friendly and based on JPL SBDB solution 27 (2025-10-10).

> **TL;DR**
> - **Stellarium** → import the supplied one-line via *Solar System Editor → Import elements in MPC format*.
> - **KStars** → run the no-install helper (Windows/macOS/Linux) or paste the provided `comets.dat` line.
> - **SkySafari** → use *Settings → Solar System → Update Orbit Data* (Plus/Pro) and keep the one-line for reference.
> - **Solar Fire** → merge the provided `[3I_ATLAS]` block into `extras.dat` (backup first); helper scripts included.
> - **Astro Gold / TimePassages** → currently no moving-body import; see the main repo notes for fixed-point workarounds.

## What’s inside

- `templates/stellarium/3I_ATLAS_mpc_elements.txt` — MPC 1-line comet element for 3I/ATLAS.
- `templates/skysafari/3I_ATLAS_mpc_1line.txt` — same one-line for archival/reference.
- `templates/kstars/3I_ATLAS_comets_dat_snippet.txt` — single line ready to append to `comets.dat` (also used by Cartes du Ciel / WinStars).
- `templates/solar_fire/3I_ATLAS_extras_dat_PLACEHOLDER.txt` — drop-in `[3I_ATLAS]` block for Solar Fire `extras.dat`.
- `tools/3i_elements_to_formats.py` — optional converter if you ever replace the official MPC line with an updated one.
- `docs/WORKFLOWS.md` — click-by-click instructions for Stellarium, KStars, SkySafari, Solar Fire.

## Quick start

Already up-to-date? jump straight to `docs/WORKFLOWS.md`.
Otherwise:
```bash
python tools/3i_elements_to_formats.py --paste   # paste a newer MPC 1-line if one is published
```
This rewrites the templates and prints the new KStars line. Otherwise you can
skip the script—the included files already contain the latest published values.

## Caveats

- **Solar Fire `extras.dat`**: field order can vary by version. Use the
  built-in help topic “Format of the Orbital Elements File” if you edit the file
  manually, and always back up first.
- **SkySafari**: there is no manual file import; rely on *Update Orbit Data*.
- **Astro Gold / TimePassages**: at the time of writing, these applications do
  not expose a moving-body import workflow. Use their fixed custom points or
  request vendor support.
