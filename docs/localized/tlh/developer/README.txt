NOTE (tlh): tlhIngan Hol mu'ghom wIghajbe' 'ej qaStaHvIS poH naQvam, HolwIj qumuvtaH 'Iw HIq. English content retained until translation volunteers arrive.

DEVELOPER TOOLKIT
=================

This folder contains everything required to regenerate the ephemeris
bundle from scratch.

Contents
--------
- `raw/` – JSON responses retrieved from the NASA/JPL Horizons API.
- `scripts/generate_ephemeris.py` – Python script that rebuilds the CSV,
  Solar Fire text files, MPC output, and sign-ingress summaries.
- `scripts/build_swisseph.sh` – helper to turn CSV tables into Swiss
  Ephemeris `.se1` binaries (requires `mksweph`).
- `vendor/` – vendored `pyswisseph` module so sidereal outputs work
  without extra installs.

Regenerating
------------
```
cd developer/scripts
python3 generate_ephemeris.py
```
The script re-queries Horizons (internet required) and updates the
folders in the repository root.

Swiss Ephemeris binaries
------------------------
If you have access to the proprietary `mksweph` utility:
```
cd developer/scripts
bash build_swisseph.sh
```
This writes `.se1` files into `../swisseph/` for distribution.

Feel free to modify the script to change cadence, coordinate systems,
or center bodies; the raw JSONs provide traceability back to Horizons.

For detailed usage notes, including the SBDB updater and verification helpers,
see `scripts/README.md`.
