NOTE (tlh): tlhIngan Hol mu'ghom wIghajbe' 'ej qaStaHvIS poH naQvam, HolwIj qumuvtaH 'Iw HIq. English content retained until translation volunteers arrive.

3I/ATLAS — Cartes du Ciel (SkyCharts) Quick Import
=================================================

Cartes du Ciel reads standard MPC comet elements. Use the supplied one-line file
(`../import-pack/3I-ATLAS/templates/stellarium/3I_ATLAS_mpc_elements.txt`) or the
copy inside this folder to add 3I/ATLAS.

### Option A — import through the GUI
1. Start Cartes du Ciel.
2. Open **Setup → Solar system** (or press `Ctrl+F3`).
3. In the **Comets** tab click **Update** (or **Import from MPC file**).
4. Choose **File on disk** and browse to `3I_ATLAS_mpc_1line.txt`.
5. After import, tick **3I/ATLAS** in the list and click **OK**.

### Option B — manual edit
1. Quit Cartes du Ciel.
2. Backup your `comet.dat`:
   - Windows: `%LOCALAPPDATA%\Skychart\cat\comet.dat`
   - Linux: `~/.skychart/cat/comet.dat`
   - macOS: `~/Library/Application Support/skychart.cat/comet.dat`
3. Append the single line from `3I_ATLAS_mpc_1line.txt` to `comet.dat`.
4. Relaunch Cartes du Ciel and enable **3I/ATLAS** in the comet list.

The line is derived from JPL SBDB solution 27 (2025-10-10). Re-import whenever a
new solution is published.
