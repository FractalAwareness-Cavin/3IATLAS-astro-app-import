3I/ATLAS FÜR SOLAR FIRE (WINDOWS)
=================================

Solar Fire importiert keine vorkalkulierten Ephemeriden für neue Körper; die Software liest Orbitalelemente aus `extras.dat`. Dieser Ordner hält den 3I/ATLAS-Eintrag synchron mit JPL-SBDB-Lösung 27.

Getestet mit
------------
- Solar Fire 9: `Documents\Solar Fire 9 User Files\Points & Colors\extras.dat`
- Solar Fire 10: `Documents\Solar Fire User Files\Points & Colors\extras.dat`
- Solar Fire 11: `Documents\Solar Fire User Files\Points & Colors\extras.dat`

Inhalt
------
- `extras.dat`: fertiger `[3I_ATLAS]`-Block (siehe unten) plus Kommentare für manuelle Merges.
- `geocentric_daily_solarfire.txt` und ähnliche Dateien: optionale Referenztabellen, falls Sie Positionen außerhalb von Solar Fire gegenprüfen möchten.

Beispielblock
-------------
Fügen Sie diesen Block in Ihr bestehendes `extras.dat` ein oder lassen Sie den Helper ihn automatisch mergen:

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
; Solar Fire ignoriert die große Halbachse, wenn Tp für Kometen angegeben ist.
; Dieses Objekt ist hyperbolisch (e>1). Prüfen Sie die Kompatibilität Ihrer Solar-Fire-Version.
```

Installationsschritte
---------------------
1. Solar Fire beenden.
2. Helferskripte ausführen (`tools/solarfire/SF_Merge_3I-DRYRUN.bat`, anschließend `tools/solarfire/SF_Merge_3I-APPLY.bat`) **oder** das aktuelle `extras.dat` sichern.
3. Öffnen Sie den Pfad der passenden Version (siehe oben) und hängen Sie den Block an. Eigene Zusatzkörper bleiben erhalten.
4. Solar Fire neu starten, **File → File Types…** öffnen und sicherstellen, dass **Extra Bodies** auf die aktualisierte Datei zeigt.
5. Im Punktauswahldialog `3I/ATLAS` unter **Extra Bodies / Other Bodies** aktivieren.

Mini-FAQ
--------
- **3I/ATLAS erscheint nicht nach dem Merge.** Prüfen Sie, ob Sie den richtigen `extras.dat`-Ordner bearbeitet haben (Solar Fire nutzt pro Hauptversion eigene Benutzerordner) und ob der Körper unter **Extra Bodies** aktiviert ist.
- **Helper meldet "access denied".** Schließen Sie Solar Fire vor dem APPLY-Skript; ein offenes `extras.dat` kann nicht überschrieben werden.
- **Aktuellere Orbitalelemente benötigt.** Führen Sie `python tools/update_orbital_elements.py` im Repository-Stamm aus und lassen Sie danach den Helper laufen, um den Block mit der neuesten SBDB-Lösung zu ersetzen.
