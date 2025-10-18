3I/ATLAS – MPC IMPORT GUIDE
===========================

`geocentric_mpc_ephemeris.txt` follows the Minor Planet Center 80-column format
with daily UT (0h) entries, J2000 right ascension/declination, geocentric
range (Δ), heliocentric range (r), elongation, and phase angle.

Use this file with any software that imports comets/asteroids from MPC data,
for example:

- TimePassages (Comet/Asteroid import)
- SkySafari / SkyVoyager (Settings → Solar System → Minor Body → Import)
- KStars / Cartes du Ciel (Comet/Asteroid import dialog)
- Stellarium (Plugins → Solar System Editor → Import MPC data)

General workflow:
1. Download or copy the file to a convenient location.
2. Open your app’s “Import MPC comet/asteroid” tool.
3. When asked for the source file, browse to `geocentric_mpc_ephemeris.txt`.
4. Assign a name (3I/ATLAS) and confirm. The body now appears alongside other
   small bodies in the program.
