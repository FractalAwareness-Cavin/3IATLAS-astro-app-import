3I/ATLAS – MPC IMPORT GUIDE
===========================

`geocentric_mpc_ephemeris.txt` contains daily MPC-style ephemerides (UT 0h, J2000 RA/Dec, delta, r, elongation, phase). Use it anywhere your software accepts classic 80-column comet data. Ready-to-go bundles live in the release downloads (see the root `README.md`) or right here under `apps-using-mpc-files/`.

Release bundles
---------------
- `Stellarium_quick-import.zip`: imports the single-object MPC file through the Solar System Editor plugin.
- `KStars_quick-append_Win-Mac-Linux.zip`: dry-run/apply helpers for `comets.dat` on every platform.
- `3I-ATLAS_apps_using_mpc_files.zip`: ships this entire folder, including one-line templates for Cartes du Ciel and WinStars.

Stellarium (Win/macOS/Linux)
----------------------------
1. Unzip `Stellarium_quick-import.zip` from the release or copy `geocentric_mpc_ephemeris.txt` to a known location.
2. In Stellarium press `F2`, open **Plugins → Solar System Editor**, tick **Load at startup**, then click **Configure**. Restart if you just enabled the plugin.
3. After restart, open **Solar System Editor → Solar System** and click **Import orbital elements in MPC format**.
4. Choose **Select file**, point to `geocentric_mpc_ephemeris.txt` (or the single-line file in the bundle), set **Object name** to `3I/ATLAS`, and leave **Object type** on *Comet*.
5. Click **Add objects**, close the dialogs, and use the search bar (`F3`) to confirm `3I/ATLAS` now resolves.

KStars (Win/macOS/Linux)
------------------------
1. Unzip `KStars_quick-append_Win-Mac-Linux.zip` and run the script that matches your platform (`*.bat`, `*.command`, `*.sh`, or `*.ps1`). Start with the DRYRUN helper; if the preview looks correct, run the APPLY helper to append the comet to `comets.dat`.
2. Manual alternative: in KStars choose **Settings → Configure KStars → Solar System** (older builds use **Data → Solar System Updates**). In the **Comets** tab click **Import**, choose `geocentric_mpc_ephemeris.txt`, and press **OK**.
3. Restart KStars if prompted, then search for `3I/ATLAS` or open the Solar System viewer to verify it is enabled.

Cartes du Ciel / SkyCharts
--------------------------
1. Copy `apps-using-mpc-files/cartes-du-ciel/3I_ATLAS_mpc_1line.txt` (also packaged in the release zip).
2. Launch Cartes du Ciel and open **Setup → Solar system** (`Ctrl+F3`).
3. In the **Comets** tab choose **Update → Import from MPC file**, pick `3I_ATLAS_mpc_1line.txt`, and confirm.
4. Tick **3I/ATLAS** in the list and click **OK**. The comet now appears in searches and charts.
5. Prefer editing by hand? Append the same single line to your `comet.dat` (see the per-folder README for exact paths).

WinStars 3 (Win/macOS/Linux)
----------------------------
1. Keep `apps-using-mpc-files/winstars/3I_ATLAS_mpc_1line.txt` handy or unzip the MPC release bundle.
2. In WinStars open **Preferences → Solar system → Import orbital elements** (or **Add object**).
3. Select the **MPC single line** option, paste the contents of the file, and save.
4. Verify `3I/ATLAS` is enabled in the displayed-body list; restart if the catalogue cache was open.

SkySafari / SkyVoyager Plus/Pro (iOS/Android/macOS)
---------------------------------------------------
1. Copy the one-line file (`3I_ATLAS_mpc_1line.txt`) into a text editor you can access on your device.
2. In SkySafari open **Settings → Solar System → Solar System Data** and tap **Import Comet Data** (older versions use **Update Orbit Data → Custom Comet/Asteroid**).
3. Paste the MPC line, ensure the name reads `3I/ATLAS`, and confirm the import.
4. Search for `3I/ATLAS` and add it to your observing lists if desired.
5. The app periodically refreshes MPC feeds; repeat this import after you update the orbital solution.

Other MPC-compatible software
-----------------------------
1. Copy `geocentric_mpc_ephemeris.txt` or the single-line template that matches your program.
2. Use the software's comet/asteroid import feature, choose the file, and set the display name to `3I/ATLAS`.
3. Restart the program if it caches solar-system data and confirm the body is enabled.

Keep the single-line files updated by running `python tools/update_orbital_elements.py` whenever JPL publishes a new SBDB solution, and spot-check positions with `python tools/verify_ephemeris.py` if you need an extra layer of confidence.
