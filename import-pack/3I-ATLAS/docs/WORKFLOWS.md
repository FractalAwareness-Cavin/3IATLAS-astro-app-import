# App workflows for 3I/ATLAS

All values in this pack come from JPL SBDB solution 27 (2025-10-10). Update the
files with the converter script if a newer solution is released.

## Stellarium (Windows/macOS/Linux)

**Accepts:** MPC 1-line comet elements  
**Steps:**
1. **Configuration → Plugins → Solar System Editor** → tick **Load at startup** (restart if needed).  
2. **Solar System Editor → Configure → Solar System → Import elements in MPC format → File**.  
3. Select `templates/stellarium/3I_ATLAS_mpc_elements.txt`.  
4. Click **Add object(s)** and search for **3I/ATLAS**.

## KStars (Windows/macOS/Linux)

**Accepts:** `comets.dat` line  
**Helpers:**
- Windows: `tools/kstars/Windows_KStars_Append_3I-DRYRUN.bat` (preview), then `Windows_KStars_Append_3I-APPLY.bat`.  
- macOS: double-click `tools/kstars/MacOS_SEEREADME_KStars_Append_3I.command`.  
- Linux: run `bash tools/kstars/Linux_KStars_Append_3I.sh`.  
All helpers back up the file before appending.

Manual:
1. Back up your `comets.dat` (`~/.local/share/kstars/comets.dat` on Linux, `%LOCALAPPDATA%\kstars\comets.dat` on Windows, `~/Library/Application Support/kstars/comets.dat` on macOS).  
2. Append the single line in `templates/kstars/3I_ATLAS_comets_dat_snippet.txt`.  
3. Restart KStars and search for **3I/ATLAS**.

## SkySafari / SkyVoyager (iOS/Android)

**Accepts:** No manual import  
Use *Settings → Solar System → Update Orbit Data* (Plus/Pro tiers). Keep
`templates/skysafari/3I_ATLAS_mpc_1line.txt` for reference only.

## Cartes du Ciel (SkyCharts)

**Accepts:** MPC element files  
Follow the instructions in `apps-using-mpc-files/cartes-du-ciel/README.txt`
(GUI import or manual append to `comet.dat`).

## WinStars 3

**Accepts:** MPC element files  
See `apps-using-mpc-files/winstars/README.txt` for the quick import steps.

## Solar Fire (Windows)

**Accepts:** `extras.dat` orbital elements (Other Bodies)  
**Helpers:**
- Windows: `tools/solarfire/SF_Merge_3I-DRYRUN.bat` (preview) then `…-APPLY.bat` to merge `[3I_ATLAS]` automatically.  
Both scripts back up `extras.dat` with a timestamp.

Manual:
1. Quit Solar Fire and back up `Documents\Solar Fire User Files\Userdata\extras.dat`.  
2. Copy or merge the `[3I_ATLAS]` block from `templates/solar_fire/3I_ATLAS_extras_dat_PLACEHOLDER.txt`.  
3. Relaunch and enable **3I/ATLAS** under **Extra Bodies** in your point selection dialog.

## Apps without import hooks

Astro Gold (macOS/iOS/iPadOS) and TimePassages Desktop (macOS/Windows) currently
only expose vendor-supplied extra points. They do not accept user-supplied
moving-body ephemerides. See the repo folder `Time-Passages-Astro-Gold/` for
workarounds (fixed custom points) and vendor contact links.
