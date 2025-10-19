3I/ATLAS ET APPS SANS IMPORT
============================

Cette note décrit les limites actuelles de **Astro Gold** (macOS, iOS/iPadOS)
et de **TimePassages Desktop** (macOS / Windows), ainsi que les moyens de tirer parti
de leurs fonctions intégrées de « points supplémentaires ».

## Astro Gold (macOS / iOS / iPadOS)
- Astro Gold permet uniquement d'activer/désactiver le catalogue de corps livré
  par l'éditeur. Il n'existe pas de fonction documentée pour importer des éphémérides
  ou éléments orbitaux tiers.
- Vous pouvez activer les points fournis par le développeur via :
  - **macOS** : `Astro Gold → Preferences → Displayed Points → Add Extra Points…`
  - **iOS / iPadOS** : `Settings → Chart Points → Add Extra Points…`
- Les « Custom Points » d'Astro Gold sont des longitudes écliptiques fixes saisies
  manuellement. Idéaux pour des étoiles de référence ou des degrés de thème, mais ils
  ne se mettent pas à jour avec le temps.
- Les utilisateurs avancés peuvent explorer les dossiers de l'application (par ex.
  `~/Library/Application Support/com.ajnaware.Astro-Gold` sur macOS ou
  `~/Documents/Astro Gold` pour les thèmes), mais ces dossiers n'acceptent **pas**
  d'éphémérides dynamiques à glisser-déposer.

**À retenir :** Tant qu'Esoteric Technologies n'ajoute pas 3I/ATLAS à son catalogue (ou
n'expose pas un crochet d'import), vous ne pouvez pas l'installer comme corps mobile dans
Astro Gold. Utilisez les extras intégrés, ou créez un point personnalisé fixe si vous
voulez simplement sa position à une date donnée.

### Procédure point fixe (Astro Gold)
1. Choisissez la date/heure à figer (exemple : **2025-10-29 00:00 UT** proche du périhélie).
2. Ouvrez `apps-using-csv-files/geocentric_daily.csv` et repérez la ligne correspondante. Relevez la longitude tropicale (`lambda_deg`) et la latitude (`beta_deg`). Dans l'exemple, le tableau indique `lambda_deg = 203.560 deg` (≈ 23°33' Scorpion) et `beta_deg = 2.283 deg`.
3. Dans Astro Gold (macOS) : **Astro Gold → Preferences → Displayed Points → Add Extra Points…**, puis onglet **Custom Points**. Sur iOS/iPadOS : **Settings → Chart Points → Add Extra Points…**.
4. Créez un nouveau point nommé par exemple `3I/ATLAS 2025-10-29 UT`, saisissez la longitude en décimal (ou dans le format signe/degré attendu) et, si besoin, notez latitude ou distance.
5. Enregistrez le point. Il restera statique ; répétez l'opération avec une nouvelle longitude quand vous voulez un autre epoch.

## TimePassages Desktop (macOS / Windows)
- TimePassages permet d'activer les corps fournis (astéroïdes majeurs, centaures,
  Eris/TNO, etc.). Le flux habituel :
  - `Preferences → Edit Chart Points` (macOS) ou `Edit → Chart Points…` (Windows)
    pour activer les catégories.
  - `Display → Chart Points…` pour vérifier qu'elles s'affichent.
- La fonction **Custom Points** est également un outil à degré fixe (par ex. saisir le centre galactique à 27° Sagittaire). À ce jour, TimePassages n'offre aucun mécanisme d'import pour de nouveaux objets mobiles.
- Les dossiers visibles côté utilisateur (par ex.
  `~/Library/Application Support/TimePassages/` sur macOS ou
  `%APPDATA%\TimePassages\` sur Windows) stockent uniquement préférences et thèmes ;
  on ne peut pas y déposer une éphéméride à intégrer.

**À retenir :** TimePassages ne peut pas encore suivre 3I/ATLAS automatiquement. Si
un futur version ajoute l'import, les instructions seront mises à jour ici. Pour l'instant,
vous pouvez créer un point fixe personnalisé à une date/heure donnée si vous avez besoin
d'une référence statique.

### Procédure point fixe (TimePassages)
1. Choisissez l'époque voulue (ex. **2025-10-18 00:00 UT** près de l'élongation maximale).
2. Consultez `apps-using-csv-files/geocentric_daily.csv`. La ligne du 2025-10-18 indique
   `lambda_deg = 209.285 deg` (≈ 29°17' Balance) et `beta_deg = 2.715 deg`.
3. Dans TimePassages ouvrez **Edit → Chart Points…** (Windows) ou **Preferences → Edit Chart Points** (macOS), allez dans **Custom Points** et cliquez sur **Add**.
4. Entrez un nom (ex. `3I/ATLAS 2025-10-18 UT`) et saisissez la longitude dans le format signe/degré utilisé par TimePassages. Ajoutez latitude ou distance dans la description si utile.
5. Sauvegardez et activez le point personnalisé. Mettez-le à jour avec une nouvelle longitude lorsque vous avez besoin d'un autre instantané.

---

### Contacter l'éditeur
Si vous souhaitez que ces logiciels gèrent 3I/ATLAS (ou les imports personnalisés en général), contactez directement les équipes :
- Esoteric Technologies (Astro Gold) :
  https://www.astrogold.io/contact
- AstroGraph (TimePassages) :
  https://www.astrograph.com/contact.php

N'hésitez pas à leur signaler les éléments orbitaux disponibles dans ce dépôt pour faciliter l'intégration officielle.
