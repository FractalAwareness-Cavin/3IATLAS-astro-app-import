# Entwickler-Skripte

Die Werkzeuge zum Regenerieren und Validieren des 3I/ATLAS-Ephemeriden-Kits befinden sich in `developer/scripts/` und `tools/`. Dieses Dokument hilft, den Datensatz zu aktualisieren oder Änderungen vor einer neuen Veröffentlichung zu prüfen.

## Voraussetzungen
- Python 3.10 oder neuer (`python3 --version` prüfen).
- Optional: virtuelles Environment (`python3 -m venv .venv && source .venv/bin/activate`), falls zusätzliche Pakete installiert werden.
- Internetzugang für den SBDB-Updater oder den Horizons-Checker.
- Optional: `mksweph`, wenn Swiss-Ephemeris-Binaries mit `build_swisseph.sh` erstellt werden sollen.

Das Repository liefert `pyswisseph` in `developer/vendor/` mit, damit siderische Ausgaben ohne weitere Installation funktionieren.

## Standard-Horizons-Rezept

Die Roh-JSONs in `developer/raw/` wurden mit NASA/JPL Horizons unter folgenden Parametern erzeugt:

```
COMMAND='DES=1004083;'
MAKE_EPHEM='YES'
EPHEM_TYPE='VECTORS'
CENTER='500@399'        # Erdzentrum
REF_PLANE='ECLIPTIC'
REF_SYSTEM='J2000'
START_TIME='2016-01-01'
STOP_TIME='2040-12-31'
STEP_SIZE='1 d'
TABLE_TYPE='VECTORS'
```

Passen Sie diese Werte an, wenn Sie andere Zeiträume oder Beobachterpositionen benötigen, und aktualisieren Sie die JSON-Dateien vor dem Neuaufbau.

## `generate_ephemeris.py`
Pfad: `developer/scripts/generate_ephemeris.py`

- Liest die JSON-Vektor-Dumps in `developer/raw/` und schreibt alle abgeleiteten Produkte neu:
  - CSV-Tabellen in `apps-using-csv-files/`
  - Solar-Fire-Textdateien in `solar-fire/`
  - MPC-Ephemeris (`apps-using-mpc-files/geocentric_mpc_ephemeris.txt`)
  - Zusammenfassungen der Zeichenwechsel.
- Lädt das mitgelieferte `pyswisseph`, um siderische Felder zu befüllen.
- Erstellt Zielverzeichnisse, wenn sie fehlen.

Verwendung:

```
cd developer/scripts
python3 generate_ephemeris.py
```

Das Skript nutzt feste Einstellungen. Für andere Zeitspannen oder Abtastraten aktualisieren Sie zunächst die JSONs (oder passen die Konstanten im Kopfbereich an).

## `build_swisseph.sh`
Pfad: `developer/scripts/build_swisseph.sh`

- Benötigt das proprietäre Tool `mksweph`.
- Wandelt die CSV-Ausgaben in Swiss-Ephemeris-`.se1`-Binaries um und legt sie in `developer/swisseph/` ab.

Verwendung:

```
cd developer/scripts
bash build_swisseph.sh
```

Der Helfer startet nicht, wenn `mksweph` nicht im `PATH` gefunden wird.

## `tools/update_orbital_elements.py`
Pfad: `tools/update_orbital_elements.py`

- Ruft die aktuelle SBDB-Orbitallösung für 3I/ATLAS ab und aktualisiert alle Einzeiler-Vorlagen:
  - MPC-One-Liner (`apps-using-mpc-files/*/3I_ATLAS_mpc_1line.txt`)
  - KStars-Snippets (`apps-using-mpc-files/kstars/` sowie Import-Pack-Vorlagen)
  - Solar-Fire-`extras.dat`-Blöcke.
- Gibt die geladenen Elemente zur Kontrolle auf stdout aus.

Verwendung (aus dem Repository-Stamm):

```
python tools/update_orbital_elements.py
```

Mit `--dry-run` lassen sich die Werte anzeigen, ohne Dateien anzufassen.

## `tools/verify_ephemeris.py`
Pfad: `tools/verify_ephemeris.py`

- Prüft Stichproben aus `apps-using-mpc-files/geocentric_mpc_ephemeris.txt` gegen Live-Daten von Horizons.
- Vergleicht die geozentrische Distanz („delta“) über einen konfigurierbaren Zeitraum und markiert Zeilen, die die Toleranz überschreiten.

Verwendung (aus dem Repository-Stamm):

```
python tools/verify_ephemeris.py --start 2025-10-01 --days 5 --tolerance 5e-4
```

Argumente:
- `--start`: Startdatum der Prüfung (Standard `2025-10-01`).
- `--days`: Anzahl aufeinanderfolgender Tage (Standard `5`).
- `--tolerance`: zulässige Differenz in Astronomischen Einheiten (Standard `5e-4`, ca. 75.000 km).

Das Skript beendet sich mit einem Fehlercode, falls eine Zeile fehlschlägt, und eignet sich damit für CI-Gates.
