3I/ATLAS — Import rapide WinStars
=================================

WinStars (v3) peut intégrer les éléments MPC via son éditeur intégré.

### Méthode 1 — coller la ligne unique
1. Lancez WinStars.
2. Ouvrez **Preferences → Solar system → Import orbital elements** (ou **Add object**).
3. Choisissez **MPC single line** et collez le contenu de `3I_ATLAS_mpc_1line.txt`.
4. Validez et vérifiez que 3I/ATLAS est activé dans la liste des corps affichés.

### Méthode 2 — remplacer le fichier des comètes (avancé)
1. Fermez WinStars.
2. Sauvegardez le fichier des comètes :
   - Windows : `%APPDATA%\WinStars3\databases\comets.txt`
   - Linux : `~/.config/WinStars3/databases/comets.txt`
3. Ajoutez la ligne issue de `3I_ATLAS_mpc_1line.txt` à ce fichier.
4. Relancez WinStars ; 3I/ATLAS figurera dans la liste des comètes.

Le fichier une ligne s'appuie sur la solution 27 du JPL SBDB (2025-10-10). Mettez-le à jour lorsqu'une nouvelle solution est publiée.
