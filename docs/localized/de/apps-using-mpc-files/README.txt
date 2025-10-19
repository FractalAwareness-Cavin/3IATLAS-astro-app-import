3I/ATLAS – MPC-IMPORTLEITFADEN
===============================

`geocentric_mpc_ephemeris.txt` enthält tägliche MPC-Ephemeriden (UT 0h, RA/Dec J2000, Delta, r, Elongation, Phase). Verwenden Sie die Datei überall dort, wo Ihre Software das klassische 80-Spalten-Kometenformat akzeptiert. Fertige Bundles finden Sie in den Releases (siehe `README.md` im Root) oder direkt hier in `apps-using-mpc-files/`.

Release-Bundles
---------------
- `Stellarium_quick-import.zip`: importiert die MPC-Einzeldatei über das Solar-System-Editor-Plugin.
- `KStars_quick-append_Win-Mac-Linux.zip`: Preview/Apply-Helfer für `comets.dat` auf allen Plattformen.
- `3I-ATLAS_apps_using_mpc_files.zip`: enthält diesen gesamten Ordner inklusive Einzeiler-Vorlagen für Cartes du Ciel und WinStars.

Stellarium (Win/macOS/Linux)
----------------------------
1. Entpacken Sie `Stellarium_quick-import.zip` oder kopieren Sie `geocentric_mpc_ephemeris.txt` an einen bekannten Ort.
2. In Stellarium `F2` drücken, **Plugins → Solar System Editor** öffnen, **Load at startup** anhaken und **Configure** klicken. Bei erster Aktivierung neu starten.
3. Nach dem Neustart **Solar System Editor → Solar System** öffnen und **Import orbital elements in MPC format** wählen.
4. **Select file** anklicken, `geocentric_mpc_ephemeris.txt` (oder den Einzeiler) auswählen, **Object name** auf `3I/ATLAS` setzen, **Object type** bei *Comet* lassen.
5. **Add objects** klicken, Dialoge schließen und per Suche (`F3`) prüfen, ob `3I/ATLAS` verfügbar ist.

KStars (Win/macOS/Linux)
------------------------
1. `KStars_quick-append_Win-Mac-Linux.zip` entpacken und das passende Skript (`*.bat`, `*.command`, `*.sh` oder `*.ps1`) ausführen. Erst DRYRUN, danach APPLY zum Anhängen an `comets.dat`.
2. Manuell: **Settings → Configure KStars → Solar System** (ältere Builds: **Data → Solar System Updates**). In **Comets** auf **Import** klicken, `geocentric_mpc_ephemeris.txt` wählen und bestätigen.
3. Auf Aufforderung KStars neu starten, dann nach `3I/ATLAS` suchen oder den Solar-System-Viewer prüfen.

Cartes du Ciel / SkyCharts
--------------------------
1. `apps-using-mpc-files/cartes-du-ciel/3I_ATLAS_mpc_1line.txt` kopieren (liegt auch im Release-Zip).
2. Cartes du Ciel starten und **Setup → Solar system** (`Ctrl+F3`) öffnen.
3. Im Reiter **Comets** **Update → Import from MPC file** wählen, `3I_ATLAS_mpc_1line.txt` laden und bestätigen.
4. **3I/ATLAS** in der Liste abhaken und **OK** klicken – die Komete steht nun in Suche und Charts zur Verfügung.
5. Handbearbeitung bevorzugt? Hängen Sie den Einzeiler an `comet.dat` an (Pfade im jeweiligen README).

WinStars 3 (Win/macOS/Linux)
----------------------------
1. `apps-using-mpc-files/winstars/3I_ATLAS_mpc_1line.txt` bereithalten oder das MPC-Bundle entpacken.
2. In WinStars **Preferences → Solar system → Import orbital elements** (oder **Add object**) öffnen.
3. **MPC single line** wählen, Inhalt einfügen und speichern.
4. Prüfen, ob `3I/ATLAS` in der Liste aktiv ist; ggf. Neustart bei aktivem Katalogcache.

SkySafari / SkyVoyager Plus/Pro (iOS/Android/macOS)
---------------------------------------------------
1. Den Einzeiler (`3I_ATLAS_mpc_1line.txt`) in einen Editor kopieren, auf den das Gerät zugreifen kann.
2. In SkySafari **Settings → Solar System → Solar System Data → Import Comet Data** öffnen (ältere Versionen: **Update Orbit Data → Custom Comet/Asteroid**).
3. MPC-Zeile einfügen, sicherstellen, dass der Name `3I/ATLAS` lautet, und bestätigen.
4. `3I/ATLAS` suchen und bei Bedarf zu Beobachtungslisten hinzufügen.
5. Die App aktualisiert MPC-Feeds regelmäßig; wiederholen Sie den Import nach Orbitalupdates.

Weitere MPC-kompatible Software
-------------------------------
1. `geocentric_mpc_ephemeris.txt` oder den passenden Einzeiler kopieren.
2. Importfunktion für Kometen/Asteroiden nutzen, Datei wählen und Objektname auf `3I/ATLAS` setzen.
3. Programm neu starten, falls es Solar-System-Daten cached, und sicherstellen, dass das Objekt aktiv ist.

Aktualisieren Sie die Einzeiler mit `python tools/update_orbital_elements.py`, sobald JPL eine neue SBDB-Lösung veröffentlicht, und prüfen Sie Positionen bei Bedarf per `python tools/verify_ephemeris.py`.
