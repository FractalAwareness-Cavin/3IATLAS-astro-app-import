# 3I/ATLAS — Importpaket (v0.2)

Dieses Paket liefert **einsatzbereite MPC-Orbitalelemente** sowie
plattformbezogene Helfer, um 3I/ATLAS in Astronomie-Software zu importieren.
Alles funktioniert offline und basiert auf JPL-SBDB-Lösung 27 (2025-10-10).

> **TL;DR**
> - **Stellarium** → importieren Sie die mitgelieferte Einzeile über *Solar System Editor → Import elements in MPC format*.
> - **KStars** → starten Sie den Helfer ohne Installation (Windows/macOS/Linux) oder fügen Sie die bereitgestellte `comets.dat`-Zeile ein.
> - **SkySafari** → verwenden Sie *Settings → Solar System → Update Orbit Data* (Plus/Pro) und behalten Sie die Einzeile als Referenz.
> - **Solar Fire** → führen Sie den `[3I_ATLAS]`-Block in `extras.dat` zusammen (vorher sichern); Hilfsskripte liegen bei.
> - **Astro Gold / TimePassages** → derzeit kein Import bewegter Objekte; siehe die Hinweise im Haupt-Repository für Workarounds mit festen Punkten.

## Inhalt

- `templates/stellarium/3I_ATLAS_mpc_elements.txt` — MPC-Einzeiler für 3I/ATLAS.
- `templates/skysafari/3I_ATLAS_mpc_1line.txt` — derselbe Einzeiler zur Archivierung/Referenz.
- `templates/kstars/3I_ATLAS_comets_dat_snippet.txt` — fertige Zeile für `comets.dat` (auch für Cartes du Ciel / WinStars nutzbar).
- `templates/solar_fire/3I_ATLAS_extras_dat_PLACEHOLDER.txt` — `[3I_ATLAS]`-Block zum Einfügen in `extras.dat` von Solar Fire.
- `tools/3i_elements_to_formats.py` — optionaler Konverter für neue MPC-Einzeiler.
- `tools/update_orbital_elements.py` — holt die neueste JPL-SBDB-Lösung und überschreibt alle Vorlagen.
- `docs/WORKFLOWS.md` — Schritt-für-Schritt-Anleitungen für Stellarium, KStars, Cartes du Ciel, WinStars, SkySafari, Solar Fire.

## Schnellstart

Bereits auf Stand? Springen Sie direkt zu `docs/WORKFLOWS.md`. Wenn JPL eine neue
Bahn veröffentlicht, aktualisieren Sie mit:
```bash
python tools/update_orbital_elements.py --dry-run  # Vorschau der neuesten Elemente
python tools/update_orbital_elements.py            # Vorlagen überschreiben
```
Falls Sie Dateien manuell ersetzen möchten, erzeugt `tools/3i_elements_to_formats.py`
die Ausschnitte für Stellarium/KStars/Solar Fire aus jedem MPC-Einzeiler.

## Hinweise

- **Solar Fire `extras.dat`**: Die Feldreihenfolge variiert je nach Version. Nutzen Sie
den Hilfetext „Format of the Orbital Elements File“, wenn Sie manuell editieren, und legen Sie stets ein Backup an.
- **SkySafari**: Es gibt keinen manuellen Datei-Import; verwenden Sie *Update Orbit Data*.
- **Astro Gold / TimePassages**: Zum Zeitpunkt der Erstellung bieten diese Programme keinen Import beweglicher Himmelskörper. Nutzen Sie feste benutzerdefinierte Punkte oder kontaktieren Sie den Anbieter.
- **Validierung**: Führen Sie `tools/verify_ephemeris.py` aus, um Stichproben aus
`apps-using-mpc-files/geocentric_mpc_ephemeris.txt` mit Live-Daten von Horizons zu vergleichen, falls Sie die Ephemeriden gegenprüfen möchten.
