3I/ATLAS — Snelle import in Cartes du Ciel (SkyCharts)
=====================================================

Cartes du Ciel leest standaard MPC-kometelementen. Gebruik de meegeleverde eenregelige file (`../import-pack/3I-ATLAS/templates/stellarium/3I_ATLAS_mpc_elements.txt`) of de kopie in deze map om 3I/ATLAS toe te voegen.

### Optie A — import via de GUI
1. Start Cartes du Ciel.
2. Open **Setup → Solar system** (of `Ctrl+F3`).
3. Klik in het tabblad **Comets** op **Update** (of **Import from MPC file**).
4. Kies **File on disk** en blader naar `3I_ATLAS_mpc_1line.txt`.
5. Vink na de import **3I/ATLAS** aan en klik **OK**.

### Optie B — handmatige bewerking
1. Sluit Cartes du Ciel.
2. Maak een back-up van `comet.dat`:
   - Windows: `%LOCALAPPDATA%\Skychart\cat\comet.dat`
   - Linux: `~/.skychart/cat/comet.dat`
   - macOS: `~/Library/Application Support/skychart.cat/comet.dat`
3. Voeg de eenregelige invoer uit `3I_ATLAS_mpc_1line.txt` toe aan `comet.dat`.
4. Start het programma opnieuw en activeer **3I/ATLAS** in de kometenlijst.

De regel is gebaseerd op JPL SBDB-oplossing 27 (2025-10-10). Importeer opnieuw zodra er een nieuwe oplossing beschikbaar komt.
