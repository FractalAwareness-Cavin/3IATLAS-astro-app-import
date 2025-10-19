NOTE (tlh): tlhIngan Hol mu'ghom wIghajbe' 'ej qaStaHvIS poH naQvam, HolwIj qumuvtaH 'Iw HIq. English content retained until translation volunteers arrive.

# Developer scripts

Utilities for regenerating and validating the 3I/ATLAS ephemeris kit live under `developer/scripts/` and `tools/`. Use this guide when you need to refresh the data set or sanity-check changes before publishing a new release.

## Prerequisites
- Python 3.10 or newer (`python3 --version` to confirm).
- Optional: a virtual environment (`python3 -m venv .venv && source .venv/bin/activate`) if you plan to install extra packages.
- Internet access when running the SBDB updater or the Horizons verifier.
- Optional: `mksweph` if you intend to build Swiss Ephemeris binaries with `build_swisseph.sh`.

The repository vendors `pyswisseph` in `developer/vendor/`, so sidereal output works without additional installs.

## Default Horizons recipe

Raw JSON outputs in `developer/raw/` were generated from NASA/JPL Horizons with the following parameters:

```
COMMAND='DES=1004083;'
MAKE_EPHEM='YES'
EPHEM_TYPE='VECTORS'
CENTER='500@399'        # Earth centre
REF_PLANE='ECLIPTIC'
REF_SYSTEM='J2000'
START_TIME='2016-01-01'
STOP_TIME='2040-12-31'
STEP_SIZE='1 d'
TABLE_TYPE='VECTORS'
```

Adjust those values if you need a different coverage window or vantage point, then refresh the JSON files before regenerating outputs.

## `generate_ephemeris.py`
Location: `developer/scripts/generate_ephemeris.py`

- Reads the JSON vector dumps in `developer/raw/` and rewrites every derived product:
  - CSV tables in `apps-using-csv-files/`
  - Solar Fire text tables in `solar-fire/`
  - MPC ephemeris (`apps-using-mpc-files/geocentric_mpc_ephemeris.txt`)
  - Sign-ingress summaries.
- Automatically loads the vendored `pyswisseph` module when available to populate sidereal fields.
- Creates target directories if they do not exist.

Usage:

```
cd developer/scripts
python3 generate_ephemeris.py
```

The script runs with baked-in settings. If you need to tweak time spans or cadence, update the JSON files first (or modify the constants at the top of the script).

## `build_swisseph.sh`
Location: `developer/scripts/build_swisseph.sh`

- Requires the proprietary `mksweph` utility.
- Converts the CSV outputs into Swiss Ephemeris `.se1` binaries and stores them in `developer/swisseph/`.

Usage:

```
cd developer/scripts
bash build_swisseph.sh
```

The helper refuses to run if `mksweph` is not on your `PATH`.

## `tools/update_orbital_elements.py`
Location: `tools/update_orbital_elements.py`

- Fetches the latest SBDB orbital solution for 3I/ATLAS and updates every single-line template:
  - MPC one-line files (`apps-using-mpc-files/*/3I_ATLAS_mpc_1line.txt`)
  - KStars snippets (`apps-using-mpc-files/kstars/` and import-pack templates)
  - Solar Fire `extras.dat` blocks.
- Prints the retrieved elements to stdout for auditability.

Usage (from the repository root):

```
python tools/update_orbital_elements.py
```

Add `--dry-run` to preview the values without touching the files.

## `tools/verify_ephemeris.py`
Location: `tools/verify_ephemeris.py`

- Spot-checks rows from `apps-using-mpc-files/geocentric_mpc_ephemeris.txt` against live Horizons data.
- Compares the geocentric distance ("delta") over a configurable date range and flags rows that exceed the tolerance.

Usage (from the repository root):

```
python tools/verify_ephemeris.py --start 2025-10-01 --days 5 --tolerance 5e-4
```

Arguments:
- `--start`: first date to verify (default `2025-10-01`).
- `--days`: number of consecutive days to check (default `5`).
- `--tolerance`: allowable difference in astronomical units (default `5e-4`, roughly 75,000 km).

The script exits with a non-zero status if any rows fail, making it suitable for CI gating.
