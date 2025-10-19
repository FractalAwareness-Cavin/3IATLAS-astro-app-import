# Kit di efemeridi 3I/ATLAS

Efemeridi giornaliere per il comet a interstellare **3I/ATLAS (C/2025 N1)**, generate direttamente da NASA/JPL Horizons e organizzate per consentire agli astrologi di inserirlo nelle proprie applicazioni. La copertura comprende l’intero passaggio nell’eliosfera (2016‑01‑01 → 2040‑12‑31). Questa release si basa sulla **soluzione Horizons n. 27 (2025‑10‑10)**; esegui `tools/update_orbital_elements.py` ogni volta che JPL pubblica una soluzione più recente per aggiornare gli ausili.

## Avvio rapido
1. Scarica il pacchetto corrispondente alla tua applicazione (vedi **Download diretti**) oppure clona il repository.
2. Estrai il pacchetto per accedere al `README` specifico della cartella.
3. Segui la checklist del `README` oppure esegui gli script helper inclusi per Solar Fire, KStars e Stellarium.
4. Manutenzione facoltativa: `python tools/update_orbital_elements.py` scarica l’ultima soluzione SBDB e `python tools/verify_ephemeris.py` confronta alcune date con Horizons prima di ridistribuire.

## Indice
- [Avvio rapido](#avvio-rapido)
- [App supportate (import corpi mobili)](#app-supportate-import-corpi-mobili)
- [Da dove cominciare?](#da-dove-cominciare)
- [Download diretti](#download-diretti)
- [Guida alle cartelle](#guida-alle-cartelle)
- [Glossario](#glossario)
- [Istruzioni per applicazione](#istruzioni-per-applicazione)
  - [Pack d’importazione & script](#pack-dimportazione--script)
  - [Stato di Astro Gold](#stato-di-astro-gold)
  - [Solar Fire (Windows)](#solarfire-instructions-windows)
  - [Import in formato MPC](#import-in-formato-mpc)
  - [Astro Gold & TimePassages](#astro-gold--timepassages)
  - [Note sui CSV](#note-sui-csv)
- [Ricetta Horizons](#ricetta-horizons)
- [Rigenerare le efemeridi](#rigenerare-le-efemeridi)
- [Script di manutenzione](#script-di-manutenzione)
- [Traguardi principali](#traguardi-principali)
- [Note e avvertenze](#note-e-avvertenze)
- [Risoluzione problemi](#risoluzione-problemi)
- [Opzionale: installare gli strumenti Horizons](#opzionale-installare-gli-strumenti-horizons)

App supportate (import corpi mobili)
------------------------------------
- **Stellarium** (Win/macOS/Linux) – import tramite Solar System Editor in formato MPC.
- **KStars** (Win/macOS/Linux) – append a `comets.dat` (helper forniti).
- **Solar Fire** (Windows) – merge del blocco `[3I_ATLAS]` in `extras.dat`.
- **Cartes du Ciel / SkyCharts** (Win/macOS/Linux) – import MPC o modifica di `comet.dat`.
- **WinStars 3** (Win/macOS/Linux) – incolla la linea MPC nell’editor.
- **SkySafari / SkyVoyager Plus/Pro** (iOS/Android/macOS) – aggiorna i dati orbitali dai feed MPC.

Senza import dinamico:
- **Astro Gold** (macOS/iOS/iPadOS) e **TimePassages** (macOS/Windows). Usa i workaround con punti fissi se serve una posizione statica.

Dubbi o problemi? Scrivi a [cavinbirdseyetarot@gmail.com](mailto:cavinbirdseyetarot@gmail.com) e perfezionerò la documentazione.



## Da dove cominciare?

Usa la cartella che corrisponde al tuo software oppure scarica uno dei pacchetti. Se non sei certo, controlla nel menu *File → Importa* quale formato accetta l’applicazione.

- `solar-fire/` – voce `extras.dat` per Solar Fire ed efemeridi di riferimento.
- `apps-using-mpc-files/` – `geocentric_mpc_ephemeris.txt` in formato MPC a 80 colonne (giornaliero, UT 0h, RA/Dec J2000, Δ, r, elongazione, fase).
- `apps-using-csv-files/` – vettori heliocentrici/geocentrici/baricentrici in CSV, ingressi nei segni, latitudini.
- `developer/` – dump JSON Horizons, script di rigenerazione, `pyswisseph` vendorizzato, helper Swiss Ephemeris.
- `Time-Passages-Astro-Gold/` – limiti attuali e soluzioni a punti fissi.

#### Download diretti
- [Helper di merge per Solar Fire (Windows)](https://github.com/FractalAwareness-Cavin/3IATLAS-astro-app-import/releases/download/v1.0.0/SolarFire_merge-helper_Windows.zip)
- [Append veloce KStars (Win/macOS/Linux)](https://github.com/FractalAwareness-Cavin/3IATLAS-astro-app-import/releases/download/v1.0.0/KStars_quick-append_Win-Mac-Linux.zip)
- [Import rapido Stellarium](https://github.com/FractalAwareness-Cavin/3IATLAS-astro-app-import/releases/download/v1.0.0/Stellarium_quick-import.zip)
- [Efemeride MPC (80 colonne)](https://github.com/FractalAwareness-Cavin/3IATLAS-astro-app-import/releases/download/v1.0.0/3I-ATLAS_apps_using_mpc_files.zip)
- [Kit di ricerca CSV](https://github.com/FractalAwareness-Cavin/3IATLAS-astro-app-import/releases/download/v1.0.0/3I-ATLAS_apps_using_csv_files.zip)

Ogni zip riproduce la cartella corrispondente e include un `README.txt` con le istruzioni: estrai prima di eseguire script o copiare file.

## Guida alle cartelle

- **solar-fire/** – extra per Solar Fire (`extras.dat`) e tabelle di riferimento.
- **apps-using-mpc-files/** – ephemeride MPC giornaliere, linee singole, guide per app.
- **apps-using-csv-files/** – tabelle CSV (heliocentrico, geocentrico, baricentrico), ingressi, metriche.
- **developer/** – script, `pyswisseph` incluso, dati grezzi, utility Swiss Ephemeris.
- **Time-Passages-Astro-Gold/** – workaround per software senza import.
- **import-pack/** – bundle compatto con template, script e documentazione.

## Glossario

- **MPC 80 colonne**: formato classico del Minor Planet Center.
- **Horizons SBDB**: Small-Body Database NASA/JPL.
- **Elongazione**: angolo Sole-oggetto visto dalla Terra.
- **Δ (delta)**: distanza geocentrica.
- **r**: distanza eliocentrica.
- **UT**: Universal Time / UTC.

## Istruzioni per applicazione

### Pack d’importazione & script

Dettagli in `import-pack/3I-ATLAS/README.md`: template, script, workflow di aggiornamento.

### Stato di Astro Gold

Nessun import di corpi mobili; consulta `Time-Passages-Astro-Gold/` per punti fissi personalizzati.

### SolarFire instructions Windows

`solar-fire/README.txt` spiega come fondere `[3I_ATLAS]` in `extras.dat`. Gli helper in `tools/solarfire/` offrono modalità Dry-Run/Apply.

### Import in formato MPC

`apps-using-mpc-files/` contiene README specifici per Stellarium, KStars, Cartes du Ciel, WinStars e i relativi file MPC.

### Astro Gold & TimePassages

Al momento non supportano corpi mobili; crea punti fissi con date specifiche.

### Note sui CSV

`apps-using-csv-files/README.txt` descrive colonne, unità e casi d’uso in fogli di calcolo, notebook o script. Per longitudini siderali sottrai l’ayanāṃśa dalla longitudine tropicale.

## Ricetta Horizons

`developer/raw/` ospita i JSON ottenuti da Horizons con:

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

Modifica i parametri per altre finestre temporali o centri di osservazione, poi aggiorna i JSON prima di rigenerare.

## Rigenerare le efemeridi

### `developer/scripts/generate_ephemeris.py`

- Legge i JSON in `developer/raw/` e ricostruisce:
  - Tabelle CSV (`apps-using-csv-files/`)
  - Tabelle testuali per Solar Fire (`solar-fire/`)
  - Efemeride MPC (`apps-using-mpc-files/geocentric_mpc_ephemeris.txt`)
  - Riepiloghi di ingresso nei segni.
- Crea le cartelle di destinazione se mancanti.

```
cd developer/scripts
python3 generate_ephemeris.py
```

### `developer/scripts/build_swisseph.sh`

- Richiede l’utility proprietaria `mksweph`.
- Converte i CSV in binari `.se1` di Swiss Ephemeris (`developer/swisseph/`).

```
cd developer/scripts
bash build_swisseph.sh
```

### `tools/update_orbital_elements.py`

- Scarica la soluzione SBDB più recente e aggiorna gli Einzeiler MPC, gli snippet KStars e i blocchi Solar Fire.

```
python tools/update_orbital_elements.py
```

Aggiungi `--dry-run` per visualizzare i valori senza modificare file.

### `tools/verify_ephemeris.py`

- Confronta righe di `apps-using-mpc-files/geocentric_mpc_ephemeris.txt` con Horizons live.

```
python tools/verify_ephemeris.py --start 2025-10-01 --days 5 --tolerance 5e-4
```

Predefiniti: start `2025-10-01`, `days=5`, `tolerance=5e-4` UA (≈75.000 km). Esce con codice ≠0 se rileva scarti, utile per CI.

## Script di manutenzione

- **`tools/3i_elements_to_formats.py`**: converte un nuovo Einzeiler MPC in template (Stellarium, KStars, Solar Fire).
- **`tools/kstars/`**: helper per OS per salvare e aggiungere a `comets.dat`.
- **`tools/solarfire/`**: helper Windows per unire automaticamente `extras.dat`.

## Traguardi principali

- 2024-10-xx – prima estrazione Horizons e struttura directory.
- 2025-10-xx – aggiornamento alla soluzione SBDB 27.
- 2025-10-xx – aggiunti script di verifica e pacchetto di import.

## Note e avvertenze

- **Solar Fire**: crea un backup di `extras.dat` prima del merge.
- **SkySafari**: nessun import file; usare *Update Orbit Data*.
- **Astro Gold / TimePassages**: niente import dinamico; affidarsi a punti fissi.
- **Validazione**: `tools/verify_ephemeris.py` confronta rapidamente con Horizons.

## Risoluzione problemi

- **3I/ATLAS non compare dopo l’import.** Riavvia l’app e verifica l’ortografia `3I/ATLAS`.
- **Posizioni sfalsate di un giorno.** Il file MPC è timbrato a **UT 0h**; lavora in UTC o applica la correzione di fuso.
- **Solar Fire mostra ancora la lista vecchia.** Controlla il percorso `extras.dat` (ogni major version ha una propria cartella) o riesegui lo script APPLY.
- **Voglio verificare i dati.** `python tools/verify_ephemeris.py` confronta con Horizons in tempo reale.

Buone osservazioni con 3I/ATLAS!

## Opzionale: installare gli strumenti Horizons

Non è obbligatorio (il kit include già i dati), ma se vuoi estrarli autonomamente:

### macOS / Linux
1. Verifica che `python3 --version` sia ≥ 3.10.
2. Installa Astroquery:
   ```bash
   python3 -m pip install astroquery --user
   ```
3. Interroga Horizons:
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
1. Installa Python 3 da https://www.python.org/downloads/ (seleziona “Add Python to PATH”).
2. In PowerShell:
   ```powershell
   py -m pip install astroquery
   py - <<'PY'
   from astroquery.jplhorizons import Horizons
   obj = Horizons(id='DES=1004083;', location='500@399', epochs={'start':'2025-01-01', 'stop':'2025-01-10', 'step':'1d'})
   print(obj.vectors())
   PY
   ```
3. In WSL segui le istruzioni macOS/Linux.

### CLI classica (Telnet)
```bash
telnet horizons.jpl.nasa.gov 6775
```
Segui le indicazioni per inserire `DES=1004083;` e le opzioni di output.

### Installare Python 3.10+ su Linux

Usa il gestore pacchetti (apt, dnf, zypper, pacman…). Se la distribuzione non fornisce la versione richiesta, passa a pyenv o compila dai sorgenti. Anche se il sistema ha già Python, conviene installare una versione dedicata ≥3.10 e usare ambienti virtuali (`python3 -m venv`).
