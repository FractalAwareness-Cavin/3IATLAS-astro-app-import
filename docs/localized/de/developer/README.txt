ENTWICKLER-TOOLKIT
==================

Dieser Ordner enthält alles, was benötigt wird, um das Ephemeridenpaket
von Grund auf neu zu erzeugen.

Inhalt
------
- `raw/` – JSON-Antworten, die über die NASA/JPL-Horizons-API abgerufen wurden.
- `scripts/generate_ephemeris.py` – Python-Skript, das die CSV-Dateien,
  Solar-Fire-Textdateien, MPC-Ausgabe und Sign-Ingress-Zusammenfassungen neu erstellt.
- `scripts/build_swisseph.sh` – Helfer, der CSV-Tabellen in Swiss-Ephemeris-`.se1`-Binärdateien
  umwandelt (benötigt `mksweph`).
- `vendor/` – mitgeliefertes `pyswisseph`-Modul, damit siderische Ausgaben ohne zusätzliche
  Installation funktionieren.

Neu erzeugen
------------
```
cd developer/scripts
python3 generate_ephemeris.py
```
Das Skript fragt Horizons erneut ab (Internet erforderlich) und aktualisiert die
Ordner im Repository-Stamm.

Swiss-Ephemeris-Binärdateien
----------------------------
Wenn Sie über das proprietäre Tool `mksweph` verfügen:
```
cd developer/scripts
bash build_swisseph.sh
```
Die `.se1`-Dateien werden nach `../swisseph/` exportiert.

Passen Sie das Skript nach Bedarf an (Kadenz, Koordinatensysteme, Zentralkörper);
die Roh-JSONs liefern eine Rückverfolgbarkeit zu Horizons.

Ausführliche Hinweise – inklusive SBDB-Updater und Verifikationshelfer –
finden Sie in `scripts/README.md`.
