# Parcours d'applications pour 3I/ATLAS

Toutes les valeurs de ce pack proviennent de la solution 27 du JPL SBDB (2025-10-10).
Mettez à jour les fichiers avec le script de conversion lorsqu'une solution plus récente est publiée.

## Stellarium (Windows/macOS/Linux)

**Accepte :** éléments de comète MPC en une ligne  
**Étapes :**
1. **Configuration → Plugins → Solar System Editor** → cochez **Load at startup** (redémarrez si nécessaire).  
2. **Solar System Editor → Configure → Solar System → Import elements in MPC format → File**.  
3. Sélectionnez `templates/stellarium/3I_ATLAS_mpc_elements.txt`.  
4. Cliquez sur **Add object(s)** et cherchez **3I/ATLAS**.

## KStars (Windows/macOS/Linux)

**Accepte :** ligne `comets.dat`  
**Assistants :**
- Windows : `tools/kstars/KStars_Append_3I-DRYRUN.bat` (aperçu), puis `…-APPLY.bat`.  
- macOS : double-cliquez sur `tools/kstars/KStars_Append_3I.command`.  
- Linux : exécutez `bash tools/kstars/KStars_Append_3I.sh`.  
Tous les assistants sauvegardent le fichier avant l'ajout.

Manuel :
1. Sauvegardez votre `comets.dat` (`~/.local/share/kstars/comets.dat` sous Linux, `%LOCALAPPDATA%\kstars\comets.dat` sous Windows, `~/Library/Application Support/kstars/comets.dat` sous macOS).  
2. Ajoutez la ligne unique située dans `templates/kstars/3I_ATLAS_comets_dat_snippet.txt`.  
3. Redémarrez KStars et recherchez **3I/ATLAS**.

## SkySafari / SkyVoyager (iOS/Android)

**Accepte :** aucun import manuel  
Utilisez *Settings → Solar System → Update Orbit Data* (niveaux Plus/Pro). Conservez
`templates/skysafari/3I_ATLAS_mpc_1line.txt` pour référence uniquement.

## Cartes du Ciel (SkyCharts)

**Accepte :** fichiers d'éléments MPC  
Suivez les instructions de `apps-using-mpc-files/cartes-du-ciel/README.txt`
(import via l'interface graphique ou ajout manuel à `comet.dat`).

## WinStars 3

**Accepte :** fichiers d'éléments MPC  
Voir `apps-using-mpc-files/winstars/README.txt` pour les étapes d'import rapide.

## Solar Fire (Windows)

**Accepte :** éléments orbitaux `extras.dat` (Other Bodies)  
**Assistants :**
- Windows : `tools/solarfire/SF_Merge_3I-DRYRUN.bat` (aperçu), puis `…-APPLY.bat` pour fusionner automatiquement `[3I_ATLAS]`.  
Les deux scripts sauvegardent `extras.dat` avec un horodatage.

Manuel :
1. Quittez Solar Fire et sauvegardez `Documents\Solar Fire User Files\Userdata\extras.dat`.  
2. Copiez ou fusionnez le bloc `[3I_ATLAS]` depuis `templates/solar_fire/3I_ATLAS_extras_dat_PLACEHOLDER.txt`.  
3. Relancez et activez **3I/ATLAS** dans **Extra Bodies** depuis la boîte de sélection des points.

## Applications sans import

Astro Gold (macOS/iOS/iPadOS) et TimePassages Desktop (macOS/Windows) exposent
uniquement les points additionnels fournis par l'éditeur. Ils n'acceptent pas
d'éphémérides pour les corps mobiles. Consultez le dossier `Time-Passages-Astro-Gold/`
pour des solutions de points fixes et des liens vers le support éditeur.
