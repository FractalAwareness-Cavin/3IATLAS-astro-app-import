3I/ATLAS — Import rapide Cartes du Ciel (SkyCharts)
==================================================

Cartes du Ciel lit les éléments standard MPC. Utilisez la ligne fournie (`../import-pack/3I-ATLAS/templates/stellarium/3I_ATLAS_mpc_elements.txt`) ou la copie présente ici pour ajouter 3I/ATLAS.

### Option A — import via l'interface
1. Lancez Cartes du Ciel.
2. Ouvrez **Setup → Solar system** (ou `Ctrl+F3`).
3. Dans l'onglet **Comets** cliquez sur **Update** (ou **Import from MPC file**).
4. Choisissez **File on disk** et sélectionnez `3I_ATLAS_mpc_1line.txt`.
5. Après l'import, cochez **3I/ATLAS** dans la liste et validez.

### Option B — édition manuelle
1. Fermez Cartes du Ciel.
2. Sauvegardez votre `comet.dat` :
   - Windows : `%LOCALAPPDATA%\Skychart\cat\comet.dat`
   - Linux : `~/.skychart/cat/comet.dat`
   - macOS : `~/Library/Application Support/skychart.cat/comet.dat`
3. Ajoutez la ligne unique de `3I_ATLAS_mpc_1line.txt` à `comet.dat`.
4. Relancez Cartes du Ciel et activez **3I/ATLAS** dans la liste des comètes.

La ligne repose sur la solution 27 du JPL SBDB (2025-10-10). Réimportez-la lorsqu'une nouvelle solution est publiée.
