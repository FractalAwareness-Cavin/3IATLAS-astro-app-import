# Skripty pro vývojáře

Nástroje pro regeneraci a ověřování sady efemerid 3I/ATLAS najdete v `developer/scripts/` a `tools/`. Tento návod využijte při aktualizaci dat nebo kontrole změn před vydáním nové verze.

## Požadavky
- Python 3.10 nebo novější (`python3 --version`).
- Volitelně: virtuální prostředí (`python3 -m venv .venv && source .venv/bin/activate`), pokud instalujete další balíčky.
- Přístup k internetu při spuštění SBDB updateru nebo verifikace Horizons.
- Volitelně: `mksweph`, chcete-li vytvářet binárky Swiss Ephemeris pomocí `build_swisseph.sh`.

Repozitář dodává `pyswisseph` ve složce `developer/vendor/`, takže siderické výstupy fungují bez extra instalací.

## Výchozí recept Horizons

Surové JSONy v `developer/raw/` byly vygenerovány na NASA/JPL Horizons s těmito parametry:

```
COMMAND='DES=1004083;'
MAKE_EPHEM='YES'
EPHEM_TYPE='VECTORS'
CENTER='500@399'        # střed Země
REF_PLANE='ECLIPTIC'
REF_SYSTEM='J2000'
START_TIME='2016-01-01'
STOP_TIME='2040-12-31'
STEP_SIZE='1 d'
TABLE_TYPE='VECTORS'
```

Upravte hodnoty podle potřeby (rozsah dat, stanoviště) a před regenerací nechte JSONy znovu vytvořit.

## `generate_ephemeris.py`
Umístění: `developer/scripts/generate_ephemeris.py`

- Čte JSON výstupy ve `developer/raw/` a přepočítává všechny derivované produkty:
  - CSV tabulky v `apps-using-csv-files/`
  - Textové tabulky pro Solar Fire v `solar-fire/`
  - Efermeridu MPC (`apps-using-mpc-files/geocentric_mpc_ephemeris.txt`)
  - Souhrny vstupů do znamení.
- Automaticky načte přibalený modul `pyswisseph`, aby doplnil siderická pole.
- Vytvoří cílové adresáře, pokud chybí.

Použití:

```
cd developer/scripts
python3 generate_ephemeris.py
```

Skript využívá pevné nastavení. Pro změnu časového rozpětí nebo kroku nejprve aktualizujte JSONy (případně upravte konstanty na začátku skriptu).

## `build_swisseph.sh`
Umístění: `developer/scripts/build_swisseph.sh`

- Vyžaduje proprietární utilitu `mksweph`.
- Převádí výstupy CSV na binárky Swiss Ephemeris `.se1` a ukládá je do `developer/swisseph/`.

Použití:

```
cd developer/scripts
bash build_swisseph.sh
```

Pomocník skončí s chybou, pokud `mksweph` není v proměnné `PATH`.

## `tools/update_orbital_elements.py`
Umístění: `tools/update_orbital_elements.py`

- Stahuje poslední orbitální řešení SBDB pro 3I/ATLAS a aktualizuje všechny jednořádkové šablony:
  - MPC soubory (`apps-using-mpc-files/*/3I_ATLAS_mpc_1line.txt`)
  - Úryvky pro KStars (`apps-using-mpc-files/kstars/` a šablony importního balíčku)
  - Bloky `extras.dat` pro Solar Fire.
- Vypisuje získané elementy na stdout pro kontrolu.

Použití (z kořene repozitáře):

```
python tools/update_orbital_elements.py
```

Přidejte `--dry-run`, chcete-li vidět hodnoty bez změny souborů.

## `tools/verify_ephemeris.py`
Umístění: `tools/verify_ephemeris.py`

- Porovnává vybrané řádky `apps-using-mpc-files/geocentric_mpc_ephemeris.txt` s živými daty Horizons.
- Sleduje geocentrickou vzdálenost („delta“) v nastavitelném intervalu a označí řádky přesahující toleranci.

Použití (z kořene repozitáře):

```
python tools/verify_ephemeris.py --start 2025-10-01 --days 5 --tolerance 5e-4
```

Parametry:
- `--start`: první kontrolované datum (výchozí `2025-10-01`).
- `--days`: počet po sobě jdoucích dnů (výchozí `5`).
- `--tolerance`: maximální povolená odchylka v astronomických jednotkách (výchozí `5e-4`, cca 75 000 km).

Skript vrací nenulový kód, pokud některé řádky nevyhoví, takže je vhodný pro CI.
