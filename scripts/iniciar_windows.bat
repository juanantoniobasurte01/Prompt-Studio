@echo off
setlocal
cd /d "%~dp0.."
where python >nul 2>&1
if errorlevel 1 (echo ERROR: Instala Python 3.11 o superior & pause & exit /b 1)
where npm >nul 2>&1
if errorlevel 1 (echo ERROR: Instala Node.js LTS & pause & exit /b 1)
start "promptstudio Backend" powershell -NoExit -ExecutionPolicy Bypass -File "%~dp0iniciar_backend.ps1"
start "promptstudio Frontend" powershell -NoExit -ExecutionPolicy Bypass -File "%~dp0iniciar_frontend.ps1"
echo Servidores iniciando en dos ventanas. Abre http://127.0.0.1:5173
pause
