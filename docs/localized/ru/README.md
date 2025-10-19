# Набор эфемерид 3I/ATLAS

Ежедневные эфемериды для межзвёздной кометы **3I/ATLAS (C/2025 N1)**, полученные напрямую из NASA/JPL Horizons и структурированные так, чтобы астрологи могли добавить объект в любимые приложения. Диапазон охватывает весь проход через гелиосферу (2016‑01‑01 → 2040‑12‑31). Текущая сборка основана на **решении Horizons №27 (2025‑10‑10)**; запускайте `tools/update_orbital_elements.py`, когда JPL публикует более свежие данные и вы хотите обновить вспомогательные файлы.

## Быстрый старт
1. Скачайте архив, соответствующий вашему приложению (см. **Прямые загрузки**) или клонируйте репозиторий.
2. Распакуйте архив, чтобы открыть `README` в нужной папке.
3. Следуйте инструкции в `README` или запустите хелперы для Solar Fire, KStars и Stellarium.
4. По желанию: `python tools/update_orbital_elements.py` загрузит актуальную SBDB, а `python tools/verify_ephemeris.py` сверит несколько дат с Horizons перед распространением обновлений.

## Содержание
- [Быстрый старт](#быстрый-старт)
- [Поддерживаемые приложения (импорт движущихся тел)](#поддерживаемые-приложения-импорт-движущихся-тел)
- [С чего начать?](#с-чего-начать)
- [Прямые загрузки](#прямые-загрузки)
- [Проводник по папкам](#проводник-по-папкам)
- [Глоссарий](#глоссарий)
- [Инструкции по приложениям](#инструкции-по-приложениям)
  - [Пакет импорта и скрипты](#пакет-импорта-и-скрипты)
  - [Статус Astro Gold](#статус-astro-gold)
  - [Solar Fire (Windows)](#solarfire-instructions-windows)
  - [Импорт в формате MPC](#импорт-в-формате-mpc)
  - [Astro Gold и TimePassages](#astro-gold-и-timepassages)
  - [Примечания по CSV](#примечания-по-csv)
- [Рецепт Horizons](#рецепт-horizons)
- [Перегенерация эфемерид](#перегенерация-эфемерид)
- [Служебные скрипты](#служебные-скрипты)
- [Ключевые этапы](#ключевые-этапы)
- [Заметки и предупреждения](#заметки-и-предупреждения)
- [Устранение неполадок](#устранение-неполадок)
- [Дополнительно: установка инструментов Horizons](#дополнительно-установка-инструментов-horizons)

Поддерживаемые приложения (импорт движущихся тел)
-------------------------------------------------
- **Stellarium** (Win/macOS/Linux) — импорт через Solar System Editor в формате MPC.
- **KStars** (Win/macOS/Linux) — добавление строки в `comets.dat` (есть хелперы).
- **Solar Fire** (Windows) — слияние блока `[3I_ATLAS]` в `extras.dat`.
- **Cartes du Ciel / SkyCharts** (Win/macOS/Linux) — импорт MPC или ручное редактирование `comet.dat`.
- **WinStars 3** (Win/macOS/Linux) — вставка MPC-строки во встроенный редактор.
- **SkySafari / SkyVoyager Plus/Pro** (iOS/Android/macOS) — обновление орбитальных данных через MPC-ленты.

Без функций импорта:
- **Astro Gold** (macOS/iOS/iPadOS) и **TimePassages** (macOS/Windows). Используйте рекомендации по фиксированным точкам.

Вопросы? Пишите на [cavinbirdseyetarot@gmail.com](mailto:cavinbirdseyetarot@gmail.com) — помогу и улучшу документацию.



## С чего начать?

Выберите папку под вашу программу или скачайте соответствующий архив. Если не уверены, откройте в приложении *Файл → Импорт* и посмотрите, какие форматы поддерживаются.

- `solar-fire/` — блок `extras.dat` для Solar Fire и эталонные таблицы.
- `apps-using-mpc-files/` — файл MPC на 80 колонок `geocentric_mpc_ephemeris.txt` (UT 0h, J2000 RA/Dec, Δ, r, элонгация, фаза).
- `apps-using-csv-files/` — CSV-сводки (гелиоцентрические, геоцентрические, барицентрические), входы в знаки, широты.
- `developer/` — JSON Horizons, скрипты генерации, встроенный `pyswisseph`, Swiss-Ephemeris-хелпер.
- `Time-Passages-Astro-Gold/` — ограничения и способы работы с фиксированными точками.

#### Прямые загрузки
- [Скрипты объединения для Solar Fire (Windows)](https://github.com/FractalAwareness-Cavin/3IATLAS-astro-app-import/releases/download/v1.0.0/SolarFire_merge-helper_Windows.zip)
- [Быстрое добавление KStars (Win/macOS/Linux)](https://github.com/FractalAwareness-Cavin/3IATLAS-astro-app-import/releases/download/v1.0.0/KStars_quick-append_Win-Mac-Linux.zip)
- [Быстрый импорт Stellarium](https://github.com/FractalAwareness-Cavin/3IATLAS-astro-app-import/releases/download/v1.0.0/Stellarium_quick-import.zip)
- [MPC-эфемерида (80 колонок)](https://github.com/FractalAwareness-Cavin/3IATLAS-astro-app-import/releases/download/v1.0.0/3I-ATLAS_apps_using_mpc_files.zip)
- [CSV-набор для исследований](https://github.com/FractalAwareness-Cavin/3IATLAS-astro-app-import/releases/download/v1.0.0/3I-ATLAS_apps_using_csv_files.zip)

Каждый архив отражает соответствующую папку и содержит `README.txt` с пошаговыми инструкциями — распакуйте перед запуском скриптов или копированием.

## Проводник по папкам

- **solar-fire/** — данные для Solar Fire (`extras.dat`) и справочные таблицы.
- **apps-using-mpc-files/** — полная MPC-эфемерида, однострочные шаблоны, инструкции по приложениям.
- **apps-using-csv-files/** — CSV-векторы (гелио-, гео-, барицентрические), моменты входа, метрики.
- **developer/** — скрипты, vendored `pyswisseph`, источники, Swiss-Ephemeris-утилиты.
- **Time-Passages-Astro-Gold/** — решения для приложений без импорта.
- **import-pack/** — компактный набор с шаблонами, скриптами и документацией.

## Глоссарий

- **MPC 80 columns** — классический формат Minor Planet Center.
- **Horizons SBDB** — база малых тел NASA/JPL.
- **Элонгация** — угловое расстояние до Солнца, видимое с Земли.
- **Δ (delta)** — геоцентрическая дистанция.
- **r** — гелиоцентрическая дистанция.
- **UT** — универсальное время (UTC).

## Инструкции по приложениям

### Пакет импорта и скрипты

См. `import-pack/3I-ATLAS/README.md` (шаблоны, хелперы, сценарий обновления).

### Статус Astro Gold

Импорт движущихся тел пока недоступен; см. `Time-Passages-Astro-Gold/` для фиксированных точек.

### SolarFire instructions Windows

`solar-fire/README.txt` описывает слияние `[3I_ATLAS]` в `extras.dat`. Скрипты `tools/solarfire/` поддерживают Dry-Run и Apply.

### Импорт в формате MPC

В `apps-using-mpc-files/` лежат README по Stellarium, KStars, Cartes du Ciel, WinStars и нужные файлы.

### Astro Gold и TimePassages

Импорт отсутствует; используйте статические точки на выбранную дату.

### Примечания по CSV

`apps-using-csv-files/README.txt` объясняет колонки и единицы для таблиц, ноутбуков, скриптов. Для сидерических расчётов вычитайте айанамсу из тропической долготы.

## Рецепт Horizons

JSON в `developer/raw/` получены с параметрами:

```
COMMAND='DES=1004083;'
MAKE_EPHEM='YES'
EPHEM_TYPE='VECTORS'
CENTER='500@399'
REF_PLANE='ECLIPTIC'
REF_SYSTEM='J2000'
START_TIME='2016-01-01'
STOP_TIME='2040-12-31'
STEP_SIZE='1 d'
TABLE_TYPE='VECTORS'
```

Изменяйте при необходимости интервал/центр наблюдения и пересоздавайте JSON перед повторной генерацией.

## Перегенерация эфемерид

### `developer/scripts/generate_ephemeris.py`

- Читает JSON-векторы и формирует:
  - CSV (`apps-using-csv-files/`)
  - Таблицы Solar Fire (`solar-fire/`)
  - MPC-эфемериду (`apps-using-mpc-files/geocentric_mpc_ephemeris.txt`)
  - Сводки входов в знаки.
- Создаёт недостающие каталоги.

```
cd developer/scripts
python3 generate_ephemeris.py
```

### `developer/scripts/build_swisseph.sh`

- Требует `mksweph`.
- Преобразует CSV в Swiss-Ephemeris `.se1` (`developer/swisseph/`).

```
cd developer/scripts
bash build_swisseph.sh
```

### `tools/update_orbital_elements.py`

- Загружает свежую SBDB и обновляет MPC-файлы, KStars-кусочки, Solar Fire.

```
python tools/update_orbital_elements.py
```

`--dry-run` показывает значения без записи.

### `tools/verify_ephemeris.py`

- Сверяет строки `apps-using-mpc-files/geocentric_mpc_ephemeris.txt` с live Horizons.

```
python tools/verify_ephemeris.py --start 2025-10-01 --days 5 --tolerance 5e-4
```

По умолчанию: начало 2025-10-01, 5 дней, допуск `5e-4` а. е. (~75 000 км). При расхождениях возвращает ненулевой код — удобно для CI.

## Служебные скрипты

- **`tools/3i_elements_to_formats.py`** — преобразует новую MPC-строку в шаблоны (Stellarium, KStars, Solar Fire).
- **`tools/kstars/`** — OS-специфичные помощники по резервному копированию и добавлению в `comets.dat`.
- **`tools/solarfire/`** — Windows-сценарии для автоматического слияния `extras.dat`.

## Ключевые этапы

- 2024-10-xx — первичные выгрузки Horizons, структура проекта.
- 2025-10-xx — переход на SBDB-решение 27.
- 2025-10-xx — добавлены скрипты проверки и пакет импорта.

## Заметки и предупреждения

- **Solar Fire**: перед объединением делайте бэкап `extras.dat`.
- **SkySafari**: импорт файлов недоступен — используйте *Update Orbit Data*.
- **Astro Gold / TimePassages**: только фиксированные точки.
- **Проверка**: `tools/verify_ephemeris.py` быстро сопоставит данные с Horizons.

## Устранение неполадок

- **3I/ATLAS не появился после импорта.** Перезапустите приложение и убедитесь в написании `3I/ATLAS`.
- **Сутки сдвига в позициях.** MPC-файл отмечен на **UT 0h**; работайте в UTC или учитывайте поправку по часовому поясу.
- **Solar Fire показывает старый список.** Проверьте путь `extras.dat` (у каждой версии своя папка) или перезапустите APPLY-скрипт.
- **Нужно проверить данные.** `python tools/verify_ephemeris.py` сверит выборку с Horizons.

Приятной работы с 3I/ATLAS!

## Дополнительно: установка инструментов Horizons

Данные уже входят в комплект, но если хотите получать их самостоятельно:

### macOS / Linux
1. Убедитесь, что `python3 --version` ≥ 3.10.
2. Установите Astroquery:
   ```bash
   python3 -m pip install astroquery --user
   ```
3. Запрос к Horizons:
   ```bash
   python3 - <<'PY'
   from astroquery.jplhorizons import Horizons
   obj = Horizons(id='DES=1004083;', location='500@399', epochs={'start':'2025-01-01', 'stop':'2025-01-10', 'step':'1d'})
   print(obj.vectors())
   PY
   ```

Альтернатива:

```bash
curl "https://ssd.jpl.nasa.gov/api/horizons.api?format=json&COMMAND='DES=1004083;'&MAKE_EPHEM=YES&EPHEM_TYPE=VECTORS&CENTER='500@399'&REF_PLANE=ECLIPTIC&STEP_SIZE=1%20d&START_TIME=2025-01-01&STOP_TIME=2025-01-03"
```

### Windows
1. Установите Python 3 с https://www.python.org/downloads/ (галочка «Add Python to PATH»).
2. PowerShell:
   ```powershell
   py -m pip install astroquery
   py - <<'PY'
   from astroquery.jplhorizons import Horizons
   obj = Horizons(id='DES=1004083;', location='500@399', epochs={'start':'2025-01-01', 'stop':'2025-01-10', 'step':'1d'})
   print(obj.vectors())
   PY
   ```
3. Пользователи WSL могут следовать инструкциям для macOS/Linux.

### Классический CLI (Telnet)
```bash
telnet horizons.jpl.nasa.gov 6775
```
Следуйте подсказкам, вводите `DES=1004083;` и нужные параметры.

### Установка Python 3.10+ в Linux

Используйте пакетные менеджеры (apt, dnf, zypper, pacman …). Если нужной версии нет — pyenv или сборка из исходников. Даже если Python уже установлен, лучше иметь собственную версии ≥3.10 и виртуальные окружения (`python3 -m venv`).
