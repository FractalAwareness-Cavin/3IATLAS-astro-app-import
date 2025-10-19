3I/ATLAS — rychlý import do WinStars
====================================

WinStars (v3) dokáže načíst kometární prvky MPC přes vestavěný editor.

### Metoda 1 — vložení jednoho řádku
1. Spusťte WinStars.
2. Otevřete **Preferences → Solar system → Import orbital elements** (nebo **Add object**).
3. Zvolte **MPC single line** a vložte obsah `3I_ATLAS_mpc_1line.txt`.
4. Potvrďte a ověřte, že 3I/ATLAS je zapnutý v seznamu zobrazených těles.

### Metoda 2 — výměna souboru s kometami (pokročilé)
1. Ukončete WinStars.
2. Zálohujte soubor komet:
   - Windows: `%APPDATA%\WinStars3\databases\comets.txt`
   - Linux: `~/.config/WinStars3/databases/comets.txt`
3. Přidejte do souboru jeden řádek z `3I_ATLAS_mpc_1line.txt`.
4. Spusťte WinStars znovu; 3I/ATLAS se objeví v seznamu komet.

Soubor s jedním řádkem vychází z řešení JPL SBDB 27 (2025-10-10). Aktualizujte jej při vydání nového řešení.
