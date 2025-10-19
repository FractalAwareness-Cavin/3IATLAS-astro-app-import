# Scripts développeur

Les utilitaires permettant de régénérer et de valider le kit d'éphémérides 3I/ATLAS se trouvent dans `developer/scripts/` et `tools/`. Utilisez ce guide pour actualiser l'ensemble de données ou vérifier vos modifications avant de publier une nouvelle version.

## Pré-requis
- Python 3.10 ou plus récent (`python3 --version` pour vérifier).
- Facultatif : un environnement virtuel (`python3 -m venv .venv && source .venv/bin/activate`) si vous installez des paquets supplémentaires.
- Accès internet lors de l'exécution de l'outil SBDB ou du vérificateur Horizons.
- Facultatif : `mksweph` si vous prévoyez de générer des binaires Swiss Ephemeris avec `build_swisseph.sh`.

Le dépôt embarque `pyswisseph` dans `developer/vendor/`, ce qui permet aux sorties sidérales de fonctionner sans installation additionnelle.

## Recette Horizons par défaut

Les JSON bruts dans `developer/raw/` ont été produits via NASA/JPL Horizons avec les paramètres suivants :

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

Adaptez ces valeurs si vous avez besoin d'une autre fenêtre temporelle ou d'un point de vue différent, puis régénérez les JSON avant de produire les sorties.

## `generate_ephemeris.py`
Emplacement : `developer/scripts/generate_ephemeris.py`

- Lit les dumps de vecteurs JSON dans `developer/raw/` et réécrit chaque produit dérivé :
  - Tables CSV dans `apps-using-csv-files/`
  - Fichiers texte Solar Fire dans `solar-fire/`
  - Éphéméride MPC (`apps-using-mpc-files/geocentric_mpc_ephemeris.txt`)
  - Résumés d'entrées en signe.
- Charge automatiquement le module `pyswisseph` embarqué pour remplir les champs sidéraux.
- Crée les répertoires cibles s'ils n'existent pas.

Utilisation :

```
cd developer/scripts
python3 generate_ephemeris.py
```

Le script tourne avec des paramètres intégrés. Pour ajuster la période ou la cadence, mettez d'abord à jour les JSON (ou modifiez les constantes en tête de script).

## `build_swisseph.sh`
Emplacement : `developer/scripts/build_swisseph.sh`

- Nécessite l'utilitaire propriétaire `mksweph`.
- Convertit les sorties CSV en binaires Swiss Ephemeris `.se1` stockés dans `developer/swisseph/`.

Utilisation :

```
cd developer/scripts
bash build_swisseph.sh
```

L'assistant refuse de s'exécuter si `mksweph` n'est pas présent dans votre `PATH`.

## `tools/update_orbital_elements.py`
Emplacement : `tools/update_orbital_elements.py`

- Récupère la dernière solution orbitale SBDB pour 3I/ATLAS et met à jour tous les modèles à une ligne :
  - Fichiers MPC ( `apps-using-mpc-files/*/3I_ATLAS_mpc_1line.txt` )
  - Extraits KStars (`apps-using-mpc-files/kstars/` et modèles du pack d'import)
  - Blocs `extras.dat` de Solar Fire.
- Affiche les éléments récupérés sur stdout pour vérification.

Utilisation (depuis la racine du dépôt) :

```
python tools/update_orbital_elements.py
```

Ajoutez `--dry-run` pour afficher les valeurs sans modifier les fichiers.

## `tools/verify_ephemeris.py`
Emplacement : `tools/verify_ephemeris.py`

- Vérifie ponctuellement des lignes de `apps-using-mpc-files/geocentric_mpc_ephemeris.txt` face aux données Horizons en direct.
- Compare la distance géocentrique (« delta ») sur une plage de dates configurable et signale les lignes dépassant la tolérance.

Utilisation (depuis la racine du dépôt) :

```
python tools/verify_ephemeris.py --start 2025-10-01 --days 5 --tolerance 5e-4
```

Arguments :
- `--start` : première date à vérifier (défaut `2025-10-01`).
- `--days` : nombre de jours consécutifs (défaut `5`).
- `--tolerance` : écart maximal admissible en unités astronomiques (défaut `5e-4`, environ 75 000 km).

Le script renvoie un code de sortie non nul en cas d'échec, ce qui le rend exploitable en CI.
