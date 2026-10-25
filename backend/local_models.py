"""User-selected inference engines and local GGUF imports; never runs inference."""
from __future__ import annotations

import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import threading
from urllib.parse import urlparse

import httpx

ROOT = Path(__file__).resolve().parents[1]
_settings_lock = threading.Lock()
_import_lock = threading.Lock()


def models_directory() -> Path:
    base = Path(sys.executable).parent if getattr(sys, 'frozen', False) else ROOT
    folder = Path(os.environ.get('PROMPT_STUDIO_MODELS_DIR', str(base / 'ai-models'))).resolve()
    folder.mkdir(parents=True, exist_ok=True)
    return folder


def settings_file() -> Path:
    return Path(os.environ.get('PROMPT_STUDIO_SETTINGS_DIR', str(ROOT / 'data'))) / 'engine-settings.json'


def selected_model() -> str:
    try:
        return str(json.loads(settings_file().read_text(encoding='utf-8')).get('model') or '').strip()
    except (OSError, ValueError):
        return os.environ.get('OLLAMA_MODEL', '').strip()


def validate_model_name(name: str) -> str:
    name = name.strip()
    if not re.fullmatch(r'[a-zA-Z0-9][a-zA-Z0-9._/-]*(?::[a-zA-Z0-9][a-zA-Z0-9._-]*)?', name) or len(name) > 120 or '..' in name or '//' in name:
        raise ValueError('Nombre del modelo Ollama no válido.')
    return name


def save_selection(model: str) -> None:
    model = validate_model_name(model)
    with _settings_lock:
        target = settings_file()
        target.parent.mkdir(parents=True, exist_ok=True)
        temporary = target.with_suffix('.tmp')
        temporary.write_text(json.dumps({'model': model}, ensure_ascii=False) + '\n', encoding='utf-8')
        temporary.replace(target)


def local_files() -> list[dict]:
    folder = models_directory()
    files = []
    for path in folder.iterdir():
        if path.is_file() and path.suffix.lower() == '.gguf' and path.resolve().parent == folder:
            slug = re.sub(r'[^a-z0-9._-]+', '-', path.stem.lower()).strip('-.')[:85] or 'local-model'
            files.append({'filename': path.name, 'size': path.stat().st_size, 'suggested_name': f'promptstudio/{slug}:latest'})
    return sorted(files, key=lambda item: item['filename'].casefold())


async def installed_models(url: str) -> list[str]:
    async with httpx.AsyncClient(timeout=5.0) as client:
        response = await client.get(url + '/api/tags')
        response.raise_for_status()
    return sorted({item['name'] for item in response.json().get('models', []) if item.get('name')}, key=str.casefold)


def import_gguf(filename: str, name: str, url: str) -> None:
    name = validate_model_name(name)
    if urlparse(url).hostname not in ('127.0.0.1', 'localhost', '::1'):
        raise ValueError('La importación de archivos requiere Ollama en este equipo.')
    folder = models_directory()
    path = (folder / filename).resolve()
    if path.parent != folder or path.name != filename or path.suffix.lower() != '.gguf' or not path.is_file():
        raise ValueError('Selecciona un archivo GGUF de la carpeta de modelos.')
    if re.search(r'-\d{5}-of-\d{5}\.gguf$', filename, re.I):
        raise ValueError('Los GGUF divididos deben importarse con Ollama fuera de la aplicación.')
    with path.open('rb') as source:
        if source.read(4) != b'GGUF':
            raise ValueError('El archivo no tiene una cabecera GGUF válida.')
    executable = shutil.which('ollama')
    if not executable and sys.platform == 'win32':
        candidate = Path(os.environ.get('LOCALAPPDATA', '')) / 'Programs/Ollama/ollama.exe'
        if candidate.is_file():
            executable = str(candidate)
    if not executable:
        raise RuntimeError('No se encuentra Ollama. Instálalo y vuelve a abrir la aplicación.')
    if not _import_lock.acquire(blocking=False):
        raise RuntimeError('Ya hay una importación en curso.')
    try:
        # Relative filename avoids Windows path escaping in the Modelfile parser.
        with tempfile.TemporaryDirectory(prefix='.import-', dir=folder) as temporary:
            manifest = Path(temporary) / 'Modelfile'
            manifest.write_text('FROM ' + json.dumps('../' + filename, ensure_ascii=False) + '\n', encoding='utf-8')
            result = subprocess.run([executable, 'create', name, '-f', str(manifest)],
                                    env={**os.environ, 'OLLAMA_HOST': url}, capture_output=True,
                                    timeout=1800, creationflags=getattr(subprocess, 'CREATE_NO_WINDOW', 0))
        if result.returncode:
            raise RuntimeError('Ollama no pudo importar el archivo. Comprueba que su arquitectura sea compatible y que haya espacio en disco.')
    except subprocess.TimeoutExpired as exc:
        raise RuntimeError('La importación ha superado el tiempo de espera. Comprueba los modelos instalados antes de repetirla.') from exc
    finally:
        _import_lock.release()
