3I/ATLAS — szybki import w WinStars
===================================

WinStars (v3) potrafi wczytać elementy komet MPC przez wbudowany edytor.

### Metoda 1 — wklejenie linii
1. Uruchom WinStars.
2. Przejdź do **Preferences → Solar system → Import orbital elements** (lub **Add object**).
3. Wybierz **MPC single line** i wklej zawartość `3I_ATLAS_mpc_1line.txt`.
4. Zatwierdź i upewnij się, że 3I/ATLAS jest aktywna na liście obiektów.

### Metoda 2 — podmiana pliku komet (zaawansowane)
1. Zamknij WinStars.
2. Wykonaj kopię pliku komet:
   - Windows: `%APPDATA%\WinStars3\databases\comets.txt`
   - Linux: `~/.config/WinStars3/databases/comets.txt`
3. Dodaj do pliku linię z `3I_ATLAS_mpc_1line.txt`.
4. Uruchom WinStars ponownie; 3I/ATLAS pojawi się na liście komet.

Plik jednoliniowy oparto na rozwiązaniu JPL SBDB 27 (2025-10-10). Aktualizuj go, gdy pojawi się nowe rozwiązanie.
