# Скрипты для разработчиков

Утилиты для регенерации и проверки набора эфемерид 3I/ATLAS находятся в `developer/scripts/` и `tools/`. Эта памятка пригодится, когда нужно обновить данные или убедиться в корректности правок перед выпуском релиза.

## Требования
- Python 3.10 или новее (`python3 --version` для проверки).
- Опционально: виртуальное окружение (`python3 -m venv .venv && source .venv/bin/activate`), если планируются дополнительные пакеты.
- Доступ в интернет при запуске обновления SBDB или проверяющего Horizons.
- Опционально: `mksweph`, если хотите собирать бинарные файлы Swiss Ephemeris через `build_swisseph.sh`.

Репозиторий включает `pyswisseph` в `developer/vendor/`, поэтому сидерические данные работают без отдельных установок.

## Рецепт Horizons по умолчанию

Сырые JSON-файлы в `developer/raw/` получены из NASA/JPL Horizons со следующими параметрами:

```
COMMAND='DES=1004083;'
MAKE_EPHEM='YES'
EPHEM_TYPE='VECTORS'
CENTER='500@399'        # центр Земли
REF_PLANE='ECLIPTIC'
REF_SYSTEM='J2000'
START_TIME='2016-01-01'
STOP_TIME='2040-12-31'
STEP_SIZE='1 d'
TABLE_TYPE='VECTORS'
```

Меняйте их под свои задачи (другой интервал, точка наблюдения), затем перегенерируйте JSON до пересборки результатов.

## `generate_ephemeris.py`
Путь: `developer/scripts/generate_ephemeris.py`

- Читает JSON-векторы в `developer/raw/` и формирует все производные артефакты:
  - CSV-таблицы в `apps-using-csv-files/`
  - Текстовые таблицы Solar Fire в `solar-fire/`
  - Эфемериду MPC (`apps-using-mpc-files/geocentric_mpc_ephemeris.txt`)
  - Сводки входов в знаки.
- Автоматически подключает встроенный модуль `pyswisseph` для заполнения сидерических полей.
- Создаёт целевые каталоги, если их нет.

Использование:

```
cd developer/scripts
python3 generate_ephemeris.py
```

Скрипт использует встроенные настройки. Чтобы изменить временной диапазон или шаг, обновите JSON (или правьте константы в верхней части файла).

## `build_swisseph.sh`
Путь: `developer/scripts/build_swisseph.sh`

- Требует проприетарную утилиту `mksweph`.
- Преобразует CSV-выводы в бинарные файлы Swiss Ephemeris `.se1` и сохраняет их в `developer/swisseph/`.

Использование:

```
cd developer/scripts
bash build_swisseph.sh
```

Помощник завершится с ошибкой, если `mksweph` отсутствует в `PATH`.

## `tools/update_orbital_elements.py`
Путь: `tools/update_orbital_elements.py`

- Загружает свежую SBDB-орбиту для 3I/ATLAS и обновляет все однострочные шаблоны:
  - MPC-файлы (`apps-using-mpc-files/*/3I_ATLAS_mpc_1line.txt`)
  - Фрагменты KStars (`apps-using-mpc-files/kstars/` и шаблоны набора импорта)
  - Блоки `extras.dat` для Solar Fire.
- Выводит полученные элементы в stdout для проверки.

Использование (из корня репозитория):

```
python tools/update_orbital_elements.py
```

Добавьте `--dry-run`, чтобы посмотреть значения, не изменяя файлы.

## `tools/verify_ephemeris.py`
Путь: `tools/verify_ephemeris.py`

- Проверяет строки `apps-using-mpc-files/geocentric_mpc_ephemeris.txt` на соответствие актуальным данным Horizons.
- Сравнивает геоцентрическое расстояние («delta») в заданном диапазоне дат и отмечает строки, превышающие допустимую погрешность.

Использование (из корня репозитория):

```
python tools/verify_ephemeris.py --start 2025-10-01 --days 5 --tolerance 5e-4
```

Параметры:
- `--start`: начальная дата проверки (по умолчанию `2025-10-01`).
- `--days`: количество последовательных дней (по умолчанию `5`).
- `--tolerance`: допустимая разница в астрономических единицах (по умолчанию `5e-4`, примерно 75 000 км).

Скрипт завершится с ненулевым кодом, если найдены отклонения, что удобно для CI.
