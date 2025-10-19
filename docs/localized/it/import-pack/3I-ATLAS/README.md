# Pacchetto di importazione 3I/ATLAS

Modelli per un avvio rapido, script di supporto e documentazione per portare
**3I/ATLAS (C/2025 N1)** nei software astronomici compatibili MPC.

## Contenuto
- `docs/INSTALL_3I-ATLAS.md` — panoramica, avvertenze e guida rapida (versione attuale v0.2).
- `docs/WORKFLOWS.md` — istruzioni passo-passo per Stellarium, KStars,
  SkySafari, Solar Fire e note sulle app non supportate.
- `templates/` — elementi MPC a una riga pronti all'uso, riga `comets.dat` per KStars
  e blocco `[3I_ATLAS]` per Solar Fire (tutti basati sulla soluzione JPL SBDB 27).
- `tools/3i_elements_to_formats.py` — convertitore opzionale: incolla un nuovo
  elemento MPC a una riga e i modelli vengono aggiornati automaticamente.
- `tools/kstars/` — strumenti per Windows/macOS/Linux che eseguono il backup
  e aggiungono la riga di KStars.
- `tools/solarfire/` — strumenti per Windows che eseguono il backup e uniscono il blocco
  `extras.dat` per 3I/ATLAS.

## Istante d'uso
- Stellarium: importa la riga fornita tramite **Solar System Editor → Import elements in MPC format → File**.
- KStars: esegui lo script per il tuo sistema operativo oppure aggiungi manualmente la riga fornita a `comets.dat`.
- SkySafari: usa **Settings → Solar System → Update Orbit Data** (tier Plus/Pro).  
- Solar Fire: unisci il blocco `[3I_ATLAS]` in `extras.dat` (fai prima un backup).  
- Astro Gold / TimePassages: al momento non supportano l'importazione di corpi mobili; consulta le note del repository se ti servono punti fissi personalizzati.

Aggiorna i modelli con lo script di conversione ogni volta che esce una nuova soluzione orbitale.
