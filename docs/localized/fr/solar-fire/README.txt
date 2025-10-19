3I/ATLAS POUR SOLAR FIRE (WINDOWS)
=================================

Solar Fire n'importe pas d'éphémérides pré-calculées pour les nouveaux corps ; il lit les éléments orbitaux depuis `extras.dat`. Ce dossier maintient l'entrée 3I/ATLAS alignée sur la solution 27 du JPL SBDB.

Testé sur
---------
- Solar Fire 9 : `Documents\Solar Fire 9 User Files\Points & Colors\extras.dat`
- Solar Fire 10 : `Documents\Solar Fire User Files\Points & Colors\extras.dat`
- Solar Fire 11 : `Documents\Solar Fire User Files\Points & Colors\extras.dat`

Contenu
-------
- `extras.dat` : bloc `[3I_ATLAS]` prêt à l'emploi (voir ci-dessous) avec commentaires pour les fusions manuelles.
- `geocentric_daily_solarfire.txt` et fichiers similaires : tables de référence facultatives pour vérifier les positions en dehors de Solar Fire.

Bloc exemple
------------
Collez ce bloc dans votre `extras.dat` existant ou laissez l'assistant le fusionner automatiquement :

```
[3I_ATLAS]
Name = 3I/ATLAS
Number = 0
EpochJD = 2460884.5
PerihelionDistance_AU = 1.356065571
Eccentricity = 6.137350157
Inclination_deg = 175.112857794
AscendingNode_deg = 322.152284965
ArgumentOfPerihelion_deg = 128.011608252
PerihelionTime_JD = 2460977.983535961
AbsoluteMagnitude = 12.3
SlopeParameter = 4.5
; Solar Fire ignore le demi-grand axe lorsque Tp est fourni pour les comètes.
; Cet objet est hyperbolique (e>1). Vérifiez la compatibilité avec votre version de Solar Fire.
```

Étapes d'installation
---------------------
1. Fermez Solar Fire.
2. Exécutez les scripts d'aide (`tools/solarfire/SF_Merge_3I-DRYRUN.bat`, puis `tools/solarfire/SF_Merge_3I-APPLY.bat`) **ou** sauvegardez votre `extras.dat` actuel.
3. Ouvrez le chemin correspondant à votre version (voir ci-dessus) et ajoutez le bloc. Conservez vos autres corps personnalisés.
4. Relancez Solar Fire, ouvrez **File → File Types…** et vérifiez que **Extra Bodies** pointe vers le fichier mis à jour.
5. Dans le dialogue de sélection des points, cochez `3I/ATLAS` sous **Extra Bodies / Other Bodies**.

Mini-FAQ
--------
- **3I/ATLAS n'apparaît pas après la fusion.** Vérifiez que vous avez édité le bon dossier `extras.dat` (Solar Fire garde un dossier utilisateur par version majeure) et que le corps est activé via **Extra Bodies**.
- **Le script d'aide indique "access denied".** Fermez Solar Fire avant d'exécuter le script APPLY ; la fusion ne peut pas remplacer un `extras.dat` ouvert.
- **Besoin d'éléments orbitaux plus récents.** Lancez `python tools/update_orbital_elements.py` à la racine du dépôt, puis relancez l'assistant pour remplacer le bloc par la dernière solution SBDB.
