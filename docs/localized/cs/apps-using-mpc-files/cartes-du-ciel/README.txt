3I/ATLAS — rychlý import do Cartes du Ciel (SkyCharts)
======================================================

Cartes du Ciel načítá standardní kometární prvky MPC. Použijte dodaný jednořádkový soubor (`../import-pack/3I-ATLAS/templates/stellarium/3I_ATLAS_mpc_elements.txt`) nebo kopii v této složce.

### Varianta A — import přes GUI
1. Spusťte Cartes du Ciel.
2. Otevřete **Setup → Solar system** (nebo `Ctrl+F3`).
3. Na kartě **Comets** klikněte na **Update** (popř. **Import from MPC file**).
4. Zvolte **File on disk** a vyberte `3I_ATLAS_mpc_1line.txt`.
5. Po importu zaškrtněte **3I/ATLAS** a potvrďte **OK**.

### Varianta B — ruční úprava
1. Ukončete Cartes du Ciel.
2. Zálohujte `comet.dat`:
   - Windows: `%LOCALAPPDATA%\Skychart\cat\comet.dat`
   - Linux: `~/.skychart/cat/comet.dat`
   - macOS: `~/Library/Application Support/skychart.cat/comet.dat`
3. Připojte jednořádkový záznam z `3I_ATLAS_mpc_1line.txt` do souboru `comet.dat`.
4. Restartujte program a aktivujte **3I/ATLAS** v seznamu komet.

Řádka vychází z řešení JPL SBDB 27 (2025-10-10). Po zveřejnění nového řešení proveďte import znovu.
