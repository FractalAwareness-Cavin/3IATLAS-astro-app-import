# Ontwikkelaarsscripts

De tools om het 3I/ATLAS-efemeridenpakket te regenereren en te valideren staan in `developer/scripts/` en `tools/`. Gebruik deze gids wanneer je de dataset wilt verversen of wijzigingen wilt controleren voordat je een release publiceert.

## Vereisten
- Python 3.10 of nieuwer (`python3 --version` ter controle).
- Optioneel: een virtuele omgeving (`python3 -m venv .venv && source .venv/bin/activate`) als je extra pakketten installeert.
- Internettoegang bij het draaien van de SBDB-updater of de Horizons-verificatie.
- Optioneel: `mksweph` om Swiss-Ephemeris-binaries te bouwen met `build_swisseph.sh`.

Het repository levert `pyswisseph` mee in `developer/vendor/`, zodat siderische output zonder extra installaties werkt.

## Standaard Horizons-recept

De ruwe JSON-bestanden in `developer/raw/` zijn met NASA/JPL Horizons gegenereerd met deze parameters:

```
COMMAND='DES=1004083;'
MAKE_EPHEM='YES'
EPHEM_TYPE='VECTORS'
CENTER='500@399'        # aardcentrum
REF_PLANE='ECLIPTIC'
REF_SYSTEM='J2000'
START_TIME='2016-01-01'
STOP_TIME='2040-12-31'
STEP_SIZE='1 d'
TABLE_TYPE='VECTORS'
```

Pas de waarden aan voor een ander tijdsvenster of gezichtspunt en vernieuw de JSON-bestanden voordat je outputs herbouwt.

## `generate_ephemeris.py`
Locatie: `developer/scripts/generate_ephemeris.py`

- Leest de JSON-vector-dumps in `developer/raw/` en herschrijft alle afgeleide producten:
  - CSV-tabellen in `apps-using-csv-files/`
  - Solar-Fire-teksttabellen in `solar-fire/`
  - MPC-efemeriden (`apps-using-mpc-files/geocentric_mpc_ephemeris.txt`)
  - Samenvattingen van teken-ingressen.
- Laadt automatisch de meegeleverde module `pyswisseph` om siderische kolommen te vullen.
- Maakt doelmappen aan als ze nog niet bestaan.

Gebruik:

```
cd developer/scripts
python3 generate_ephemeris.py
```

Het script draait met ingebakken instellingen. Wil je de periode of cadence veranderen, werk dan eerst de JSON's bij (of wijzig de constante waarden in de header).

## `build_swisseph.sh`
Locatie: `developer/scripts/build_swisseph.sh`

- Vereist de proprietaire tool `mksweph`.
- Converteert de CSV-uitvoer naar Swiss-Ephemeris-`.se1`-binaries in `developer/swisseph/`.

Gebruik:

```
cd developer/scripts
bash build_swisseph.sh
```

De helper voert niets uit als `mksweph` niet op de `PATH` staat.

## `tools/update_orbital_elements.py`
Locatie: `tools/update_orbital_elements.py`

- Haalt de nieuwste SBDB-baanoplossing voor 3I/ATLAS op en werkt alle eenregelige sjablonen bij:
  - MPC-bestanden (`apps-using-mpc-files/*/3I_ATLAS_mpc_1line.txt`)
  - KStars-snippets (`apps-using-mpc-files/kstars/` en import-pack-sjablonen)
  - Solar-Fire-`extras.dat`-blokken.
- Drukt de opgehaalde elementen af naar stdout voor controle.

Gebruik (in de root van de repository):

```
python tools/update_orbital_elements.py
```

Voeg `--dry-run` toe om de waarden alleen te bekijken.

## `tools/verify_ephemeris.py`
Locatie: `tools/verify_ephemeris.py`

- Controleert rijen uit `apps-using-mpc-files/geocentric_mpc_ephemeris.txt` tegen live Horizons-gegevens.
- Vergelijkt de geocentrische afstand (“delta”) over een configureerbare periode en markeert rijen die buiten de tolerantie vallen.

Gebruik (in de root van de repository):

```
python tools/verify_ephemeris.py --start 2025-10-01 --days 5 --tolerance 5e-4
```

Argumenten:
- `--start`: eerste datum voor controle (standaard `2025-10-01`).
- `--days`: aantal opeenvolgende dagen (standaard `5`).
- `--tolerance`: toegestane afwijking in astronomische eenheden (standaard `5e-4`, ~75.000 km).

Het script geeft een niet-nul exitcode terug als er fouten zijn en is daardoor bruikbaar in CI.
