# App-workflows voor 3I/ATLAS

Alle waarden in dit pakket zijn afkomstig uit JPL SBDB-oplossing 27 (2025-10-10).
Werk de bestanden bij met het conversiescript zodra er een nieuwere oplossing beschikbaar is.

## Stellarium (Windows/macOS/Linux)

**Accepteert:** MPC-eenregelige komeetelementen  
**Stappen:**
1. **Configuration → Plugins → Solar System Editor** → vink **Load at startup** aan (herstart indien nodig).  
2. **Solar System Editor → Configure → Solar System → Import elements in MPC format → File**.  
3. Kies `templates/stellarium/3I_ATLAS_mpc_elements.txt`.  
4. Klik op **Add object(s)** en zoek naar **3I/ATLAS**.

## KStars (Windows/macOS/Linux)

**Accepteert:** `comets.dat`-regel  
**Hulpen:**
- Windows: `tools/kstars/KStars_Append_3I-DRYRUN.bat` (preview), daarna `…-APPLY.bat`.  
- macOS: dubbelklik op `tools/kstars/KStars_Append_3I.command`.  
- Linux: voer `bash tools/kstars/KStars_Append_3I.sh` uit.  
Alle hulpen maken een back-up voordat ze toevoegen.

Handmatig:
1. Maak een back-up van `comets.dat` (`~/.local/share/kstars/comets.dat` op Linux, `%LOCALAPPDATA%\kstars\comets.dat` op Windows, `~/Library/Application Support/kstars/comets.dat` op macOS).  
2. Voeg de enkele regel uit `templates/kstars/3I_ATLAS_comets_dat_snippet.txt` toe.  
3. Start KStars opnieuw en zoek **3I/ATLAS**.

## SkySafari / SkyVoyager (iOS/Android)

**Accepteert:** geen handmatige import  
Gebruik *Settings → Solar System → Update Orbit Data* (Plus/Pro-niveaus). Bewaar
`templates/skysafari/3I_ATLAS_mpc_1line.txt` alleen als referentie.

## Cartes du Ciel (SkyCharts)

**Accepteert:** MPC-elementbestanden  
Volg de instructies in `apps-using-mpc-files/cartes-du-ciel/README.txt`
(GUI-import of handmatig toevoegen aan `comet.dat`).

## WinStars 3

**Accepteert:** MPC-elementbestanden  
Zie `apps-using-mpc-files/winstars/README.txt` voor de snelle importstappen.

## Solar Fire (Windows)

**Accepteert:** `extras.dat`-baanelementen (Other Bodies)  
**Hulpen:**
- Windows: `tools/solarfire/SF_Merge_3I-DRYRUN.bat` (preview), daarna `…-APPLY.bat` voor automatische samenvoeging van `[3I_ATLAS]`.  
Beide scripts maken een timestamp-back-up van `extras.dat`.

Handmatig:
1. Sluit Solar Fire en maak een backup van `Documents\Solar Fire User Files\Userdata\extras.dat`.  
2. Kopieer of voeg het `[3I_ATLAS]`-blok samen vanuit `templates/solar_fire/3I_ATLAS_extras_dat_PLACEHOLDER.txt`.  
3. Start opnieuw en activeer **3I/ATLAS** onder **Extra Bodies** in het puntselectievenster.

## Apps zonder importhaken

Astro Gold (macOS/iOS/iPadOS) en TimePassages Desktop (macOS/Windows) bieden
alleen extra punten van de leverancier en accepteren geen eigen efemeriden
voor bewegende objecten. Raadpleeg de map `Time-Passages-Astro-Gold/` voor workarounds
(met vaste punten) en contactlinks van de leverancier.
