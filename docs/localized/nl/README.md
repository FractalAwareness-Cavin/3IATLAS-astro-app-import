# 3I/ATLAS-ephemeridenkit

Dagelijkse efemeriden voor de interstellaire komeet **3I/ATLAS (C/2025 N1)**, rechtstreeks uit NASA/JPL Horizons en zo opgebouwd dat astrologen het object in hun favoriete apps kunnen inladen. Dekking: de volledige doortocht door de heliosfeer (2016‑01‑01 → 2040‑12‑31). Deze editie gebruikt **Horizons-oplossing 27 (2025‑10‑10)**; voer `tools/update_orbital_elements.py` uit zodra JPL nieuwe elementen publiceert en je de hulpfiles wilt bijwerken.

## Snelstart
1. Download het pakket dat past bij jouw app (zie **Directe downloads**) of clone deze repo.
2. Pak het archief uit zodat je de `README` in elke map ziet.
3. Volg de checklist of run de bijgeleverde helpers voor Solar Fire, KStars en Stellarium.
4. Optioneel onderhoud: `python tools/update_orbital_elements.py` haalt de nieuwste SBDB-oplossing op en `python tools/verify_ephemeris.py` vergelijkt sampledata met live Horizons voor je een release maakt.

## Inhoud
- [Snelstart](#snelstart)
- [Ondersteunde apps (import bewegende lichamen)](#ondersteunde-apps-import-bewegende-lichamen)
- [Waar begin ik?](#waar-begin-ik)
- [Directe downloads](#directe-downloads)
- [Mapgids](#mapgids)
- [Glossarium](#glossarium)
- [Instructies per app](#instructies-per-app)
  - [Importpakket & scripts](#importpakket--scripts)
  - [Status Astro Gold](#status-astro-gold)
  - [Solar Fire (Windows)](#solarfire-instructions-windows)
  - [Import in MPC-formaat](#import-in-mpc-formaat)
  - [Astro Gold & TimePassages](#astro-gold--timepassages)
  - [CSV-notities](#csv-notities)
- [Horizons-recept](#horizons-recept)
- [Ephemeriden regenereren](#ephemeriden-regenereren)
- [Onderhoudsscripts](#onderhoudsscripts)
- [Mijlpaalmomenten](#mijlpaalmomenten)
- [Notities & waarschuwingen](#notities--waarschuwingen)
- [Probleemoplossing](#probleemoplossing)
- [Optioneel: Horizons-tools installeren](#optioneel-horizons-tools-installeren)

Ondersteunde apps (import bewegende lichamen)
---------------------------------------------
- **Stellarium** (Win/macOS/Linux) – import via Solar System Editor, MPC-formaat.
- **KStars** (Win/macOS/Linux) – voeg toe aan `comets.dat` (helpers beschikbaar).
- **Solar Fire** (Windows) – merge `[3I_ATLAS]` in `extras.dat`.
- **Cartes du Ciel / SkyCharts** (Win/macOS/Linux) – MPC file import of `comet.dat` bewerken.
- **WinStars 3** (Win/macOS/Linux) – plak de MPC-regel in de objecteditor.
- **SkySafari / SkyVoyager Plus/Pro** (iOS/Android/macOS) – update orbitdata via MPC-feeds.

Geen importhooks:
- **Astro Gold** (macOS/iOS/iPadOS) en **TimePassages** (macOS/Windows). Gebruik de tips voor vaste punten.

Vragen? Mail [cavinbirdseyetarot@gmail.com](mailto:cavinbirdseyetarot@gmail.com).



## Waar begin ik?

Gebruik de map die bij je software hoort of download een van de zips. Onzeker? Check in je app *File → Import* welke formaten worden ondersteund.

- `solar-fire/` – `extras.dat`-blok voor Solar Fire plus referentie-efemeriden.
- `apps-using-mpc-files/` – `geocentric_mpc_ephemeris.txt` (MPC 80 kolommen, UT 0h, J2000 RA/Dec, Δ, r, elongatie, fase).
- `apps-using-csv-files/` – heliocentrische/geocentrische/barycentrische CSV’s, tekenwissels, latituden.
- `developer/` – Horizons JSON dumps, regeneratiescripts, vendored `pyswisseph`, Swiss Ephemeris-helper.
- `Time-Passages-Astro-Gold/` – uitleg beperkingen + vaste-punt-workarounds.

#### Directe downloads
- [Solar Fire merge helper (Windows)](https://github.com/FractalAwareness-Cavin/3IATLAS-astro-app-import/releases/download/v1.0.0/SolarFire_merge-helper_Windows.zip)
- [KStars quick append (Win/macOS/Linux)](https://github.com/FractalAwareness-Cavin/3IATLAS-astro-app-import/releases/download/v1.0.0/KStars_quick-append_Win-Mac-Linux.zip)
- [Stellarium quick import](https://github.com/FractalAwareness-Cavin/3IATLAS-astro-app-import/releases/download/v1.0.0/Stellarium_quick-import.zip)
- [MPC-efemeriden (80 kolommen)](https://github.com/FractalAwareness-Cavin/3IATLAS-astro-app-import/releases/download/v1.0.0/3I-ATLAS_apps_using_mpc_files.zip)
- [CSV-onderzoeksset](https://github.com/FractalAwareness-Cavin/3IATLAS-astro-app-import/releases/download/v1.0.0/3I-ATLAS_apps_using_csv_files.zip)

Elk zip weerspiegelt de betreffende map en bevat een `README.txt` met stappen. Pak uit vóór je scripts draait of bestanden kopieert.

## Mapgids

- **solar-fire/** – Solar Fire extras (`extras.dat`) en referentietabellen.
- **apps-using-mpc-files/** – volledige MPC-efemeride, eenregelige templates, app-notities.
- **apps-using-csv-files/** – CSV-vectoren, tekenwissels, latituden, snelheden.
- **developer/** – scripts, vendored `pyswisseph`, ruwe Horizons-data, Swiss-Ephemeris-tools.
- **Time-Passages-Astro-Gold/** – tips voor apps zonder import.
- **import-pack/** – compact pakket met templates, scripts, documentatie.

## Glossarium

- **MPC 80 kolommen** – klassiek Minor Planet Center-formaat.
- **Horizons SBDB** – Small-Body Database van NASA/JPL.
- **Elongatie** – hoekafstand tot de zon gezien vanaf de aarde.
- **Δ (delta)** – geocentrische afstand.
- **r** – heliocentrische afstand.
- **UT** – Universal Time / UTC.

## Instructies per app

### Importpakket & scripts

Zie `import-pack/3I-ATLAS/README.md` voor templates, helpers, updateflow.

### Status Astro Gold

Geen import van bewegende lichamen; gebruik `Time-Passages-Astro-Gold/` voor vaste punten.

### SolarFire instructions Windows

`solar-fire/README.txt` legt het mergen van `[3I_ATLAS]` in `extras.dat` uit. Helper scripts staan in `tools/solarfire/`.

### Import in MPC-formaat

Onder `apps-using-mpc-files/` vind je per app een `README` plus benodigde bestanden.

### Astro Gold & TimePassages

Momenteel geen import; werk met vaste referentiepunten per datum.

### CSV-notities

`apps-using-csv-files/README.txt` beschrijft kolommen, units en gebruik in spreadsheets, notebooks of scripts. Voor sidereale analyses trek je je ayanāṃśa van de tropische lengte af.

## Horizons-recept

`developer/raw/` bevat JSON-sessies gemaakt met:

```
COMMAND='DES=1004083;'
MAKE_EPHEM='YES'
EPHEM_TYPE='VECTORS'
CENTER='500@399'
REF_PLANE='ECLIPTIC'
REF_SYSTEM='J2000'
START_TIME='2016-01-01'
STOP_TIME='2040-12-31'
STEP_SIZE='1 d'
TABLE_TYPE='VECTORS'
```

Pas parameters aan voor andere periodes of observators en regenereer de JSON’s voorafgaand aan nieuwe runs.

## Ephemeriden regenereren

### `developer/scripts/generate_ephemeris.py`

- Leest de JSON’s en bouwt opnieuw:
  - CSV-tabellen (`apps-using-csv-files/`)
  - Solar-Fire-tabellen (`solar-fire/`)
  - MPC-efemeride (`apps-using-mpc-files/geocentric_mpc_ephemeris.txt`)
  - Tekenwisseloverzichten.
- Maakt doelmappen indien nodig.

```
cd developer/scripts
python3 generate_ephemeris.py
```

### `developer/scripts/build_swisseph.sh`

- Vereist `mksweph`.
- Converteert CSV’s naar Swiss-Ephemeris-`.se1` (`developer/swisseph/`).

```
cd developer/scripts
bash build_swisseph.sh
```

### `tools/update_orbital_elements.py`

- Haalt de nieuwste SBDB-oplossing op en werkt MPC-files, KStars-snippets en Solar-Fire-blokken bij.

```
python tools/update_orbital_elements.py
```

`--dry-run` toont waarden zonder te schrijven.

### `tools/verify_ephemeris.py`

- Vergelijkt regels uit `apps-using-mpc-files/geocentric_mpc_ephemeris.txt` met live Horizons-gegevens.

```
python tools/verify_ephemeris.py --start 2025-10-01 --days 5 --tolerance 5e-4
```

Standaard: start 2025-10-01, duur 5 dagen, tolerantie `5e-4` AE (~75.000 km). Retourneert een foutcode bij afwijkingen → geschikt voor CI.

## Onderhoudsscripts

- **`tools/3i_elements_to_formats.py`** – vormt een nieuwe MPC-eenregelige om tot templates (Stellarium, KStars, Solar Fire).
- **`tools/kstars/`** – OS-specifieke helpers voor backup/append in `comets.dat`.
- **`tools/solarfire/`** – Windowshelpers die `extras.dat` automatisch samenvoegen.

## Mijlpaalmomenten

- 2024-10-xx – eerste Horizons-export en mapstructuur.
- 2025-10-xx – update naar SBDB-oplossing 27.
- 2025-10-xx – verificatiescripts en importpakket toegevoegd.

## Notities & waarschuwingen

- **Solar Fire**: maak altijd een backup van `extras.dat` vóór merge.
- **SkySafari**: geen bestandsimport — gebruik *Update Orbit Data*.
- **Astro Gold / TimePassages**: enkel vaste punten.
- **Validatie**: `tools/verify_ephemeris.py` geeft snelle checks tegen Horizons.

## Probleemoplossing

- **3I/ATLAS ontbreekt na import.** Herstart de app, controleer spelling `3I/ATLAS`.
- **Posities verschoven.** MPC-bestand staat op **UT 0h**; werk in UTC of compenseer tijdzone.
- **Solar Fire toont oude lijst.** Controleer het juiste `extras.dat` (versiegebonden map) of run APPLY opnieuw.
- **Data dubbelchecken.** `python tools/verify_ephemeris.py` vergelijkt met live Horizons.

Veel plezier met 3I/ATLAS!

## Optioneel: Horizons-tools installeren

Niet vereist (data zijn inbegrepen), maar als je zelf wilt genereren:

### macOS / Linux
1. Zorg dat `python3 --version` ≥ 3.10.
2. Installeer Astroquery:
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

Alternatief:

```bash
curl "https://ssd.jpl.nasa.gov/api/horizons.api?format=json&COMMAND='DES=1004083;'&MAKE_EPHEM=YES&EPHEM_TYPE=VECTORS&CENTER='500@399'&REF_PLANE=ECLIPTIC&STEP_SIZE=1%20d&START_TIME=2025-01-01&STOP_TIME=2025-01-03"
```

### Windows
1. Installeer Python 3 via https://www.python.org/downloads/ (vink “Add Python to PATH” aan).
2. PowerShell:
   ```powershell
   py -m pip install astroquery
   py - <<'PY'
   from astroquery.jplhorizons import Horizons
   obj = Horizons(id='DES=1004083;', location='500@399', epochs={'start':'2025-01-01', 'stop':'2025-01-10', 'step':'1d'})
   print(obj.vectors())
   PY
   ```
3. WSL-gebruikers volgen de macOS/Linux instructies.

### Klassieke CLI (Telnet)
```bash
telnet horizons.jpl.nasa.gov 6775
```
Volg de prompts, voer `DES=1004083;` in en kies opties.

### Python 3.10+ op Linux installeren

Gebruik pakketbeheerders (apt, dnf, zypper, pacman …). Als de versie ontbreekt, gebruik pyenv of bouw uit bron. Ook wanneer er al Python aanwezig is, is een eigen installatie ≥3.10 plus virtuele omgevingen (`python3 -m venv`) aan te raden.
