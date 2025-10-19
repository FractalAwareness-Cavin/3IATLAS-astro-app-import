3I/ATLAS AND APPS WITHOUT IMPORT HOOKS
======================================

This note explains the current limitations in **Astro Gold** (macOS, iOS/iPadOS)
and **TimePassages Desktop** (macOS / Windows), and how you can still work with
their built-in "extra point" features.

## Astro Gold (macOS / iOS / iPadOS)
- Astro Gold only allows you to toggle the catalogue of bodies that the
developers ship with the app. There is no documented facility for importing
third-party ephemerides or orbital elements.
- You can enable the vendor's extras via:
  - **macOS**: `Astro Gold → Preferences → Displayed Points → Add Extra Points…`
  - **iOS / iPadOS**: `Settings → Chart Points → Add Extra Points…`
- "Custom Points" inside Astro Gold are fixed ecliptic longitudes that you type
manually. They are great for reference stars or chart degrees, but they do not
update with time.
- Advanced users can view the application-support folders (e.g.
  `~/Library/Application Support/com.ajnaware.Astro-Gold` on macOS, or
  `~/Documents/Astro Gold` for charts), but these folders do **not** accept a
"drop-in" moving-body ephemeris.

**Takeaway:** Until Esoteric Technologies adds 3I/ATLAS to their catalogue (or
exposes an import hook), you cannot install it as a moving body in Astro Gold.
Use the built-in extras, or record 3I/ATLAS as a fixed custom point if you only
need its position at a single epoch.

### Fixed-point walkthrough (Astro Gold)
1. Pick the date/time you want to freeze (example: **2025-10-29 00:00 UT** near perihelion).
2. Open `apps-using-csv-files/geocentric_daily.csv` and find the matching row. Note the tropical longitude (`lambda_deg`) and latitude (`beta_deg`). For the example above the table gives `lambda_deg = 203.560 deg` (approx 23 deg 33' Scorpio) and `beta_deg = 2.283 deg`.
3. In Astro Gold (macOS) choose **Astro Gold → Preferences → Displayed Points → Add Extra Points…**, then switch to the **Custom Points** tab. On iOS/iPadOS use **Settings → Chart Points → Add Extra Points…**.
4. Create a new point named something like `3I/ATLAS 2025-10-29 UT`, set the longitude field to the decimal value (or the sign/degree format Astro Gold expects), and optionally record the latitude or distance in the notes.
5. Save the point. It will remain static; repeat the process with updated longitude values when you need a new epoch.

## TimePassages Desktop (macOS / Windows)
- TimePassages lets you toggle the bodies that ship with the program: major
asteroids, centaurs, Eris/TNOs, etc. The workflow is:
  - `Preferences → Edit Chart Points` (macOS) or `Edit → Chart Points…` (Windows)
    to enable the categories.
  - `Display → Chart Points…` to confirm they are shown in charts.
- The **Custom Points** feature is also a fixed-degree tool (for example, you can
enter the Galactic Center at 27° Sagittarius). TimePassages currently provides
no import mechanism for new moving objects.
- User-visible data folders (e.g.
  `~/Library/Application Support/TimePassages/` on macOS or
  `%APPDATA%\TimePassages\` on Windows) store preferences and saved charts only;
an imported ephemeris cannot simply be dropped there.

**Takeaway:** TimePassages cannot yet track 3I/ATLAS automatically. If the
software adds import support in a future release you will find the relevant
instructions in this directory. For now you can create a custom fixed point at a
specific Julian Date if you just need a static reference.

### Fixed-point walkthrough (TimePassages)
1. Decide which epoch you want (for example **2025-10-18 00:00 UT** close to maximum elongation).
2. Look up the coordinates in `apps-using-csv-files/geocentric_daily.csv`. The row for 2025-10-18 lists `lambda_deg = 209.285 deg` (approx 29 deg 17' Libra) and `beta_deg = 2.715 deg`.
3. In TimePassages open **Edit → Chart Points…** (Windows) or **Preferences → Edit Chart Points** (macOS), switch to the **Custom Points** section, and click **Add**.
4. Enter a descriptive name (for example `3I/ATLAS 2025-10-18 UT`) and type the longitude in the sign/degree format TimePassages uses. Store the latitude or distance in the description if you want extra context.
5. Save and enable the custom point. Remember to replace it with a fresh longitude when you need a new snapshot.

---

### Requesting vendor support
If you would like these applications to support 3I/ATLAS (or custom imports in
general), contact the maintainers directly:
- Esoteric Technologies (Astro Gold):
  https://www.astrogold.io/contact
- AstroGraph (TimePassages):
  https://www.astrograph.com/contact.php

Feel free to point them at the orbital-element data provided in this repo so
they can integrate it officially.
