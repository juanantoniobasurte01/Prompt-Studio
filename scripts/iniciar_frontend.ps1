$ErrorActionPreference = 'Stop'
$root=Split-Path -Parent $PSScriptRoot
Set-Location "$root/frontend"
if (-not (Test-Path node_modules)) {
  npm.cmd ci
  if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
}
npm.cmd run dev
exit $LASTEXITCODE
