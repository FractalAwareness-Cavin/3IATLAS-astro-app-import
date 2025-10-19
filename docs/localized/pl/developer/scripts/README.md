# Skrypty deweloperskie

Narzędzia do odtwarzania i weryfikacji pakietu efemeryd 3I/ATLAS znajdują się w katalogach `developer/scripts/` oraz `tools/`. Skorzystaj z tego przewodnika, gdy chcesz odświeżyć dane lub sprawdzić zmiany przed publikacją nowego wydania.

## Wymagania
- Python 3.10 lub nowszy (`python3 --version`).
- Opcjonalnie: środowisko wirtualne (`python3 -m venv .venv && source .venv/bin/activate`), jeśli instalujesz dodatkowe pakiety.
- Dostęp do internetu podczas uruchamiania aktualizatora SBDB lub weryfikatora Horizons.
- Opcjonalnie: `mksweph`, jeśli planujesz budować binaria Swiss Ephemeris przy użyciu `build_swisseph.sh`.

Repozytorium dołącza `pyswisseph` w `developer/vendor/`, więc wyjścia gwiazdowe działają bez dodatkowych instalacji.

## Domyślna recepta Horizons

Surowe pliki JSON w `developer/raw/` wygenerowano z NASA/JPL Horizons z następującymi parametrami:

```
COMMAND='DES=1004083;'
MAKE_EPHEM='YES'
EPHEM_TYPE='VECTORS'
CENTER='500@399'        # środek Ziemi
REF_PLANE='ECLIPTIC'
REF_SYSTEM='J2000'
START_TIME='2016-01-01'
STOP_TIME='2040-12-31'
STEP_SIZE='1 d'
TABLE_TYPE='VECTORS'
```

Dostosuj je, jeśli potrzebujesz innego zakresu czasu lub punktu obserwacji, a następnie ponownie wygeneruj JSON-y przed budową wyników.

## `generate_ephemeris.py`
Ścieżka: `developer/scripts/generate_ephemeris.py`

- Czyta zrzuty wektorów JSON w `developer/raw/` i przebudowuje wszystkie produkty pochodne:
  - Tabele CSV w `apps-using-csv-files/`
  - Pliki tekstowe Solar Fire w `solar-fire/`
  - Efemerydę MPC (`apps-using-mpc-files/geocentric_mpc_ephemeris.txt`)
  - Podsumowania wejść do znaków.
- Automatycznie ładuje dołączony moduł `pyswisseph`, aby uzupełnić pola gwiazdowe.
- Tworzy katalogi docelowe, jeśli jeszcze nie istnieją.

Użycie:

```
cd developer/scripts
python3 generate_ephemeris.py
```

Skrypt korzysta z wbudowanych ustawień. Aby zmienić zakres czasowy lub krok, zaktualizuj najpierw pliki JSON (lub edytuj stałe na początku skryptu).

## `build_swisseph.sh`
Ścieżka: `developer/scripts/build_swisseph.sh`

- Wymaga własnościowego narzędzia `mksweph`.
- Konwertuje wyniki CSV na binaria `.se1` Swiss Ephemeris i zapisuje je w `developer/swisseph/`.

Użycie:

```
cd developer/scripts
bash build_swisseph.sh
```

Pomocnik odmówi działania, jeśli `mksweph` nie znajduje się w `PATH`.

## `tools/update_orbital_elements.py`
Ścieżka: `tools/update_orbital_elements.py`

- Pobiera najnowsze rozwiązanie orbitalne SBDB dla 3I/ATLAS i aktualizuje wszystkie jednowierszowe szablony:
  - Pliki MPC (`apps-using-mpc-files/*/3I_ATLAS_mpc_1line.txt`)
  - Fragmenty KStars (`apps-using-mpc-files/kstars/` oraz szablony pakietu importowego)
  - Bloki `extras.dat` w Solar Fire.
- Wypisuje pozyskane elementy na stdout w celu weryfikacji.

Użycie (z katalogu głównego repozytorium):

```
python tools/update_orbital_elements.py
```

Dodaj `--dry-run`, aby obejrzeć wartości bez modyfikacji plików.

## `tools/verify_ephemeris.py`
Ścieżka: `tools/verify_ephemeris.py`

- Sprawdza wybrane wiersze z `apps-using-mpc-files/geocentric_mpc_ephemeris.txt` względem danych Horizons w czasie rzeczywistym.
- Porównuje odległość geocentryczną („delta”) w konfigurowalnym zakresie dat i oznacza wiersze przekraczające tolerancję.

Użycie (z katalogu głównego repozytorium):

```
python tools/verify_ephemeris.py --start 2025-10-01 --days 5 --tolerance 5e-4
```

Argumenty:
- `--start`: pierwsza sprawdzana data (domyślnie `2025-10-01`).
- `--days`: liczba kolejnych dni (domyślnie `5`).
- `--tolerance`: dopuszczalna różnica w jednostkach astronomicznych (domyślnie `5e-4`, ok. 75 000 km).

Skrypt kończy działanie kodem różnym od zera, jeśli wykryje odchylenia, dzięki czemu nadaje się do pipeline'ów CI.
