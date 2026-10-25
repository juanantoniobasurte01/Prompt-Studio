$ErrorActionPreference = 'Stop'
$root=Split-Path -Parent $PSScriptRoot
Set-Location $root
if (-not (Test-Path .venv/Scripts/python.exe)) {
  python -m venv .venv
  if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
}
$hashAlgorithm = [System.Security.Cryptography.SHA256]::Create()
try {
  $requirementsHash = [BitConverter]::ToString($hashAlgorithm.ComputeHash([IO.File]::ReadAllBytes((Join-Path $root 'requirements.txt'))))
} finally {
  $hashAlgorithm.Dispose()
}
$stamp = '.venv/requirements.sha256'
if (-not (Test-Path $stamp) -or (Get-Content $stamp -Raw).Trim() -ne $requirementsHash) {
  & .\.venv\Scripts\python.exe -m pip install --disable-pip-version-check -r requirements.txt
  if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
  Set-Content -Path $stamp -Value $requirementsHash -Encoding ASCII
}
$serverArgs = @('-m', 'uvicorn', 'backend.main:app', '--host', '127.0.0.1', '--port', '8000')
if (Test-Path .env) { $serverArgs += @('--env-file', '.env') }
& .\.venv\Scripts\python.exe @serverArgs
exit $LASTEXITCODE
