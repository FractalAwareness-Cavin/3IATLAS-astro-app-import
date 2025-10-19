3I/ATLAS FOR SOLAR FIRE (WINDOWS)
=================================

Solar Fire does not ingest pre-computed ephemerides for new bodies; it reads orbital elements from `extras.dat`. This folder (and the `SolarFire_merge-helper_Windows.zip` download kit) keep the 3I/ATLAS entry aligned with **JPL SBDB solution 27 (2025-10-10)**.

Tested on
---------
- Solar Fire 9: `Documents\Solar Fire 9 User Files\Points & Colors\extras.dat`
- Solar Fire 10: `Documents\Solar Fire User Files\Points & Colors\extras.dat`
- Solar Fire 11: `Documents\Solar Fire User Files\Points & Colors\extras.dat`

Contents
--------
- `extras.dat`: ready-made `[3I_ATLAS]` block (see below) plus comments for manual merges.
- `geocentric_daily_solarfire.txt` and similar files: optional reference tables if you need to spot-check positions outside Solar Fire.
- `tools/solarfire/SF_Merge_3I-DRYRUN.bat`: Windows preview helper; shows the planned merge and exits.
- `tools/solarfire/SF_Merge_3I-APPLY.bat`: Windows apply helper; writes the block after backing up `extras.dat`.
- `tools/solarfire/SF_Merge_3I.ps1`: PowerShell backend used by both batch files (can be run directly if desired). In the download zip these files live in `tools/`.

Example block
-------------
Paste this block into your existing `extras.dat` or let the helper merge it automatically:

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
; Solar Fire ignores semi-major axis when Tp supplied for comets.
; This object is hyperbolic (e>1). Verify compatibility with your Solar Fire version.
```

Install steps
-------------
1. Quit Solar Fire so `extras.dat` is not locked.
2. Run `tools/solarfire/SF_Merge_3I-DRYRUN.bat` (or `tools/SF_Merge_3I-DRYRUN.bat` inside the download zip) to confirm the target path and review the block that will be merged. For a direct PowerShell run, execute `tools/solarfire/SF_Merge_3I.ps1 -DryRun`.
3. Run `tools/solarfire/SF_Merge_3I-APPLY.bat` (or the download-zip equivalent) to merge the block. Prefer PowerShell? `tools/solarfire/SF_Merge_3I.ps1 -Apply` performs the same action. A timestamped backup is created automatically.
4. Open the path that matches your version (see above) and confirm the updated `extras.dat` is in place (skip this if you used the helper).
5. Relaunch Solar Fire, open **File → File Types…**, and ensure **Extra Bodies** points at the updated file.
6. In your chart’s point selection dialog, tick `3I/ATLAS` under **Extra Bodies / Other Bodies**.

Mini-FAQ
--------
- **3I/ATLAS does not appear after merging.** Confirm you edited the correct `extras.dat` folder (Solar Fire keeps separate user folders per major version) and that the body is enabled under **Extra Bodies**.
- **Helper script reports "access denied."** Close Solar Fire before running the APPLY helper; the merge cannot overwrite an open `extras.dat`.
- **Need fresher orbital elements.** Run `python tools/update_orbital_elements.py` from the repo root, then re-run the helper to replace the block with the latest SBDB solution.
