# 3I/ATLAS Ephemeris Data Kit

This folder packages daily ephemerides for the interstellar comet **3I/ATLAS (C/2025 N1)** so astrologers can experiment with the body inside their favourite tools. The numbers come directly from NASA/JPL Horizons and cover the full interval that the comet resides inside the heliosphere (2016‑01‑01 through 2040‑12‑31).

## Contents

- `raw/` – JSON dumps returned by Horizons (heliocentric, geocentric, and barycentric frames). Each file can be regenerated with `scripts/generate_ephemeris.py`.
- `data/`
  - `*_daily.csv` – Cartesian + spherical coordinates in the ecliptic of J2000 frame, one row per TDB midnight.
  - `geocentric_*_sign_ingresses.csv` – pre-computed tropical and sidereal ingress timestamps.
  - `geocentric_sidereal_{lahiri,fagan_bradley}_daily.csv` – sidereal longitudes with the chosen ayanāṃśa and the exact ayanāṃśa value per day.
  - `geocentric_mpc_ephemeris.txt` – MPC-style daily ephemeris (RA/Dec, Δ, r, elongation, phase) for quick import via “Add MPC comet/object” dialogs.
- `text/`
  - `*_daily_solarfire.txt` – tropical tables (`YYYY MM DD HHMM longitude latitude distance`) ready for Solar Fire / Astro Gold / TimePassages.
  - `geocentric_sidereal_{lahiri,fagan_bradley}_daily_solarfire.txt` – same layout but with sidereal longitude plus an ayanāṃśa column.
- `scripts/`
  - `generate_ephemeris.py` – re-runs all Horizons queries and rebuilds every table. Optional sidereal outputs require `pyswisseph` (vendored under `vendor/`).

## Horizons recipe

All tables were generated with the Horizons API using:

```
COMMAND='DES=1004083;'
MAKE_EPHEM='YES'
EPHEM_TYPE='VECTORS'
REF_PLANE='ECLIPTIC'
OUT_UNITS='KM-S'
STEP_SIZE='1 d'
CENTER='500@10'    (heliocentric)
CENTER='500@399'   (geocentric Earth)
CENTER='500@0'     (solar-system barycentre)
```

The raw responses are stored so you can reprocess them with different coordinate systems or cadences if needed.

## Using the data

### 1. Solar Fire / Astro Gold / TimePassages

1. Pick the text file that matches your tradition (tropical `geocentric_daily_solarfire.txt` or sidereal `geocentric_sidereal_lahiri_daily_solarfire.txt`, etc.).
2. In Solar Fire choose *File → Open Ephemeris → Import → Text*, select the file, and map the columns as longitude, latitude, distance (and ayanāṃśa if present).
3. Assign the body to a free **User-Defined object slot** (User #1 is a safe default if unused) so you can toggle it from *Chart Options → Points*.

Astro Gold and TimePassages accept the same format through their custom-object import dialogs. Keep both tropical and sidereal files handy so you can swap depending on the chart style.

If your software supports the MPC comet import workflow, point it at `data/geocentric_mpc_ephemeris.txt`—each line is the standard 80-column daily entry (UT midnight, J2000 coordinates).

### 2. Open-source tools (Astrolog, Morinus, etc.)

- `data/geocentric_daily.csv` – tropical longitude/latitude/distance plus heliocentric Cartesian coordinates and km s⁻¹ velocities.
- `data/geocentric_sidereal_lahiri_daily.csv` / `data/geocentric_sidereal_fagan_bradley_daily.csv` – sidereal longitude columns (`lambda_sidereal_deg`) with the daily ayanāṃśa (`ayanamsa_deg`).
- `geocentric_*_sign_ingresses.csv` – quick reference for sign changes (tropical and the two sidereal modes).
- `data/geocentric_mpc_ephemeris.txt` – MPC 80-column ephemeris (daily UT 0h) suitable for programs that expect the classic MPC comet format.

### 3. Swiss Ephemeris users

Swiss Ephemeris stores custom bodies in `.se1` binaries. Use the official `mksweph` utility once you have compiled the Swiss Ephemeris tools from https://www.astro.com/ftp/swisseph/ (or run `scripts/build_swisseph.sh` after installing them):

```
# Tropical ephemeris
mksweph -i data/geocentric_daily.csv \
        -o swisseph/3I_ATLAS_geocentric.se1 \
        -n "3I/ATLAS" \
        -b 2016-01-01 -e 2040-12-31

# Sidereal (Lahiri) ephemeris
mksweph -i data/geocentric_sidereal_lahiri_daily.csv \
        -o swisseph/3I_ATLAS_Lahiri.se1 \
        -n "3I/ATLAS (Lahiri)" \
        -b 2016-01-01 -e 2040-12-31
```

Copy the resulting `.se1` files into your program’s `SWEPHEM` directory and assign them to any open asteroid/comet number. If you add the Swiss tools to your PATH, you can hook these commands into `scripts/generate_ephemeris.py` to rebuild the binaries automatically after a Horizons refresh.

## Key milestones

- Heliosphere entry (94 au termination shock, inbound): **2018‑03‑22 21:14 TDB** (JD 2458200.385)
- Perihelion (from Horizons solution #27): **2025‑10‑29 11:36 TDB**
- Heliosphere exit (94 au, outbound): **2033‑06‑06 18:49 TDB** (JD 2463755.284)
- Current geocentric snapshot near 2025‑10‑18: longitude ≈ 209.78° (Libra), distance ≈ 1.43 au, radial speed ≈ −20.17 km s⁻¹.

## Rebuilding the tables

```
cd atlas_ephemeris
python3 scripts/generate_ephemeris.py
```

The script re-queries Horizons (internet connection required) and overwrites the CSV/TXT outputs. Install `pyswisseph` beforehand if you want sidereal tables regenerated (`python3 -m pip install pyswisseph --target vendor`).

## Notes and caveats

- All timestamps are Barycentric Dynamical Time (TDB) at 00:00 each day. Convert to UT if your software expects it.
- Horizons uses the DE441 planetary ephemeris and SB441-N16 perturbing asteroid model (solution date 2025‑10‑10).
- Distances in the CSV are heliocentric by default. Geocentric files show topocentric range from Earth’s centre. Run Horizons with an observatory code if you need a specific location.
- Sidereal practitioners can substitute a different ayanāṃśa by subtracting their preferred value from the tropical longitude. The sidereal tables provided here use Lahiri and Fagan/Bradley for convenience.
- The termination shock is treated as a 94 au sphere; adjust if your research uses a different heliosphere model.

Enjoy exploring 3I/ATLAS inside your charts!
