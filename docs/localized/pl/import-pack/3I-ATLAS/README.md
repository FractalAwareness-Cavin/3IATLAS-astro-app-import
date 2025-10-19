# Pakiet importu 3I/ATLAS

Szablony szybkiego startu, skrypty pomocnicze i dokumentacja, które pozwalają wprowadzić
**3I/ATLAS (C/2025 N1)** do oprogramowania astronomicznego zgodnego z MPC.

## Zawartość
- `docs/INSTALL_3I-ATLAS.md` — przegląd, uwagi i szybki start (obecnie wersja 0.2).
- `docs/WORKFLOWS.md` — instrukcje krok po kroku dla Stellarium, KStars,
  SkySafari, Solar Fire oraz notatki dotyczące aplikacji bez wsparcia.
- `templates/` — gotowe jednowierszowe elementy MPC, wpis `comets.dat` dla KStars
  oraz blok `[3I_ATLAS]` dla Solar Fire (wszystko oparte na rozwiązaniu JPL SBDB nr 27).
- `tools/3i_elements_to_formats.py` — opcjonalny konwerter: wklej nowszy
  jednowierszowy wpis MPC, a szablony zostaną automatycznie przepisane.
- `tools/kstars/` — narzędzia dla Windows/macOS/Linux, które wykonują kopię zapasową
  i dodają wiersz KStars.
- `tools/solarfire/` — narzędzia dla Windows, które tworzą kopię zapasową i scalają blok
  `extras.dat` dla 3I/ATLAS.

## Szybki podgląd użycia
- Stellarium: zaimportuj dostarczony wiersz przez **Solar System Editor → Import elements in MPC format → File**.
- KStars: uruchom skrypt dla swojego systemu operacyjnego lub dodaj dostarczony wiersz do `comets.dat` ręcznie.
- SkySafari: użyj **Settings → Solar System → Update Orbit Data** (poziomy Plus/Pro).  
- Solar Fire: scal blok `[3I_ATLAS]` z `extras.dat` (najpierw wykonaj kopię zapasową).  
- Astro Gold / TimePassages: obecnie brak importu ciał ruchomych; zajrzyj do notatek w repozytorium, jeśli potrzebujesz własnych punktów stałych.

Aktualizuj szablony przy pomocy skryptu konwersji po każdej publikacji nowego rozwiązania orbitalnego.
