# Pack d'importation 3I/ATLAS

Modèles de démarrage rapide, scripts d'assistance et documentation pour intégrer
**3I/ATLAS (C/2025 N1)** dans les logiciels d'astronomie compatibles MPC.

## Contenu
- `docs/INSTALL_3I-ATLAS.md` — vue d'ensemble, avertissements et démarrage rapide (version actuelle v0.2).
- `docs/WORKFLOWS.md` — instructions pas à pas pour Stellarium, KStars,
  SkySafari, Solar Fire, ainsi que des notes sur les applications non prises en charge.
- `templates/` — éléments MPC 1-ligne prêts à l'emploi, ligne `comets.dat` pour KStars,
  et bloc `[3I_ATLAS]` pour Solar Fire (tous basés sur la solution JPL SBDB 27).
- `tools/3i_elements_to_formats.py` — convertisseur optionnel : collez une nouvelle
  ligne MPC et les modèles sont réécrits automatiquement.
- `tools/kstars/` — assistants Windows/macOS/Linux qui sauvegardent et ajoutent la
  ligne KStars.
- `tools/solarfire/` — assistants Windows qui sauvegardent et fusionnent le bloc
  `extras.dat` pour 3I/ATLAS.

## Aperçu d'utilisation
- Stellarium : importez la ligne fournie via **Solar System Editor → Import elements in MPC format → File**.
- KStars : exécutez le script adapté à votre OS ou ajoutez manuellement la ligne fournie à `comets.dat`.
- SkySafari : utilisez **Settings → Solar System → Update Orbit Data** (niveaux Plus/Pro).  
- Solar Fire : fusionnez le bloc `[3I_ATLAS]` dans `extras.dat` (effectuez d'abord une sauvegarde).  
- Astro Gold / TimePassages : pas d'importation de corps mobile pour l'instant ; consultez les notes du dépôt si vous avez besoin de points fixes personnalisés.

Mettez à jour les modèles avec le script de conversion dès qu'une nouvelle solution orbitale est publiée.
