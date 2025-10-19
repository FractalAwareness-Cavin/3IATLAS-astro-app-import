# Sada efemerid 3I/ATLAS

Denní efemeridy pro mezihvězdný komet **3I/ATLAS (C/2025 N1)**, vygenerované přímo z NASA/JPL Horizons a uspořádané tak, aby je astrologové snadno přidali do svých oblíbených aplikací. Pokrytí zahrnuje celý průchod heliosférou (2016‑01‑01 → 2040‑12‑31). Tato verze stojí na **řešení Horizons č. 27 (2025‑10‑10)**; spusťte `tools/update_orbital_elements.py`, jakmile JPL zveřejní novější řešení a chcete aktualizovat pomocné soubory.

## Rychlý start
1. Stáhněte archiv odpovídající vaší aplikaci (viz **Přímé downloady**) nebo naklonujte repo.
2. Archiv rozbalte, abyste v každé složce našli `README`.
3. Postupujte podle uvedených kroků nebo spusťte skripty pro Solar Fire, KStars a Stellarium.
4. Volitelné: `python tools/update_orbital_elements.py` stáhne nejnovější SBDB, `python tools/verify_ephemeris.py` ověří několik dat proti Horizons.

## Obsah
- [Rychlý start](#rychlý-start)
- [Podporované aplikace (import pohyblivých těles)](#podporované-aplikace-import-pohyblivých-těles)
- [Kde začít?](#kde-začít)
- [Přímé downloady](#přímé-downloady)
- [Průvodce složkami](#průvodce-složkami)
- [Glosář](#glosář)
- [Pokyny dle aplikace](#pokyny-dle-aplikace)
  - [Importní balíček a skripty](#importní-balíček-a-skripty)
  - [Stav Astro Gold](#stav-astro-gold)
  - [Solar Fire (Windows)](#solarfire-instructions-windows)
  - [Import ve formátu MPC](#import-ve-formátu-mpc)
  - [Astro Gold & TimePassages](#astro-gold--timepassages)
  - [Poznámky k CSV](#poznámky-k-csv)
- [Recept Horizons](#recept-horizons)
- [Regenerace efemerid](#regenerace-efemerid)
- [Servisní skripty](#servisní-skripty)
- [Klíčové milníky](#klíčové-milníky)
- [Poznámky a upozornění](#poznámky-a-upozornění)
- [Řešení problémů](#řešení-problémů)
- [Volitelné: instalace nástrojů Horizons](#volitelné-instalace-nástrojů-horizons)

Podporované aplikace (import pohyblivých těles)
----------------------------------------------
- **Stellarium** (Win/macOS/Linux) – import přes Solar System Editor (MPC).
- **KStars** (Win/macOS/Linux) – přidání řádku do `comets.dat` (pomocné skripty přiloženy).
- **Solar Fire** (Windows) – sloučení bloku `[3I_ATLAS]` do `extras.dat`.
- **Cartes du Ciel / SkyCharts** (Win/macOS/Linux) – import MPC nebo ruční úprava `comet.dat`.
- **WinStars 3** (Win/macOS/Linux) – vložení MPC-řádku v editoru objektů.
- **SkySafari / SkyVoyager Plus/Pro** (iOS/Android/macOS) – aktualizace orbitálních dat z MPC feedů.

Bez podpory importu pohyblivých těles:
- **Astro Gold** (macOS/iOS/iPadOS) a **TimePassages** (macOS/Windows). Použijte návody pro pevné body.

Otázky? Napište na [cavinbirdseyetarot@gmail.com](mailto:cavinbirdseyetarot@gmail.com).



## Kde začít?

Sáhněte po složce, která odpovídá vašemu software, nebo si stáhněte příslušné zipy. Nejste si jistí? Zkontrolujte v aplikaci *Soubor → Import*, jaké formáty bere.

- `solar-fire/` – `extras.dat` pro Solar Fire a referenční tabulky.
- `apps-using-mpc-files/` – `geocentric_mpc_ephemeris.txt` (MPC 80 sloupců, UT 0h, J2000 RA/Dec, Δ, r, elongace, fáze).
- `apps-using-csv-files/` – CSV s heliogeobaricentrickými vektory, vstupy do znamení, latitudy.
- `developer/` – JSON Horizons, skripty pro regeneraci, vendored `pyswisseph`, pomocník Swiss Ephemeris.
- `Time-Passages-Astro-Gold/` – omezení a postupy pro fixní body.

#### Přímé downloady
- [Solar Fire merge helper (Windows)](https://github.com/FractalAwareness-Cavin/3IATLAS-astro-app-import/releases/download/v1.0.0/SolarFire_merge-helper_Windows.zip)
- [KStars quick append (Win/macOS/Linux)](https://github.com/FractalAwareness-Cavin/3IATLAS-astro-app-import/releases/download/v1.0.0/KStars_quick-append_Win-Mac-Linux.zip)
- [Stellarium quick import](https://github.com/FractalAwareness-Cavin/3IATLAS-astro-app-import/releases/download/v1.0.0/Stellarium_quick-import.zip)
- [MPC efemerida (80 sloupců)](https://github.com/FractalAwareness-Cavin/3IATLAS-astro-app-import/releases/download/v1.0.0/3I-ATLAS_apps_using_mpc_files.zip)
- [CSV výzkumný set](https://github.com/FractalAwareness-Cavin/3IATLAS-astro-app-import/releases/download/v1.0.0/3I-ATLAS_apps_using_csv_files.zip)

Každý zip odpovídá stejnojmenné složce a obsahuje `README.txt` s konkrétními kroky—rozbalte před spuštěním skriptů nebo kopírováním.

## Průvodce složkami

- **solar-fire/** – data `extras.dat` pro Solar Fire a kontrolní tabulky.
- **apps-using-mpc-files/** – denní MPC efemerida, jednolinky, návody podle aplikace.
- **apps-using-csv-files/** – CSV s vektory, průchody znameními, další metriky.
- **developer/** – skripty, vendored `pyswisseph`, surová data, Swiss-Ephemeris nástroje.
- **Time-Passages-Astro-Gold/** – řešení pro software bez importu.
- **import-pack/** – kompaktní balíček s templaty, skripty, dokumentací.

## Glosář

- **MPC 80 columns** – klasický formát Minor Planet Center.
- **Horizons SBDB** – databáze malých těles NASA/JPL.
- **Elongace** – úhlová vzdálenost od Slunce ze Země.
- **Δ (delta)** – geocentrická vzdálenost.
- **r** – heliocentrická vzdálenost.
- **UT** – univerzální čas / UTC.

## Pokyny dle aplikace

### Importní balíček a skripty

Podrobnosti v `import-pack/3I-ATLAS/README.md`.

### Stav Astro Gold

Zatím bez importu pohyblivých těles; viz `Time-Passages-Astro-Gold/` pro pevné body.

### SolarFire instructions Windows

`solar-fire/README.txt` popisuje merge `[3I_ATLAS]` do `extras.dat`. Pomocné skripty najdete v `tools/solarfire/`.

### Import ve formátu MPC

Pod složkou `apps-using-mpc-files/` jsou README pro Stellarium, KStars, Cartes du Ciel, WinStars.

### Astro Gold & TimePassages

Import není dostupný; vytvářejte statické body pro konkrétní epochy.

### Poznámky k CSV

`apps-using-csv-files/README.txt` vysvětluje sloupce/unity pro tabulky, notebooky či skripty. Pro siderální práci odečtěte preferovanou ayanámšu od tropické délky.

## Recept Horizons

`developer/raw/` uchovává JSON vytvořené s parametry:

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

Upravte podle potřeby (časové okno, stanoviště), poté znovu vytvořte JSON před regenerací výstupů.

## Regenerace efemerid

### `developer/scripts/generate_ephemeris.py`

- Čte JSON a přegeneruje:
  - CSV tabulky (`apps-using-csv-files/`)
  - Textové tabulky pro Solar Fire (`solar-fire/`)
  - MPC efemeridu (`apps-using-mpc-files/geocentric_mpc_ephemeris.txt`)
  - Souhrny vstupů do znamení.
- Vytvoří složky, pokud chybí.

```
cd developer/scripts
python3 generate_ephemeris.py
```

### `developer/scripts/build_swisseph.sh`

- Vyžaduje nástroj `mksweph`.
- Konvertuje CSV do Swiss-Ephemeris `.se1` (`developer/swisseph/`).

```
cd developer/scripts
bash build_swisseph.sh
```

### `tools/update_orbital_elements.py`

- Stáhne nejnovější SBDB řešení, aktualizuje MPC soubory, KStars snippet a bloky Solar Fire.

```
python tools/update_orbital_elements.py
```

`--dry-run` pouze zobrazí hodnoty.

### `tools/verify_ephemeris.py`

- Kontroluje řádky `apps-using-mpc-files/geocentric_mpc_ephemeris.txt` proti live Horizons.

```
python tools/verify_ephemeris.py --start 2025-10-01 --days 5 --tolerance 5e-4
```

Výchozí: start 2025-10-01, 5 dní, tolerance `5e-4` AU (~75 000 km). Vrací nenulový kód, pokud narazí na odchylky (hodí se do CI).

## Servisní skripty

- **`tools/3i_elements_to_formats.py`** – převod nového MPC řádku do templátů (Stellarium, KStars, Solar Fire).
- **`tools/kstars/`** – helpery dle OS pro zálohu a přidání řádku do `comets.dat`.
- **`tools/solarfire/`** – Windows skripty pro automatické sloučení `extras.dat`.

## Klíčové milníky

- 2024-10-xx — první export Horizons, struktura projektu.
- 2025-10-xx — upgrade na SBDB řešení 27.
- 2025-10-xx — přidány verifikační skripty a importní balíček.

## Poznámky a upozornění

- **Solar Fire**: před sloučením vždy zálohujte `extras.dat`.
- **SkySafari**: nepodporuje ruční soubory; používejte *Update Orbit Data*.
- **Astro Gold / TimePassages**: pouze statické body.
- **Validace**: `tools/verify_ephemeris.py` rychle porovná data s Horizons.

## Řešení problémů

- **3I/ATLAS se nezobrazuje.** Restartujte aplikaci, ověřte zápis `3I/ATLAS`.
- **Pozice posunuté o den.** MPC soubor je značkován na **UT 0h**; pracujte v UTC nebo aplikujte časový offset.
- **Solar Fire má starý seznam.** Zkontrolujte správný `extras.dat` (verze mají vlastní složky) nebo spusťte APPLY znovu.
- **Potřebuji ověřit data.** `python tools/verify_ephemeris.py` porovná vybrané dny s Horizons.

Hodně zdaru s 3I/ATLAS!

## Volitelné: instalace nástrojů Horizons

Není nutné (data jsou součástí sady), ale pokud si chcete ephemeridy stahovat sami:

### macOS / Linux
1. Zkontrolujte `python3 --version` ≥ 3.10.
2. Nainstalujte Astroquery:
   ```bash
   python3 -m pip install astroquery --user
   ```
3. Dotaz na Horizons:
   ```bash
   python3 - <<'PY'
   from astroquery.jplhorizons import Horizons
   obj = Horizons(id='DES=1004083;', location='500@399', epochs={'start':'2025-01-01', 'stop':'2025-01-10', 'step':'1d'})
   print(obj.vectors())
   PY
   ```

Alternativa:

```bash
curl "https://ssd.jpl.nasa.gov/api/horizons.api?format=json&COMMAND='DES=1004083;'&MAKE_EPHEM=YES&EPHEM_TYPE=VECTORS&CENTER='500@399'&REF_PLANE=ECLIPTIC&STEP_SIZE=1%20d&START_TIME=2025-01-01&STOP_TIME=2025-01-03"
```

### Windows
1. Nainstalujte Python 3 z https://www.python.org/downloads/ (zaškrtněte „Add Python to PATH“).
2. PowerShell:
   ```powershell
   py -m pip install astroquery
   py - <<'PY'
   from astroquery.jplhorizons import Horizons
   obj = Horizons(id='DES=1004083;', location='500@399', epochs={'start':'2025-01-01', 'stop':'2025-01-10', 'step':'1d'})
   print(obj.vectors())
   PY
   ```
3. Uživatelé WSL následují pokyny pro macOS/Linux.

### Klasická CLI (Telnet)
```bash
telnet horizons.jpl.nasa.gov 6775
```
Postupujte podle pokynů, zadejte `DES=1004083;` a nastavte výstup.

### Instalace Pythonu 3.10+ na Linuxu

Použijte správce balíčků (apt, dnf, zypper, pacman…). Pokud není aktuální verze, využijte pyenv nebo sestavení ze zdrojů. I když systém Python má, doporučuje se vlastní instalace ≥3.10 a virtuální prostředí (`python3 -m venv`).
