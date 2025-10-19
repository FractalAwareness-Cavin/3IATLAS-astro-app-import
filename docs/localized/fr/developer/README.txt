KIT OUTIL DÉVELOPPEUR
=====================

Ce dossier rassemble tout le nécessaire pour régénérer le lot d'éphémérides
à partir de zéro.

Contenu
-------
- `raw/` – réponses JSON récupérées via l'API NASA/JPL Horizons.
- `scripts/generate_ephemeris.py` – script Python qui reconstruit les CSV,
  fichiers texte Solar Fire, sortie MPC et résumés d'entrées en signe.
- `scripts/build_swisseph.sh` – assistant qui convertit les tables CSV en
  binaires Swiss Ephemeris `.se1` (nécessite `mksweph`).
- `vendor/` – module `pyswisseph` embarqué pour produire les sorties sidérales
  sans installation supplémentaire.

Régénération
------------
```
cd developer/scripts
python3 generate_ephemeris.py
```
Le script interroge de nouveau Horizons (connexion requise) et met à jour
les dossiers à la racine du dépôt.

Binaires Swiss Ephemeris
------------------------
Si vous disposez de l'outil propriétaire `mksweph` :
```
cd developer/scripts
bash build_swisseph.sh
```
Les fichiers `.se1` seront écrits dans `../swisseph/` pour distribution.

N'hésitez pas à modifier le script pour changer la cadence, les systèmes de coordonnées
ou les corps centraux ; les JSON bruts assurent la traçabilité jusqu'à Horizons.

Pour des notes d'utilisation détaillées, y compris l'outil de mise à jour SBDB et les scripts de vérification,
consultez `scripts/README.md`.
