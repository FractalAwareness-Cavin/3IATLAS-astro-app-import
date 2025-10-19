3I/ATLAS Y APLICACIONES SIN IMPORTACIÓN
======================================

Esta nota explica las limitaciones actuales de **Astro Gold** (macOS, iOS/iPadOS)
y **TimePassages Desktop** (macOS / Windows), además de cómo aprovechar sus
funciones integradas de «puntos extra».

## Astro Gold (macOS / iOS / iPadOS)
- Astro Gold solo permite activar o desactivar el catálogo de cuerpos que el
  desarrollador incluye con la app. No existe un método documentado para importar
  efemérides o elementos orbitales de terceros.
- Puedes activar los extras del proveedor desde:
  - **macOS**: `Astro Gold → Preferences → Displayed Points → Add Extra Points…`
  - **iOS / iPadOS**: `Settings → Chart Points → Add Extra Points…`
- Los «Custom Points» de Astro Gold son longitudes eclípticas fijas que introduces
  manualmente. Sirven para estrellas de referencia o grados específicos, pero
  no se actualizan con el tiempo.
- Los usuarios avanzados pueden revisar las carpetas de soporte (p. ej.
  `~/Library/Application Support/com.ajnaware.Astro-Gold` en macOS o
  `~/Documents/Astro Gold` para cartas), aunque esas carpetas **no** aceptan
  efemérides móviles mediante simple copia.

**Conclusión:** Hasta que Esoteric Technologies añada 3I/ATLAS a su catálogo (o brinde
un mecanismo de importación), no es posible instalarlo como cuerpo móvil en Astro Gold.
Utiliza los extras integrados o registra 3I/ATLAS como punto fijo si solo necesitas
su posición en una época concreta.

### Guía de punto fijo (Astro Gold)
1. Elige la fecha y hora a congelar (ejemplo: **2025-10-29 00:00 UT** cerca del perihelio).
2. Abre `apps-using-csv-files/geocentric_daily.csv` y localiza la fila correspondiente. Anota la longitud tropical (`lambda_deg`) y la latitud (`beta_deg`). En el ejemplo: `lambda_deg = 203.560 deg` (≈ 23°33' Escorpio) y `beta_deg = 2.283 deg`.
3. En Astro Gold (macOS) ve a **Astro Gold → Preferences → Displayed Points → Add Extra Points…** y cambia a la pestaña **Custom Points**. En iOS/iPadOS usa **Settings → Chart Points → Add Extra Points…**.
4. Crea un nuevo punto con un nombre como `3I/ATLAS 2025-10-29 UT`, introduce la longitud en formato decimal (o en el formato signo/grado que espera la app) y guarda opcionalmente la latitud o la distancia.
5. Guarda el punto. Permanecerá estático; repite el proceso con otra longitud cuando necesites un nuevo momento.

## TimePassages Desktop (macOS / Windows)
- TimePassages permite activar los cuerpos incluidos con el programa (asteroides
  principales, centauros, Eris/TNO, etc.). El flujo es:
  - `Preferences → Edit Chart Points` (macOS) o `Edit → Chart Points…` (Windows) para activar categorías.
  - `Display → Chart Points…` para asegurarte de que se vean en las cartas.
- La función **Custom Points** también trabaja con grados fijos (por ejemplo, puedes
  introducir el Centro Galáctico a 27° Sagitario). Actualmente TimePassages no ofrece
  un mecanismo de importación para nuevos objetos móviles.
- Las carpetas visibles para el usuario (p. ej.
  `~/Library/Application Support/TimePassages/` en macOS o
  `%APPDATA%\TimePassages\` en Windows) solo almacenan preferencias y cartas guardadas;
  no aceptan efemérides externas.

**Conclusión:** TimePassages aún no puede seguir 3I/ATLAS de forma automática. Si en el
futuro añade soporte de importación, aquí encontrarás las instrucciones. Por ahora puedes
crear un punto fijo personalizado en una fecha concreta para tener una referencia estática.

### Guía de punto fijo (TimePassages)
1. Decide la época que necesitas (p. ej. **2025-10-18 00:00 UT** cerca de la máxima elongación).
2. Consulta `apps-using-csv-files/geocentric_daily.csv`. La fila de 2025-10-18 muestra
   `lambda_deg = 209.285 deg` (≈ 29°17' Libra) y `beta_deg = 2.715 deg`.
3. En TimePassages abre **Edit → Chart Points…** (Windows) o **Preferences → Edit Chart Points** (macOS), ve a **Custom Points** y pulsa **Add**.
4. Escribe un nombre (por ejemplo `3I/ATLAS 2025-10-18 UT`) e introduce la longitud en el formato signo/grado propio de TimePassages. Añade latitud o distancia en la descripción si quieres más contexto.
5. Guarda y habilita el punto. Sustitúyelo por una longitud actualizada cuando necesites otro instante.

---

### Solicitar soporte al proveedor
Si deseas que estas aplicaciones admitan 3I/ATLAS (o importaciones personalizadas en general), contacta con los responsables:
- Esoteric Technologies (Astro Gold):
  https://www.astrogold.io/contact
- AstroGraph (TimePassages):
  https://www.astrograph.com/contact.php

Puedes remitirles los datos orbitales presentes en este repositorio para facilitar una integración oficial.
