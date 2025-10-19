3I/ATLAS — Schneller Import für Cartes du Ciel (SkyCharts)
=========================================================

Cartes du Ciel liest standardisierte MPC-Kometenelemente. Nutzen Sie den bereitgestellten Einzeiler (`../import-pack/3I-ATLAS/templates/stellarium/3I_ATLAS_mpc_elements.txt`) oder die Kopie in diesem Ordner.

### Option A — Import über die Oberfläche
1. Cartes du Ciel starten.
2. **Setup → Solar system** öffnen (oder `Ctrl+F3`).
3. Im Reiter **Comets** auf **Update** (bzw. **Import from MPC file**) klicken.
4. **File on disk** wählen und `3I_ATLAS_mpc_1line.txt` angeben.
5. Nach dem Import **3I/ATLAS** markieren und mit **OK** bestätigen.

### Option B — manuelles Editieren
1. Cartes du Ciel schließen.
2. `comet.dat` sichern:
   - Windows: `%LOCALAPPDATA%\Skychart\cat\comet.dat`
   - Linux: `~/.skychart/cat/comet.dat`
   - macOS: `~/Library/Application Support/skychart.cat/comet.dat`
3. Den Einzeiler aus `3I_ATLAS_mpc_1line.txt` an `comet.dat` anhängen.
4. Programm neu starten und **3I/ATLAS** in der Kometenliste aktivieren.

Der Einzeiler basiert auf JPL-SBDB-Lösung 27 (2025-10-10). Importieren Sie die Daten erneut, wenn eine neue Lösung erscheint.
