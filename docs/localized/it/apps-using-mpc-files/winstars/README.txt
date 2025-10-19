3I/ATLAS — Importazione rapida WinStars
======================================

WinStars (v3) può leggere elementi MPC tramite l'editor integrato.

### Metodo 1 — incollare la riga singola
1. Avvia WinStars.
2. Apri **Preferences → Solar system → Import orbital elements** (oppure **Add object**).
3. Seleziona **MPC single line** e incolla il contenuto di `3I_ATLAS_mpc_1line.txt`.
4. Conferma e verifica che 3I/ATLAS sia attivo nell'elenco dei corpi visualizzati.

### Metodo 2 — sostituire il file delle comete (avanzato)
1. Chiudi WinStars.
2. Fai il backup del file comets:
   - Windows: `%APPDATA%\WinStars3\databases\comets.txt`
   - Linux: `~/.config/WinStars3/databases/comets.txt`
3. Aggiungi a quel file la riga da `3I_ATLAS_mpc_1line.txt`.
4. Riavvia WinStars; 3I/ATLAS sarà presente nell'elenco delle comete.

Il file a riga singola si basa sulla soluzione 27 del JPL SBDB (2025-10-10). Aggiorna ogni volta che esce una nuova soluzione.
