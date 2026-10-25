# promptstudio

Editor local de prompts para modelos de imagen y vídeo. Es una aplicación de escritorio para Windows que utiliza Ollama, con guías por modelo, campos opcionales y un resultado editable para copiar en tu generador.

[English](README.md)

Escribe una idea en el campo libre y, si tienes un modelo de destino, selecciónalo. El editor guiado permite concretar personas, ropa, acciones, cámara, luz y tiempos. Puedes dejar cualquier campo vacío o escribir tu propio valor.

promptstudio redacta prompts. No genera imágenes ni vídeos, no sube archivos de referencia y no llama a proveedores de generación.

## Qué incluye

- Descarga de 15 motores comunitarios uncensored/abliterated, con estado de instalación y progreso por archivo.
- Tema claro, oscuro o del sistema y entrada separada de prompt negativo.
- 43 perfiles de imagen y vídeo, entre ellos FLUX, Stable Diffusion, Midjourney, Kling, Wan y MiniMax.
- Seis ejemplos editables por perfil: 258 presets con personas, acciones y entornos variados.
- 119 campos opcionales. Género, edad, complexión y musculatura se definen por separado.
- Formato específico para referencias, planos, diálogos, audio y negativos según el modelo.
- Interfaz en español e inglés, independiente del idioma del prompt.
- Presets propios e historial en SQLite, copia al portapapeles y exportación JSON.

La [lista de modelos](docs/MODELS.md) enlaza cada perfil con su guía. Los perfiles con documentación parcialmente verificada conservan esa indicación en la aplicación.

## Usar la aplicación en Windows

Descarga `promptstudio.exe` desde la pestaña **Releases** del repositorio y ábrelo. El ejecutable incluye interfaz, backend, guías y presets de ejemplo. Para usarlo no necesitas Python ni Node.js.

Necesitas Windows 10 u 11, Microsoft Edge WebView2 y [Ollama](https://ollama.com/) en ejecución. Elige un modelo de conversación instalado en **Configuración → Motor de IA**. La aplicación guarda tu elección y la mantiene al abrir presets o historial; no depende de una familia concreta.

Para añadir un modelo local, copia un archivo `.gguf` compatible en `ai-models`, junto al EXE. Desde Configuración puedes abrir esa carpeta, actualizar la lista, importar el archivo en Ollama con un nombre único y seleccionarlo. Al ejecutar desde código, la carpeta está en la raíz del proyecto. Consulta [Modelos locales](docs/MODELO_LOCAL.md) para conocer la compatibilidad y las rutas configurables. Los pesos no se incluyen ni se descargan automáticamente.

Los presets, el historial y la configuración se guardan en `%LOCALAPPDATA%\promptstudio`. Actualizar el EXE no reemplaza esa carpeta. Consulta [Escritorio](docs/ESCRITORIO.md) para configurar la aplicación o importar una base existente.

## Compilar el EXE

Instala Python 3.11 y Node.js 22 o posterior. Desde la raíz del proyecto:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\empaquetar_windows.ps1
```

El resultado queda en `dist/promptstudio.exe`. Las dependencias de compilación están en `requirements-build.txt`; el script compila la interfaz antes de empaquetar.

## Desarrollo

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.\.venv\Scripts\python.exe -m pytest -q
```

Para trabajar en la interfaz, ejecuta la API y Vite en dos terminales:

```powershell
.\.venv\Scripts\python.exe -m uvicorn backend.main:app --host 127.0.0.1 --port 8000
```

```powershell
cd frontend
npm ci
npm run dev
```

Abre `http://127.0.0.1:5173`. `npm run build` comprueba la compilación de producción. Las pruebas simulan la inferencia: no necesitan Ollama ni descargar modelos.

La interfaz utiliza React y Vite; el backend, FastAPI. `models/catalog.json` relaciona cada perfil con su guía Markdown. Cada petición carga únicamente la guía elegida y sus reglas comunes.

## Documentación

- [Aplicación de escritorio](docs/ESCRITORIO.md)
- [Modelos y guías](docs/MODELS.md)
- [Presets e idiomas](docs/PRESETS_E_IDIOMAS.md)
- [Configuración del modelo local](docs/MODELO_LOCAL.md)
- [Contrato de la API](docs/CONTRATO_API.md)
- [Contribuir](CONTRIBUTING.md)
- [Cambios](CHANGELOG.md)

## Licencia

[MIT](LICENSE). Las dependencias y los proveedores conservan sus licencias y marcas; consulta [NOTICE](NOTICE.md).
