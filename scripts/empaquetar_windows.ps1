param([string]$OutputDirectory = 'dist')
$ErrorActionPreference = 'Stop'
$projectRoot = Split-Path -Parent $PSScriptRoot
Set-Location $projectRoot
if (-not (Test-Path .venv/Scripts/python.exe)) {
    python -m venv .venv
    if ($LASTEXITCODE -ne 0) { throw 'No se pudo crear el entorno Python.' }
}
& .venv/Scripts/python.exe -m pip install --disable-pip-version-check -r requirements-build.txt
if ($LASTEXITCODE -ne 0) { throw 'Falló la instalación de dependencias de escritorio.' }
Push-Location frontend
try {
    if (-not (Test-Path node_modules)) {
        & npm.cmd ci
        if ($LASTEXITCODE -ne 0) { throw 'Falló npm ci.' }
    }
    & npm.cmd run build
    if ($LASTEXITCODE -ne 0) { throw 'Falló la compilación de la interfaz.' }
} finally { Pop-Location }
& $PSScriptRoot/generar_icono.ps1
& .venv/Scripts/python.exe -m PyInstaller --noconfirm --clean --workpath laboratorio/pyinstaller --distpath $OutputDirectory promptstudio.spec
if ($LASTEXITCODE -ne 0) { throw 'No se pudo empaquetar el EXE.' }
$modelsDirectory = Join-Path $OutputDirectory 'ai-models'
New-Item -ItemType Directory -Path $modelsDirectory -Force | Out-Null
Copy-Item -LiteralPath ai-models/README.md -Destination (Join-Path $modelsDirectory 'README.md') -Force
Write-Output ('EXE creado: ' + (Join-Path $OutputDirectory 'promptstudio.exe'))
