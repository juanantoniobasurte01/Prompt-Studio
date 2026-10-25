import os
import tempfile
from unittest.mock import AsyncMock, Mock, patch
from pathlib import Path

# Set DB path before app import. Tests never contact Ollama.
_LAB = Path(__file__).resolve().parents[1] / 'laboratorio'
_LAB.mkdir(exist_ok=True)
_TEST_DIR = tempfile.TemporaryDirectory(dir=_LAB)
os.environ['PROMPT_STUDIO_DB'] = os.path.join(_TEST_DIR.name, 'test.db')
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)


def test_download_routes_only_start_requested_missing_model(monkeypatch):
    from backend import main, local_models
    monkeypatch.setattr(local_models, 'installed_models', AsyncMock(return_value=['huihui_ai/qwen3-abliterated:8b']))
    manager = Mock()
    manager.start.return_value = {'id':'test', 'state':'running', 'model':'huihui_ai/qwen3-abliterated:4b'}
    manager.status.return_value = manager.start.return_value
    monkeypatch.setattr(main, 'downloads', manager)
    assert client.post('/api/local-models/download', json={'model':'huihui_ai/qwen3-abliterated:8b'}).json()['installed'] is True
    manager.start.assert_not_called()
    assert client.post('/api/local-models/download', json={'model':'huihui_ai/qwen3-abliterated:4b'}).json()['job']['state'] == 'running'
    assert client.get('/api/local-models/download').json()['job']['id'] == 'test'
    manager.start.assert_called_once()


def test_local_model_selection_and_import(monkeypatch):
    from backend import local_models
    installed = AsyncMock(return_value=['mistral:latest', 'zebra:latest'])
    monkeypatch.setattr(local_models, 'installed_models', installed)
    monkeypatch.setattr(local_models, 'local_files', lambda: [{'filename':'model.gguf'}])
    monkeypatch.setattr(local_models, 'models_directory', lambda: Path(_TEST_DIR.name))
    monkeypatch.setenv('PROMPT_STUDIO_SETTINGS_DIR', _TEST_DIR.name)
    response = client.get('/api/local-models')
    assert response.status_code == 200
    assert response.json()['files'] == [{'filename':'model.gguf'}]
    assert client.put('/api/local-models/selection', json={'model':'missing:latest'}).status_code == 400
    assert client.put('/api/local-models/selection', json={'model':'mistral:latest'}).json()['selected'] == 'mistral:latest'
    assert client.get('/api/models').json()['default_ollama_model'] == 'mistral:latest'
    importer = Mock()
    monkeypatch.setattr(local_models, 'import_gguf', importer)
    assert client.post('/api/local-models/import', json={'filename':'model.gguf', 'model':'mistral'}).status_code == 409
    importer.assert_not_called()
    assert client.post('/api/local-models/import', json={'filename':'model.gguf', 'model':'new-engine'}).json()['ok']
    importer.assert_called_once()


def test_api_health_and_catalog():
    assert client.get('/api/health').json()['ok'] is True
    models = client.get('/api/models').json()['profiles']
    assert any(m['medium'] == 'video' for m in models)


def test_preset_crud():
    r = client.post('/api/presets', json={'name':'Ejemplo','content':{'free_prompt':'Una ciudad'}})
    assert r.status_code == 200
    key = r.json()['id']
    assert any(x['id']==key for x in client.get('/api/presets').json())
    assert client.put(f'/api/presets/{key}', json={'name':'Nuevo','content':{'free_prompt':'Montañas'}}).status_code==200
    assert client.delete(f'/api/presets/{key}').status_code==200


def test_generation_uses_local_engine_mock():
    with patch('backend.main.engine.generate_with_ollama',new_callable=AsyncMock) as mock:
        mock.return_value={'prompt':'A cinematic sunset','negative_prompt':'','notes':'', 'medium':'image', 'profile_id':None,'ollama_model':'qwen3:8b'}
        r=client.post('/api/generate',json={'medium':'image','free_prompt':'Un atardecer'})
        assert r.status_code==200
        assert r.json()['prompt']=='A cinematic sunset'
        assert len(client.get('/api/history').json())>=1


def test_negative_input_is_passed_saved_and_validated():
    with patch('backend.main.engine.generate_with_ollama', new_callable=AsyncMock) as mock:
        mock.return_value = {'prompt':'A garden', 'negative_prompt':'blur', 'notes':''}
        payload = {'free_prompt':'A garden', 'negative_prompt':'blur, watermark'}
        assert client.post('/api/generate', json=payload).status_code == 200
        assert mock.call_args.args[0]['negative_prompt'] == 'blur, watermark'
        assert any(item['content']['input'].get('negative_prompt') == 'blur, watermark' for item in client.get('/api/history').json())
        assert client.post('/api/generate', json={**payload, 'negative_prompt':'x' * 5001}).status_code == 422
        preset = client.post('/api/presets', json={'name':'With exclusions', 'content':payload}).json()
        assert any(item['content'].get('negative_prompt') == 'blur, watermark' for item in client.get('/api/presets').json())
        assert client.delete('/api/presets/' + preset['id']).status_code == 200
