# 3I/ATLAS-Ephemeridenkit

Tägliche Ephemeriden für den interstellaren Kometen **3I/ATLAS (C/2025 N1)**, direkt aus NASA/JPL Horizons erzeugt und so organisiert, dass Astrolog:innen den Körper in ihre Lieblingssoftware einbinden können. Die Daten decken den gesamten Durchflug durch die Heliosphäre ab (2016‑01‑01 → 2040‑12‑31). Diese Ausgabe basiert auf **Horizons-Lösung Nr. 27 (2025‑10‑10)**; führen Sie `tools/update_orbital_elements.py` aus, sobald JPL eine neuere Lösung veröffentlicht und Sie die Hilfsdateien aktualisieren möchten.

## Schnellstart
1. Laden Sie das Archiv herunter, das zu Ihrer Anwendung passt (siehe **Direkte Downloads** unten), oder klonen Sie das Repository.
2. Entpacken Sie das Archiv, um den jeweiligen `README` im Zielordner zu sehen.
3. Befolgen Sie die Checkliste im `README` oder führen Sie die mitgelieferten Helper-Skripte für Solar Fire, KStars und Stellarium aus.
4. Optional: `python tools/update_orbital_elements.py` lädt die neueste SBDB-Lösung, `python tools/verify_ephemeris.py` vergleicht Stichproben mit live Horizons, bevor Sie neue Pakete verteilen.

## Inhaltsverzeichnis
- [Schnellstart](#schnellstart)
- [Unterstützte Apps (Import beweglicher Körper)](#unterstützte-apps-import-beweglicher-körper)
- [Wo beginne ich?](#wo-beginne-ich)
- [Direkte Downloads](#direkte-downloads)
- [Ordnerübersicht](#ordnerübersicht)
- [Glossar](#glossar)
- [Anweisungen pro App](#anweisungen-pro-app)
  - [Importpaket & Helferskripte](#importpaket--helferskripte)
  - [Status Astro Gold](#status-astro-gold)
  - [Solar Fire (Windows)](#solarfire-instructions-windows)
  - [Import im MPC-Format](#import-im-mpc-format)
  - [Status Astro Gold & TimePassages](#status-astro-gold--timepassages)
  - [CSV-Hinweise](#csv-hinweise)
- [Horizons-Rezept](#horizons-rezept)
- [Ephemeriden neu erzeugen](#ephemeriden-neu-erzeugen)
- [Wartungsskripte](#wartungsskripte)
- [Wichtige Meilensteine](#wichtige-meilensteine)
- [Notizen & Hinweise](#notizen--hinweise)
- [Troubleshooting](#troubleshooting)
- [Optional: Horizons-Tools installieren](#optional-horizons-tools-installieren)

Unterstützte Apps (Import beweglicher Körper)
--------------------------------------------
- **Stellarium** (Win/macOS/Linux) – Solar-System-Editor, Import im MPC-Format.
- **KStars** (Win/macOS/Linux) – `comets.dat` erweitern (Helper inklusive).
- **Solar Fire** (Windows) – `[3I_ATLAS]`-Block in `extras.dat` mergen.
- **Cartes du Ciel / SkyCharts** (Win/macOS/Linux) – MPC-Import oder `comet.dat` ergänzen.
- **WinStars 3** (Win/macOS/Linux) – MPC-Einzeiler in den Objektseditor einfügen.
- **SkySafari / SkyVoyager Plus/Pro** (iOS/Android/macOS) – Orbitdaten über MPC-Feeds aktualisieren.

Ohne Import-Hooks:
- **Astro Gold** (macOS/iOS/iPadOS) und **TimePassages** (macOS/Windows). Nutzen Sie die Hinweise zu festen Punkten, wenn Sie nur eine Referenz benötigen.

Fragen oder Probleme? Schreiben Sie an [cavinbirdseyetarot@gmail.com](mailto:cavinbirdseyetarot@gmail.com); Feedback fließt in die Doku ein.



## Wo beginne ich?

Wählen Sie den Ordner, der zu Ihrer Software passt, oder laden Sie eines der Zips. Falls unklar, prüfen Sie im Programm *Datei → Importieren* (o. ä.), welche Formate unterstützt werden.

- `solar-fire/` – `extras.dat`-Eintrag für Solar Fire plus Referenzephemeriden.
- `apps-using-mpc-files/` – `geocentric_mpc_ephemeris.txt` im MPC-80-Spalten-Format (tägl. UT 0h, J2000 RA/Dec, Δ, r, Elongation, Phase).
- `apps-using-csv-files/` – heliogeozentrische/baryzentrische CSV-Vektoren, Zeichenwechsel, Latituden.
- `developer/` – Horizons-JSONs, Regenerationsskripte, vendortes `pyswisseph`, Swiss-Ephemeris-Helfer.
- `Time-Passages-Astro-Gold/` – aktuelle Einschränkungen und fixe-Punkt-Workarounds.

#### Direkte Downloads
- [Solar-Fire-Merge-Helfer (Windows)](https://github.com/FractalAwareness-Cavin/3IATLAS-astro-app-import/releases/download/v1.0.0/SolarFire_merge-helper_Windows.zip)
- [KStars-Schnellanhang (Win/macOS/Linux)](https://github.com/FractalAwareness-Cavin/3IATLAS-astro-app-import/releases/download/v1.0.0/KStars_quick-append_Win-Mac-Linux.zip)
- [Stellarium-Schnellimport](https://github.com/FractalAwareness-Cavin/3IATLAS-astro-app-import/releases/download/v1.0.0/Stellarium_quick-import.zip)
- [MPC-Ephemeris (80 Spalten)](https://github.com/FractalAwareness-Cavin/3IATLAS-astro-app-import/releases/download/v1.0.0/3I-ATLAS_apps_using_mpc_files.zip)
- [CSV-Forschungsset](https://github.com/FractalAwareness-Cavin/3IATLAS-astro-app-import/releases/download/v1.0.0/3I-ATLAS_apps_using_csv_files.zip)

Jedes Zip spiegelt den passenden Ordner und enthält ein `README.txt` mit konkreten Schritten—entpacken, bevor Sie Skripte ausführen oder Dateien kopieren.

## Ordnerübersicht

- **solar-fire/** – Zusatzdaten für Solar Fire (`extras.dat`) plus Referenzwerte.
- **apps-using-mpc-files/** – tägliche MPC-Ephemeriden, Einzeiler, App-spezifische Hinweise.
- **apps-using-csv-files/** – CSV-Tabellen (helios, geos, bary), Zeichenwechsel, Statistiken.
- **developer/** – Skripte, vendortes `pyswisseph`, Rohdaten, Swiss-Ephemeris-Ausgabe.
- **Time-Passages-Astro-Gold/** – Workarounds für Programme ohne Import.
- **import-pack/** – kompaktes Bundle mit Templates, Skripten, Docs für Distribution.

## Glossar

- **MPC 80 Spalten**: klassisches Minor-Planet-Center-Format.
- **Horizons SBDB**: Small-Body-Datenbank der NASA/JPL.
- **Elongation**: Sonnenwinkel vom Objekt aus Erdperspektive.
- **Δ (delta)**: geozentrische Distanz.
- **r**: heliozentrische Distanz.
- **UT**: Universal Time / UTC.

## Anweisungen pro App

### Importpaket & Helferskripte

Details in `import-pack/3I-ATLAS/README.md` (Templates, Skripte, Updateprozess).

### Status Astro Gold

Kein Body-Import – siehe `Time-Passages-Astro-Gold/` für feste Punkte.

### SolarFire instructions Windows

`solar-fire/README.txt` erklärt das Mergen von `[3I_ATLAS]` in `extras.dat`. Helper unter `tools/solarfire/` bieten Dry-Run/Apply.

### Import im MPC-Format

Unter `apps-using-mpc-files/` finden Sie pro App einen `README` plus MPC-Dateien.

### Status Astro Gold & TimePassages

Keine dynamischen Imports; nutzen Sie feste Punkte je Datum.

### CSV-Hinweise

`apps-using-csv-files/README.txt` beschreibt Spalten, Einheiten, Einsatz in Tabellen, Notebooks oder Skripten. Sidereal? Ziehen Sie Ihre Ayanāṃśa von der tropischen Länge ab.

## Horizons-Rezept

`developer/raw/` enthält JSON-Ausgaben, erzeugt mit:

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

Passen Sie Parameter an (Zeitraum, Beobachter), aktualisieren Sie die JSONs, bevor Sie Skripte erneut ausführen.

## Ephemeriden neu erzeugen

### `developer/scripts/generate_ephemeris.py`

- Liest die JSON-Vektoren und generiert:
  - CSV-Tabellen (`apps-using-csv-files/`)
  - Solar-Fire-Tabellen (`solar-fire/`)
  - MPC-Ephemeriden (`apps-using-mpc-files/geocentric_mpc_ephemeris.txt`)
  - Zeichenwechsel-Summaries.
- Erstellt Zielordner bei Bedarf.

```
cd developer/scripts
python3 generate_ephemeris.py
```

### `developer/scripts/build_swisseph.sh`

- Benötigt `mksweph`.
- Wandelt CSVs in Swiss-Ephemeris-`.se1` um (`developer/swisseph/`).

```
cd developer/scripts
bash build_swisseph.sh
```

### `tools/update_orbital_elements.py`

- Holt die aktuelle SBDB-Lösung und aktualisiert MPC-Einzeiler, KStars-Snippets, Solar-Fire-Blöcke.

```
python tools/update_orbital_elements.py
```

`--dry-run` zeigt Werte ohne Dateischreibzugriff.

### `tools/verify_ephemeris.py`

- Vergleicht Stichproben aus `apps-using-mpc-files/geocentric_mpc_ephemeris.txt` mit live Horizons.

```
python tools/verify_ephemeris.py --start 2025-10-01 --days 5 --tolerance 5e-4
```

Standard: Start 2025-10-01, Dauer 5 Tage, Toleranz `5e-4` AE (~75.000 km). Bei Abweichungen endet das Skript mit Fehlercode – CI-tauglich.

## Wartungsskripte

- **`tools/3i_elements_to_formats.py`** – wandelt frische MPC-Einzeiler in Templates (Stellarium, KStars, Solar Fire).
- **`tools/kstars/`** – OS-spezifische Helper zum Sichern/Anhängen in `comets.dat`.
- **`tools/solarfire/`** – Windows-Helper für `extras.dat`.

## Wichtige Meilensteine

- 2024-10-xx – erste Horizons-Exporte und Ordnerstruktur.
- 2025-10-xx – Update auf SBDB-Lösung 27.
- 2025-10-xx – Verifikationsskripte und Importpaket ergänzt.

## Notizen & Hinweise

- **Solar Fire**: vor dem Mergen `extras.dat` sichern.
- **SkySafari**: nur über *Update Orbit Data* aktualisieren, kein Dateiimport.
- **Astro Gold / TimePassages**: keine beweglichen Imports, feste Punkte nötig.
- **Validierung**: `tools/verify_ephemeris.py` liefert schnelle Checks gegen Horizons.

## Troubleshooting

- **3I/ATLAS fehlt nach Import.** Programm neu starten, Schreibweise `3I/ATLAS` prüfen.
- **Position um einen Tag verschoben.** MPC-Datei ist auf **UT 0h** gestempelt; auf UTC umstellen oder den Zeitversatz berücksichtigen.
- **Solar Fire nutzt alte Liste.** Pfad zu `extras.dat` kontrollieren (Version-spezifische Benutzerordner) oder APPLY-Helper erneut ausführen.
- **Daten nachprüfen.** `python tools/verify_ephemeris.py` gegen live Horizons laufen lassen.

Viel Erfolg beim Beobachten von 3I/ATLAS!

## Optional: Horizons-Tools installieren

Nicht nötig für dieses Kit, aber falls Sie selbst Ephemeriden ziehen möchten:

### macOS / Linux
1. `python3 --version` (>=3.10) prüfen.
2. Astroquery installieren:
   ```bash
   python3 -m pip install astroquery --user
   ```
3. Horizons abfragen:
   ```bash
   python3 - <<'PY'
   from astroquery.jplhorizons import Horizons
   obj = Horizons(id='DES=1004083;', location='500@399', epochs={'start':'2025-01-01', 'stop':'2025-01-10', 'step':'1d'})
   print(obj.vectors())
   PY
   ```

Alternative:

```bash
curl "https://ssd.jpl.nasa.gov/api/horizons.api?format=json&COMMAND='DES=1004083;'&MAKE_EPHEM=YES&EPHEM_TYPE=VECTORS&CENTER='500@399'&REF_PLANE=ECLIPTIC&STEP_SIZE=1%20d&START_TIME=2025-01-01&STOP_TIME=2025-01-03"
```

### Windows
1. Python 3 unter https://www.python.org/downloads/ installieren (Häkchen „Add Python to PATH“).
2. PowerShell:
   ```powershell
   py -m pip install astroquery
   py - <<'PY'
   from astroquery.jplhorizons import Horizons
   obj = Horizons(id='DES=1004083;', location='500@399', epochs={'start':'2025-01-01', 'stop':'2025-01-10', 'step':'1d'})
   print(obj.vectors())
   PY
   ```
3. WSL-Nutzende folgen den macOS-/Linux-Anweisungen.

### Klassische CLI (Telnet)
```bash
telnet horizons.jpl.nasa.gov 6775
```
Aufforderungen folgen, Ziel `DES=1004083;` und Ausgabeoptionen setzen.

### Python 3.10+ unter Linux installieren

Verwenden Sie die Paketverwaltung (apt, dnf, zypper, pacman …). Falls nötig, pyenv oder Quellenbau. Eigene Python-Installation plus virtuelle Umgebungen (`python3 -m venv`) empfiehlt sich, um Abhängigkeiten zu isolieren.
