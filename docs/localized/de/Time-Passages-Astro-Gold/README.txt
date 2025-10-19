3I/ATLAS UND APPS OHNE IMPORTFUNKTION
====================================

Diese Notiz erläutert die aktuellen Einschränkungen von **Astro Gold** (macOS, iOS/iPadOS)
und **TimePassages Desktop** (macOS / Windows) sowie Möglichkeiten, über die integrierten
„Extra-Point“-Funktionen dennoch mit 3I/ATLAS zu arbeiten.

## Astro Gold (macOS / iOS / iPadOS)
- Astro Gold erlaubt nur das Ein- und Ausschalten der Körper, die vom Hersteller
  mitgeliefert werden. Es gibt keine dokumentierte Option, um eigene Ephemeriden
  oder Orbitalelemente zu importieren.
- Die Zusatzpunkte des Herstellers aktivieren Sie über:
  - **macOS**: `Astro Gold → Preferences → Displayed Points → Add Extra Points…`
  - **iOS / iPadOS**: `Settings → Chart Points → Add Extra Points…`
- „Custom Points“ in Astro Gold sind feste ekliptikale Längen, die manuell
  eingetragen werden. Sie eignen sich für Referenzsterne oder Gradangaben, werden
  jedoch nicht zeitabhängig aktualisiert.
- Fortgeschrittene Anwender können die Support-Verzeichnisse einsehen (z. B.
  `~/Library/Application Support/com.ajnaware.Astro-Gold` auf macOS bzw.
  `~/Documents/Astro Gold` für Charts), doch lassen sich dort **keine** beweglichen
  Ephemeriden einfach ablegen.

**Fazit:** Solange Esoteric Technologies 3I/ATLAS nicht in den Katalog aufnimmt (oder
keinen Import-Hook bereitstellt), lässt sich der Körper in Astro Gold nicht als bewegliches
Objekt installieren. Nutzen Sie die eingebauten Extras oder legen Sie 3I/ATLAS als festen
Custom Point an, wenn Sie nur eine Position für einen Zeitpunkt benötigen.

### Schritt-für-Schritt für feste Punkte (Astro Gold)
1. Wählen Sie Datum/Uhrzeit, die eingefroren werden sollen (z. B. **2025-10-29 00:00 UT** nahe Perihel).
2. Öffnen Sie `apps-using-csv-files/geocentric_daily.csv`, suchen Sie die entsprechende Zeile und notieren Sie die tropische Länge (`lambda_deg`) und Breite (`beta_deg`). Im Beispiel: `lambda_deg = 203.560 deg` (≈ 23°33' Skorpion) und `beta_deg = 2.283 deg`.
3. In Astro Gold (macOS): **Astro Gold → Preferences → Displayed Points → Add Extra Points…**, dann zum Tab **Custom Points** wechseln. Auf iOS/iPadOS: **Settings → Chart Points → Add Extra Points…**.
4. Legen Sie einen neuen Punkt an, z. B. `3I/ATLAS 2025-10-29 UT`, tragen Sie die Dezimallänge ein (oder das von Astro Gold erwartete Zeichen/Grad-Format) und notieren Sie optional Breite oder Distanz.
5. Speichern Sie den Punkt. Er bleibt statisch; wiederholen Sie den Vorgang mit aktualisierten Längen, wenn Sie einen neuen Zeitpunkt benötigen.

## TimePassages Desktop (macOS / Windows)
- TimePassages erlaubt das Umschalten der mitgelieferten Körper (Hauptasteroiden,
  Zentauren, Eris/TNOs usw.). Vorgehensweise:
  - `Preferences → Edit Chart Points` (macOS) bzw. `Edit → Chart Points…` (Windows),
    um Kategorien zu aktivieren.
  - `Display → Chart Points…`, um sicherzustellen, dass sie angezeigt werden.
- Die Funktion **Custom Points** arbeitet ebenfalls mit festen Gradzahlen (z. B.
  Galaktisches Zentrum bei 27° Schütze). Es gibt derzeit keinen Importworkflow
  für neue bewegte Objekte.
- Sichtbare Benutzerdaten-Verzeichnisse (z. B.
  `~/Library/Application Support/TimePassages/` auf macOS oder
  `%APPDATA%\TimePassages\` unter Windows) speichern nur Einstellungen und Charts;
  eine Ephemeride lässt sich dort nicht einfach ablegen.

**Fazit:** TimePassages kann 3I/ATLAS derzeit nicht automatisch verfolgen. Sollte eine
künftige Version einen Import erlauben, finden Sie hier aktualisierte Hinweise. Bis dahin
können Sie einen festen Custom Point für einen bestimmten Julian-Tag anlegen, wenn Sie nur
einen statischen Referenzwert benötigen.

### Schritt-für-Schritt für feste Punkte (TimePassages)
1. Legen Sie die gewünschte Epoche fest (z. B. **2025-10-18 00:00 UT** nahe maximaler Elongation).
2. Schlagen Sie die Koordinaten in `apps-using-csv-files/geocentric_daily.csv` nach. Die Zeile für 2025-10-18 liefert `lambda_deg = 209.285 deg` (≈ 29°17' Waage) und `beta_deg = 2.715 deg`.
3. Öffnen Sie in TimePassages **Edit → Chart Points…** (Windows) oder **Preferences → Edit Chart Points** (macOS), wechseln Sie zu **Custom Points** und klicken Sie auf **Add**.
4. Geben Sie einen Namen wie `3I/ATLAS 2025-10-18 UT` ein und tragen Sie die Länge im Zeichen/Grad-Format ein, das TimePassages verwendet. Optional können Sie Breite oder Distanz in der Beschreibung speichern.
5. Speichern und aktivieren Sie den Custom Point. Aktualisieren Sie ihn mit einer neuen Länge, wenn Sie einen weiteren Zeitpunkt benötigen.

---

### Support beim Hersteller anfragen
Wenn Sie möchten, dass diese Anwendungen 3I/ATLAS (oder benutzerdefinierte Importe generell) unterstützen, wenden Sie sich direkt an die Anbieter:
- Esoteric Technologies (Astro Gold):
  https://www.astrogold.io/contact
- AstroGraph (TimePassages):
  https://www.astrograph.com/contact.php

Verweisen Sie gerne auf die Orbitalelemente aus diesem Repository, damit sie das Objekt offiziell integrieren können.
