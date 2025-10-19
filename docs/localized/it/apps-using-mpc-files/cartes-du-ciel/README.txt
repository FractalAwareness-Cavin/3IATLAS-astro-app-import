3I/ATLAS — Importazione rapida Cartes du Ciel (SkyCharts)
========================================================

Cartes du Ciel legge i classici elementi cometari MPC. Usa la riga fornita (`../import-pack/3I-ATLAS/templates/stellarium/3I_ATLAS_mpc_elements.txt`) o la copia qui presente per aggiungere 3I/ATLAS.

### Opzione A — import via GUI
1. Avvia Cartes du Ciel.
2. Apri **Setup → Solar system** (o `Ctrl+F3`).
3. Nella scheda **Comets** clicca **Update** (o **Import from MPC file**).
4. Seleziona **File on disk** e scegli `3I_ATLAS_mpc_1line.txt`.
5. Dopo l'import, spunta **3I/ATLAS** nell'elenco e premi **OK**.

### Opzione B — modifica manuale
1. Chiudi Cartes du Ciel.
2. Esegui il backup di `comet.dat`:
   - Windows: `%LOCALAPPDATA%\Skychart\cat\comet.dat`
   - Linux: `~/.skychart/cat/comet.dat`
   - macOS: `~/Library/Application Support/skychart.cat/comet.dat`
3. Aggiungi la riga di `3I_ATLAS_mpc_1line.txt` al file `comet.dat`.
4. Riavvia Cartes du Ciel e abilita **3I/ATLAS** nella lista comete.

La riga deriva dalla soluzione 27 del JPL SBDB (2025-10-10). Reimportala ogni volta che esce una nuova soluzione.
