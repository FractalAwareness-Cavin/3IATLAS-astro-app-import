3I/ATLAS — РУКОВОДСТВО ПО ИМПОРТУ MPC
=====================================

`geocentric_mpc_ephemeris.txt` содержит ежедневные эфемериды в стиле MPC (UT 0h, ПР/СК J2000, delta, r, элонгация, фаза). Используйте файл в любом ПО, которое понимает классический 80-колоночный формат комет. Готовые наборы лежат в релизах (см. `README.md` в корне) и в каталоге `apps-using-mpc-files/`.

Релизные наборы
---------------
- `Stellarium_quick-import.zip`: импортирует одиночный файл MPC через плагин Solar System Editor.
- `KStars_quick-append_Win-Mac-Linux.zip`: помощники предпросмотра/применения для `comets.dat` на всех платформах.
- `3I-ATLAS_apps_using_mpc_files.zip`: полный набор этого каталога с шаблонами одной строки для Cartes du Ciel и WinStars.

Stellarium (Win/macOS/Linux)
----------------------------
1. Распакуйте `Stellarium_quick-import.zip` или скопируйте `geocentric_mpc_ephemeris.txt` в доступное место.
2. В Stellarium нажмите `F2`, откройте **Plugins → Solar System Editor**, поставьте **Load at startup**, затем **Configure** (при первой активации перезапустите).
3. После перезапуска выберите **Solar System Editor → Solar System → Import orbital elements in MPC format**.
4. Нажмите **Select file**, укажите `geocentric_mpc_ephemeris.txt` (или строку из набора), задайте **Object name** = `3I/ATLAS`, тип оставьте *Comet*.
5. Нажмите **Add objects**, закройте диалоги и через поиск (`F3`) убедитесь, что `3I/ATLAS` находится.

KStars (Win/macOS/Linux)
------------------------
1. Распакуйте `KStars_quick-append_Win-Mac-Linux.zip` и запустите скрипт для своей платформы (`*.bat`, `*.command`, `*.sh`, `*.ps1`). Сначала DRYRUN, затем APPLY, чтобы дописать `comets.dat`.
2. Вручную: **Settings → Configure KStars → Solar System** (старые версии: **Data → Solar System Updates**). Во вкладке **Comets** нажмите **Import**, выберите `geocentric_mpc_ephemeris.txt` и подтвердите.
3. При необходимости перезапустите KStars, затем найдите `3I/ATLAS` или откройте Solar System Viewer.

Cartes du Ciel / SkyCharts
--------------------------
1. Скопируйте `apps-using-mpc-files/cartes-du-ciel/3I_ATLAS_mpc_1line.txt` (есть в релизном архиве).
2. Запустите Cartes du Ciel и откройте **Setup → Solar system** (`Ctrl+F3`).
3. Во вкладке **Comets** выберите **Update → Import from MPC file**, укажите `3I_ATLAS_mpc_1line.txt` и подтвердите.
4. Отметьте **3I/ATLAS** в списке и нажмите **OK**. Комета появится в поиске и на картах.
5. Предпочитаете вручную? Добавьте эту строку в `comet.dat` (пути приведены в README подпапки).

WinStars 3 (Win/macOS/Linux)
----------------------------
1. Держите `apps-using-mpc-files/winstars/3I_ATLAS_mpc_1line.txt` под рукой или распакуйте MPC-набор.
2. В WinStars перейдите **Preferences → Solar system → Import orbital elements** (или **Add object**).
3. Выберите режим **MPC single line**, вставьте строку и сохраните.
4. Проверьте, что `3I/ATLAS` включён в списке отображаемых тел; при необходимости перезапустите.

SkySafari / SkyVoyager Plus/Pro (iOS/Android/macOS)
---------------------------------------------------
1. Скопируйте `3I_ATLAS_mpc_1line.txt` в редактор, доступный на устройстве.
2. В SkySafari откройте **Settings → Solar System → Solar System Data** и выберите **Import Comet Data** (в старых версиях **Update Orbit Data → Custom Comet/Asteroid**).
3. Вставьте строку MPC, убедитесь, что имя `3I/ATLAS`, и подтвердите.
4. Найдите `3I/ATLAS`, при необходимости добавьте в список наблюдений.
5. Приложение периодически обновляет MPC-потоки; повторите импорт после смены орбиты.

Другое ПО с поддержкой MPC
-------------------------
1. Скопируйте `geocentric_mpc_ephemeris.txt` или соответствующий однострочный шаблон.
2. Используйте функцию импорта комет/астероидов, выберите файл и назовите объект `3I/ATLAS`.
3. Перезапустите программу, если данные Солнечной системы кэшируются, и убедитесь, что тело включено.

Обновляйте однострочные файлы командой `python tools/update_orbital_elements.py` при выходе новой SBDB-версии и при необходимости проверяйте позиции через `python tools/verify_ephemeris.py`.
