# Przepływy pracy aplikacji dla 3I/ATLAS

Wszystkie wartości w tym pakiecie pochodzą z rozwiązania 27 JPL SBDB (2025-10-10).
Aktualizuj pliki skryptem konwersji, gdy tylko pojawi się nowsze rozwiązanie.

## Stellarium (Windows/macOS/Linux)

**Obsługuje:** jednowierszowe elementy komety MPC  
**Kroki:**
1. **Configuration → Plugins → Solar System Editor** → zaznacz **Load at startup** (w razie potrzeby uruchom ponownie).  
2. **Solar System Editor → Configure → Solar System → Import elements in MPC format → File**.  
3. Wybierz `templates/stellarium/3I_ATLAS_mpc_elements.txt`.  
4. Kliknij **Add object(s)** i wyszukaj **3I/ATLAS**.

## KStars (Windows/macOS/Linux)

**Obsługuje:** wpis `comets.dat`  
**Narzędzia:**
- Windows: `tools/kstars/KStars_Append_3I-DRYRUN.bat` (podgląd), następnie `…-APPLY.bat`.  
- macOS: kliknij dwukrotnie `tools/kstars/KStars_Append_3I.command`.  
- Linux: uruchom `bash tools/kstars/KStars_Append_3I.sh`.  
Wszystkie narzędzia tworzą kopię zapasową przed dodaniem wpisu.

Ręcznie:
1. Zrób kopię `comets.dat` (`~/.local/share/kstars/comets.dat` w Linuxie, `%LOCALAPPDATA%\kstars\comets.dat` w Windows, `~/Library/Application Support/kstars/comets.dat` w macOS).  
2. Dodaj jedną linię z `templates/kstars/3I_ATLAS_comets_dat_snippet.txt`.  
3. Uruchom ponownie KStars i wyszukaj **3I/ATLAS**.

## SkySafari / SkyVoyager (iOS/Android)

**Obsługuje:** brak ręcznego importu  
Użyj *Settings → Solar System → Update Orbit Data* (poziomy Plus/Pro). Zachowaj
`templates/skysafari/3I_ATLAS_mpc_1line.txt` wyłącznie jako referencję.

## Cartes du Ciel (SkyCharts)

**Obsługuje:** pliki elementów MPC  
Postępuj według wskazówek z `apps-using-mpc-files/cartes-du-ciel/README.txt`
(import przez GUI lub ręczne dopisanie do `comet.dat`).

## WinStars 3

**Obsługuje:** pliki elementów MPC  
Zajrzyj do `apps-using-mpc-files/winstars/README.txt`, aby poznać szybkie kroki importu.

## Solar Fire (Windows)

**Obsługuje:** elementy orbitalne `extras.dat` (Other Bodies)  
**Narzędzia:**
- Windows: `tools/solarfire/SF_Merge_3I-DRYRUN.bat` (podgląd), następnie `…-APPLY.bat`, aby automatycznie scalić `[3I_ATLAS]`.  
Oba skrypty wykonują kopię `extras.dat` z sygnaturą czasową.

Ręcznie:
1. Zamknij Solar Fire i wykonaj kopię `Documents\Solar Fire User Files\Userdata\extras.dat`.  
2. Skopiuj lub scal blok `[3I_ATLAS]` z `templates/solar_fire/3I_ATLAS_extras_dat_PLACEHOLDER.txt`.  
3. Uruchom ponownie i włącz **3I/ATLAS** w **Extra Bodies** w oknie wyboru punktów.

## Aplikacje bez mechanizmu importu

Astro Gold (macOS/iOS/iPadOS) oraz TimePassages Desktop (macOS/Windows) udostępniają
wyłącznie dodatkowe punkty dostarczone przez producenta i nie akceptują
użytkowniczych efemeryd ciał ruchomych. Zajrzyj do folderu `Time-Passages-Astro-Gold/`
po obejścia (punkty stałe) i dane kontaktowe producenta.
