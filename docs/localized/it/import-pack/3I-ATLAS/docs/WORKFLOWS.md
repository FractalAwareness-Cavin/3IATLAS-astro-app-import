# Flussi di lavoro per 3I/ATLAS

Tutti i valori di questo pacchetto provengono dalla soluzione 27 del JPL SBDB (2025-10-10).
Aggiorna i file con lo script di conversione quando esce una soluzione più recente.

## Stellarium (Windows/macOS/Linux)

**Accetta:** elementi cometari MPC a una riga  
**Passaggi:**
1. **Configuration → Plugins → Solar System Editor** → spunta **Load at startup** (riavvia se necessario).  
2. **Solar System Editor → Configure → Solar System → Import elements in MPC format → File**.  
3. Seleziona `templates/stellarium/3I_ATLAS_mpc_elements.txt`.  
4. Clicca **Add object(s)** e cerca **3I/ATLAS**.

## KStars (Windows/macOS/Linux)

**Accetta:** riga `comets.dat`  
**Helper:**
- Windows: `tools/kstars/KStars_Append_3I-DRYRUN.bat` (anteprima), poi `…-APPLY.bat`.  
- macOS: fai doppio clic su `tools/kstars/KStars_Append_3I.command`.  
- Linux: esegui `bash tools/kstars/KStars_Append_3I.sh`.  
Tutti gli helper eseguono un backup prima di aggiungere la riga.

Manuale:
1. Effettua il backup di `comets.dat` (`~/.local/share/kstars/comets.dat` su Linux, `%LOCALAPPDATA%\kstars\comets.dat` su Windows, `~/Library/Application Support/kstars/comets.dat` su macOS).  
2. Aggiungi la riga singola contenuta in `templates/kstars/3I_ATLAS_comets_dat_snippet.txt`.  
3. Riavvia KStars e cerca **3I/ATLAS**.

## SkySafari / SkyVoyager (iOS/Android)

**Accetta:** nessuna importazione manuale  
Usa *Settings → Solar System → Update Orbit Data* (tier Plus/Pro). Conserva
`templates/skysafari/3I_ATLAS_mpc_1line.txt` come riferimento.

## Cartes du Ciel (SkyCharts)

**Accetta:** file di elementi MPC  
Segui le istruzioni in `apps-using-mpc-files/cartes-du-ciel/README.txt`
(import via interfaccia grafica o aggiunta manuale a `comet.dat`).

## WinStars 3

**Accetta:** file di elementi MPC  
Consulta `apps-using-mpc-files/winstars/README.txt` per i passaggi di importazione rapida.

## Solar Fire (Windows)

**Accetta:** elementi orbitali di `extras.dat` (Other Bodies)  
**Helper:**
- Windows: `tools/solarfire/SF_Merge_3I-DRYRUN.bat` (anteprima), poi `…-APPLY.bat` per unire automaticamente `[3I_ATLAS]`.  
Entrambi gli script creano un backup di `extras.dat` con timestamp.

Manuale:
1. Chiudi Solar Fire e crea una copia di `Documents\Solar Fire User Files\Userdata\extras.dat`.  
2. Copia o unisci il blocco `[3I_ATLAS]` da `templates/solar_fire/3I_ATLAS_extras_dat_PLACEHOLDER.txt`.  
3. Riavvia e abilita **3I/ATLAS** in **Extra Bodies** nella finestra di scelta dei punti.

## App senza percorso di importazione

Astro Gold (macOS/iOS/iPadOS) e TimePassages Desktop (macOS/Windows) espongono solo
punti extra forniti dal produttore e non accettano efemeridi di corpi mobili definite dall'utente.
Consulta la cartella `Time-Passages-Astro-Gold/` per i workaround con punti fissi e i contatti del fornitore.
