3I/ATLAS – PRZEWODNIK IMPORTU MPC
=================================

`geocentric_mpc_ephemeris.txt` zawiera dzienne efemerydy w formacie MPC (UT 0h, RA/Dec J2000, delta, r, elongacja, faza). Używaj pliku wszędzie tam, gdzie program akceptuje klasyczny format komet 80 kolumn. Gotowe paczki są w wydaniach (zob. `README.md` w katalogu głównym) oraz w `apps-using-mpc-files/`.

Pakiety release
----------------
- `Stellarium_quick-import.zip`: importuje pojedynczy plik MPC przez wtyczkę Solar System Editor.
- `KStars_quick-append_Win-Mac-Linux.zip`: skrypty podgląd/zastosowanie dla `comets.dat` na każdej platformie.
- `3I-ATLAS_apps_using_mpc_files.zip`: zawiera cały katalog wraz z szablonami jednoliniowymi dla Cartes du Ciel i WinStars.

Stellarium (Win/macOS/Linux)
----------------------------
1. Rozpakuj `Stellarium_quick-import.zip` albo skopiuj `geocentric_mpc_ephemeris.txt` w znane miejsce.
2. W Stellarium wciśnij `F2`, otwórz **Plugins → Solar System Editor**, zaznacz **Load at startup** i kliknij **Configure**. Jeśli dopiero włączyłeś plugin, zrestartuj program.
3. Po restarcie przejdź do **Solar System Editor → Solar System** i kliknij **Import orbital elements in MPC format**.
4. Wybierz **Select file**, wskaż `geocentric_mpc_ephemeris.txt` (lub plik jednoliniowy), ustaw **Object name** na `3I/ATLAS`, zostaw **Object type** jako *Comet*.
5. Kliknij **Add objects**, zamknij okna i sprawdź wyszukiwarką (`F3`), że `3I/ATLAS` jest dostępny.

KStars (Win/macOS/Linux)
------------------------
1. Rozpakuj `KStars_quick-append_Win-Mac-Linux.zip` i uruchom odpowiadający systemowi skrypt (`*.bat`, `*.command`, `*.sh`, `*.ps1`). Zacznij od DRYRUN; jeśli podgląd jest OK, uruchom APPLY, aby dopisać kometę do `comets.dat`.
2. Ręcznie: **Settings → Configure KStars → Solar System** (starsze wersje: **Data → Solar System Updates**). W zakładce **Comets** kliknij **Import**, wybierz `geocentric_mpc_ephemeris.txt` i potwierdź.
3. Uruchom KStars ponownie, jeśli pojawi się komunikat, następnie wyszukaj `3I/ATLAS` lub sprawdź przeglądarkę układu.

Cartes du Ciel / SkyCharts
--------------------------
1. Skopiuj `apps-using-mpc-files/cartes-du-ciel/3I_ATLAS_mpc_1line.txt` (w zestawie release).
2. Uruchom Cartes du Ciel i otwórz **Setup → Solar system** (`Ctrl+F3`).
3. W zakładce **Comets** wybierz **Update → Import from MPC file**, wskaż `3I_ATLAS_mpc_1line.txt` i zatwierdź.
4. Zaznacz **3I/ATLAS** na liście i kliknij **OK**. Kometa będzie dostępna w wyszukiwaniu i na mapach.
5. Wolisz ręcznie? Dodaj tę samą linię do `comet.dat` (ścieżki w README odpowiedniego folderu).

WinStars 3 (Win/macOS/Linux)
----------------------------
1. Trzymaj pod ręką `apps-using-mpc-files/winstars/3I_ATLAS_mpc_1line.txt` albo wypakuj paczkę MPC.
2. W WinStars przejdź do **Preferences → Solar system → Import orbital elements** (lub **Add object**).
3. Wybierz **MPC single line**, wklej zawartość i zapisz.
4. Upewnij się, że `3I/ATLAS` jest włączony na liście wyświetlanych obiektów; zrestartuj, jeśli cache katalogu był otwarty.

SkySafari / SkyVoyager Plus/Pro (iOS/Android/macOS)
---------------------------------------------------
1. Skopiuj `3I_ATLAS_mpc_1line.txt` do edytora dostępnego na urządzeniu.
2. W SkySafari przejdź do **Settings → Solar System → Solar System Data** i wybierz **Import Comet Data** (starsze wersje: **Update Orbit Data → Custom Comet/Asteroid**).
3. Wklej linię MPC, upewnij się, że nazwa to `3I/ATLAS`, i potwierdź.
4. Wyszukaj `3I/ATLAS` i dodaj do list obserwacyjnych, jeśli chcesz.
5. Aplikacja okresowo odświeża dane MPC; po aktualizacji orbity powtórz import.

Inne programy zgodne z MPC
--------------------------
1. Skopiuj `geocentric_mpc_ephemeris.txt` lub pasujący szablon jednoliniowy.
2. Użyj funkcji importu komet/asteroid w programie, wskaż plik, nazwij obiekt `3I/ATLAS`.
3. Uruchom program ponownie, jeśli buforuje dane Układu Słonecznego, i sprawdź, czy obiekt jest aktywny.

Uaktualniaj pliki jednoliniowe, uruchamiając `python tools/update_orbital_elements.py` po każdej nowej rozwiązaniu SBDB, a pozycje weryfikuj narzędziem `python tools/verify_ephemeris.py`.
