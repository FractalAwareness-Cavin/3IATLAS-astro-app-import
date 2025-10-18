# 3I/ATLAS Ephemeris Kit

Daily ephemerides for the interstellar comet **3I/ATLAS (C/2025 N1)**, generated straight from NASA/JPL Horizons and organised so astrologers can drop the body into their favourite apps. Coverage spans the comet’s passage through the heliosphere (2016‑01‑01 → 2040‑12‑31).

## Where to start?

**For non-developers**

Use the folder that matches your app or the file type it accepts or download the corresponding `zip` file. If you are unsure, open your software, choose *File → Import* (or similar), and note the file extensions it expects. Keep this guide handy while you explore:

- `astro-gold/` – ready-to-import text tables for Astro Gold (tropical + Lahiri and Fagan/Bradley sidereal variants).
- `solar-fire/` – the same layout packaged for Solar Fire.
- `time-passages/` – the same layout packaged for TimePassages.
- `apps-using-mpc-files/` – MPC-style daily ephemeris for software that wants classic MPC comet/asteroid files.
- `apps-using-csv-files/` – full CSV datasets for tools that can read spreadsheets or plain data tables.

Direct download shortcuts:
- [Astro Gold kit](https://github.com/FractalAwareness-Cavin/3IATLAS-astro-app-import/releases/download/v1.0.0/3I-ATLAS_astro_gold.zip)
- [Solar Fire kit](https://github.com/FractalAwareness-Cavin/3IATLAS-astro-app-import/releases/download/v1.0.0/3I-ATLAS_solar_fire.zip)
- [TimePassages kit](https://github.com/FractalAwareness-Cavin/3IATLAS-astro-app-import/releases/download/v1.0.0/3I-ATLAS_time_passages.zip)
- [MPC import kit](https://github.com/FractalAwareness-Cavin/3IATLAS-astro-app-import/releases/download/v1.0.0/3I-ATLAS_apps_using_mpc_files.zip)
- [CSV research kit](https://github.com/FractalAwareness-Cavin/3IATLAS-astro-app-import/releases/download/v1.0.0/3I-ATLAS_apps_using_csv_files.zip)

**For developers & tinkerers**

Everything needed to regenerate or tweak the ephemerides lives in `developer/` (Horizons JSON dumps, Python scripts, vendored `pyswisseph`, Swiss Ephemeris helper).

## Folder guide

- **astro-gold/** – importable text ephemerides (`YYYY MM DD HHMM longitude latitude distance`) suited to Astro Gold. Contains tropical and sidereal versions (Lahiri, Fagan/Bradley).
- **solar-fire/** – identical files labelled for Solar Fire users.
- **time-passages/** – identical files labelled for TimePassages users.
- **apps-using-mpc-files/** – `geocentric_mpc_ephemeris.txt`, formatted in the standard MPC 80-column style (daily UT 0h, J2000 RA/Dec, Δ, r, elongation, phase angle).
- **apps-using-csv-files/** – the complete CSV suite: heliocentric/geocentric/barycentric vectors, tropical and sidereal longitudes, and sign-ingress summaries.
- **developer/** – Horizons raw outputs, regeneration scripts, vendored `pyswisseph`, and Swiss Ephemeris build helper (`scripts/build_swisseph.sh`).

## File guide (for end-users)

**Use these** if you want to download all the relevant files for your app so they are ready to use on your device once unzipped:

* **[astro-gold.zip](https://github.com/FractalAwareness-Cavin/3IATLAS-astro-app-import/blob/main/astro-gold.zip)**
* **[solar-fire.zip](https://github.com/FractalAwareness-Cavin/3IATLAS-astro-app-import/blob/main/solar-fire.zip)**
* [**time-passages.zip**](https://github.com/FractalAwareness-Cavin/3IATLAS-astro-app-import/blob/main/time-passages.zip)
* **[apps-using-mpc-files.zip](https://github.com/FractalAwareness-Cavin/3IATLAS-astro-app-import/blob/main/apps-using-mpc-files.zip)**
* [**apps-using-csv-files.zip**](https://github.com/FractalAwareness-Cavin/3IATLAS-astro-app-import/blob/main/apps-using-csv-files.zip)



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

## Quick instructions by format

### Astro Gold / Solar Fire / TimePassages
1. Pick the correct folder (`astro-gold/`, `solar-fire/`, or `time-passages/`) and choose the file that matches your tradition (e.g. `geocentric_daily_solarfire.txt` for tropical, `geocentric_sidereal_lahiri_daily_solarfire.txt` for Lahiri sidereal).
2. Import through your app’s *File → Import → Text* (or equivalent), mapping columns to longitude / latitude / distance (and ayanāṃśa if present).
3. Assign the body to a free custom slot (Solar Fire’s User #1, for example) so you can toggle it in chart settings.

### MPC-compatible comet/asteroid dialogs
Use `apps-using-mpc-files/geocentric_mpc_ephemeris.txt`. Each line is a daily UT-midnight entry with J2000 RA/Dec, geocentric distance Δ, heliocentric distance *r*, elongation, phase, and a placeholder magnitude.

### CSV / research workflows
`apps-using-csv-files/` holds everything:
- `geocentric_daily.csv` – tropical ecliptic longitude/latitude/distance plus heliocentric Cartesian coordinates and velocities.
- `geocentric_sidereal_lahiri_daily.csv` and `geocentric_sidereal_fagan_bradley_daily.csv` – sidereal longitudes (`lambda_sidereal_deg`) with the daily ayanāṃśa values.
- `geocentric_*_sign_ingresses.csv` – tropical and sidereal sign-change timestamps.
- `heliocentric_daily.csv`, `barycentric_daily.csv` – alternative reference frames.

### Swiss Ephemeris `.se1`
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

   a. If on **Mac** and not installed, install homebrew by opening the Terminal app and inputting:

   ```zsh
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
   
   
   
   b.  If on **Linux** and not installed, see below. 

2. Install the official Horizons client via Astroquery:
   ```bash
   python3 -m pip install astroquery --user
   ```
3. Query Horizons from the terminal:
   ```bash
   python3 - <<'PY'
   from astroquery.jplhorizons import Horizons
   obj = Horizons(id='DES=1004083;', location='500@399', epochs={'start':'2025-01-01', 'stop':'2025-01-10', 'step':'1d'})
   print(obj.vectors())
   PY
   ```


​	Astroquery wraps the official service and returns Pandas tables you can export to CSV.

​	Alternative: use `curl` directly (macOS/Linux ship with it):

​		

```bash
curl 'https://ssd.jpl.nasa.gov/api/horizons.api?format=json&COMMAND=\'DES=1004083;%27&MAKE_EPHEM=YES&EPHEM_TYPE=VECTORS&CENTER=\'500@399\'&REF_PLANE=ECLIPTIC&STEP_SIZE=1%20d&START_TIME=2025-01-01&STOP_TIME=2025-01-03'
```



```bash

```

### Windows
1. Install Python 3 from https://www.python.org/downloads/ (tick “Add Python to PATH”).
2. Open PowerShell and run:
   ```powershell
   py -m pip install astroquery
   ```
3. Fetch Horizons data:
   ```powershell
   py - <<'PY'
   from astroquery.jplhorizons import Horizons
   obj = Horizons(id='DES=1004083;', location='500@399', epochs={'start':'2025-01-01', 'stop':'2025-01-10', 'step':'1d'})
   print(obj.vectors())
   PY
   ```

You can also use Windows Subsystem for Linux (WSL) and follow the macOS/Linux steps.

### Classic CLI (Telnet)
JPL still offers the traditional interactive interface:
```bash
telnet horizons.jpl.nasa.gov 6775
```
Follow the prompts to enter the target (`DES=1004083;`) and output options. This is handy if you prefer the legacy workflow.



 ## Linux install of Python

  Most desktop/server Linux installs ship with a Python interpreter because the OS (and many
  tools) rely on it, but the default version may be older than 3.10. When you need Python 3.10+
  explicitly, use the package manager for your distribution—or install from source/pyenv if the
  repos are behind. Below are the common CLI commands by family:

  - **Debian / Ubuntu / Linux Mint**
    - Check current version: `python3 --version`
    - Install latest repo build:
      `sudo apt update && sudo apt install python3 python3-pip`
    - If the official repos lag behind 3.10, add the deadsnakes PPA (Ubuntu-based only):
      `sudo add-apt-repository ppa:deadsnakes/ppa && sudo apt update && sudo apt install python3.10
      python3.10-venv python3.10-distutils`

  - **Fedora**
    - `sudo dnf install python3` (Fedora 35+ already includes ≥3.10)

  - **RHEL / CentOS / Alma / Rocky**
    - Enable CodeReady/PowerTools if needed, then:
      `sudo dnf install python3`
    - For older releases, use Software Collections (SCL) or EPEL modules:
      `sudo dnf module enable python:3.11 && sudo dnf install python3`

  - **openSUSE / SLES**
    - `sudo zypper install python310 python310-pip`

  - **Arch / Manjaro**
    - Arch typically tracks the newest CPython:
      `sudo pacman -S python`
    - For a specific older/newer release use pyenv or AUR packages (e.g., `python310`).

  - **Gentoo**
    - `sudo emerge --ask dev-lang/python:3.11`
    - Then select the default with `eselect python list` / `eselect python set python3.11`.

  - **Void Linux**
    - `sudo xbps-install -S python3`

  - **NixOS / Nix**
    - `nix-shell -p python311`
    - Or add `python311` to your environment configuration.

  If you’re on a distribution that doesn’t package your desired version, use one of these portable
  approaches:

  1. **pyenv**
     ```bash
     curl https://pyenv.run | bash
     exec $SHELL
     pyenv install 3.12.2
     pyenv global 3.12.2

  2. Official source

     ```bash
     sudo apt install build-essential zlib1g-dev libssl-dev libffi-dev
     wget https://www.python.org/ftp/python/3.12.2/Python-3.12.2.tgz
     tar -xzf Python-3.12.2.tgz
     cd Python-3.12.2
     ./configure --enable-optimizations
     make -j$(nproc)
     sudo make altinstall
     ```
     
     

  This installs as python3.12 without replacing system python

-----

  Even if a base system already includes Python, it’s best to install your own 3.10+ alongside the
  system interpreter so you don’t break core utilities. Use virtual environments (python3 -m venv)
  to keep project dependencies isolated.
