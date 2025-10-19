# Script per sviluppatori

Le utility per rigenerare e validare il kit di efemeridi 3I/ATLAS si trovano in `developer/scripts/` e `tools/`. Usa questa guida quando devi aggiornare il dataset o verificare le modifiche prima di pubblicare una nuova release.

## Prerequisiti
- Python 3.10 o successivo (`python3 --version` per controllare).
- Opzionale: un ambiente virtuale (`python3 -m venv .venv && source .venv/bin/activate`) se prevedi di installare pacchetti aggiuntivi.
- Accesso a Internet quando esegui l'aggiornamento SBDB o il verificatore Horizons.
- Opzionale: `mksweph` se vuoi generare binari Swiss Ephemeris con `build_swisseph.sh`.

Il repository include `pyswisseph` in `developer/vendor/`, per cui le uscite siderali funzionano senza installazioni extra.

## Ricetta Horizons predefinita

I JSON grezzi in `developer/raw/` sono stati generati con NASA/JPL Horizons usando i seguenti parametri:

```
COMMAND='DES=1004083;'
MAKE_EPHEM='YES'
EPHEM_TYPE='VECTORS'
CENTER='500@399'        # centro della Terra
REF_PLANE='ECLIPTIC'
REF_SYSTEM='J2000'
START_TIME='2016-01-01'
STOP_TIME='2040-12-31'
STEP_SIZE='1 d'
TABLE_TYPE='VECTORS'
```

Modifica questi valori se ti serve un intervallo temporale o un punto di vista diverso, poi rigenera i JSON prima di ricostruire i risultati.

## `generate_ephemeris.py`
Percorso: `developer/scripts/generate_ephemeris.py`

- Legge i dump JSON in `developer/raw/` e riscrive ogni prodotto derivato:
  - Tabelle CSV in `apps-using-csv-files/`
  - Tabelle testuali per Solar Fire in `solar-fire/`
  - Efemeride MPC (`apps-using-mpc-files/geocentric_mpc_ephemeris.txt`)
  - Riepiloghi degli ingressi nei segni.
- Carica automaticamente il modulo `pyswisseph` incluso per riempire i campi siderali.
- Crea le directory di destinazione se non esistono.

Uso:

```
cd developer/scripts
python3 generate_ephemeris.py
```

Lo script utilizza impostazioni predefinite. Per modificare intervallo o cadenza, aggiorna prima i JSON (oppure modifica le costanti nella parte iniziale del file).

## `build_swisseph.sh`
Percorso: `developer/scripts/build_swisseph.sh`

- Richiede l'utility proprietaria `mksweph`.
- Converte gli output CSV in binari `.se1` di Swiss Ephemeris e li salva in `developer/swisseph/`.

Uso:

```
cd developer/scripts
bash build_swisseph.sh
```

L'helper si interrompe se `mksweph` non è presente nel `PATH`.

## `tools/update_orbital_elements.py`
Percorso: `tools/update_orbital_elements.py`

- Recupera l'ultima soluzione orbitale SBDB per 3I/ATLAS e aggiorna tutte le template a riga singola:
  - File MPC (`apps-using-mpc-files/*/3I_ATLAS_mpc_1line.txt`)
  - Snippet per KStars (`apps-using-mpc-files/kstars/` e modelli del pacchetto di importazione)
  - Blocchi `extras.dat` di Solar Fire.
- Stampa gli elementi recuperati su stdout per consentire la verifica.

Uso (dalla root del repository):

```
python tools/update_orbital_elements.py
```

Aggiungi `--dry-run` per visualizzare i valori senza modificare i file.

## `tools/verify_ephemeris.py`
Percorso: `tools/verify_ephemeris.py`

- Confronta un campione di righe da `apps-using-mpc-files/geocentric_mpc_ephemeris.txt` con i dati live di Horizons.
- Confronta la distanza geocentrica ("delta") su un intervallo configurabile e segnala le righe che superano la tolleranza.

Uso (dalla root del repository):

```
python tools/verify_ephemeris.py --start 2025-10-01 --days 5 --tolerance 5e-4
```

Argomenti:
- `--start`: data iniziale da verificare (default `2025-10-01`).
- `--days`: numero di giorni consecutivi (default `5`).
- `--tolerance`: differenza massima ammessa in unità astronomiche (default `5e-4`, circa 75 000 km).

Lo script restituisce un codice di uscita diverso da zero se trova discrepanze, così può essere usato in CI.
