# 3I/ATLAS — pakiet importu (v0.2)

Skorzystaj z tego pakietu, gdy potrzebujesz **gotowych elementów orbitalnych MPC**
albo narzędzia pomocniczego dla swojej platformy, aby wprowadzić 3I/ATLAS do oprogramowania astronomicznego.
Wszystko działa offline i bazuje na rozwiązaniu 27 JPL SBDB (2025-10-10).

> **W skrócie**
> - **Stellarium** → zaimportuj dostarczony wiersz przez *Solar System Editor → Import elements in MPC format*.
> - **KStars** → uruchom pomocnik bez instalacji (Windows/macOS/Linux) lub wklej dostarczony wpis `comets.dat`.
> - **SkySafari** → użyj *Settings → Solar System → Update Orbit Data* (Plus/Pro) i zachowaj wiersz MPC jako odniesienie.
> - **Solar Fire** → scal blok `[3I_ATLAS]` z `extras.dat` (najpierw wykonaj kopię zapasową); dołączono skrypty pomocnicze.
> - **Astro Gold / TimePassages** → obecnie brak importu ciał ruchomych; zobacz notatki w głównym repozytorium, aby zastosować obejścia z punktami stałymi.

## Zawartość

- `templates/stellarium/3I_ATLAS_mpc_elements.txt` — jednowierszowe elementy MPC dla 3I/ATLAS.
- `templates/skysafari/3I_ATLAS_mpc_1line.txt` — ten sam wiersz do archiwum/referencji.
- `templates/kstars/3I_ATLAS_comets_dat_snippet.txt` — wiersz gotowy do dodania do `comets.dat` (używany także przez Cartes du Ciel / WinStars).
- `templates/solar_fire/3I_ATLAS_extras_dat_PLACEHOLDER.txt` — blok `[3I_ATLAS]` przygotowany dla `extras.dat` w Solar Fire.
- `tools/3i_elements_to_formats.py` — opcjonalny konwerter dla nowych wpisów MPC.
- `tools/update_orbital_elements.py` — pobiera najnowsze rozwiązanie JPL SBDB i nadpisuje wszystkie szablony.
- `docs/WORKFLOWS.md` — instrukcje krok po kroku dla Stellarium, KStars, Cartes du Ciel, WinStars, SkySafari, Solar Fire.

## Szybki start

Masz aktualne dane? Przejdź bezpośrednio do `docs/WORKFLOWS.md`. Aby odświeżać zestaw, gdy JPL
publikuje nową orbitę, uruchom:
```bash
python tools/update_orbital_elements.py --dry-run  # podgląd najnowszych elementów
python tools/update_orbital_elements.py            # nadpisuje szablony
```
Jeżeli wolisz podmieniać pliki ręcznie, `tools/3i_elements_to_formats.py`
wygeneruje fragmenty dla Stellarium/KStars/Solar Fire z dowolnego wiersza MPC.

## Uwagi

- **Solar Fire `extras.dat`**: kolejność pól może się różnić w zależności od wersji. Korzystaj
z wbudowanej pomocy „Format of the Orbital Elements File” podczas ręcznej edycji i zawsze twórz kopię zapasową.
- **SkySafari**: brak ręcznego importu plików; polegaj na *Update Orbit Data*.
- **Astro Gold / TimePassages**: w chwili pisania nie udostępniają procesu importu ciał ruchomych. Użyj ich stałych punktów niestandardowych lub zgłoś się do producenta.
- **Weryfikacja**: uruchom `tools/verify_ephemeris.py`, aby porównać wybrane wiersze z
`apps-using-mpc-files/geocentric_mpc_ephemeris.txt` z danymi Horizons w trybie on-line, gdy chcesz potwierdzić efemerydy.
