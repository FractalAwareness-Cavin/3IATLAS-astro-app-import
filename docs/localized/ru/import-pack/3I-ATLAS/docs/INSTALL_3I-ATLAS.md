# 3I/ATLAS — набор для импорта (v0.2)

Используйте этот набор, когда вам нужны **готовые орбитальные элементы MPC**
или вспомогательные инструменты для переноса 3I/ATLAS в астрономическое ПО.
Все работает офлайн и основано на решении JPL SBDB №27 (2025-10-10).

> **Коротко**
> - **Stellarium** → импортируйте предоставленную строку через *Solar System Editor → Import elements in MPC format*.
> - **KStars** → запустите помощник без установки (Windows/macOS/Linux) или вставьте строку `comets.dat`.
> - **SkySafari** → используйте *Settings → Solar System → Update Orbit Data* (Plus/Pro) и храните MPC-строку для справки.
> - **Solar Fire** → объедините блок `[3I_ATLAS]` с `extras.dat` (сделайте резервную копию); прилагаются скрипты.
> - **Astro Gold / TimePassages** → импорт движущихся тел пока недоступен; подробности см. в основном репозитории.

## Содержимое

- `templates/stellarium/3I_ATLAS_mpc_elements.txt` — орбитальные элементы MPC в одну строку.
- `templates/skysafari/3I_ATLAS_mpc_1line.txt` — та же строка для хранения и ссылок.
- `templates/kstars/3I_ATLAS_comets_dat_snippet.txt` — готовая строка для `comets.dat` (подходит и для Cartes du Ciel / WinStars).
- `templates/solar_fire/3I_ATLAS_extras_dat_PLACEHOLDER.txt` — готовый блок `[3I_ATLAS]` для `extras.dat` в Solar Fire.
- `tools/3i_elements_to_formats.py` — опциональный конвертер для новых MPC-строк.
- `tools/update_orbital_elements.py` — получает последнюю JPL SBDB и перезаписывает шаблоны.
- `docs/WORKFLOWS.md` — пошаговые инструкции для Stellarium, KStars, Cartes du Ciel, WinStars, SkySafari, Solar Fire.

## Быстрый старт

Все актуально? Перейдите прямо к `docs/WORKFLOWS.md`. Чтобы обновлять набор, когда JPL
публикует новую орбиту, выполните:
```bash
python tools/update_orbital_elements.py --dry-run  # просмотр свежих элементов
python tools/update_orbital_elements.py            # перезапись шаблонов
```
Если проще заменить файлы вручную, `tools/3i_elements_to_formats.py`
создаст фрагменты для Stellarium/KStars/Solar Fire из любой MPC-строки.

## Предупреждения

- **Solar Fire `extras.dat`**: порядок полей зависит от версии. При ручном редактировании
воспользуйтесь подсказкой «Format of the Orbital Elements File» и обязательно сделайте резервную копию.
- **SkySafari**: ручного импорта файлов нет; полагайтесь на *Update Orbit Data*.
- **Astro Gold / TimePassages**: на момент написания эти программы не поддерживают импорт движущихся тел. Используйте пользовательские фиксированные точки или обращайтесь к разработчику.
- **Проверка**: запустите `tools/verify_ephemeris.py`, чтобы сравнить выбранные строки из
`apps-using-mpc-files/geocentric_mpc_ephemeris.txt` с актуальными данными Horizons, если хотите перепроверить эфемериды.
