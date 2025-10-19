# Zestaw efemeryd 3I/ATLAS

Dzienne efemerydy dla międzygwiezdnej komety **3I/ATLAS (C/2025 N1)**, wygenerowane bezpośrednio z NASA/JPL Horizons i przygotowane tak, by łatwo wprowadzić je do popularnych aplikacji astrologicznych. Zakres obejmuje cały przelot przez heliosferę (2016‑01‑01 → 2040‑12‑31). Ta wersja opiera się na **rozwiązaniu Horizons nr 27 (2025‑10‑10)**; uruchom `tools/update_orbital_elements.py`, gdy JPL opublikuje nowsze elementy i chcesz zaktualizować pomocnicze pliki.

## Szybki start
1. Pobierz paczkę odpowiadającą twojej aplikacji (patrz **Bezpośrednie pobrania**) lub sklonuj repozytorium.
2. Rozpakuj archiwum, aby zobaczyć `README` w każdej podfolderze.
3. Postępuj według listy kroków lub uruchom dołączone skrypty dla Solar Fire, KStars i Stellarium.
4. Opcjonalna konserwacja: `python tools/update_orbital_elements.py` pobiera najnowsze SBDB, a `python tools/verify_ephemeris.py` weryfikuje wybrane daty z Horizons.

## Spis treści
- [Szybki start](#szybki-start)
- [Obsługiwane aplikacje (import obiektów ruchomych)](#obsługiwane-aplikacje-import-obiektów-ruchomych)
- [Od czego zacząć?](#od-czego-zacząć)
- [Bezpośrednie pobrania](#bezpośrednie-pobrania)
- [Przewodnik po folderach](#przewodnik-po-folderach)
- [Glosariusz](#glosariusz)
- [Instrukcje dla aplikacji](#instrukcje-dla-aplikacji)
  - [Pakiet importu i skrypty](#pakiet-importu-i-skrypty)
  - [Status Astro Gold](#status-astro-gold)
  - [Solar Fire (Windows)](#solarfire-instructions-windows)
  - [Import w formacie MPC](#import-w-formacie-mpc)
  - [Astro Gold & TimePassages](#astro-gold--timepassages)
  - [Uwagi o CSV](#uwagi-o-csv)
- [Przepis Horizons](#przepis-horizons)
- [Regeneracja efemeryd](#regeneracja-efemeryd)
- [Skrypty serwisowe](#skrypty-serwisowe)
- [Kluczowe kamienie milowe](#kluczowe-kamienie-milowe)
- [Uwagi i ostrzeżenia](#uwagi-i-ostrzeżenia)
- [Rozwiązywanie problemów](#rozwiązywanie-problemów)
- [Opcjonalnie: instalacja narzędzi Horizons](#opcjonalnie-instalacja-narzędzi-horizons)

Obsługiwane aplikacje (import obiektów ruchomych)
-------------------------------------------------
- **Stellarium** (Win/macOS/Linux) — import przez Solar System Editor w formacie MPC.
- **KStars** (Win/macOS/Linux) — dopisanie linii do `comets.dat` (dostępne skrypty).
- **Solar Fire** (Windows) — scalenie bloku `[3I_ATLAS]` z `extras.dat`.
- **Cartes du Ciel / SkyCharts** (Win/macOS/Linux) — import plików MPC lub edycja `comet.dat`.
- **WinStars 3** (Win/macOS/Linux) — wklejenie linii MPC w edytorze obiektów.
- **SkySafari / SkyVoyager Plus/Pro** (iOS/Android/macOS) — aktualizacja danych orbitalnych z kanałów MPC.

Bez importu obiektów ruchomych:
- **Astro Gold** (macOS/iOS/iPadOS) oraz **TimePassages** (macOS/Windows). Skorzystaj z porad dotyczących punktów stałych.

Pytania? Napisz na [cavinbirdseyetarot@gmail.com](mailto:cavinbirdseyetarot@gmail.com).



## Od czego zacząć?

Wybierz folder zgodny z używaną aplikacją lub pobierz odpowiednie archiwum. Jeśli nie wiesz, sprawdź w programie *Plik → Importuj*, jakie formaty obsługuje.

- `solar-fire/` – wpis `extras.dat` dla Solar Fire i efemerydy referencyjne.
- `apps-using-mpc-files/` – `geocentric_mpc_ephemeris.txt` (MPC, 80 kolumn, UT 0h, RA/Dec J2000, Δ, r, elongacja, faza).
- `apps-using-csv-files/` – pliki CSV z wektorami heliogeobarycentrycznymi, wejściami w znaki, szerokościami.
- `developer/` – zrzuty JSON z Horizons, skrypty regeneracji, wbudowany `pyswisseph`, helper Swiss Ephemeris.
- `Time-Passages-Astro-Gold/` – ograniczenia oraz rozwiązania z punktami stałymi.

#### Bezpośrednie pobrania
- [Asystent scalania Solar Fire (Windows)](https://github.com/FractalAwareness-Cavin/3IATLAS-astro-app-import/releases/download/v1.0.0/SolarFire_merge-helper_Windows.zip)
- [Szybkie dopisanie KStars (Win/macOS/Linux)](https://github.com/FractalAwareness-Cavin/3IATLAS-astro-app-import/releases/download/v1.0.0/KStars_quick-append_Win-Mac-Linux.zip)
- [Szybki import Stellarium](https://github.com/FractalAwareness-Cavin/3IATLAS-astro-app-import/releases/download/v1.0.0/Stellarium_quick-import.zip)
- [Efemeryda MPC (80 kolumn)](https://github.com/FractalAwareness-Cavin/3IATLAS-astro-app-import/releases/download/v1.0.0/3I-ATLAS_apps_using_mpc_files.zip)
- [Zestaw CSV do badań](https://github.com/FractalAwareness-Cavin/3IATLAS-astro-app-import/releases/download/v1.0.0/3I-ATLAS_apps_using_csv_files.zip)

Każde archiwum odzwierciedla strukturę folderu i zawiera `README.txt` ze szczegółami—rozpakuj je przed uruchomieniem skryptów lub kopiowaniem plików.

## Przewodnik po folderach

- **solar-fire/** – dane `extras.dat` dla Solar Fire i tabele referencyjne.
- **apps-using-mpc-files/** – dzienna efemeryda MPC, linie pojedyncze, instrukcje dla aplikacji.
- **apps-using-csv-files/** – CSV z wektorami, wejściami znaków, metrykami.
- **developer/** – skrypty, vendored `pyswisseph`, surowe dane Horizons, narzędzia Swiss Ephemeris.
- **Time-Passages-Astro-Gold/** – obejścia dla programów bez importu.
- **import-pack/** – kompaktowy zestaw z templatem, skryptami i dokumentacją.

## Glosariusz

- **MPC 80 kolumn** – klasyczny format Minor Planet Center.
- **Horizons SBDB** – baza małych ciał NASA/JPL.
- **Elongacja** – kątowa odległość od Słońca widziana z Ziemi.
- **Δ (delta)** – odległość geocentryczna.
- **r** – odległość heliocentryczna.
- **UT** – czas uniwersalny (UTC).

## Instrukcje dla aplikacji

### Pakiet importu i skrypty

Szczegóły w `import-pack/3I-ATLAS/README.md` (templaty, helpery, proces aktualizacji).

### Status Astro Gold

Na razie brak importu ruchomych obiektów; patrz `Time-Passages-Astro-Gold/` po wskazówki dotyczące punktów stałych.

### SolarFire instructions Windows

`solar-fire/README.txt` opisuje, jak scalić `[3I_ATLAS]` do `extras.dat`. Skrypty w `tools/solarfire/` oferują tryb podglądu i zastosowania.

### Import w formacie MPC

Pod `apps-using-mpc-files/` znajdziesz README i pliki dla Stellarium, KStars, Cartes du Ciel, WinStars.

### Astro Gold & TimePassages

Brak wsparcia dla importu; twórz punkty stałe dla konkretnych epoch.

### Uwagi o CSV

`apps-using-csv-files/README.txt` omawia kolumny i jednostki do pracy w arkuszach, notebookach czy skryptach. Dla ujęcia syderycznego odejmij preferowaną ayanāṃśa od długości tropikalnej.

## Przepis Horizons

`developer/raw/` zawiera JSON wygenerowane parametrami:

```
COMMAND='DES=1004083;'
MAKE_EPHEM='YES'
EPHEM_TYPE='VECTORS'
CENTER='500@399'
REF_PLANE='ECLIPTIC'
REF_SYSTEM='J2000'
START_TIME='2016-01-01'
STOP_TIME='2040-12-31'
STEP_SIZE='1 d'
TABLE_TYPE='VECTORS'
```

Zmień je w razie potrzeby (okno czasowe, obserwator) i odśwież JSON przed ponownym generowaniem.

## Regeneracja efemeryd

### `developer/scripts/generate_ephemeris.py`

- Czyta JSON i odbudowuje:
  - CSV (`apps-using-csv-files/`)
  - Tabele tekstowe Solar Fire (`solar-fire/`)
  - Efemerydę MPC (`apps-using-mpc-files/geocentric_mpc_ephemeris.txt`)
  - Zestawienia wejść w znaki.
- Tworzy brakujące katalogi.

```
cd developer/scripts
python3 generate_ephemeris.py
```

### `developer/scripts/build_swisseph.sh`

- Wymaga `mksweph`.
- Konwertuje CSV na binaria Swiss Ephemeris `.se1` (`developer/swisseph/`).

```
cd developer/scripts
bash build_swisseph.sh
```

### `tools/update_orbital_elements.py`

- Pobiera najnowsze rozwiązanie SBDB i aktualizuje pliki MPC, snippet KStars oraz bloki Solar Fire.

```
python tools/update_orbital_elements.py
```

`--dry-run` wyświetla wartości bez zapisu.

### `tools/verify_ephemeris.py`

- Porównuje wiersze `apps-using-mpc-files/geocentric_mpc_ephemeris.txt` z Horizons online.

```
python tools/verify_ephemeris.py --start 2025-10-01 --days 5 --tolerance 5e-4
```

Domyślnie: start 2025-10-01, 5 dni, tolerancja `5e-4` AU (~75 000 km). Zwraca niezerowy kod przy odchyleniach (przydatne w CI).

## Skrypty serwisowe

- **`tools/3i_elements_to_formats.py`** — tworzy templaty ze świeżego MPC Einzeilera (Stellarium, KStars, Solar Fire).
- **`tools/kstars/`** — systemowe helpery do backupu i dopisywania w `comets.dat`.
- **`tools/solarfire/`** — skrypty Windows do automatycznego scalania `extras.dat`.

## Kluczowe kamienie milowe

- 2024-10-xx — pierwsza ekstrakcja Horizons i struktura folderów.
- 2025-10-xx — aktualizacja do rozwiązania SBDB 27.
- 2025-10-xx — dodane skrypty weryfikacyjne i pakiet importu.

## Uwagi i ostrzeżenia

- **Solar Fire**: zrób kopię `extras.dat` przed scaleniem.
- **SkySafari**: brak importu plików — korzystaj z *Update Orbit Data*.
- **Astro Gold / TimePassages**: tylko punkty stałe.
- **Weryfikacja**: `tools/verify_ephemeris.py` umożliwia szybkie porównanie z Horizons.

## Rozwiązywanie problemów

- **3I/ATLAS nie pojawia się po imporcie.** Uruchom program ponownie i upewnij się, że nazwa to `3I/ATLAS`.
- **Pozycje przesunięte.** Plik MPC ma znacznik **UT 0h**; pracuj w UTC lub wprowadź korektę strefy.
- **Solar Fire pokazuje starą listę.** Zweryfikuj folder `extras.dat` (każda wersja ma własny) lub uruchom helper APPLY ponownie.
- **Chcę sprawdzić dane.** `python tools/verify_ephemeris.py` porówna sample z Horizons.

Powodzenia z 3I/ATLAS!

## Opcjonalnie: instalacja narzędzi Horizons

Nie jest to wymagane (dane są w zestawie), ale jeśli chcesz generować je samodzielnie:

### macOS / Linux
1. Sprawdź, czy `python3 --version` ≥ 3.10.
2. Zainstaluj Astroquery:
   ```bash
   python3 -m pip install astroquery --user
   ```
3. Zapytanie Horizons:
   ```bash
   python3 - <<'PY'
   from astroquery.jplhorizons import Horizons
   obj = Horizons(id='DES=1004083;', location='500@399', epochs={'start':'2025-01-01', 'stop':'2025-01-10', 'step':'1d'})
   print(obj.vectors())
   PY
   ```

Alternatywnie:

```bash
curl "https://ssd.jpl.nasa.gov/api/horizons.api?format=json&COMMAND='DES=1004083;'&MAKE_EPHEM=YES&EPHEM_TYPE=VECTORS&CENTER='500@399'&REF_PLANE=ECLIPTIC&STEP_SIZE=1%20d&START_TIME=2025-01-01&STOP_TIME=2025-01-03"
```

### Windows
1. Zainstaluj Python 3 z https://www.python.org/downloads/ (z zaznaczonym „Add Python to PATH”).
2. W PowerShell:
   ```powershell
   py -m pip install astroquery
   py - <<'PY'
   from astroquery.jplhorizons import Horizons
   obj = Horizons(id='DES=1004083;', location='500@399', epochs={'start':'2025-01-01', 'stop':'2025-01-10', 'step':'1d'})
   print(obj.vectors())
   PY
   ```
3. W użytkownicy WSL mogą iść za instrukcją macOS/Linux.

### Klasyczne CLI (Telnet)
```bash
telnet horizons.jpl.nasa.gov 6775
```
Podążaj za instrukcjami, wpisz `DES=1004083;` i wybierz opcje.

### Instalacja Python 3.10+ na Linuxie

Skorzystaj z menedżera pakietów (apt, dnf, zypper, pacman…). Jeśli brak nowej wersji, użyj pyenv lub kompilacji ze źródeł. Nawet jeśli system ma Python, warto zainstalować własną wersję ≥3.10 i pracować w wirtualnych środowiskach (`python3 -m venv`).
