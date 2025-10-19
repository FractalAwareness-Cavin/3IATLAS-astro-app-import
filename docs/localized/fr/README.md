# Kit d'éphémérides 3I/ATLAS

Éphémérides quotidiennes pour la comète interstellaire **3I/ATLAS (C/2025 N1)**, générées directement depuis NASA/JPL Horizons et organisées pour que les astrologues puissent l’ajouter à leurs applications préférées. La couverture s’étend sur la traversée de l’héliosphère (2016‑01‑01 → 2040‑12‑31). Cette version se base sur la **solution Horizons n°27 (2025‑10‑10)** ; relancez `tools/update_orbital_elements.py` dès que JPL publie une solution plus récente et que vous voulez mettre à jour les fichiers auxiliaires.

## Prise en main rapide
1. Téléchargez l’archive correspondant à votre application (voir **Téléchargements directs** ci-dessous) ou clonez ce dépôt.
2. Décompressez l’archive pour accéder au `README` spécifique présent dans chaque dossier.
3. Suivez la checklist du `README` ou exécutez le script d’assistance fourni pour Solar Fire, KStars et Stellarium.
4. Entretien facultatif : lancez `python tools/update_orbital_elements.py` pour récupérer la dernière solution SBDB et `python tools/verify_ephemeris.py` pour comparer quelques dates avec Horizons avant de redistribuer des mises à jour.

## Table des matières
- [Prise en main rapide](#prise-en-main-rapide)
- [Applications compatibles (import de corps mobiles)](#applications-compatibles-import-de-corps-mobiles)
- [Par où commencer ?](#par-où-commencer-)
- [Téléchargements directs](#téléchargements-directs)
- [Guide des dossiers](#guide-des-dossiers)
- [Glossaire](#glossaire)
- [Instructions par application](#instructions-par-application)
  - [Pack d’import & scripts d’assistance](#pack-dimport--scripts-dassistance)
  - [État d’Astro Gold](#état-dastro-gold)
  - [Solar Fire (Windows)](#solarfire-instructions-windows)
  - [Import en format MPC](#import-en-format-mpc)
  - [État d’Astro Gold & TimePassages](#état-dastro-gold--timepassages)
  - [Notes sur les CSV](#notes-sur-les-csv)
- [Recette Horizons](#recette-horizons)
- [Régénérer les éphémérides](#régénérer-les-éphémérides)
- [Scripts de maintenance](#scripts-de-maintenance)
- [Étapes clés](#étapes-clés)
- [Notes & avertissements](#notes--avertissements)
- [Dépannage](#dépannage)
- [Option : installer les outils Horizons](#option--installer-les-outils-horizons)

Applications compatibles (import de corps mobiles)
-------------------------------------------------
- **Stellarium** (Win/macOS/Linux) — import via l’éditeur du système solaire au format MPC.
- **KStars** (Win/macOS/Linux) — ajout à `comets.dat` (assistants fournis).
- **Solar Fire** (Windows) — fusion du bloc `[3I_ATLAS]` dans `extras.dat`.
- **Cartes du Ciel / SkyCharts** (Win/macOS/Linux) — import MPC ou ajout à `comet.dat`.
- **WinStars 3** (Win/macOS/Linux) — collez la ligne MPC dans l’éditeur d’objets.
- **SkySafari / SkyVoyager Plus/Pro** (iOS/Android/macOS) — mise à jour des données orbitales depuis les flux MPC.

Applications sans import de corps mobiles :
- **Astro Gold** (macOS/iOS/iPadOS) et **TimePassages** (macOS/Windows). Voir les astuces pour points fixes si vous avez besoin d’une référence statique.

Si quelque chose vous semble confus ou si vous rencontrez un problème, écrivez-moi à l’adresse [cavinbirdseyetarot@gmail.com](mailto:cavinbirdseyetarot@gmail.com) et je continuerai d’améliorer la documentation.



## Par où commencer ?

Utilisez le dossier correspondant à votre application ou téléchargez les archives ci-dessous. Si vous hésitez, ouvrez votre logiciel, choisissez *Fichier → Importer* (ou équivalent) et notez les extensions prises en charge.

- `solar-fire/` – entrée `extras.dat` pour Solar Fire et éphémérides de référence.
- `apps-using-mpc-files/` – fichier MPC 80 colonnes `geocentric_mpc_ephemeris.txt` (quotidien à 0h TU, RA/Dec J2000, Δ, r, élongation, phase).
- `apps-using-csv-files/` – vecteurs CSV héliocentriques, géocentriques, barycentriques, tableaux d’entrées en signe et latitudes.
- `developer/` – exports JSON Horizons, scripts de régénération, `pyswisseph` embarqué et l’assistant Swiss Ephemeris.
- `Time-Passages-Astro-Gold/` – explication sur l’absence d’import de corps mobiles dans Astro Gold / TimePassages, plus des solutions pour points fixes.

#### Téléchargements directs
- [Assistant fusion Solar Fire (Windows)](https://github.com/FractalAwareness-Cavin/3IATLAS-astro-app-import/releases/download/v1.0.0/SolarFire_merge-helper_Windows.zip)
- [Pack d’ajout rapide KStars (Win/macOS/Linux)](https://github.com/FractalAwareness-Cavin/3IATLAS-astro-app-import/releases/download/v1.0.0/KStars_quick-append_Win-Mac-Linux.zip)
- [Import rapide Stellarium](https://github.com/FractalAwareness-Cavin/3IATLAS-astro-app-import/releases/download/v1.0.0/Stellarium_quick-import.zip)
- [Éphéméride MPC (80 colonnes)](https://github.com/FractalAwareness-Cavin/3IATLAS-astro-app-import/releases/download/v1.0.0/3I-ATLAS_apps_using_mpc_files.zip)
- [Kit de recherche CSV](https://github.com/FractalAwareness-Cavin/3IATLAS-astro-app-import/releases/download/v1.0.0/3I-ATLAS_apps_using_csv_files.zip)

Chaque archive reflète le dossier correspondant et inclut un `README.txt` avec les étapes précises—décompressez avant d’exécuter les scripts ou de copier les fichiers.

## Guide des dossiers

- **solar-fire/** – compléments Solar Fire (`extras.dat`) et éphémérides de référence pour contrôle.
- **apps-using-mpc-files/** – épheméride quotidienne MPC 80 colonnes (Δ, r, RA/Dec, élongation, phase).
- **apps-using-csv-files/** – vecteurs héliocentriques/géocentriques/barycentriques, entrées en signe, latitudes, distances, vitesses.
- **developer/** – scripts de régénération, modules vendus (`pyswisseph`), exports Horizons, outils de vérification.
- **Time-Passages-Astro-Gold/** – limites actuelles et procédures pour points fixes.
- **import-pack/** – mini bundle contenant scripts, modèles et documentation ; pratique si vous distribuez une version prête à l’emploi.

## Glossaire

- **MPC 80 colonnes** : format classique du Minor Planet Center pour les comètes/astéroïdes.
- **Horizons SBDB** : Small-Body DataBase de la NASA/JPL, source des éléments orbitaux.
- **Élongation** : distance angulaire Soleil-objet vue depuis la Terre.
- **Δ (delta)** : distance géocentrique.
- **r** : distance héliocentrique.
- **UT** : Temps universel (UTC).

## Instructions par application

### Pack d’import & scripts d’assistance

Consultez `import-pack/3I-ATLAS/README.md`. Il répertorie les modèles, scripts et mises à jour.

### État d’Astro Gold

Pas d’import de corps mobiles pour l’instant ; reportez-vous à `Time-Passages-Astro-Gold/` pour les points fixes.

### SolarFire instructions Windows

Voir `solar-fire/README.txt` pour fusionner le bloc `[3I_ATLAS]` dans `extras.dat`. Utilisez les scripts `tools/solarfire/` pour prévisualiser et appliquer.

### Import en format MPC

Les dossiers sous `apps-using-mpc-files/` contiennent des `README` spécifiques (Stellarium, KStars, Cartes du Ciel, WinStars) et le fichier quotidien complet.

### État d’Astro Gold & TimePassages

Pas d’import dynamique à ce jour ; les guides détaillent comment créer un point fixe à date donnée.

### Notes sur les CSV

`apps-using-csv-files/README.txt` décrit les colonnes, unités et cas d’usage (tableurs, notebooks, scripts). Les longitudes tropicales nécessitent un retrait d’ayanāṃśa si vous travaillez en sidéral.

## Recette Horizons

Le dossier `developer/raw/` contient les sorties JSON issues de NASA/JPL Horizons via la requête suivante :

```
COMMAND='DES=1004083;'
MAKE_EPHEM='YES'
EPHEM_TYPE='VECTORS'
CENTER='500@399'        # centre de la Terre
REF_PLANE='ECLIPTIC'
REF_SYSTEM='J2000'
START_TIME='2016-01-01'
STOP_TIME='2040-12-31'
STEP_SIZE='1 d'
TABLE_TYPE='VECTORS'
```

Modifiez ces paramètres pour une autre fenêtre temporelle ou un autre point d’observation, puis régénérez les JSON avant de relancer les scripts.

## Régénérer les éphémérides

### `developer/scripts/generate_ephemeris.py`

- Lit les JSON de `developer/raw/` et régénère :
  - Les CSV (`apps-using-csv-files/`)
  - Les tables Solar Fire (`solar-fire/`)
  - L’éphéméride MPC (`apps-using-mpc-files/geocentric_mpc_ephemeris.txt`)
  - Les résumés d’entrées en signe.
- Crée les dossiers au besoin.

Usage :

```
cd developer/scripts
python3 generate_ephemeris.py
```

### `developer/scripts/build_swisseph.sh`

- Nécessite l’outil propriétaire `mksweph`.
- Transforme les CSV en binaires Swiss Ephemeris `.se1` placés dans `developer/swisseph/`.

```
cd developer/scripts
bash build_swisseph.sh
```

### `tools/update_orbital_elements.py`

- Récupère la dernière solution SBDB et met à jour toutes les lignes (fichiers MPC, snippets KStars, blocs Solar Fire).

```
python tools/update_orbital_elements.py
```

Ajoutez `--dry-run` pour afficher les valeurs sans modifier les fichiers.

### `tools/verify_ephemeris.py`

- Compare des lignes de `apps-using-mpc-files/geocentric_mpc_ephemeris.txt` avec Horizons en direct.

```
python tools/verify_ephemeris.py --start 2025-10-01 --days 5 --tolerance 5e-4
```

Réglages par défaut : `start=2025-10-01`, `days=5`, `tolerance=5e-4` UA (~75 000 km). Sortie non nulle en cas d’écart, idéal pour du CI.

## Scripts de maintenance

- **`tools/3i_elements_to_formats.py`** – convertit une nouvelle ligne MPC en modèles (Stellarium, KStars, Solar Fire).
- **`tools/kstars/`** – scripts pour sauvegarder/ajouter la ligne dans `comets.dat` selon l’OS.
- **`tools/solarfire/`** – scripts Windows pour fusionner le bloc `[3I_ATLAS]` dans `extras.dat`.

## Étapes clés

- 2024-10-xx — extraction initiale Horizons et structuration des dossiers.
- 2025-10-xx — mise à jour vers solution SBDB 27.
- 2025-10-xx — ajout des scripts de vérification et du pack import.

## Notes & avertissements

- **Solar Fire** : sauvegardez toujours `extras.dat` avant de fusionner.
- **SkySafari** : pas d’import fichier manuel—utilisez *Update Orbit Data*.
- **Astro Gold / TimePassages** : pas d’import dynamique ; utilisez des points fixes.
- **Validation** : exécutez `tools/verify_ephemeris.py` pour comparer quelques dates.

## Dépannage

- **Je ne trouve pas 3I/ATLAS après import.** Redémarrez l’application, vérifiez l’orthographe `3I/ATLAS`.
- **Les positions sont décalées d’un jour.** Les fichiers MPC sont horodatés à **UT 0h** ; travaillez en UTC ou appliquez l’offset de fuseau.
- **Solar Fire reste sur l’ancienne liste.** Vérifiez le chemin `extras.dat` (souvent `Documents\Solar Fire User Files\Points & Colors\extras.dat`) ou relancez le script APPLY.
- **Besoin de vérifier les données.** `python tools/verify_ephemeris.py` compare quelques dates avec Horizons.

Bonnes observations de 3I/ATLAS !

## Option : installer les outils Horizons

Vous n’avez pas besoin d’une installation locale heuristique, les données sont déjà extraites. Pour récupérer vous-même des éphémérides :

### macOS / Linux
1. Vérifiez `python3 --version` (3.10+ recommandé).
2. Installez Astroquery :
   ```bash
   python3 -m pip install astroquery --user
   ```
3. Interrogez Horizons :
   ```bash
   python3 - <<'PY'
   from astroquery.jplhorizons import Horizons
   obj = Horizons(id='DES=1004083;', location='500@399', epochs={'start':'2025-01-01', 'stop':'2025-01-10', 'step':'1d'})
   print(obj.vectors())
   PY
   ```

Alternative :

```bash
curl "https://ssd.jpl.nasa.gov/api/horizons.api?format=json&COMMAND='DES=1004083;'&MAKE_EPHEM=YES&EPHEM_TYPE=VECTORS&CENTER='500@399'&REF_PLANE=ECLIPTIC&STEP_SIZE=1%20d&START_TIME=2025-01-01&STOP_TIME=2025-01-03"
```

### Windows
1. Installez Python 3 depuis https://www.python.org/downloads/ (cocher “Add Python to PATH”).
2. Dans PowerShell :
   ```powershell
   py -m pip install astroquery
   py - <<'PY'
   from astroquery.jplhorizons import Horizons
   obj = Horizons(id='DES=1004083;', location='500@399', epochs={'start':'2025-01-01', 'stop':'2025-01-10', 'step':'1d'})
   print(obj.vectors())
   PY
   ```
3. Les utilisateurs WSL peuvent suivre les instructions macOS/Linux.

### Interface classique (Telnet)
```bash
telnet horizons.jpl.nasa.gov 6775
```
Suivez les invites pour saisir la cible (`DES=1004083;`) et les options de sortie.

### Installer Python 3.10+ sous Linux

Consultez les commandes dans la documentation (APT, DNF, zypper, pacman, etc.). Lorsque la distribution ne propose pas la version requise, utilisez pyenv ou compilez depuis les sources.

Même si votre système fournit déjà Python, mieux vaut installer votre propre 3.10+ et utiliser des environnements virtuels (`python3 -m venv`) pour isoler les dépendances.
