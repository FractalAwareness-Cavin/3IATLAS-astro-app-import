# 3I/ATLAS Import Pack

## TL;DR

Paste a single **MPC 1-line** for `3I/ATLAS` (aka `C/2025 N1 (ATLAS)`), run the tool, then import into Stellarium; paste the generated line into KStars; Solar Fire has a guarded `extras.dat` path; Astro Gold/TimePassages can’t import new moving bodies today.

## Status

| App                    | Method                      | Import Type           | Ready Today          |
| ---------------------- | --------------------------- | --------------------- | -------------------- |
| Astro Gold (macOS/iOS) | Enable built-ins in UI      | — (no user import)    | ✅ built-ins only     |
| Solar Fire (Windows)   | `extras.dat` (Other Bodies) | Orbital elements      | ✅ with care          |
| TimePassages (Mac/Win) | Enable built-ins in UI      | — (no user import)    | ✅ built-ins only     |
| Stellarium (all)       | Solar System Editor import  | MPC 1-line elements   | ✅                    |
| KStars (all)           | `comets.dat` line           | KStars comet line     | ✅                    |
| SkySafari (Plus/Pro)   | Update Orbit Data           | MPC elements (online) | ✅ when MPC publishes |

See `docs/INSTALL_3I-ATLAS.md` and `docs/WORKFLOWS.md` for exact steps.
