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
