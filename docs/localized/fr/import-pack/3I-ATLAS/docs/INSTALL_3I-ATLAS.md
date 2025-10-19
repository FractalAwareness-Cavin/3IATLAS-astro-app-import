# 3I/ATLAS — Pack d'importation (v0.2)

Utilisez ce pack lorsque vous avez besoin **d'éléments orbitaux MPC prêts à l'emploi** ou
d'un assistant spécifique à votre plateforme pour intégrer 3I/ATLAS dans un logiciel
d'astronomie. Tout fonctionne hors ligne et s'appuie sur la solution JPL SBDB 27 (2025-10-10).

> **TL;DR**
> - **Stellarium** → importer la ligne fournie via *Solar System Editor → Import elements in MPC format*.
> - **KStars** → lancer l'assistant sans installation (Windows/macOS/Linux) ou coller la ligne `comets.dat` fournie.
> - **SkySafari** → utiliser *Settings → Solar System → Update Orbit Data* (Plus/Pro) et conserver la ligne MPC en référence.
> - **Solar Fire** → fusionner le bloc `[3I_ATLAS]` dans `extras.dat` (sauvegarde préalable) ; scripts d'aide inclus.
> - **Astro Gold / TimePassages** → toujours pas d'import de corps mobiles ; voir les notes du dépôt principal pour les solutions à points fixes.

## Contenu

- `templates/stellarium/3I_ATLAS_mpc_elements.txt` — élément MPC en une ligne pour 3I/ATLAS.
- `templates/skysafari/3I_ATLAS_mpc_1line.txt` — la même ligne, à conserver en archive/référence.
- `templates/kstars/3I_ATLAS_comets_dat_snippet.txt` — ligne prête à ajouter à `comets.dat` (également utilisée par Cartes du Ciel / WinStars).
- `templates/solar_fire/3I_ATLAS_extras_dat_PLACEHOLDER.txt` — bloc `[3I_ATLAS]` prêt pour `extras.dat` de Solar Fire.
- `tools/3i_elements_to_formats.py` — convertisseur optionnel si vous collez une nouvelle ligne MPC.
- `tools/update_orbital_elements.py` — récupère la dernière solution JPL SBDB et réécrit chaque modèle sur place.
- `docs/WORKFLOWS.md` — instructions pas à pas pour Stellarium, KStars, Cartes du Ciel, WinStars, SkySafari, Solar Fire.

## Démarrage rapide

Déjà à jour ? Passez directement à `docs/WORKFLOWS.md`. Pour actualiser dès que JPL
publie une nouvelle orbite, exécutez l'outil de mise à jour :
```bash
python tools/update_orbital_elements.py --dry-run  # prévisualisation des derniers éléments
python tools/update_orbital_elements.py            # réécriture des modèles
```
Si vous préférez remplacer les fichiers manuellement, `tools/3i_elements_to_formats.py`
génèrera les extraits Stellarium/KStars/Solar Fire à partir de n'importe quelle ligne MPC.

## Mises en garde

- **Solar Fire `extras.dat`** : l'ordre des champs peut varier selon la version. Consultez
aide intégrée « Format of the Orbital Elements File » si vous modifiez le fichier
manuellement et effectuez toujours une sauvegarde au préalable.
- **SkySafari** : aucune importation de fichier manuel ; utilisez *Update Orbit Data*.
- **Astro Gold / TimePassages** : au moment de la rédaction, ces applications ne
proposent pas de procédure d'import de corps mobiles. Utilisez leurs points fixes personnalisés
ou sollicitez le support de l'éditeur.
- **Validation** : lancez `tools/verify_ephemeris.py` pour comparer certaines lignes de
`apps-using-mpc-files/geocentric_mpc_ephemeris.txt` aux données Horizons en direct si
vous souhaitez vérifier l'éphéméride.
