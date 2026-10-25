from __future__ import annotations
import os
import asyncio
from typing import Any, Literal
from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
import httpx
from . import engine, store
from .preset_library import preset_library
from . import local_models
from .engine_catalog import engine_catalog
from .model_downloads import downloads

app = FastAPI(title='promptstudio Local API', version='1.0.0', docs_url='/api/docs', openapi_url='/api/openapi.json')
app.add_middleware(CORSMiddleware, allow_origins=['http://127.0.0.1:5173', 'http://localhost:5173'], allow_methods=['GET','POST','PUT','DELETE'], allow_headers=['Content-Type'])
store.init()

class FieldValue(BaseModel):
    selected: str = Field(default='', max_length=1200)
    manual: str = Field(default='', max_length=5000)

class DraftRequest(BaseModel):
    medium: Literal['auto','image','video'] = 'auto'
    model_id: str | None = None
    manual_model: str = Field(default='', max_length=150)
    mode: Literal['free','guided'] = 'free'
    free_prompt: str = Field(default='', max_length=18000)
    fields: dict[str, FieldValue] = Field(default_factory=dict)
    extra_instructions: str = Field(default='', max_length=3000)
    negative_prompt: str = Field(default='', max_length=5000)
    output_language: str = 'English'
    interface_language: Literal['es', 'en'] = 'es'
    ollama_model: str = Field(default='', max_length=120)
    temperature: float = Field(default=0.45, ge=0, le=1.5)

class PresetRequest(BaseModel):
    name: str = Field(min_length=1, max_length=120)
    content: dict[str, Any]

@app.get('/api/health')
def health():
    return {'ok': True, 'app': 'promptstudio', 'offline': True}

@app.get('/api/models')
def models():
    return {'profiles': engine.catalog(), 'default_ollama_model': local_models.selected_model()}


class EngineSelection(BaseModel):
    model: str = Field(min_length=1, max_length=120)


class ModelImport(EngineSelection):
    filename: str = Field(min_length=1, max_length=255)


@app.get('/api/local-models')
async def local_model_list():
    try:
        files = local_models.local_files()
        directory = str(local_models.models_directory())
    except OSError as exc:
        raise HTTPException(503, 'No se puede acceder a la carpeta de modelos. Configura PROMPT_STUDIO_MODELS_DIR con una ruta escribible.') from exc
    try:
        installed = await local_models.installed_models(engine.OLLAMA_URL)
        online = True
    except (httpx.HTTPError, ValueError):
        installed, online = [], False
    return {'directory': directory, 'files': files, 'installed': installed, 'online': online, 'selected': local_models.selected_model(), 'catalog': engine_catalog()}


@app.get('/api/local-models/download')
def download_status():
    return {'job': downloads.status()}


@app.post('/api/local-models/download')
async def download_engine(request: EngineSelection):
    try:
        if request.model in await local_models.installed_models(engine.OLLAMA_URL):
            return {'job': None, 'installed': True}
        return {'job': downloads.start(request.model, engine.OLLAMA_URL), 'installed': False}
    except ValueError as exc:
        raise HTTPException(400, str(exc)) from exc
    except RuntimeError as exc:
        raise HTTPException(409, str(exc)) from exc
    except httpx.HTTPError as exc:
        raise HTTPException(503, 'Ollama no responde. Abre Ollama antes de descargar.') from exc


@app.put('/api/local-models/selection')
async def select_engine(request: EngineSelection):
    try:
        name = local_models.validate_model_name(request.model)
        if name not in await local_models.installed_models(engine.OLLAMA_URL):
            raise HTTPException(400, 'El motor seleccionado no está instalado en Ollama.')
        local_models.save_selection(name)
        return {'selected': name}
    except ValueError as exc:
        raise HTTPException(400, str(exc)) from exc
    except (httpx.HTTPError, OSError) as exc:
        raise HTTPException(503, 'No se pudo guardar el motor seleccionado. Comprueba Ollama y los permisos de la carpeta de datos.') from exc


@app.post('/api/local-models/import')
async def import_engine(request: ModelImport):
    try:
        name = local_models.validate_model_name(request.model)
        installed = await local_models.installed_models(engine.OLLAMA_URL)
        canonical = name if ':' in name else name + ':latest'
        if canonical.casefold() in {item.casefold() for item in installed}:
            raise HTTPException(409, 'Ya existe un modelo con ese nombre. Elige otro nombre para importarlo.')
        await asyncio.to_thread(local_models.import_gguf, request.filename, name, engine.OLLAMA_URL)
        return {'ok': True, 'model': canonical}
    except ValueError as exc:
        raise HTTPException(400, str(exc)) from exc
    except httpx.HTTPError as exc:
        raise HTTPException(503, 'Ollama no responde. Abre Ollama antes de importar.') from exc
    except (RuntimeError, OSError) as exc:
        raise HTTPException(503, str(exc) if isinstance(exc, RuntimeError) else 'No se pudo leer el archivo o ejecutar Ollama.') from exc

@app.get('/api/ollama/status')
async def ollama_status():
    try:
        async with httpx.AsyncClient(timeout=3.0) as client:
            r = await client.get(engine.OLLAMA_URL + '/api/tags')
            r.raise_for_status()
        names = [m.get('name','') for m in r.json().get('models', [])]
        return {'online': True, 'installed': names, 'default': local_models.selected_model()}
    except (httpx.HTTPError, ValueError):
        return {'online': False, 'installed': [], 'default': local_models.selected_model()}

@app.post('/api/generate')
async def generate(request: DraftRequest):
    payload = request.model_dump()
    payload['fields'] = {k: v.model_dump() for k,v in request.fields.items()}
    try:
        result = await engine.generate_with_ollama(payload)
        store.save('history', {'input': payload, 'result': result})
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e
    except (RuntimeError, ConnectionError, TimeoutError) as e:
        raise HTTPException(status_code=503, detail=str(e)) from e

@app.get('/api/history')
def history():
    return store.list_records('history', 100)

@app.delete('/api/history/{record_id}')
def delete_history(record_id: str):
    if not store.remove('history', record_id):
        raise HTTPException(status_code=404, detail='No encontrado')
    return {'ok': True}

@app.get('/api/presets')
def presets():
    return store.list_records('presets', 100)

@app.get('/api/preset-library')
def examples(language: Literal['es', 'en'] = 'es', model_id: str | None = None):
    try:
        return preset_library(language, model_id)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

@app.post('/api/presets')
def save_preset(body: PresetRequest):
    return {'id': store.save('presets', body.content, body.name)}

@app.put('/api/presets/{preset_id}')
def update_preset(preset_id: str, body: PresetRequest):
    existing = {i['id'] for i in store.list_records('presets', 10000)}
    if preset_id not in existing:
        raise HTTPException(status_code=404, detail='No encontrado')
    return {'id': store.save('presets', body.content, body.name, preset_id)}

@app.delete('/api/presets/{preset_id}')
def delete_preset(preset_id: str):
    if not store.remove('presets', preset_id):
        raise HTTPException(status_code=404, detail='No encontrado')
    return {'ok': True}

DIST = Path(__file__).resolve().parents[1] / 'frontend' / 'dist'
if DIST.is_dir():
    app.mount('/assets', StaticFiles(directory=DIST / 'assets'), name='assets')

    @app.get('/')
    def frontend_index():
        return FileResponse(DIST / 'index.html')
