import asyncio
from pathlib import Path
import json
import subprocess
import tempfile
from unittest.mock import AsyncMock, Mock

import pytest
from backend import engine, local_models


@pytest.fixture
def sandbox(monkeypatch):
    lab = Path(__file__).resolve().parents[1] / 'laboratorio'
    lab.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(dir=lab) as directory:
        folder = Path(directory)
        monkeypatch.setenv('PROMPT_STUDIO_MODELS_DIR', str(folder / 'models'))
        monkeypatch.setenv('PROMPT_STUDIO_SETTINGS_DIR', str(folder / 'settings'))
        monkeypatch.delenv('OLLAMA_MODEL', raising=False)
        yield folder


def gguf(name='model.gguf', content=b'GGUFtest'):
    path = local_models.models_directory() / name
    path.write_bytes(content)
    return path


def test_file_scan_and_persistent_independent_selection(sandbox):
    gguf('Zulu.gguf')
    gguf('alpha.GGUF')
    gguf('notes.txt')
    assert [file['filename'] for file in local_models.local_files()] == ['alpha.GGUF', 'Zulu.gguf']
    assert local_models.selected_model() == ''
    local_models.save_selection('mistral:latest')
    assert local_models.selected_model() == 'mistral:latest'
    assert json.loads(local_models.settings_file().read_text())['model'] == 'mistral:latest'


@pytest.mark.parametrize('name', ['../bad', '-f', 'x;run', 'a\nb', 'a:tag:tag', 'a//b'])
def test_invalid_engine_names(name):
    with pytest.raises(ValueError):
        local_models.validate_model_name(name)


@pytest.mark.parametrize('filename', ['../outside.gguf', 'missing.gguf', '/outside.gguf'])
def test_import_rejects_paths_outside_folder(sandbox, filename):
    with pytest.raises(ValueError):
        local_models.import_gguf(filename, 'local-model', 'http://127.0.0.1:11434')


def test_bad_header_split_and_remote_import_are_rejected(sandbox):
    gguf(content=b'not a model')
    with pytest.raises(ValueError, match='cabecera'):
        local_models.import_gguf('model.gguf', 'local-model', 'http://localhost:11434')
    gguf('model-00001-of-00002.gguf')
    with pytest.raises(ValueError, match='divididos'):
        local_models.import_gguf('model-00001-of-00002.gguf', 'local-model', 'http://localhost:11434')
    with pytest.raises(ValueError, match='este equipo'):
        local_models.import_gguf('model.gguf', 'local-model', 'https://remote.example')


def test_import_uses_only_selected_file_and_no_inference(sandbox, monkeypatch):
    source = gguf('Mí modelo.gguf')
    monkeypatch.setattr(local_models.shutil, 'which', lambda _: 'ollama.exe')
    calls = []
    def run(args, **kwargs):
        calls.append(args)
        assert args[1:3] == ['create', 'my-model']
        manifest = Path(args[-1])
        text = manifest.read_text(encoding='utf-8')
        assert len(text.splitlines()) == 1
        relative = json.loads(text.removeprefix('FROM ').strip())
        assert (manifest.parent / relative).resolve() == source
        assert kwargs['env']['OLLAMA_HOST'] == 'http://127.0.0.1:11434'
        return Mock(returncode=0)
    monkeypatch.setattr(local_models.subprocess, 'run', run)
    local_models.import_gguf(source.name, 'my-model', 'http://127.0.0.1:11434')
    assert len(calls) == 1
    assert not list(local_models.models_directory().glob('.import-*'))


@pytest.mark.parametrize('failure', ['exit', 'timeout'])
def test_failed_import_cleans_manifest_and_releases_lock(sandbox, monkeypatch, failure):
    gguf()
    monkeypatch.setattr(local_models.shutil, 'which', lambda _: 'ollama.exe')
    def run(*args, **kwargs):
        if failure == 'timeout':
            raise subprocess.TimeoutExpired('ollama', 1800)
        return Mock(returncode=1)
    monkeypatch.setattr(local_models.subprocess, 'run', run)
    with pytest.raises(RuntimeError):
        local_models.import_gguf('model.gguf', 'my-model', 'http://127.0.0.1:11434')
    assert not local_models._import_lock.locked()
    assert not list(local_models.models_directory().glob('.import-*'))


def test_generation_uses_saved_engine_without_qwen_dependency(sandbox, monkeypatch):
    local_models.save_selection('llama3.2:latest')
    response = Mock(status_code=200)
    response.json.return_value = {'message': {'content': '{"prompt":"A scene","negative_prompt":"","notes":""}'}}
    client = AsyncMock()
    client.post.return_value = response
    manager = AsyncMock()
    manager.__aenter__.return_value = client
    monkeypatch.setattr(engine.httpx, 'AsyncClient', lambda **_: manager)
    result = asyncio.run(engine.generate_with_ollama({'free_prompt': 'A scene'}))
    assert result['ollama_model'] == 'llama3.2:latest'
    assert client.post.call_args.kwargs['json']['model'] == 'llama3.2:latest'


def test_no_engine_does_not_contact_ollama(sandbox, monkeypatch):
    client = Mock()
    monkeypatch.setattr(engine.httpx, 'AsyncClient', client)
    with pytest.raises(ValueError, match='Selecciona un motor'):
        asyncio.run(engine.generate_with_ollama({'free_prompt': 'A scene'}))
    client.assert_not_called()


def test_unsupported_negative_field_keeps_original_exclusions_in_notes(sandbox, monkeypatch):
    response = Mock(status_code=200)
    response.json.return_value = {'message': {'content': '{"prompt":"A garden","negative_prompt":"blur","notes":""}'}}
    client = AsyncMock()
    client.post.return_value = response
    manager = AsyncMock()
    manager.__aenter__.return_value = client
    monkeypatch.setattr(engine.httpx, 'AsyncClient', lambda **_: manager)
    result = asyncio.run(engine.generate_with_ollama({'free_prompt':'A garden', 'model_id':'video_runway_gen_4_5', 'negative_prompt':'watermarks, unwanted text', 'ollama_model':'test:latest', 'interface_language':'en'}))
    assert result['negative_prompt'] == ''
    assert 'watermarks, unwanted text' in result['notes']
