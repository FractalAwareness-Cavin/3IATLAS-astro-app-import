# 3I/ATLAS — Pacchetto di importazione (v0.2)

Usa questo pacchetto quando ti servono **elementi orbitali MPC pronti all'uso**
o un helper specifico per la piattaforma per portare 3I/ATLAS nel software di astronomia.
Tutto funziona offline e si basa sulla soluzione 27 del JPL SBDB (2025-10-10).

> **TL;DR**
> - **Stellarium** → importa la riga fornita tramite *Solar System Editor → Import elements in MPC format*.
> - **KStars** → esegui l'helper senza installazione (Windows/macOS/Linux) oppure incolla la riga `comets.dat` fornita.
> - **SkySafari** → usa *Settings → Solar System → Update Orbit Data* (Plus/Pro) e conserva la riga MPC come riferimento.
> - **Solar Fire** → unisci il blocco `[3I_ATLAS]` in `extras.dat` (prima fai un backup); sono inclusi script di supporto.
> - **Astro Gold / TimePassages** → al momento non supportano l'importazione di corpi mobili; consulta le note del repository principale per i workaround con punti fissi.

## Contenuto

- `templates/stellarium/3I_ATLAS_mpc_elements.txt` — elemento MPC a una riga per 3I/ATLAS.
- `templates/skysafari/3I_ATLAS_mpc_1line.txt` — la stessa riga, da conservare per archivio/riferimento.
- `templates/kstars/3I_ATLAS_comets_dat_snippet.txt` — riga pronta da aggiungere a `comets.dat` (valida anche per Cartes du Ciel / WinStars).
- `templates/solar_fire/3I_ATLAS_extras_dat_PLACEHOLDER.txt` — blocco `[3I_ATLAS]` già pronto per `extras.dat` di Solar Fire.
- `tools/3i_elements_to_formats.py` — convertitore opzionale se incolli una nuova riga MPC.
- `tools/update_orbital_elements.py` — recupera l'ultima soluzione JPL SBDB e riscrive tutte le template.
- `docs/WORKFLOWS.md` — istruzioni passo passo per Stellarium, KStars, Cartes du Ciel, WinStars, SkySafari, Solar Fire.

## Avvio rapido

Già aggiornato? Vai direttamente a `docs/WORKFLOWS.md`. Per eseguire l'aggiornamento ogni volta che JPL
pubblica una nuova orbita, esegui l'updater:
```bash
python tools/update_orbital_elements.py --dry-run  # anteprima degli ultimi elementi
python tools/update_orbital_elements.py            # riscrive le template
```
Se preferisci sostituire i file manualmente, `tools/3i_elements_to_formats.py`
genera gli snippet per Stellarium/KStars/Solar Fire da qualsiasi riga MPC.

## Avvertenze

- **Solar Fire `extras.dat`**: l'ordine dei campi può cambiare a seconda della versione. Consulta
l'help integrato “Format of the Orbital Elements File” quando modifichi manualmente e fai sempre un backup.
- **SkySafari**: non esiste un'importazione manuale di file; affidati a *Update Orbit Data*.
- **Astro Gold / TimePassages**: al momento non offrono un flusso di importazione per corpi mobili. Usa i punti personalizzati fissi o contatta il fornitore.
- **Validazione**: esegui `tools/verify_ephemeris.py` per confrontare righe selezionate di
`apps-using-mpc-files/geocentric_mpc_ephemeris.txt` con i dati live di Horizons se vuoi verificare l'efemeride.
