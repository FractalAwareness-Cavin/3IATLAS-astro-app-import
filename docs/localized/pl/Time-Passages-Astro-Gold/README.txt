3I/ATLAS I APLIKACJE BEZ IMPORTU
=================================

Ten dokument opisuje obecne ograniczenia **Astro Gold** (macOS, iOS/iPadOS)
oraz **TimePassages Desktop** (macOS / Windows) i pokazuje, jak korzystać
z wbudowanych funkcji „extra point”.

## Astro Gold (macOS / iOS / iPadOS)
- Astro Gold umożliwia tylko włączanie/wyłączanie ciał dostarczanych z aplikacją.
  Nie ma udokumentowanej opcji importu zewnętrznych efemeryd ani elementów orbitalnych.
- Dodatkowe punkty producenta włączysz poprzez:
  - **macOS**: `Astro Gold → Preferences → Displayed Points → Add Extra Points…`
  - **iOS / iPadOS**: `Settings → Chart Points → Add Extra Points…`
- „Custom Points” w Astro Gold to stałe długości ekliptyczne wpisywane ręcznie. Są dobre dla gwiazd referencyjnych lub konkretnych stopni, lecz nie aktualizują się wraz z czasem.
- Zaawansowani użytkownicy mogą zajrzeć do katalogów wsparcia (np.
  `~/Library/Application Support/com.ajnaware.Astro-Gold` na macOS lub
  `~/Documents/Astro Gold` dla wykresów), ale katalogi te **nie** akceptują ruchomej efemerydy w formie pliku „wrzuć i używaj”.

**Wniosek:** dopóki Esoteric Technologies nie doda 3I/ATLAS do katalogu (albo nie udostępni importu), nie da się zainstalować go jako ciała ruchomego w Astro Gold. Korzystaj z wbudowanych extras lub zanotuj 3I/ATLAS jako punkt stały, jeśli potrzebujesz pozycji dla jednej epoki.

### Instrukcja dla punktu stałego (Astro Gold)
1. Wybierz datę/godzinę do zamrożenia (np. **2025-10-29 00:00 UT** blisko peryhelium).
2. Otwórz `apps-using-csv-files/geocentric_daily.csv` i znajdź odpowiedni wiersz. Zanotuj długość tropikalną (`lambda_deg`) i szerokość (`beta_deg`). W przykładzie: `lambda_deg = 203.560 deg` (≈ 23°33' Skorpiona) oraz `beta_deg = 2.283 deg`.
3. W Astro Gold (macOS) przejdź do **Astro Gold → Preferences → Displayed Points → Add Extra Points…**, a następnie na kartę **Custom Points**. W iOS/iPadOS użyj **Settings → Chart Points → Add Extra Points…**.
4. Utwórz nowy punkt, np. `3I/ATLAS 2025-10-29 UT`, ustaw długość w formacie dziesiętnym (lub znak/stopnie) i opcjonalnie zanotuj szerokość oraz dystans.
5. Zapisz punkt. Pozostanie on statyczny; powtórz czynności z nową długością, gdy potrzebujesz kolejnej epoki.

## TimePassages Desktop (macOS / Windows)
- TimePassages pozwala przełączać wbudowane ciała (główne asteroidy, centaury, Eris/TNO itp.). Schemat:
  - `Preferences → Edit Chart Points` (macOS) lub `Edit → Chart Points…` (Windows), aby aktywować kategorie.
  - `Display → Chart Points…`, aby upewnić się, że są widoczne na wykresach.
- Funkcja **Custom Points** również operuje na stałych stopniach (np. można wpisać Centrum Galaktyczne na 27° Strzelca). Na razie TimePassages nie oferuje mechanizmu importu nowych ciał ruchomych.
- Widoczne katalogi danych użytkownika (np.
  `~/Library/Application Support/TimePassages/` na macOS lub
  `%APPDATA%\TimePassages\` na Windows) przechowują tylko ustawienia i zapisane wykresy; nie można tam wrzucić efemerydy.

**Wniosek:** TimePassages nie potrafi jeszcze automatycznie śledzić 3I/ATLAS. Jeśli w przyszłości pojawi się wsparcie importu, znajdziesz tu instrukcje. Na razie możesz stworzyć statyczny punkt własny dla konkretnej daty.

### Instrukcja dla punktu stałego (TimePassages)
1. Wybierz epokę (np. **2025-10-18 00:00 UT** w pobliżu maksymalnej elongacji).
2. Sprawdź `apps-using-csv-files/geocentric_daily.csv`. Wiersz z 18.10.2025 zawiera `lambda_deg = 209.285 deg` (≈ 29°17' Wagi) i `beta_deg = 2.715 deg`.
3. W TimePassages otwórz **Edit → Chart Points…** (Windows) lub **Preferences → Edit Chart Points** (macOS), przejdź do **Custom Points** i kliknij **Add**.
4. Nazwij punkt (np. `3I/ATLAS 2025-10-18 UT`) i wpisz długość w formacie znak/stopnie używanym przez aplikację. W opisie możesz zapisać szerokość lub odległość.
5. Zapisz i włącz punkt. Zastąp go nową długością, gdy potrzebujesz świeżego odczytu.

---

### Kontakt z producentami
Jeśli chcesz, aby aplikacje wspierały 3I/ATLAS (lub własne importy), skontaktuj się bezpośrednio:
- Esoteric Technologies (Astro Gold):
  https://www.astrogold.io/contact
- AstroGraph (TimePassages):
  https://www.astrograph.com/contact.php

Możesz wskazać im dane orbitalne z tego repozytorium, by ułatwić oficjalną integrację.
