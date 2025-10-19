# App-Workflows für 3I/ATLAS

Alle Werte in diesem Paket stammen aus JPL-SBDB-Lösung 27 (2025-10-10).
Aktualisieren Sie die Dateien mit dem Konverter-Skript, sobald eine neuere Lösung erscheint.

## Stellarium (Windows/macOS/Linux)

**Akzeptiert:** MPC-Einzeiler für Kometen  
**Schritte:**
1. **Configuration → Plugins → Solar System Editor** → **Load at startup** aktivieren (ggf. neu starten).  
2. **Solar System Editor → Configure → Solar System → Import elements in MPC format → File**.  
3. Wählen Sie `templates/stellarium/3I_ATLAS_mpc_elements.txt`.  
4. **Add object(s)** anklicken und nach **3I/ATLAS** suchen.

## KStars (Windows/macOS/Linux)

**Akzeptiert:** `comets.dat`-Zeile  
**Helfer:**
- Windows: `tools/kstars/KStars_Append_3I-DRYRUN.bat` (Vorschau), danach `…-APPLY.bat`.  
- macOS: `tools/kstars/KStars_Append_3I.command` doppelklicken.  
- Linux: `bash tools/kstars/KStars_Append_3I.sh` ausführen.  
Alle Helfer legen vor dem Anhängen eine Sicherung an.

Manuell:
1. Sichern Sie `comets.dat` (`~/.local/share/kstars/comets.dat` unter Linux, `%LOCALAPPDATA%\kstars\comets.dat` unter Windows, `~/Library/Application Support/kstars/comets.dat` unter macOS).  
2. Hängen Sie die Zeile aus `templates/kstars/3I_ATLAS_comets_dat_snippet.txt` an.  
3. Starten Sie KStars neu und suchen Sie nach **3I/ATLAS**.

## SkySafari / SkyVoyager (iOS/Android)

**Akzeptiert:** keinen manuellen Import  
Verwenden Sie *Settings → Solar System → Update Orbit Data* (Plus/Pro-Stufen). Bewahren Sie
`templates/skysafari/3I_ATLAS_mpc_1line.txt` nur als Referenz auf.

## Cartes du Ciel (SkyCharts)

**Akzeptiert:** MPC-Elementdateien  
Folgen Sie den Anweisungen in `apps-using-mpc-files/cartes-du-ciel/README.txt`
(GUI-Import oder manuelles Anhängen an `comet.dat`).

## WinStars 3

**Akzeptiert:** MPC-Elementdateien  
Siehe `apps-using-mpc-files/winstars/README.txt` für die Schnellimport-Schritte.

## Solar Fire (Windows)

**Akzeptiert:** Orbitalelemente in `extras.dat` (Other Bodies)  
**Helfer:**
- Windows: `tools/solarfire/SF_Merge_3I-DRYRUN.bat` (Vorschau), anschließend `…-APPLY.bat`, um `[3I_ATLAS]` automatisch zu mergen.  
Beide Skripte sichern `extras.dat` mit Zeitstempel.

Manuell:
1. Beenden Sie Solar Fire und sichern Sie `Documents\Solar Fire User Files\Userdata\extras.dat`.  
2. Kopieren oder mergen Sie den `[3I_ATLAS]`-Block aus `templates/solar_fire/3I_ATLAS_extras_dat_PLACEHOLDER.txt`.  
3. Starten Sie neu und aktivieren Sie **3I/ATLAS** unter **Extra Bodies** in der Punktauswahl.

## Apps ohne Import-Schnittstellen

Astro Gold (macOS/iOS/iPadOS) und TimePassages Desktop (macOS/Windows) stellen
ausschließlich vom Anbieter bereitgestellte Zusatzpunkte zur Verfügung und
akzeptieren keine benutzerdefinierten Ephemeriden beweglicher Himmelskörper. Siehe Ordner
`Time-Passages-Astro-Gold/` für Workarounds (feste Punkte) und Kontakthinweise zum Anbieter.
