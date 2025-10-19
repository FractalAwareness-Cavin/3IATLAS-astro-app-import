3I/ATLAS A APLIKACE BEZ IMPORTU
==============================

Tento dokument popisuje omezení aplikací **Astro Gold** (macOS, iOS/iPadOS)
a **TimePassages Desktop** (macOS / Windows) a ukazuje, jak využít jejich zabudované
funkce „extra point“.

## Astro Gold (macOS / iOS / iPadOS)
- Astro Gold dovoluje pouze zapnout/vypnout katalog těles, který dodává výrobce. Neexistuje dokumentovaný způsob, jak importovat efemeridy či orbitální prvky třetích stran.
- Výchozí extra body aktivujete přes:
  - **macOS**: `Astro Gold → Preferences → Displayed Points → Add Extra Points…`
  - **iOS / iPadOS**: `Settings → Chart Points → Add Extra Points…`
- „Custom Points“ v Astro Gold jsou pevné ekliptické délky zadávané ručně. Hodí se pro referenční hvězdy či konkrétní stupně, ale neaktualizují se v čase.
- Pokročilí uživatelé mohou procházet aplikační složky (např. `~/Library/Application Support/com.ajnaware.Astro-Gold` na macOS nebo `~/Documents/Astro Gold` pro horoskopy), nicméně tyto složky **neumožňují** vložit pohyblivou efemeridu.

**Shrnutí:** dokud Esoteric Technologies nezařadí 3I/ATLAS do katalogu (nebo neotevře import), nelze ho v Astro Gold nainstalovat jako pohyblivé těleso. Použijte integrované extra body, případně si vytvořte pevný vlastní bod.

### Postup pro pevný bod (Astro Gold)
1. Zvolte datum a čas (např. **2025-10-29 00:00 UT** poblíž perihélia).
2. Otevřete `apps-using-csv-files/geocentric_daily.csv`, najděte odpovídající řádek a poznamenejte tropickou délku (`lambda_deg`) a šířku (`beta_deg`). V příkladu: `lambda_deg = 203.560 deg` (≈ 23°33' Štíra) a `beta_deg = 2.283 deg`.
3. V Astro Gold (macOS) jděte na **Astro Gold → Preferences → Displayed Points → Add Extra Points…** a přepněte na záložku **Custom Points**. Na iOS/iPadOS použijte **Settings → Chart Points → Add Extra Points…**.
4. Vytvořte nový bod (např. `3I/ATLAS 2025-10-29 UT`), zadejte délku v desetinném formátu (nebo ve formátu znamení/stupně) a případně si poznamenejte šířku či vzdálenost.
5. Uložte bod. Zůstane statický; při další epoše zopakujte postup s novou délkou.

## TimePassages Desktop (macOS / Windows)
- TimePassages umožňuje zapínat tělesa dodaná s programem (hlavní asteroidy, kentaury, Eris/TNO atd.). Postup:
  - `Preferences → Edit Chart Points` (macOS) nebo `Edit → Chart Points…` (Windows) pro aktivaci kategorií.
  - `Display → Chart Points…` k ověření, že se objekty zobrazují.
- Funkce **Custom Points** je také založená na pevných stupních (např. Galaktické centrum na 27° Střelce). Momentálně neexistuje importní mechanismus pro nová pohyblivá tělesa.
- Uživatelské složky (např. `~/Library/Application Support/TimePassages/` na macOS nebo `%APPDATA%\TimePassages\` ve Windows) obsahují pouze nastavení a uložené horoskopy; efemeridu tam jednoduše vložit nelze.

**Shrnutí:** TimePassages zatím neumí 3I/ATLAS sledovat automaticky. Pokud budoucí verze přidá import, najdete zde aktualizované pokyny. Do té doby si můžete vytvořit pevný vlastní bod pro konkrétní datum.

### Postup pro pevný bod (TimePassages)
1. Zvolte epochu (např. **2025-10-18 00:00 UT** poblíž maximální elongace).
2. Najděte souřadnice v `apps-using-csv-files/geocentric_daily.csv`. Řádek pro 18.10.2025 uvádí `lambda_deg = 209.285 deg` (≈ 29°17' Váhy) a `beta_deg = 2.715 deg`.
3. V TimePassages otevřete **Edit → Chart Points…** (Windows) nebo **Preferences → Edit Chart Points** (macOS), přejděte do **Custom Points** a stiskněte **Add**.
4. Zadejte název (např. `3I/ATLAS 2025-10-18 UT`) a napište délku ve formátu znamení/stupně, který TimePassages používá. Šířku nebo vzdálenost můžete přidat do poznámky.
5. Uložte a aktivujte bod. Pro nový snímek nahraďte délkou odpovídající další epoše.

---

### Podpora u dodavatelů
Chcete-li, aby tyto aplikace podporovaly 3I/ATLAS (nebo obecně vlastní importy), kontaktujte přímo vývojáře:
- Esoteric Technologies (Astro Gold):
  https://www.astrogold.io/contact
- AstroGraph (TimePassages):
  https://www.astrograph.com/contact.php

Odkazujte je na orbitální data z tohoto repozitáře, aby mohli objekt oficiálně integrovat.
