3I/ATLAS — KStars Quick Append (Windows/macOS/Linux)
===================================================

Helpers in `tools/` back up your `comets.dat`, show a preview, then append 3I/ATLAS
(JPL SBDB solution 27).

Files by platform
-----------------
- `MacOS_SEEREADME_KStars_Append_3I.command` — macOS helper (auto-detects `~/Library/Application Support/kstars/comets.dat`).
- `Linux_KStars_Append_3I.sh` — Linux helper.
- `Windows_KStars_Append_3I-DRYRUN.bat` — Windows preview wrapper.
- `Windows_KStars_Append_3I-APPLY.bat` — Windows apply wrapper.
- `Windows_KStars_Append_3I.ps1` — PowerShell backend invoked by both batch files.
- `append_line.sh` — cross-platform backend used by all launchers.
- `3I_ATLAS_comets_dat_line.txt` — manual line for `comets.dat`.
- `3I_ATLAS_mpc_1line.txt` — MPC single line (shared with Stellarium/SkySafari).

macOS
-----
1. Open **System Settings → Privacy & Security**. If needed, set **Allow applications downloaded from** to *App Store & identified developers*.
2. Run `MacOS_SEEREADME_KStars_Append_3I.command`. When the preview appears, type `y` and press **Enter**. Gatekeeper may require you to click **Done** and then **Open Anyway** once.

Linux
-----
1. Run `bash tools/Linux_KStars_Append_3I.sh --apply` (or invoke `append_line.sh` directly).

Windows
-------
1. Run `Windows_KStars_Append_3I-DRYRUN.bat` to preview.
2. Run `Windows_KStars_Append_3I-APPLY.bat` to write the change.

After appending (all platforms)
------------------------------
1. Restart KStars so it reloads `comets.dat`.
2. Go to **Tools → Solar System… → Comets**, enable **Show comets**, raise the magnitude limit, search for `3I/ATLAS` (or `C/2025 N1`), tick it, and click **OK**.
