DONNÉES CSV 3I/ATLAS
====================

Ce dossier contient les tableaux CSV bruts générés par NASA/JPL Horizons.
Chaque fichier utilise des dates TDB à 00:00 et le repère écliptique J2000,
sauf mention contraire.

Fichiers
--------
- `geocentric_daily.csv` – longitude/latitude/distances en écliptique tropicale
  ainsi que coordonnées cartésiennes et composantes de vitesse héliocentriques.
- `geocentric_sidereal_lahiri_daily.csv` – longitudes sidérales dérivées avec
  l'ayanāṃśa Lahiri (colonne `lambda_sidereal_deg`) et l'ayanāṃśa quotidien dans
  `ayanamsa_deg`.
- `geocentric_sidereal_fagan_bradley_daily.csv` – idem ci-dessus avec
  l'ayanāṃśa Fagan/Bradley.
- `geocentric_*_sign_ingresses.csv` – horodatages des passages de longitude géocentrique
  à chaque frontière tropicale/sidérale de 30°.
- `heliocentric_daily.csv`, `barycentric_daily.csv` – vecteurs position/vitesse
  dans les cadres héliocentrique et barycentrique du système solaire.

Conseils d'utilisation
----------------------
- Importez-les dans des tableurs (Excel, LibreOffice), notebooks scientifiques
  ou environnements de script (Python/pandas, R, etc.).
- Les longitudes sont en degrés ; enroulez-les ou convertissez-les en radians si besoin.
- Les distances sont en unités astronomiques (UA) ; les vitesses en km/s.
- Utilisez les tableaux sidéraux si vous voulez des longitudes déjà corrigées—
  sinon soustrayez votre ayanāṃśa préféré de la longitude tropicale.
- La cadence des données est de 1 jour ; interpolez si vous avez besoin d'une
  résolution plus fine.
