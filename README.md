# 3I/ATLAS Ephemeris Kit

Daily ephemerides for the interstellar comet **3I/ATLAS (C/2025 N1)**, generated straight from NASA/JPL Horizons and organised so astrologers can drop the body into their favourite apps. Coverage spans the comet’s passage through the heliosphere (2016‑01‑01 → 2040‑12‑31).

## Where to start?

Use the folder that matches your app or download the zip files below. If you are unsure, open your software, choose *File → Import* (or similar), and note the file extensions it expects.

- `astro-gold/` – ready-to-import text tables for Astro Gold (tropical + Lahiri and Fagan/Bradley sidereal variants).
- `solar-fire/` – the same layout packaged for Solar Fire.
- `time-passages/` – the same layout packaged for TimePassages.
- `apps-using-mpc-files/` – MPC-style daily ephemeris for software that wants classic MPC comet/asteroid files.
- `apps-using-csv-files/` – full CSV datasets for tools that can read spreadsheets or plain data tables.
- `developer/` – Horizons JSON dumps, regeneration scripts, vendored `pyswisseph`, and the Swiss Ephemeris helper.

#### End-user direct downloads
- [Astro Gold kit](https://github.com/FractalAwareness-Cavin/3IATLAS-astro-app-import/releases/download/v1.0.0/3I-ATLAS_astro_gold.zip)
- [Solar Fire kit](https://github.com/FractalAwareness-Cavin/3IATLAS-astro-app-import/releases/download/v1.0.0/3I-ATLAS_solar_fire.zip)
- [TimePassages kit](https://github.com/FractalAwareness-Cavin/3IATLAS-astro-app-import/releases/download/v1.0.0/3I-ATLAS_time_passages.zip)
- [MPC import kit](https://github.com/FractalAwareness-Cavin/3IATLAS-astro-app-import/releases/download/v1.0.0/3I-ATLAS_apps_using_mpc_files.zip)
- [CSV research kit](https://github.com/FractalAwareness-Cavin/3IATLAS-astro-app-import/releases/download/v1.0.0/3I-ATLAS_apps_using_csv_files.zip)

Each zip contains the files from the matching folder plus a `README.txt` with the instructions below—unzip the bundle before importing into your software.

Need step-by-step instructions? Jump to:
- [Astro Gold (macOS / iOS)](#astro-gold-instructions)
- [Solar Fire (Windows)](#solar-fire-instructions)
- [TimePassages (macOS / Windows)](#timepassages-instructions)
- [MPC-format import](#mpc-import-instructions)
- [CSV usage](#csv-usage-notes)

## Folder guide

- **astro-gold/** – importable text ephemerides (`YYYY MM DD HHMM longitude latitude distance`) for Astro Gold.
- **solar-fire/** – same files labelled for Solar Fire.
- **time-passages/** – same files labelled for TimePassages.
- **apps-using-mpc-files/** – `geocentric_mpc_ephemeris.txt` in MPC 80-column format (daily UT 0h, J2000 RA/Dec, Δ, r, elongation, phase angle).
- **apps-using-csv-files/** – the complete CSV suite: heliocentric/geocentric/barycentric vectors, tropical and sidereal longitudes, sign-ingress summaries.
- **developer/** – raw Horizons outputs, regeneration scripts, vendored `pyswisseph`, and `build_swisseph.sh`.

## App-specific instructions

### Astro Gold instructions
**macOS**
1. Copy `geocentric_daily_solarfire.txt` (or the sidereal variant) into `~/Library/Containers/au.com.esotech.AstroGoldMac/Data/Library/Application Support/Astro Gold/Ephemerides/`.
2. In Astro Gold choose **Astro Gold → Settings…** and select **Chart → Chart Points** in the sidebar.
3. Click **Manage Points… → Import**, choose **Solar Fire Text**, pick the file, and name the body (e.g. `3I/ATLAS`).
4. Tick the new point to enable it.

**iOS / iPadOS**
1. Place the `.txt` file in `On My iPhone/iPad → Astro Gold → Ephemerides` via the Files app (or Finder when connected to a Mac).
2. Inside Astro Gold go to **Settings → Chart Points → Manage Points… → Import**, choose **Solar Fire Text**, and select the file.
3. Name and enable the body.

### Solar Fire instructions (Windows)
1. Copy the desired `.txt` file into `Documents\Solar Fire User Files\Ephemerides`.
2. In Solar Fire select **File → Open Ephemeris → Import → Text**, map columns to **Longitude**, **Latitude**, **Distance (AU)**, and name the ephemeris (e.g. `3I_ATLAS`).
3. Assign it to a free User point (User #1 is common) and enable that point in chart settings.

### TimePassages instructions (macOS / Windows)
- **macOS**: copy the file to `~/Library/Application Support/TimePassages/Ephemerides/`, then use **TimePassages → Preferences → Calculations → Custom Bodies → Import** (choose *Solar Fire Text*). Enable the body and add it under **Charts → Chart Settings → Planets & Points**.
- **Windows**: copy the file to `%APPDATA%\TimePassages\Ephemerides\`, then follow **Edit → Preferences → Calculations → Custom Bodies → Import**. Enable the body and include it in your chart point selection.
- Alternatively, use **Comet/Asteroid → Import from MPC file** with `time-passages/geocentric_mpc_ephemeris.txt` (or the copy in `apps-using-mpc-files/`).

### MPC import instructions
Use `apps-using-mpc-files/geocentric_mpc_ephemeris.txt` (also duplicated in the TimePassages folder for convenience) with any MPC comet/asteroid import dialog—examples include SkySafari/SkyVoyager, Stellarium, KStars, and TimePassages' comet import. Browse to the file, name the object `3I/ATLAS`, and confirm.

### CSV usage notes
`apps-using-csv-files/` contains the raw Horizons data for spreadsheets, scripting, or custom tools. Longitudes are in degrees, distances in AU, velocities in km/s. Sidereal tables include the daily ayanāṃśa (`ayanamsa_deg`).

## Horizons recipe

All data was produced with Horizons solution #27 (2025-10-10) using:

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

## Swiss Ephemeris `.se1`
The Swiss Ephemeris authoring utility `mksweph` is proprietary. If you have access to it:

```
SCRIPT_DIR=developer/scripts
bash "$SCRIPT_DIR/build_swisseph.sh"
```

This script reads the CSVs from `apps-using-csv-files/` and writes `.se1` binaries into `swisseph/`. Copy those into your astrology program’s `SWEPHEM` folder and assign them to a free asteroid/comet slot.

## Regenerating the ephemerides

```
cd developer/scripts
python3 generate_ephemeris.py
```

The script re-queries Horizons (internet connection required), refreshes the JSON dumps in `developer/raw/`, and rewrites all output folders. `pyswisseph` is already vendored so sidereal output works out of the box.

## Key milestones

- Termination-shock entry (~94 au, inbound): **2018‑03‑22 21:14 TDB** (JD 2458200.385)
- Perihelion: **2025‑10‑29 11:36 TDB**
- Termination-shock exit (~94 au, outbound): **2033‑06‑06 18:49 TDB** (JD 2463755.284)
- Snapshot near 2025‑10‑18: longitude ≈ 209.8° (Libra), distance ≈ 1.43 au, radial velocity ≈ −20.17 km s⁻¹.

## Notes & caveats

- Times are Barycentric Dynamical Time (TDB) at 00:00 each day; convert to UT as needed.
- Horizons solution uses planetary ephemeris DE441 and SB441-N16 perturbers.
- Geocentric distances are from Earth’s centre. For topocentric viewpoints, rerun Horizons with your observatory code via the generator script.
- Sidereal tables use Lahiri and Fagan/Bradley ayanāṃśas; apply your preferred ayanāṃśa if different.
- The heliosphere boundary is approximated as a 94 au sphere. Adjust if your research uses another value.

Enjoy charting 3I/ATLAS!

## Optional: installing Horizons tooling

You do not need a local Horizons install to use this kit—the data already comes from JPL. If you want to pull fresh ephemerides yourself, here are quick ways to access NASA/JPL Horizons on each platform:

### macOS / Linux
1. Ensure Python 3.10+ is available (in Terminal: `python3 --version`).
   - **macOS**: if Python is missing, install Homebrew, then `brew install python`.
   - **Linux**: see the distribution-specific commands [below](#linux-install-of-python).
2. Install Astroquery:
   ```bash
   python3 -m pip install astroquery --user
   ```
3. Query Horizons:
   ```bash
   python3 - <<'PY'
   from astroquery.jplhorizons import Horizons
   obj = Horizons(id='DES=1004083;', location='500@399', epochs={'start':'2025-01-01', 'stop':'2025-01-10', 'step':'1d'})
   print(obj.vectors())
   PY
   ```
   Astroquery wraps the official service and returns Pandas tables you can export to CSV.

   Alternative (macOS/Linux):
   ```bash
   curl 'https://ssd.jpl.nasa.gov/api/horizons.api?format=json&COMMAND=\'DES=1004083;%27&MAKE_EPHEM=YES&EPHEM_TYPE=VECTORS&CENTER=\'500@399\'&REF_PLANE=ECLIPTIC&STEP_SIZE=1%20d&START_TIME=2025-01-01&STOP_TIME=2025-01-03'
   ```

### Windows
1. Install Python 3 from https://www.python.org/downloads/ (tick “Add Python to PATH”).
2. In PowerShell:
   ```powershell
   py -m pip install astroquery
   py - <<'PY'
   from astroquery.jplhorizons import Horizons
   obj = Horizons(id='DES=1004083;', location='500@399', epochs={'start':'2025-01-01', 'stop':'2025-01-10', 'step':'1d'})
   print(obj.vectors())
   PY
   ```
3. Windows Subsystem for Linux (WSL) users can follow the macOS/Linux instructions.

### Classic CLI (Telnet)
```bash
telnet horizons.jpl.nasa.gov 6775
```
Follow the prompts to enter the target (`DES=1004083;`) and output options.

## Linux install of Python

Most desktop/server Linux installs ship with a Python interpreter because the OS (and many tools) rely on it, but the default version may be older than 3.10. When you need Python 3.10+ explicitly, use the package manager for your distribution—or install from source/pyenv if the repos are behind. Below are the common CLI commands by family:

- **Debian / Ubuntu / Linux Mint**
  - Check current version: `python3 --version`
  - Install latest repo build: `sudo apt update && sudo apt install python3 python3-pip`
  - If the official repos lag behind 3.10, add the deadsnakes PPA (Ubuntu-based only): `sudo add-apt-repository ppa:deadsnakes/ppa && sudo apt update && sudo apt install python3.10 python3.10-venv python3.10-distutils`
- **Fedora** – `sudo dnf install python3`
- **RHEL / CentOS / Alma / Rocky**
  - Enable CodeReady/PowerTools if needed, then `sudo dnf install python3`
  - For older releases use modules: `sudo dnf module enable python:3.11 && sudo dnf install python3`
- **openSUSE / SLES** – `sudo zypper install python310 python310-pip`
- **Arch / Manjaro**
  - Arch tracks the latest CPython: `sudo pacman -S python`
  - Use `pyenv` or an AUR package (e.g. `python310`) for specific versions.
- **Gentoo**
  - `sudo emerge --ask dev-lang/python:3.11`
  - Set the default with `eselect python list` / `eselect python set python3.11`
- **Void Linux** – `sudo xbps-install -S python3`
- **NixOS / Nix** – `nix-shell -p python311` or add `python311` to your configuration.

If your distribution lacks the desired version:

1. **pyenv**
   ```bash
   curl https://pyenv.run | bash
   exec $SHELL
   pyenv install 3.12.2
   pyenv global 3.12.2
   ```
2. **Official source**
   ```bash
   sudo apt install build-essential zlib1g-dev libssl-dev libffi-dev
   wget https://www.python.org/ftp/python/3.12.2/Python-3.12.2.tgz
   tar -xzf Python-3.12.2.tgz
   cd Python-3.12.2
   ./configure --enable-optimizations
   make -j$(nproc)
   sudo make altinstall
   ```

Even if a base system already includes Python, it’s safest to install your own 3.10+ alongside the system interpreter and use virtual environments (`python3 -m venv`) to isolate project dependencies.
