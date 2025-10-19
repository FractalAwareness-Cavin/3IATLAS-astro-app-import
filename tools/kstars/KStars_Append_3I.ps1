param(
    [string]$Target = "$env:LOCALAPPDATA\kstars\comets.dat",
    [string]$LineFile,
    [switch]$Apply
)

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
if (-not $LineFile) {
    $candidates = @(
        Join-Path $scriptDir "..\3I_ATLAS_comets_dat_line.txt",
        Join-Path $scriptDir "..\..\import-pack\3I-ATLAS\templates\kstars\3I_ATLAS_comets_dat_snippet.txt"
    )
    foreach ($cand in $candidates) {
        if (Test-Path $cand) { $LineFile = (Resolve-Path $cand).Path; break }
    }
}
if (-not $LineFile -or -not (Test-Path $LineFile)) {
    Write-Error "Unable to locate 3I_ATLAS_comets_dat_line.txt. Use -LineFile to specify the path."; exit 1
}

$line = Get-Content -LiteralPath $LineFile | Where-Object { $_ -and ($_ -notmatch '^[\s#]') } | Select-Object -First 1
if (-not $line) { Write-Error "No usable entry found in $LineFile"; exit 1 }

Write-Host "Target comets.dat:" $Target
Write-Host "\n--- PREVIEW ---" `n$line`n"---------------"`n
if (-not $Apply) {
    Write-Host "[DRY-RUN] No changes made. Re-run with -Apply for actual write." -ForegroundColor Green
    exit 0
}

$targetDir = Split-Path -Parent $Target
if (-not (Test-Path $targetDir)) { New-Item -ItemType Directory -Path $targetDir | Out-Null }

$stamp = Get-Date -Format "yyyyMMdd-HHmmss"
if (Test-Path $Target) {
    $backup = "$Target.bak.$stamp"
    Copy-Item -LiteralPath $Target -Destination $backup -Force
    Write-Host "[OK] Backup created at $backup"
    $content = Get-Content -LiteralPath $Target
    $filtered = foreach ($l in $content) {
        if ($l -match '3I/ATLAS') { continue }
        $l
    }
    Set-Content -LiteralPath $Target -Value $filtered -Encoding UTF8
} else {
    New-Item -ItemType File -Path $Target | Out-Null
    Write-Host "[INFO] Target file was created."
}

if ((Get-Item $Target).Length -gt 0) { Add-Content -LiteralPath $Target -Value "" }
Add-Content -LiteralPath $Target -Value $line
Write-Host "[OK] Appended 3I/ATLAS to $Target"
