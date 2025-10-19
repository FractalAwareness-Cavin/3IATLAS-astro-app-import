3I/ATLAS PARA SOLAR FIRE (WINDOWS)
==================================

Solar Fire no importa efemérides precalculadas para nuevos cuerpos; lee los elementos orbitales desde `extras.dat`. Esta carpeta mantiene la entrada de 3I/ATLAS alineada con la solución 27 del JPL SBDB.

Probado en
---------
- Solar Fire 9: `Documents\Solar Fire 9 User Files\Points & Colors\extras.dat`
- Solar Fire 10: `Documents\Solar Fire User Files\Points & Colors\extras.dat`
- Solar Fire 11: `Documents\Solar Fire User Files\Points & Colors\extras.dat`

Contenido
---------
- `extras.dat`: bloque `[3I_ATLAS]` listo para usar (ver abajo) más comentarios para fusiones manuales.
- `geocentric_daily_solarfire.txt` y archivos similares: tablas de referencia opcionales para comprobar posiciones fuera de Solar Fire.

Bloque de ejemplo
-----------------
Pega este bloque en tu `extras.dat` o deja que el asistente lo fusione automáticamente:

```
[3I_ATLAS]
Name = 3I/ATLAS
Number = 0
EpochJD = 2460884.5
PerihelionDistance_AU = 1.356065571
Eccentricity = 6.137350157
Inclination_deg = 175.112857794
AscendingNode_deg = 322.152284965
ArgumentOfPerihelion_deg = 128.011608252
PerihelionTime_JD = 2460977.983535961
AbsoluteMagnitude = 12.3
SlopeParameter = 4.5
; Solar Fire ignora el semieje mayor cuando Tp está definido para cometas.
; Este objeto es hiperbólico (e>1). Verifica la compatibilidad con tu versión de Solar Fire.
```

Pasos de instalación
--------------------
1. Cierra Solar Fire.
2. Ejecuta los scripts auxiliares (`tools/solarfire/SF_Merge_3I-DRYRUN.bat`, luego `tools/solarfire/SF_Merge_3I-APPLY.bat`) **o** haz una copia de tu `extras.dat` actual.
3. Abre la ruta correspondiente a tu versión (arriba) y agrega el bloque. Conserva los cuerpos personalizados existentes.
4. Reinicia Solar Fire, abre **File → File Types…** y confirma que **Extra Bodies** apunta al archivo actualizado.
5. En el diálogo de selección de puntos, marca `3I/ATLAS` en **Extra Bodies / Other Bodies**.

Mini-FAQ
--------
- **3I/ATLAS no aparece tras la fusión.** Asegúrate de editar la carpeta `extras.dat` correcta (Solar Fire mantiene carpetas separadas por versión) y de que el cuerpo esté activado en **Extra Bodies**.
- **El script indica "access denied".** Cierra Solar Fire antes de ejecutar el script APPLY; la fusión no puede sobrescribir un `extras.dat` abierto.
- **Necesito elementos más recientes.** Ejecuta `python tools/update_orbital_elements.py` en la raíz del repositorio y vuelve a lanzar el asistente para reemplazar el bloque con la última solución SBDB.
