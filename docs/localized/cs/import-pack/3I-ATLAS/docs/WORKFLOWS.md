# Postupy aplikací pro 3I/ATLAS

Všechna data v tomto balíčku vycházejí z řešení 27 JPL SBDB (2025-10-10).
Aktualizujte soubory konverzním skriptem, jakmile vyjde novější řešení.

## Stellarium (Windows/macOS/Linux)

**Přijímá:** kometární elementy MPC v jedné řádce  
**Kroky:**
1. **Configuration → Plugins → Solar System Editor** → zaškrtněte **Load at startup** (případně restartujte).  
2. **Solar System Editor → Configure → Solar System → Import elements in MPC format → File**.  
3. Vyberte `templates/stellarium/3I_ATLAS_mpc_elements.txt`.  
4. Klikněte na **Add object(s)** a vyhledejte **3I/ATLAS**.

## KStars (Windows/macOS/Linux)

**Přijímá:** řádek `comets.dat`  
**Pomocníci:**
- Windows: `tools/kstars/KStars_Append_3I-DRYRUN.bat` (náhled), poté `…-APPLY.bat`.  
- macOS: dvojklik na `tools/kstars/KStars_Append_3I.command`.  
- Linux: spusťte `bash tools/kstars/KStars_Append_3I.sh`.  
Všichni pomocníci před přidáním vytvoří zálohu.

Manuálně:
1. Zálohujte `comets.dat` (`~/.local/share/kstars/comets.dat` na Linuxu, `%LOCALAPPDATA%\kstars\comets.dat` na Windows, `~/Library/Application Support/kstars/comets.dat` na macOS).  
2. Připojte jediný řádek z `templates/kstars/3I_ATLAS_comets_dat_snippet.txt`.  
3. Restartujte KStars a najděte **3I/ATLAS**.

## SkySafari / SkyVoyager (iOS/Android)

**Přijímá:** bez manuálního importu  
Použijte *Settings → Solar System → Update Orbit Data* (úrovně Plus/Pro). Soubor
`templates/skysafari/3I_ATLAS_mpc_1line.txt` si ponechte pouze jako referenci.

## Cartes du Ciel (SkyCharts)

**Přijímá:** soubory s elementy MPC  
Postupujte podle instrukcí v `apps-using-mpc-files/cartes-du-ciel/README.txt`
(import přes GUI nebo ruční přidání do `comet.dat`).

## WinStars 3

**Přijímá:** soubory s elementy MPC  
Viz `apps-using-mpc-files/winstars/README.txt` pro rychlý import.

## Solar Fire (Windows)

**Přijímá:** orbitální elementy v `extras.dat` (Other Bodies)  
**Pomocníci:**
- Windows: `tools/solarfire/SF_Merge_3I-DRYRUN.bat` (náhled), následně `…-APPLY.bat` pro automatické sloučení `[3I_ATLAS]`.  
Oba skripty zálohují `extras.dat` s časovým razítkem.

Manuálně:
1. Ukončete Solar Fire a zazálohujte `Documents\Solar Fire User Files\Userdata\extras.dat`.  
2. Zkopírujte nebo sloučte blok `[3I_ATLAS]` z `templates/solar_fire/3I_ATLAS_extras_dat_PLACEHOLDER.txt`.  
3. Znovu spusťte aplikaci a povolte **3I/ATLAS** v **Extra Bodies** v dialogu výběru bodů.

## Aplikace bez importních háčků

Astro Gold (macOS/iOS/iPadOS) a TimePassages Desktop (macOS/Windows) zpřístupňují
pouze dodatečné body od dodavatele a nepřijímají vlastní efemeridy
pohyblivých těles. Viz složku `Time-Passages-Astro-Gold/` pro workaroundy
(s pevnými body) a kontakty na výrobce.
