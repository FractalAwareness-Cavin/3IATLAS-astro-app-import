3I/ATLAS FOR SOLAR FIRE (WINDOWS)
=================================

Solar Fire does not ingest pre-computed ephemerides for new bodies; it needs
orbital elements in `extras.dat`. This folder contains:

- `extras.dat` – a ready-made entry for 3I/ATLAS (JPL SBDB solution 27).
- `geocentric_daily_solarfire.txt` etc. – kept for reference/plotting but not
  used directly by Solar Fire.

1. Quit Solar Fire.
2. Navigate to your `extras.dat` file (usually in
   `Documents\Solar Fire User Files\Userdata\extras.dat`).
3. Append or merge the `[3I_ATLAS]` block from this folder's `extras.dat`
   into your file (or replace the file entirely if you have no other custom
   entries).
4. Restart Solar Fire.
5. In **File → File Types…**, select **Extra Bodies** to confirm the file is
   active, then in your chart’s point selection tick the new 3I/ATLAS entry
   under Extra Bodies.

Note: Solar Fire ignores the `.txt` ephemeris in this folder; it is included
only for cross-checking the daily positions.
