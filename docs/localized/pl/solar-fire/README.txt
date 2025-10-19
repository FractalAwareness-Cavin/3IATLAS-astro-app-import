3I/ATLAS DLA SOLAR FIRE (WINDOWS)
=================================

Solar Fire nie importuje wcześniej wyliczonych efemeryd dla nowych ciał; odczytuje elementy orbitalne z pliku `extras.dat`. Ten katalog utrzymuje wpis 3I/ATLAS zgodnie z rozwiązaniem 27 JPL SBDB.

Przetestowano na
----------------
- Solar Fire 9: `Documents\Solar Fire 9 User Files\Points & Colors\extras.dat`
- Solar Fire 10: `Documents\Solar Fire User Files\Points & Colors\extras.dat`
- Solar Fire 11: `Documents\Solar Fire User Files\Points & Colors\extras.dat`

Zawartość
---------
- `extras.dat`: gotowy blok `[3I_ATLAS]` (patrz niżej) oraz komentarze do ręcznych merge'y.
- `geocentric_daily_solarfire.txt` i podobne pliki: opcjonalne tabele referencyjne do weryfikacji pozycji poza Solar Fire.

Przykładowy blok
----------------
Wklej blok do swojego `extras.dat` lub pozwól, by helper zrobił to automatycznie:

```
[3I_ATLAS]
Name = 3I/ATLAS
Number = 0
EpochJD = 2460884.5
PerihelionDistance_AU = 1.356065571
Eccentricity = 6.137350157
Inclination_deg = 175.112857794
AscendingNode_deg = 322.152284965
ArgumentOfPerihelion_deg = 128.011608252
PerihelionTime_JD = 2460977.983535961
AbsoluteMagnitude = 12.3
SlopeParameter = 4.5
; Solar Fire ignoruje półoś wielką, gdy Tp jest podany dla komet.
; Obiekt jest hiperboliczny (e>1). Sprawdź zgodność z używaną wersją Solar Fire.
```

Instrukcja instalacji
---------------------
1. Zamknij Solar Fire.
2. Uruchom skrypty pomocnicze (`tools/solarfire/SF_Merge_3I-DRYRUN.bat`, potem `tools/solarfire/SF_Merge_3I-APPLY.bat`) **lub** wykonaj kopię obecnego `extras.dat`.
3. Otwórz ścieżkę odpowiednią dla swojej wersji (powyżej) i dodaj blok, pozostawiając dotychczasowe punkty własne.
4. Uruchom Solar Fire ponownie, wybierz **File → File Types…** i upewnij się, że **Extra Bodies** wskazuje na zaktualizowany plik.
5. W oknie wyboru punktów zaznacz `3I/ATLAS` w **Extra Bodies / Other Bodies**.

Mini-FAQ
--------
- **3I/ATLAS nie pojawia się po scaleniu.** Sprawdź, czy edytowałeś właściwy katalog `extras.dat` (Solar Fire ma oddzielne foldery użytkownika dla kolejnych wersji) oraz czy ciało jest włączone w **Extra Bodies**.
- **Skrypt zgłasza „access denied”.** Zamknij Solar Fire przed uruchomieniem skryptu APPLY; otwarty `extras.dat` nie może zostać nadpisany.
- **Potrzebuję nowszych elementów orbitalnych.** Wykonaj `python tools/update_orbital_elements.py` w katalogu głównym repozytorium, a następnie ponownie uruchom helper, by podmienić blok na najświeższą wersję SBDB.
