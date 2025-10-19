3I/ATLAS PER SOLAR FIRE (WINDOWS)
=================================

Solar Fire non importa efemeridi precalcolate per nuovi corpi; legge gli elementi orbitali da `extras.dat`. Questa cartella mantiene la voce di 3I/ATLAS allineata con la soluzione 27 del JPL SBDB.

Test su versioni
----------------
- Solar Fire 9: `Documents\Solar Fire 9 User Files\Points & Colors\extras.dat`
- Solar Fire 10: `Documents\Solar Fire User Files\Points & Colors\extras.dat`
- Solar Fire 11: `Documents\Solar Fire User Files\Points & Colors\extras.dat`

Contenuto
---------
- `extras.dat`: blocco `[3I_ATLAS]` pronto (vedi sotto) con commenti per fusioni manuali.
- `geocentric_daily_solarfire.txt` e simili: tabelle di riferimento opzionali per controlli fuori da Solar Fire.

Blocco di esempio
-----------------
Incolla questo blocco nel tuo `extras.dat` oppure lascia che lo script lo unisca automaticamente:

```
[3I_ATLAS]
Name = 3I/ATLAS
Number = 0
EpochJD = 2460884.5
PerihelionDistance_AU = 1.356065571
Eccentricity = 6.137350157
Inclination_deg = 175.112857794
AscendingNode_deg = 322.152284965
ArgumentOfPerihelion_deg = 128.011608252
PerihelionTime_JD = 2460977.983535961
AbsoluteMagnitude = 12.3
SlopeParameter = 4.5
; Solar Fire ignora il semiasse maggiore quando Tp è fornito per le comete.
; L'oggetto è iperbolico (e>1). Verifica la compatibilità con la tua versione di Solar Fire.
```

Passaggi di installazione
-------------------------
1. Chiudi Solar Fire.
2. Esegui gli script di supporto (`tools/solarfire/SF_Merge_3I-DRYRUN.bat`, poi `tools/solarfire/SF_Merge_3I-APPLY.bat`) **oppure** salva una copia del tuo `extras.dat` attuale.
3. Apri il percorso relativo alla tua versione (sopra) e aggiungi il blocco. Mantieni eventuali corpi personalizzati.
4. Riavvia Solar Fire, apri **File → File Types…** e assicurati che **Extra Bodies** punti al file aggiornato.
5. Nel dialogo di selezione punti, seleziona `3I/ATLAS` sotto **Extra Bodies / Other Bodies**.

Mini FAQ
--------
- **3I/ATLAS non compare dopo la fusione.** Controlla di aver modificato la cartella `extras.dat` corretta (Solar Fire mantiene cartelle diverse per ogni versione) e che il corpo sia abilitato in **Extra Bodies**.
- **Lo script segnala "access denied".** Chiudi Solar Fire prima di eseguire lo script APPLY; non può sovrascrivere un `extras.dat` aperto.
- **Servono elementi orbitali aggiornati.** Esegui `python tools/update_orbital_elements.py` dalla root del repository e rilancia lo script per sostituire il blocco con l'ultima soluzione SBDB.
