@echo off
set SCRIPT_DIR=%~dp0
if exist "%ProgramFiles%\PowerShell\7\pwsh.exe" (
  "%ProgramFiles%\PowerShell\7\pwsh.exe" -ExecutionPolicy Bypass -File "%SCRIPT_DIR%SF_Merge_3I.ps1" %*
) else if exist "%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" (
  powershell -ExecutionPolicy Bypass -File "%SCRIPT_DIR%SF_Merge_3I.ps1" %*
) else (
  echo PowerShell not found. Install PowerShell 7 or use a newer Windows build.
)
pause
