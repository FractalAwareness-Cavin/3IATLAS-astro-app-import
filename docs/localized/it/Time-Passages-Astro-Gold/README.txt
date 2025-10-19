3I/ATLAS E APP SENZA IMPORT
==========================

Questa nota illustra le limitazioni attuali di **Astro Gold** (macOS, iOS/iPadOS)
e **TimePassages Desktop** (macOS / Windows), oltre a come sfruttare le loro
funzioni integrate di «punti extra».

## Astro Gold (macOS / iOS / iPadOS)
- Astro Gold consente solo di attivare/disattivare il catalogo di corpi fornito
  dagli sviluppatori. Non esiste una funzione documentata per importare
  efemeridi o elementi orbitali di terze parti.
- Puoi abilitare gli extra del fornitore da:
  - **macOS**: `Astro Gold → Preferences → Displayed Points → Add Extra Points…`
  - **iOS / iPadOS**: `Settings → Chart Points → Add Extra Points…`
- I «Custom Points» di Astro Gold sono longitudini eclittiche fisse inserite
  manualmente. Ottimi per stelle di riferimento o gradi del tema, ma non si
  aggiornano nel tempo.
- Gli utenti esperti possono esplorare le cartelle di supporto (es.
  `~/Library/Application Support/com.ajnaware.Astro-Gold` su macOS o
  `~/Documents/Astro Gold` per i temi), ma queste cartelle **non** accettano
  efemeridi mobili da copiare direttamente.

**In sintesi:** finché Esoteric Technologies non aggiunge 3I/ATLAS al catalogo (o
non fornisce un hook d'importazione), non potrai installarlo come corpo mobile in
Astro Gold. Usa gli extra integrati oppure registra 3I/ATLAS come punto fisso se
ti serve solo la posizione a un'epoca specifica.

### Procedura punto fisso (Astro Gold)
1. Scegli la data/ora da fissare (esempio: **2025-10-29 00:00 UT** vicino al perielio).
2. Apri `apps-using-csv-files/geocentric_daily.csv` e trova la riga corrispondente. Annota la longitudine tropicale (`lambda_deg`) e la latitudine (`beta_deg`). Nell'esempio: `lambda_deg = 203.560 deg` (≈ 23°33' Scorpione) e `beta_deg = 2.283 deg`.
3. In Astro Gold (macOS) vai su **Astro Gold → Preferences → Displayed Points → Add Extra Points…**, quindi scheda **Custom Points**. Su iOS/iPadOS usa **Settings → Chart Points → Add Extra Points…**.
4. Crea un nuovo punto, ad esempio `3I/ATLAS 2025-10-29 UT`, imposta la longitudine in formato decimale (o nel formato segno/grado atteso) e annota opzionalmente latitudine o distanza.
5. Salva il punto. Rimarrà statico; ripeti con una nuova longitudine quando ti serve un'altra epoca.

## TimePassages Desktop (macOS / Windows)
- TimePassages consente di attivare i corpi inclusi (asteroidi principali, centauri,
  Eris/TNO ecc.). Flusso tipico:
  - `Preferences → Edit Chart Points` (macOS) oppure `Edit → Chart Points…` (Windows)
    per abilitare le categorie.
  - `Display → Chart Points…` per verificare che siano visibili.
- La funzione **Custom Points** è anch'essa a gradi fissi (ad esempio per inserire
  il Centro Galattico a 27° Sagittario). Attualmente TimePassages non offre un
  meccanismo d'import per nuovi oggetti mobili.
- Le cartelle dati accessibili (es.
  `~/Library/Application Support/TimePassages/` su macOS o
  `%APPDATA%\TimePassages\` su Windows) contengono preferenze e temi salvati;
  un'efemeride non può essere semplicemente copiata lì.

**In sintesi:** TimePassages non può ancora seguire automaticamente 3I/ATLAS. Se in
futuro arriverà il supporto per l'import, qui troverai le istruzioni aggiornate. Per ora
puoi creare un punto fisso personalizzato a una data precisa per avere un riferimento statico.

### Procedura punto fisso (TimePassages)
1. Decidi l'epoca desiderata (es. **2025-10-18 00:00 UT** vicino alla massima elongazione).
2. Consulta `apps-using-csv-files/geocentric_daily.csv`. La riga del 18/10/2025 riporta
   `lambda_deg = 209.285 deg` (≈ 29°17' Bilancia) e `beta_deg = 2.715 deg`.
3. In TimePassages apri **Edit → Chart Points…** (Windows) oppure **Preferences → Edit Chart Points** (macOS), vai su **Custom Points** e premi **Add**.
4. Inserisci un nome descrittivo (es. `3I/ATLAS 2025-10-18 UT`) e la longitudine nel formato segno/grado usato dal programma. Opzionalmente salva latitudine o distanza nella descrizione.
5. Salva e abilita il punto. Sostituiscilo con una nuova longitudine quando hai bisogno di un nuovo snapshot.

---

### Richiedere supporto al fornitore
Se desideri che queste applicazioni supportino 3I/ATLAS (o import personalizzati in generale), contatta i manutentori direttamente:
- Esoteric Technologies (Astro Gold):
  https://www.astrogold.io/contact
- AstroGraph (TimePassages):
  https://www.astrograph.com/contact.php

Segnala loro i dati orbitali presenti in questo repository così potranno integrarli ufficialmente.
