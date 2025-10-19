NOTE (tlh): tlhIngan Hol mu'ghom wIghajbe' 'ej qaStaHvIS poH naQvam, HolwIj qumuvtaH 'Iw HIq. English content retained until translation volunteers arrive.

# 3I/ATLAS Import Pack

Quick-start templates, helper scripts, and documentation for bringing
**3I/ATLAS (C/2025 N1)** into MPC-compatible astronomy software.

## Contents
- `docs/INSTALL_3I-ATLAS.md` — overview, caveats, and quickstart (currently v0.2).
- `docs/WORKFLOWS.md` — click-by-click instructions for Stellarium, KStars,
  SkySafari, Solar Fire, and notes on non-supporting apps.
- `templates/` — ready-to-use MPC 1-line elements, KStars `comets.dat` line, and
  Solar Fire `[3I_ATLAS]` block (all based on JPL SBDB solution 27).
- `tools/3i_elements_to_formats.py` — optional converter if you paste a newer
  MPC 1-line; rewrites the templates automatically.
- `tools/kstars/` — Windows/macOS/Linux helpers that back up and append the
  KStars line.
- `tools/solarfire/` — Windows helpers that back up and merge the `extras.dat`
  block for 3I/ATLAS.

## Usage snapshot
- Stellarium: import the supplied one-line via **Solar System Editor → Import elements in MPC format → File**.
- KStars: run the helper script for your OS or append the provided `comets.dat` line manually.
- SkySafari: use **Settings → Solar System → Update Orbit Data** (Plus/Pro tiers).  
- Solar Fire: merge the `[3I_ATLAS]` block into `extras.dat` (backup first).  
- Astro Gold / TimePassages: currently no moving-body import; see the repository notes if you need fixed custom points.

Update the templates with the converter script whenever a new orbital solution is released.
