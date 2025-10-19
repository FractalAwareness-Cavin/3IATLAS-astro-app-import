3I/ATLAS — WinStars-Schnellimport
=================================

WinStars (v3) kann MPC-Kometenelemente über den integrierten Editor einlesen.

### Methode 1 — Einzeiler einfügen
1. WinStars starten.
2. **Preferences → Solar system → Import orbital elements** (oder **Add object**) öffnen.
3. **MPC single line** wählen und den Inhalt von `3I_ATLAS_mpc_1line.txt` einfügen.
4. Bestätigen und sicherstellen, dass 3I/ATLAS in der Anzeige aktiviert ist.

### Methode 2 — Austausch der Kometendatei (fortgeschritten)
1. WinStars beenden.
2. Kometendatei sichern:
   - Windows: `%APPDATA%\WinStars3\databases\comets.txt`
   - Linux: `~/.config/WinStars3/databases/comets.txt`
3. Den Einzeiler aus `3I_ATLAS_mpc_1line.txt` an diese Datei anhängen.
4. WinStars neu starten; 3I/ATLAS erscheint in der Kometenliste.

Die Einzeilerdatei basiert auf der JPL-SBDB-Lösung 27 (2025-10-10). Aktualisieren Sie sie bei neuen Lösungen.
