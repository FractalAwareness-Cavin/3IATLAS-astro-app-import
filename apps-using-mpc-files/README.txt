3I/ATLAS – MPC IMPORT GUIDE
===========================

`geocentric_mpc_ephemeris.txt` provides the daily MPC-style ephemerides (UT 0h, J2000 RA/Dec, Δ, r, elongation, phase). Every helper and quick-import bundle in this repository is built from that file. The same instructions ship inside the download archives (`Stellarium_quick-import.zip`, `KStars_quick-append_Win-Mac-Linux.zip`, and `3I-ATLAS_apps_using_mpc_files.zip`) so users who only download a zip see identical guidance.

All one-line templates reference **JPL SBDB solution 27 (retrieved 2025-10-10)**. Refresh them by running `python tools/update_orbital_elements.py` after JPL posts a newer solution; rerun the relevant helper or re-import the single-line file afterwards.

What’s included
---------------
- `geocentric_mpc_ephemeris.txt` – full daily table (80-column MPC layout) for any MPC-aware software.
- `cartes-du-ciel/`, `kstars/`, `winstars/` – single-line snippets and notes for those apps.
- Download bundles under `release-assets/` mirror the quick-start helpers described below.

Stellarium (Win/macOS/Linux)
----------------------------
1. Enable the Solar System Editor plugin (**Configuration/F2 → Plugins → Solar System Editor → Load at startup**), then restart if you just turned it on.
2. Open **Solar System Editor → Configure → Solar System**, choose **Import elements in MPC format → File**, and browse to `3I_ATLAS_mpc_1line.txt` (or the same file inside `Stellarium_quick-import.zip`).
3. Leave **Object type** set to *Comet*, keep the name as `3I/ATLAS`, click **Add object(s)**, and close the dialogs.
4. Press `F3`, search for `3I/ATLAS`, and confirm it appears. If not, restart Stellarium so it reloads the catalogue.

KStars (Win/macOS/Linux)
------------------------
From the download zip, run the helper that matches your platform in `tools/` (the repository copy lives under `tools/kstars/`).
1. Start with a preview:  
   - Windows: `Windows_KStars_Append_3I-DRYRUN.bat`  
   - macOS: double-click `MacOS_SEEREADME_KStars_Append_3I.command` (approve Gatekeeper if prompted)  
   - Linux: `bash tools/Linux_KStars_Append_3I.sh --dry-run`
2. If the preview looks correct, run the apply step:  
   - Windows: `Windows_KStars_Append_3I-APPLY.bat`  
   - macOS: rerun the `.command` script and answer **y** when prompted  
   - Linux: `bash tools/Linux_KStars_Append_3I.sh --apply`
3. Restart KStars. Use the skymap tools to work with the comet:
   - Press the search icon (or **Pointing → Find Object…** / `Ctrl+F`), type `3I/ATLAS`, and press **Ok** to center and track it. Accept the below-horizon warning if it appears.
   - Once it is visible, you can also right-click the comet and choose **Center & Track** to keep it locked.
   - For a heliocentric view, open **Tools → Solar System** (`Ctrl+Y`) to launch the Solar System Viewer and inspect the orbit alongside the planets.

Manual alternative: go to **Settings → Configure KStars → Solar System** (older builds use **Data → Solar System Updates**). In the **Comets** tab choose **Import**, select `geocentric_mpc_ephemeris.txt`, and confirm. KStars saves to `comets.dat`; the helper scripts back that file up automatically before writing.

Cartes du Ciel / SkyCharts
--------------------------
1. Copy `cartes-du-ciel/3I_ATLAS_mpc_1line.txt` (also present in `3I-ATLAS_apps_using_mpc_files.zip`).
2. Launch Cartes du Ciel and open **Setup → Solar system** (`Ctrl+F3`).
3. In **Comets**, click **Update → Import from MPC file**, pick the one-line file, and confirm.
4. Tick **3I/ATLAS** and click **OK**. Restart if the comet list stays cached.

Manual alternative: back up `comet.dat` (`%LOCALAPPDATA%\Skychart\cat\comet.dat` on Windows, `~/.skychart/cat/comet.dat` on Linux, `~/Library/Application Support/skychart.cat/comet.dat` on macOS), append the single line, then relaunch Cartes du Ciel.

WinStars 3 (Win/macOS/Linux)
----------------------------
1. Keep `winstars/3I_ATLAS_mpc_1line.txt` nearby or extract it from the download zip.
2. Open **Preferences → Solar system → Import orbital elements** (or **Add object**).
3. Choose **MPC single line**, paste the contents, and save.
4. Ensure `3I/ATLAS` is enabled in the displayed-body list. Restart if WinStars had its catalogue open.

SkySafari / SkyVoyager Plus/Pro (iOS/Android/macOS)
---------------------------------------------------
1. Copy the single-line element to a text editor you can access on your device.
2. In SkySafari go to **Settings → Solar System → Solar System Data** (older builds label it **Update Orbit Data**), then choose **Import Comet Data**.
3. Paste the line, confirm the name `3I/ATLAS`, and finish the import.
4. Search for `3I/ATLAS` and add it to any observing lists you use. Re-import whenever you refresh the orbital solution.

Other MPC-compatible tools
--------------------------
1. Use `geocentric_mpc_ephemeris.txt` (daily table) or the relevant one-line template.
2. Run the program’s comet/asteroid import feature, choose the file, and keep the display name `3I/ATLAS`.
3. Restart the software if it caches solar-system data and verify the comet is enabled.

Need a sanity check? Run `python tools/verify_ephemeris.py` to compare a few rows against live Horizons output before distributing updates.
