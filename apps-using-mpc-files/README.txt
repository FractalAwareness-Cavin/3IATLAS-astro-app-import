3I/ATLAS – MPC IMPORT GUIDE
===========================

`geocentric_mpc_ephemeris.txt` contains daily MPC-style ephemerides (UT 0h,
J2000 RA/Dec, Δ, r, elongation, phase). Use this file with astronomy tools that
accept MPC comet/asteroid ephemerides or elements. Typical workflows include:

- **Stellarium** – Plugins → Solar System Editor → Import elements in MPC format (see `stellarium/`).
- **KStars** – Append the KStars-formatted line or use the helpers in `kstars/`.
- **SkySafari / SkyVoyager (Plus/Pro)** – Settings → Solar System → Update Orbit Data (pulls
  MPC elements automatically; keep the one-line file for reference).
- **Cartes du Ciel (SkyCharts)** – Use the instructions in `cartes-du-ciel/` to import the one-line element.
- **WinStars** – Use the instructions in `winstars/` to paste or append the single-line element.
- Other MPC-compatible planners — import the 80-column file as you would any comet/asteroid catalogue.

General workflow:
1. Copy `geocentric_mpc_ephemeris.txt` to a convenient location.
2. Open your application's comet/asteroid import dialog.
3. Browse to the file and import as `3I/ATLAS`.

For platform-specific helper scripts (Windows/macOS/Linux) and one-line element templates,
see `import-pack/3I-ATLAS/`.
