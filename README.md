# promptstudio

Local prompt editor for AI image and video models. A Windows desktop app built around Ollama, with model-specific guides, a structured editor and an editable result you can copy into your generator.

[Español](README.es.md)

Write an idea in the free-text box, choose a target model if you have one, and refine the prompt. For more control, use the guided fields for people, clothing, actions, camera, lighting and timing. Every field is optional and accepts custom text.

promptstudio writes prompts. It does not render images or videos, upload reference files or call generation providers.

## What is included

- Download buttons for 15 community uncensored/abliterated engines, with installation status and file progress.
- Light, dark and system themes; a separate negative prompt input for exclusions.
- 43 model profiles for image and video prompts, including FLUX, Stable Diffusion, Midjourney, Kling, Wan and MiniMax.
- Six editable examples per profile: 258 presets covering different people, actions and settings.
- 119 optional fields, with separate controls for gender, age, build and muscle definition.
- Model-specific formatting for references, shot structure, dialogue, audio and negative prompts.
- English and Spanish interfaces. Prompt language is a separate setting.
- Saved presets and history in SQLite, plus clipboard copy and JSON export.

See the [model list](docs/MODELS.md) for the full catalogue and links to each guide. Profiles marked as partially verified keep that label in the app.

## Run on Windows

Download `promptstudio.exe` from the repository's **Releases** tab and open it. The executable includes the interface, backend, guides and example presets. Python and Node.js are not required to run it.

You need Windows 10 or 11, Microsoft Edge WebView2 and a running [Ollama](https://ollama.com/) installation. Choose an installed chat model under **Settings → AI engine**. promptstudio is not tied to a particular model family; the selection is saved and stays in effect when you load presets or history.

To add a local model, copy a compatible single-file `.gguf` into `ai-models` beside the EXE. Open the folder from Settings, refresh the list, import the file into Ollama with a unique name, then select it. The source version uses `ai-models` at the project root. [Local model setup](docs/MODELO_LOCAL.md) explains storage, compatibility and environment overrides. Model weights are not included or downloaded automatically.

Your presets, history and settings live in `%LOCALAPPDATA%\promptstudio`. Replacing the EXE does not replace that folder. [Desktop setup and storage](docs/ESCRITORIO.md) covers configuration and importing an existing database.

## Build the EXE

Install Python 3.11 and Node.js 22 or later, then run this from the project root:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\empaquetar_windows.ps1
```

The result is `dist/promptstudio.exe`. Build dependencies are listed in `requirements-build.txt`; the script compiles the frontend before packaging the app.

## Work on the source

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.\.venv\Scripts\python.exe -m pytest -q
```

For frontend development, run the API and Vite in separate terminals:

```powershell
.\.venv\Scripts\python.exe -m uvicorn backend.main:app --host 127.0.0.1 --port 8000
```

```powershell
cd frontend
npm ci
npm run dev
```

Open `http://127.0.0.1:5173`. Use `npm run build` to check the production frontend. Tests mock inference and do not need Ollama or model downloads.

The frontend is React and Vite; the backend is FastAPI. `models/catalog.json` maps each profile to its Markdown guide. Only the selected guide and its shared rules are loaded for a request.

## Documentation

- [Desktop application](docs/ESCRITORIO.md)
- [Models and guides](docs/MODELS.md)
- [Presets and languages](docs/PRESETS_E_IDIOMAS.md)
- [Local model configuration](docs/MODELO_LOCAL.md)
- [API contract](docs/CONTRATO_API.md)
- [Contributing](CONTRIBUTING.md)
- [Changelog](CHANGELOG.md)

## License

[MIT](LICENSE). Dependencies and model providers keep their own licenses and trademarks; see [NOTICE](NOTICE.md).
