# 3I/ATLAS Ephemeris Kit

Daily ephemerides for the interstellar comet **3I/ATLAS (C/2025 N1)**, generated straight from NASA/JPL Horizons and organised so astrologers can drop the body into their favorite apps. Coverage spans the comet’s passage through the heliosphere (2016‑01‑01 → 2040‑12‑31). The current build references **Horizons solution #27 (2025‑10‑10)**; rerun `tools/update_orbital_elements.py` whenever JPL posts a newer solution and you want the helpers to reflect it.

## Quick start
1. Download the release bundle that matches your app (see **End-user direct downloads** below) or clone this repository.
2. Unzip the bundle so you can see the per-app `README` inside each folder.
3. Follow the checklist in that `README` (localized copies live under `docs/localized/`) or run the helper script included for Solar Fire, KStars, and Stellarium.
4. Optional maintenance: run `python tools/update_orbital_elements.py` to pull the latest SBDB solution and `python tools/verify_ephemeris.py` to spot-check a few dates against live Horizons before distributing updates.

## Table of contents
- [Quick start](#quick-start)
- [Supported apps (moving-body import)](#supported-apps-moving-body-import)
- [Where to start?](#where-to-start)
- [End-user direct downloads](#end-user-direct-downloads)
- [Folder guide](#folder-guide)
- [Glossary](#glossary)
- [App-specific instructions](#app-specific-instructions)
  - [Stellarium (Win/macOS/Linux)](#stellarium-winmacoslinux)
  - [KStars (Win/macOS/Linux)](#kstars-winmacoslinux)
  - [Solar Fire (Windows)](#solar-fire-windows)
  - [Cartes du Ciel / SkyCharts (Win/macOS/Linux)](#cartes-du-ciel--skycharts-winmacoslinux)
  - [WinStars 3 (Win/macOS/Linux)](#winstars-3-winmacoslinux)
  - [SkySafari / SkyVoyager Plus/Pro (iOS/Android/macOS)](#skysafari--skyvoyager-pluspro-iosandroidmacos)
  - [Astro Gold (macOS/iOS/iPadOS)](#astro-gold-macosiiosipados)
  - [TimePassages Desktop (macOS/Windows)](#timepassages-desktop-macoswindows)
  - [Import pack & helper scripts](#import-pack--helper-scripts)
  - [CSV usage notes](#csv-usage-notes)
- [Horizons recipe](#horizons-recipe)
- [Regenerating the ephemerides](#regenerating-the-ephemerides)
- [Maintenance helpers](#maintenance-helpers)
- [Key milestones](#key-milestones)
- [Notes & caveats](#notes--caveats)
- [Troubleshooting](#troubleshooting)
- [Optional: installing Horizons tooling](#optional-installing-horizons-tooling)

Supported apps (moving-body import)
----------------------------------
- **Stellarium** (Win/macOS/Linux) — Solar System Editor import in MPC format.
- **KStars** (Win/macOS/Linux) — append to `comets.dat` (helpers provided).
- **Solar Fire** (Windows) — merge the `[3I_ATLAS]` block into `extras.dat`.
- **Cartes du Ciel / SkyCharts** (Win/macOS/Linux) — import the MPC one-line or append to `comet.dat`.
- **WinStars 3** (Win/macOS/Linux) — paste the MPC one-line into the object editor.
- **SkySafari / SkyVoyager Plus/Pro** (iOS/Android/macOS) — update orbit data from MPC feeds.

Apps without moving-body import hooks:
- **Astro Gold** (macOS/iOS/iPadOS) and **TimePassages** (macOS/Windows). We include fixed-point tips if you need a static reference.

If anything here feels clumsy or you run into trouble, feel free to
[email me](mailto:cavinbirdseyetarot@gmail.com) and I’ll keep polishing it.



## Where to start?

Use the folder that matches your app or download the zip files below. If you are unsure, open your software, choose *File → Import* (or similar), and note the file extensions it expects.

- `solar-fire/` – Solar Fire `extras.dat` entry and reference ephemerides.
- `apps-using-mpc-files/` – MPC-style daily ephemeris for astronomy tools that accept comet/asteroid MPC data.
- `apps-using-csv-files/` – full CSV datasets for tools that can read spreadsheets or plain data tables.
- `developer/` – Horizons JSON dumps, regeneration scripts, vendored `pyswisseph`, and the Swiss Ephemeris helper.
- `Time-Passages-Astro-Gold/` – explanation of why Astro Gold and TimePassages currently cannot import new moving bodies, plus tips for their fixed custom points.

#### End-user direct downloads
- [Solar Fire merge helper (Windows)](https://github.com/FractalAwareness-Cavin/3IATLAS-astro-app-import/releases/download/v1.0.0/SolarFire_merge-helper_Windows.zip)
- [KStars quick append bundle (Win/macOS/Linux)](https://github.com/FractalAwareness-Cavin/3IATLAS-astro-app-import/releases/download/v1.0.0/KStars_quick-append_Win-Mac-Linux.zip)
- [Stellarium quick import](https://github.com/FractalAwareness-Cavin/3IATLAS-astro-app-import/releases/download/v1.0.0/Stellarium_quick-import.zip)
- [MPC ephemeris (80-column)](https://github.com/FractalAwareness-Cavin/3IATLAS-astro-app-import/releases/download/v1.0.0/3I-ATLAS_apps_using_mpc_files.zip)
- [CSV research kit](https://github.com/FractalAwareness-Cavin/3IATLAS-astro-app-import/releases/download/v1.0.0/3I-ATLAS_apps_using_csv_files.zip)

Each zip mirrors the matching folder and includes a `README.txt` with the
specific steps—unzip before running the helper scripts or copying files.

## Folder guide

- **solar-fire/** – Solar Fire extras (`extras.dat`) plus reference ephemerides for cross-checking.
- **apps-using-mpc-files/** – `geocentric_mpc_ephemeris.txt` in MPC 80-column format (daily UT 0h, J2000 RA/Dec, Δ, r, elongation, phase angle).
- **apps-using-csv-files/** – heliocentric/geocentric/barycentric CSV vectors, tropical & sidereal longitudes, sign-ingress summaries.
- **developer/** – raw Horizons outputs, regeneration scripts, vendored `pyswisseph`, and `build_swisseph.sh`.
- **tools/** – cross-platform helper launchers plus `update_orbital_elements.py` (refresh SBDB solution) and `verify_ephemeris.py` (Horizons spot check).
- **Time-Passages-Astro-Gold/** – limitations and fixed-point tips for apps that cannot yet import moving bodies.
- **import-pack/3I-ATLAS/** – optional templates, advanced documentation, and a converter script for Stellarium, KStars, and Solar Fire power users.
- **docs/localized/** – translated documentation (Czech, Dutch, French, German, Greek, Italian, Polish, Russian, Spanish, Klingon placeholder) mirroring the English structure.

## Glossary
- **TDB** – Barycentric Dynamical Time. Horizons generates these tables at TDB 00:00 for stability across the solar system.
- **UT (UTC/UT1)** – Universal Time. Daily MPC and CSV rows are stamped at **UT 0h**; confirm your app uses UTC if day boundaries look off.
- **Delta** – Geocentric distance from Earth’s centre in astronomical units.
- **r** – Heliocentric distance from the Sun in astronomical units.
- **Elongation** – The Sun–Earth–comet angle; larger elongations make the comet easier to separate from the Sun in the sky.
- **Phase angle** – The Sun–comet–Earth angle; higher values correspond to thinner crescents and fainter apparent magnitudes.
- **J2000** – The mean equator and equinox of J2000.0 used for right ascension/declination columns in the MPC tables.

## App-specific instructions

### Stellarium (Win/macOS/Linux)
1. Press `F2`, open **Plugins → Solar System Editor**, enable **Load at startup**, and click **Configure** (restart Stellarium if you just turned it on).
2. After restart choose **Solar System Editor → Configure → Solar System → Import orbital elements in MPC format → File**.
3. Select `import-pack/3I-ATLAS/templates/stellarium/3I_ATLAS_mpc_elements.txt` (or the same file inside the release ZIP).
4. Leave **Object type** as *Comet*, set **Object name** to `3I/ATLAS`, and click **Add objects**.
5. Use `F3` (search) to confirm `3I/ATLAS` now resolves; toggle it on in the Solar System list if required.

### KStars (Win/macOS/Linux)
1. Extract the helper bundle `KStars_quick-append_Win-Mac-Linux.zip` (or open `tools/kstars/` in this repo) and run the script that matches your OS:
   - Windows: `KStars_Append_3I-DRYRUN.bat`, then `…-APPLY.bat`.
   - macOS: double-click `KStars_Append_3I.command`. If Gatekeeper warns “Apple could not verify…”, go to **System Settings → Privacy & Security**, set **Allow applications downloaded from** to *App Store & identified developers*, launch the script once (click **Done** in the warning), then press **Open Anyway** in Privacy & Security and relaunch.
   - Linux: `bash KStars_Append_3I.sh`.
   The helper starts in dry-run mode, shows the exact line it will append, and asks `Apply changes? (y/N)`. Type `y` and press **Enter** to proceed; you should see messages like `[OK] Backup created at …` and `[OK] Appended 3I/ATLAS…`. If you close the window without answering, no changes are made.
2. Each helper backs up `comets.dat` before appending the new line. If your KStars install uses a different path (for example `~/Library/Application Support/kstars/comets.dat` on some macOS builds), rerun the script with `--target "full/path/to/comets.dat"`.
3. Manual alternative: append `apps-using-mpc-files/kstars/3I_ATLAS_comets_dat_line.txt` to your `comets.dat` (default paths: `~/.local/share/kstars/` on Linux, `%LOCALAPPDATA%\kstars\` on Windows, `~/Library/Application Support/kstars/` on macOS).
4. Quit KStars completely, relaunch it, then open **Tools → Solar System…**:
   - Click the **Comets** tab/button on the left.
   - Tick **Show comets** and drag the magnitude limit slider high enough (e.g. 20) so faint objects are visible.
   - Use the filter box above the list to search for `3I/ATLAS` (or `C/2025 N1 (ATLAS)`), tick the checkbox, then press **OK**.
   - You can now locate the comet with **Find (Ctrl/⌘+F)** or open **Tools → Solar System → Solar System Viewer** to inspect its position.

### Solar Fire (Windows)

> [!WARNING]
> Always keep a backup of `extras.dat` before merging new bodies. The helper scripts ship with the release bundle and create timestamped copies automatically.

1. Run `tools/solarfire/SF_Merge_3I-DRYRUN.bat` to preview, then `…-APPLY.bat` to merge the `[3I_ATLAS]` block safely.
2. Manual workflow: copy the block from `import-pack/3I-ATLAS/templates/solar_fire/3I_ATLAS_extras_dat_PLACEHOLDER.txt` into `Documents\Solar Fire User Files\Points & Colors\extras.dat`, preserving any existing custom entries.
3. Launch Solar Fire, open **File → File Types…**, and ensure **Extra Bodies** points at the updated file.
4. In your chart point selection dialog, expand **Other Bodies / Extra Bodies** and enable `3I/ATLAS`.
5. The `.txt` ephemerides under `solar-fire/` are reference tables only—Solar Fire still reads the orbital elements from `extras.dat`.

### Cartes du Ciel / SkyCharts (Win/macOS/Linux)
1. Start the program and open **Setup → Solar system** (`Ctrl+F3`).
2. On the **Comets** tab choose **Update → Import from MPC file**.
3. Select `apps-using-mpc-files/cartes-du-ciel/3I_ATLAS_mpc_1line.txt` (or the copy in the release ZIP) and confirm.
4. Tick **3I/ATLAS** in the list, click **OK**, and the comet is ready for use.
5. Manual option: append the same line to your `comet.dat` (default paths: `%LOCALAPPDATA%\Skychart\cat\` on Windows, `~/.skychart/cat/` on Linux, `~/Library/Application Support/skychart.cat/` on macOS).

### WinStars 3 (Win/macOS/Linux)
1. Open **Preferences → Solar system → Import orbital elements** (or **Add object**).
2. Choose **MPC single line**, paste the contents of `apps-using-mpc-files/winstars/3I_ATLAS_mpc_1line.txt`, and save.
3. Confirm that `3I/ATLAS` is enabled in the object list; restart if the comet catalogue was cached.
4. Power users can append the same line to the WinStars comet database (`%APPDATA%\WinStars3\databases\comets.txt` on Windows, `~/.config/WinStars3/databases/comets.txt` on Linux).

### SkySafari / SkyVoyager Plus/Pro (iOS/Android/macOS)
1. Copy `import-pack/3I-ATLAS/templates/skysafari/3I_ATLAS_mpc_1line.txt` into a note or text editor you can open on the device.
2. In SkySafari go to **Settings → Solar System → Solar System Data → Import Comet Data** (older builds: **Update Orbit Data → Custom Comet/Asteroid**).
3. Paste the MPC line, ensure the name reads `3I/ATLAS`, and confirm.
4. Search for `3I/ATLAS` to add it to observing lists. Re-run the import whenever you update the orbital solution.

### Astro Gold (macOS/iOS/iPadOS)
Astro Gold currently exposes only the vendor-supplied “Extra Points” catalogue. There is no supported workflow to import third-party orbital elements for a new moving body. You can create fixed custom points for snapshot coordinates (see `Time-Passages-Astro-Gold/README.txt` for a walkthrough) or contact Esoteric Technologies to request native support.

### TimePassages Desktop (macOS/Windows)
TimePassages also limits users to the built-in catalogues. Use **Edit → Chart Points… → Custom Points** to record a fixed longitude/latitude for a chosen epoch, and update manually when you need a new snapshot. Refer to `Time-Passages-Astro-Gold/README.txt` for detailed steps and vendor contact links.

### Import pack & helper scripts
If you grabbed the release bundles listed above, you already have the platform-specific helpers. The raw files live in `import-pack/3I-ATLAS/`:

- `Stellarium_quick-import.zip` — MPC one-line plus README.
- `KStars_quick-append_Win-Mac-Linux.zip` — cross-platform scripts that back up and append the `comets.dat` entry.
- `SolarFire_merge-helper_Windows.zip` — helper that backs up `extras.dat` and merges the `[3I_ATLAS]` block.

### CSV usage notes
`apps-using-csv-files/` contains the raw Horizons vectors for spreadsheets, notebooks, or custom tooling. Longitudes are in degrees, distances in AU, velocities in km/s. Sidereal tables include the daily ayanāṃśa (`ayanamsa_deg`).

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

### Maintenance helpers
- `tools/update_orbital_elements.py` — fetches the latest JPL SBDB orbital solution and refreshes all 1-line templates, KStars snippets, and Solar Fire `[3I_ATLAS]` blocks in-place.
- `tools/verify_ephemeris.py` — compares selected dates from `geocentric_mpc_ephemeris.txt` against live Horizons data to sanity-check the ephemeris.

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

## Troubleshooting
- **I imported the file but can’t find 3I/ATLAS.** Most apps cache solar-system data—restart the program, re-open its “Extra Bodies” or plugin dialog, and confirm the object name is spelled `3I/ATLAS`.
- **Daily positions look shifted.** The MPC file is stamped at **UT 0h**; switch your app to UTC/UT for daily cadences or offset by your timezone if it assumes local midnight.
- **Solar Fire still shows the old list.** Double-check that you merged into the correct `extras.dat` path (usually `Documents\Solar Fire User Files\Points & Colors\extras.dat`) or re-run the helper with the `...-APPLY` script.
- **Need to double-check the data.** `python tools/verify_ephemeris.py` spot-checks daily positions against live Horizons; rerun `python tools/update_orbital_elements.py` if JPL publishes a newer orbital solution.

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
