3I/ATLAS EN APPS ZONDER IMPORT
==============================

Deze notitie beschrijft de huidige beperkingen van **Astro Gold** (macOS, iOS/iPadOS)
en **TimePassages Desktop** (macOS / Windows) en hoe je toch kunt werken met hun ingebouwde functies voor „extra punten”.

## Astro Gold (macOS / iOS / iPadOS)
- Astro Gold laat alleen toe de meegeleverde catalogus van hemellichamen aan of uit te zetten. Er is geen gedocumenteerde functie om externe efemeriden of orbitalelementen te importeren.
- Je activeert de extra punten van de leverancier via:
  - **macOS**: `Astro Gold → Preferences → Displayed Points → Add Extra Points…`
  - **iOS / iPadOS**: `Settings → Chart Points → Add Extra Points…`
- „Custom Points” in Astro Gold zijn vaste ecliptische lengten die je handmatig invoert. Handig voor referentiesterren of graden, maar ze veranderen niet met de tijd.
- Gevorderde gebruikers kunnen de ondersteuningsmappen bekijken (bijv.
  `~/Library/Application Support/com.ajnaware.Astro-Gold` op macOS of
  `~/Documents/Astro Gold` voor kaarten), maar deze mappen accepteren **geen** bewegende efemeride.

**Kortom:** totdat Esoteric Technologies 3I/ATLAS toevoegt aan de catalogus (of een importhaak aanbiedt), kun je het in Astro Gold niet als bewegend object installeren. Gebruik de ingebouwde extra’s of leg 3I/ATLAS vast als een statisch custom point wanneer je alleen één epoch nodig hebt.

### Statisch punt instellen (Astro Gold)
1. Kies de datum/tijd om vast te zetten (bijv. **2025-10-29 00:00 UT** nabij perihelium).
2. Open `apps-using-csv-files/geocentric_daily.csv`, zoek de juiste regel en noteer de tropische lengte (`lambda_deg`) en breedte (`beta_deg`). Voor dit voorbeeld: `lambda_deg = 203.560 deg` (≈ 23°33' Schorpioen) en `beta_deg = 2.283 deg`.
3. In Astro Gold (macOS): **Astro Gold → Preferences → Displayed Points → Add Extra Points…**, ga naar het tabblad **Custom Points**. Op iOS/iPadOS: **Settings → Chart Points → Add Extra Points…**.
4. Maak een punt aan, bv. `3I/ATLAS 2025-10-29 UT`, vul de lengte in (decimaal of in het teken/gradenformaat) en noteer eventueel breedte of afstand.
5. Sla op. Het punt blijft statisch; herhaal met bijgewerkte lengte wanneer je een nieuw epoch nodig hebt.

## TimePassages Desktop (macOS / Windows)
- TimePassages laat je de ingebouwde categorieën (grote asteroïden, centauren, Eris/TNO’s enz.) aanzetten. Workflow:
  - `Preferences → Edit Chart Points` (macOS) of `Edit → Chart Points…` (Windows) om categorieën te activeren.
  - `Display → Chart Points…` om te bevestigen dat ze zichtbaar zijn.
- De functie **Custom Points** werkt eveneens met vaste graden (bijv. het Galactisch Centrum op 27° Boogschutter). Er is momenteel geen importmechanisme voor nieuwe bewegende objecten.
- Gebruikersmappen (bijv.
  `~/Library/Application Support/TimePassages/` op macOS of
  `%APPDATA%\TimePassages\` op Windows) bewaren alleen voorkeuren en opgeslagen kaarten; je kunt daar geen efemeride neerzetten.

**Kortom:** TimePassages kan 3I/ATLAS nog niet automatisch volgen. Mocht een toekomstige versie import ondersteunen, dan verschijnen de instructies hier. Voor nu kun je een statisch custom point op een gekozen datum maken.

### Statisch punt instellen (TimePassages)
1. Bepaal de gewenste epoch (bijv. **2025-10-18 00:00 UT** rond maximale elongatie).
2. Raadpleeg `apps-using-csv-files/geocentric_daily.csv`. De regel voor 2025-10-18 vermeldt `lambda_deg = 209.285 deg` (≈ 29°17' Weegschaal) en `beta_deg = 2.715 deg`.
3. Open in TimePassages **Edit → Chart Points…** (Windows) of **Preferences → Edit Chart Points** (macOS), ga naar **Custom Points** en klik **Add**.
4. Geef een naam (bijv. `3I/ATLAS 2025-10-18 UT`) en voer de lengte in het teken/gradenformaat van TimePassages in. Notities over breedte of afstand kun je in de omschrijving kwijt.
5. Sla het punt op en activeer het. Werk de lengte bij wanneer je een nieuw moment nodig hebt.

---

### Ondersteuning aanvragen bij de leverancier
Wil je dat deze apps 3I/ATLAS (of custom imports algemeen) ondersteunen, neem dan contact op:
- Esoteric Technologies (Astro Gold):
  https://www.astrogold.io/contact
- AstroGraph (TimePassages):
  https://www.astrograph.com/contact.php

Wijs hen gerust op de orbitale gegevens in deze repository om officiële integratie te vergemakkelijken.
