param(
    [switch]$Apply,
    [string]$UserDataDir = "$env:USERPROFILE\Documents\Solar Fire User Files\Userdata",
    [string]$SourceExtras
)

Write-Host "[Windows helper] PowerShell merge for Solar Fire — see README for full instructions."

function Combine-Path([string]$base, [string]$child) {
    return [System.IO.Path]::GetFullPath([System.IO.Path]::Combine($base, $child))
}

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
if (-not $SourceExtras) {
    $candidates = @(
        Combine-Path $scriptDir "../extras.dat",
        Combine-Path $scriptDir "../../solar-fire/extras.dat"
    )
    foreach ($cand in $candidates) {
        if (Test-Path $cand) { $SourceExtras = (Resolve-Path $cand).Path; break }
    }
}
if (-not $SourceExtras -or -not (Test-Path $SourceExtras)) {
    Write-Error "Unable to locate source extras.dat. Use -SourceExtras to specify the path."; exit 1
}

$Target = Combine-Path $UserDataDir "extras.dat"
$Stamp = Get-Date -Format "yyyyMMdd-HHmmss"
$Backup = "$Target.bak.$Stamp"

$srcLines = Get-Content -LiteralPath $SourceExtras
$match = $srcLines | Select-String -Pattern '^\s*\[3I_ATLAS\]' -CaseSensitive:$false
if (-not $match) { Write-Error "Source extras.dat does not contain a [3I_ATLAS] block."; exit 1 }
$startIdx = $match.LineNumber
$endIdx = $srcLines.Length
for ($i = $startIdx + 1; $i -le $srcLines.Length; $i++) {
    if ($srcLines[$i-1] -match '^\s*\[') { $endIdx = $i - 1; break }
}
$block = $srcLines[($startIdx-1)..($endIdx-1)]

Write-Host "Target extras.dat:" $Target
Write-Host "\n--- PREVIEW (block to merge) ---"
$block | ForEach-Object { Write-Host $_ }
Write-Host "--- END PREVIEW ---\n"

if (-not $Apply) {
    Write-Host "[DRY-RUN] No changes made. Re-run with -Apply to write." -ForegroundColor Green
    exit 0
}

if (-not (Test-Path $UserDataDir)) { New-Item -ItemType Directory -Path $UserDataDir | Out-Null }

if (Test-Path $Target) {
    Copy-Item -LiteralPath $Target -Destination $Backup -Force
    Write-Host "[OK] Backup created at $Backup"
    $dstLines = Get-Content -LiteralPath $Target
    $clean = @()
    $skipping = $false
    foreach ($line in $dstLines) {
        if ($line -match '^\s*\[3I_ATLAS\]') { $skipping = $true; continue }
        if ($skipping -and $line -match '^\s*\[') { $skipping = $false }
        if (-not $skipping) { $clean += $line }
    }
} else {
    $clean = @()
    Write-Host "[INFO] Target extras.dat did not exist; a new file will be created."
}

if ($clean.Count -gt 0 -and $clean[-1] -ne '') { $clean += '' }
$clean += $block
$clean | Set-Content -LiteralPath $Target -Encoding UTF8
Write-Host "[OK] Merged [3I_ATLAS] into $Target"
