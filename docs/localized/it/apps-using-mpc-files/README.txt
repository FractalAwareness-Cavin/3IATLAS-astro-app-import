3I/ATLAS – GUIDA ALL'IMPORT MPC
===============================

`geocentric_mpc_ephemeris.txt` contiene efemeridi giornaliere in stile MPC (UT 0h, RA/Dec J2000, delta, r, elongazione, fase). Usala ovunque il software accetti il formato cometa a 80 colonne. I pacchetti pronti sono nelle release (vedi `README.md` principale) o in `apps-using-mpc-files/`.

Pacchetti release
-----------------
- `Stellarium_quick-import.zip`: importa l'oggetto singolo via plugin Solar System Editor.
- `KStars_quick-append_Win-Mac-Linux.zip`: helper dry-run/apply per `comets.dat` su ogni piattaforma.
- `3I-ATLAS_apps_using_mpc_files.zip`: include l'intera cartella, con template a riga singola per Cartes du Ciel e WinStars.

Stellarium (Win/macOS/Linux)
----------------------------
1. Estrai `Stellarium_quick-import.zip` oppure copia `geocentric_mpc_ephemeris.txt` in una posizione nota.
2. In Stellarium premi `F2`, apri **Plugins → Solar System Editor**, attiva **Load at startup** e premi **Configure**. Riavvia se appena abilitato.
3. Dopo il riavvio apri **Solar System Editor → Solar System** e clicca **Import orbital elements in MPC format**.
4. Seleziona **Select file**, scegli `geocentric_mpc_ephemeris.txt` (o il file a riga singola), imposta **Object name** su `3I/ATLAS` e lascia **Object type** su *Comet*.
5. Premi **Add objects**, chiudi e verifica con `F3` che `3I/ATLAS` sia disponibile.

KStars (Win/macOS/Linux)
------------------------
1. Estrai `KStars_quick-append_Win-Mac-Linux.zip` ed esegui lo script adatto (`*.bat`, `*.command`, `*.sh`, `*.ps1`). Parti da DRYRUN, poi APPLY per scrivere su `comets.dat`.
2. Alternativa manuale: **Settings → Configure KStars → Solar System** (versioni vecchie: **Data → Solar System Updates**). Nella scheda **Comets** clicca **Import**, seleziona `geocentric_mpc_ephemeris.txt` e conferma.
3. Riavvia KStars se richiesto, quindi cerca `3I/ATLAS` o controlla il Solar System Viewer.

Cartes du Ciel / SkyCharts
--------------------------
1. Copia `apps-using-mpc-files/cartes-du-ciel/3I_ATLAS_mpc_1line.txt` (compreso nel pacchetto release).
2. Avvia Cartes du Ciel e vai su **Setup → Solar system** (`Ctrl+F3`).
3. Nella scheda **Comets** seleziona **Update → Import from MPC file**, scegli `3I_ATLAS_mpc_1line.txt` e conferma.
4. Spunta **3I/ATLAS** e premi **OK**. La cometa è ora ricercabile e visibile.
5. Preferisci la modifica manuale? Aggiungi la stessa riga a `comet.dat` (consulta il README specifico per i percorsi).

WinStars 3 (Win/macOS/Linux)
----------------------------
1. Tieni a portata `apps-using-mpc-files/winstars/3I_ATLAS_mpc_1line.txt` o estrai l'archivio MPC.
2. In WinStars apri **Preferences → Solar system → Import orbital elements** (o **Add object**).
3. Scegli l'opzione **MPC single line**, incolla il contenuto e salva.
4. Controlla che `3I/ATLAS` sia attivata nella lista degli oggetti; riavvia se il cache era aperto.

SkySafari / SkyVoyager Plus/Pro (iOS/Android/macOS)
---------------------------------------------------
1. Copia il file `3I_ATLAS_mpc_1line.txt` in un editor accessibile dal dispositivo.
2. In SkySafari apri **Settings → Solar System → Solar System Data** e tocca **Import Comet Data** (o **Update Orbit Data → Custom Comet/Asteroid** nelle versioni precedenti).
3. Incolla la riga MPC, assicurati che il nome sia `3I/ATLAS` e conferma.
4. Cerca `3I/ATLAS` e aggiungila alle liste di osservazione se vuoi.
5. L'app aggiorna periodicamente i feed MPC; ripeti l'import dopo ogni aggiornamento orbitale.

Altri software compatibili MPC
------------------------------
1. Copia `geocentric_mpc_ephemeris.txt` o il template a riga singola.
2. Usa la funzione di import comete/asteroidi del software, seleziona il file e imposta il nome `3I/ATLAS`.
3. Riavvia se il programma mette in cache i dati del sistema solare e verifica che l'oggetto sia attivo.

Mantieni aggiornate le righe singole eseguendo `python tools/update_orbital_elements.py` ogni volta che il JPL pubblica una nuova soluzione SBDB e controlla le posizioni con `python tools/verify_ephemeris.py` per maggiore sicurezza.
