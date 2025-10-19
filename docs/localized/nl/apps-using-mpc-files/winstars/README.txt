3I/ATLAS — Snelle import in WinStars
====================================

WinStars (v3) kan MPC-kometelementen via de ingebouwde editor inlezen.

### Methode 1 — eenregelige invoer plakken
1. Start WinStars.
2. Open **Preferences → Solar system → Import orbital elements** (of **Add object**).
3. Kies **MPC single line** en plak de inhoud van `3I_ATLAS_mpc_1line.txt`.
4. Bevestig en controleer of 3I/ATLAS geactiveerd is in de lijst met objecten.

### Methode 2 — bestand met kometen vervangen (geavanceerd)
1. Sluit WinStars.
2. Maak een back-up van de comets-file:
   - Windows: `%APPDATA%\WinStars3\databases\comets.txt`
   - Linux: `~/.config/WinStars3/databases/comets.txt`
3. Voeg de eenregelige invoer uit `3I_ATLAS_mpc_1line.txt` toe aan dat bestand.
4. Start WinStars opnieuw; 3I/ATLAS staat nu onder de kometen.

Het eenregelige bestand is gebaseerd op JPL SBDB-oplossing 27 (2025-10-10). Werk het bij zodra er een nieuwere oplossing verschijnt.
