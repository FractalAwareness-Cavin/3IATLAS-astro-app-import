3I/ATLAS – GUIDE D'IMPORT MPC
=============================

`geocentric_mpc_ephemeris.txt` fournit l'éphéméride quotidienne au format MPC (UT 0h, RA/Dec J2000, Δ, r, élongation, phase). Utilisez-la partout où votre logiciel accepte les comètes en format 80 colonnes. Les archives prêtes à l'emploi sont disponibles dans les téléchargements de release (voir `README.md` à la racine) et dans `apps-using-mpc-files/`.

Archives de release
-------------------
- `Stellarium_quick-import.zip` : importe le fichier MPC mono-objet via le plugin Solar System Editor.
- `KStars_quick-append_Win-Mac-Linux.zip` : assistants aperçu/application pour `comets.dat` sur chaque plateforme.
- `3I-ATLAS_apps_using_mpc_files.zip` : contient ce dossier complet, y compris les modèles une ligne pour Cartes du Ciel et WinStars.

Stellarium (Win/macOS/Linux)
----------------------------
1. Décompressez `Stellarium_quick-import.zip` ou copiez `geocentric_mpc_ephemeris.txt` dans un emplacement accessible.
2. Dans Stellarium, appuyez sur `F2`, ouvrez **Plugins → Solar System Editor**, cochez **Load at startup**, puis cliquez sur **Configure**. Redémarrez si vous venez d'activer le plugin.
3. Après redémarrage, ouvrez **Solar System Editor → Solar System** et cliquez sur **Import orbital elements in MPC format**.
4. Choisissez **Select file**, pointez vers `geocentric_mpc_ephemeris.txt` (ou la ligne unique fournie), définissez **Object name** sur `3I/ATLAS` et laissez **Object type** sur *Comet*.
5. Cliquez sur **Add objects**, fermez les boîtes de dialogue et utilisez la recherche (`F3`) pour vérifier que `3I/ATLAS` est disponible.

KStars (Win/macOS/Linux)
------------------------
1. Décompressez `KStars_quick-append_Win-Mac-Linux.zip` et lancez le script correspondant (`*.bat`, `*.command`, `*.sh` ou `*.ps1`). Commencez par l'assistant DRYRUN ; si l'aperçu est correct, exécutez l'APPLY pour ajouter la comète à `comets.dat`.
2. Alternative manuelle : **Settings → Configure KStars → Solar System** (anciennes versions : **Data → Solar System Updates**). Dans l'onglet **Comets** cliquez sur **Import**, sélectionnez `geocentric_mpc_ephemeris.txt` et validez.
3. Redémarrez KStars si demandé, puis recherchez `3I/ATLAS` ou ouvrez le visualiseur du système solaire pour confirmer l'activation.

Cartes du Ciel / SkyCharts
--------------------------
1. Copiez `apps-using-mpc-files/cartes-du-ciel/3I_ATLAS_mpc_1line.txt` (également dans l'archive release).
2. Lancez Cartes du Ciel et ouvrez **Setup → Solar system** (`Ctrl+F3`).
3. Dans l'onglet **Comets**, choisissez **Update → Import from MPC file**, sélectionnez `3I_ATLAS_mpc_1line.txt` et confirmez.
4. Cochez **3I/ATLAS** dans la liste et validez. La comète apparaît désormais dans les recherches et les cartes.
5. Vous préférez éditer à la main ? Ajoutez la même ligne à `comet.dat` (voir le README dédié pour les chemins précis).

WinStars 3 (Win/macOS/Linux)
----------------------------
1. Gardez sous la main `apps-using-mpc-files/winstars/3I_ATLAS_mpc_1line.txt` ou extrayez l'archive MPC.
2. Dans WinStars ouvrez **Preferences → Solar system → Import orbital elements** (ou **Add object**).
3. Sélectionnez l'option **MPC single line**, collez le contenu du fichier et enregistrez.
4. Vérifiez que `3I/ATLAS` est activé dans la liste des objets affichés ; redémarrez si le cache du catalogue était ouvert.

SkySafari / SkyVoyager Plus/Pro (iOS/Android/macOS)
---------------------------------------------------
1. Copiez la ligne unique (`3I_ATLAS_mpc_1line.txt`) dans un éditeur accessible depuis l'appareil.
2. Dans SkySafari ouvrez **Settings → Solar System → Solar System Data** puis **Import Comet Data** (anciennes versions : **Update Orbit Data → Custom Comet/Asteroid**).
3. Collez la ligne MPC, confirmez que le nom est `3I/ATLAS` et validez.
4. Recherchez `3I/ATLAS` et ajoutez-la à vos listes d'observation si besoin.
5. L'application actualise périodiquement les flux MPC ; répétez l'import après chaque mise à jour d'orbite.

Autres logiciels compatibles MPC
--------------------------------
1. Copiez `geocentric_mpc_ephemeris.txt` ou la ligne unique adaptée à votre programme.
2. Utilisez la fonction d'import comète/astéroïde du logiciel, sélectionnez le fichier et nommez l'objet `3I/ATLAS`.
3. Redémarrez l'application si elle met en cache le système solaire et vérifiez que le corps est activé.

Maintenez les fichiers une ligne à jour via `python tools/update_orbital_elements.py` dès que le JPL publie une nouvelle solution SBDB, et vérifiez ponctuellement les positions avec `python tools/verify_ephemeris.py` pour plus de confiance.
