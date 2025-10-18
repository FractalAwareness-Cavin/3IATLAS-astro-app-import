3I/ATLAS FOR TIMEPASSAGES (MAC & WINDOWS)
========================================

These files can be imported as a custom body inside TimePassages Desktop.

macOS
-----
1. Unzip this package and copy the chosen `.txt` file into
   `~/Library/Application Support/TimePassages/Ephemerides/`
   (create the folder if necessary).
2. Launch TimePassages and open **TimePassages → Preferences → Calculations → Custom Bodies**.
3. Click **Import**, choose **Solar Fire Text** (or “Custom Ephemeris”) and select the file.
4. Name the new body (e.g. `3I/ATLAS`), ensure it is enabled, and close Preferences.
5. Add the custom body to your chart style via **Charts → Chart Settings → Planets & Points**.

Windows
-------
1. Copy the `.txt` file to `%APPDATA%\TimePassages\Ephemerides\`
   (paste that path into File Explorer to open it). Create the `Ephemerides`
   folder if it doesn’t exist.
2. In TimePassages choose **Edit → Preferences → Calculations → Custom Bodies**.
3. Use **Import** to load the file, name the body, and tick it on.
4. Add the body to your chart point selection and recalc any open charts.

If you prefer the MPC workflow, the same folder includes
`geocentric_mpc_ephemeris.txt`; use TimePassages' **Comet/Asteroid → Import
from MPC file** option and select it.
