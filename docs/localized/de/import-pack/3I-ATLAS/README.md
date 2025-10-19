# 3I/ATLAS-Importpaket

Schnellstartvorlagen, Hilfsskripte und Dokumentation, um
**3I/ATLAS (C/2025 N1)** in MPC-kompatible Astronomie-Software einzubinden.

## Inhalt
- `docs/INSTALL_3I-ATLAS.md` — Überblick, Hinweise und Schnellstart (derzeit Version 0.2).
- `docs/WORKFLOWS.md` — Schritt-für-Schritt-Anleitungen für Stellarium, KStars,
  SkySafari, Solar Fire sowie Hinweise zu nicht unterstützten Anwendungen.
- `templates/` — sofort nutzbare MPC-Einzeiler, KStars-`comets.dat`-Eintrag
  und Solar-Fire-Block `[3I_ATLAS]` (alle basieren auf JPL-SBDB-Lösung 27).
- `tools/3i_elements_to_formats.py` — optionaler Konverter: Fügen Sie einen neueren
  MPC-Einzeiler ein und die Vorlagen werden automatisch neu erzeugt.
- `tools/kstars/` — Windows/macOS/Linux-Helfer, die die KStars-Zeile sichern
  und anhängen.
- `tools/solarfire/` — Windows-Helfer, die den `extras.dat`-Block für 3I/ATLAS
  sichern und zusammenführen.

## Anwendungsschnappschuss
- Stellarium: Importieren Sie die bereitgestellte Zeile über **Solar System Editor → Import elements in MPC format → File**.
- KStars: Starten Sie das passende Skript für Ihr Betriebssystem oder fügen Sie den bereitgestellten `comets.dat`-Eintrag manuell hinzu.
- SkySafari: Verwenden Sie **Settings → Solar System → Update Orbit Data** (Plus/Pro-Versionen).  
- Solar Fire: Zusammenführen des `[3I_ATLAS]`-Blocks in `extras.dat` (zuvor sichern).  
- Astro Gold / TimePassages: Derzeit kein Import bewegter Himmelskörper; siehe Repository-Hinweise für feste benutzerdefinierte Punkte.

Aktualisieren Sie die Vorlagen mit dem Konverter-Skript, sobald eine neue Orbitallösung erscheint.
