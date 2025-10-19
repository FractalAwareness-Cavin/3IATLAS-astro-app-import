KIT PER SVILUPPATORI
===================

Questa cartella contiene tutto il necessario per rigenerare da zero
il pacchetto di efemeridi.

Contenuto
---------
- `raw/` – risposte JSON ottenute dall'API NASA/JPL Horizons.
- `scripts/generate_ephemeris.py` – script Python che ricostruisce i CSV,
  i file di testo per Solar Fire, l'output MPC e i riepiloghi degli ingressi nei segni.
- `scripts/build_swisseph.sh` – helper che trasforma le tabelle CSV in binari
  Swiss Ephemeris `.se1` (richiede `mksweph`).
- `vendor/` – modulo `pyswisseph` incluso per ottenere output siderali
  senza installazioni aggiuntive.

Rigenerazione
-------------
```
cd developer/scripts
python3 generate_ephemeris.py
```
Lo script interroga nuovamente Horizons (serve connessione) e aggiorna
le cartelle nella root del repository.

Binari Swiss Ephemeris
----------------------
Se disponi dell'utility proprietaria `mksweph`:
```
cd developer/scripts
bash build_swisseph.sh
```
I file `.se1` vengono scritti in `../swisseph/` pronti per la distribuzione.

Modifica liberamente lo script per cambiare cadenza, sistemi di coordinate
o corpi centrali; i JSON grezzi garantiscono la tracciabilità verso Horizons.

Per note d'uso dettagliate, incluso l'aggiornamento SBDB e gli helper di verifica,
consulta `scripts/README.md`.
