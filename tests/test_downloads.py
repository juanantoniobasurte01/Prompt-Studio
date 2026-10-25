import json
from unittest.mock import MagicMock, Mock

import httpx
import pytest
from backend.engine_catalog import engine_catalog
from backend.model_downloads import DownloadManager

MODEL = 'huihui_ai/qwen3-abliterated:4b'


def manager_with_job(monkeypatch):
    thread = Mock()
    monkeypatch.setattr('backend.model_downloads.threading.Thread', thread)
    manager = DownloadManager()
    manager.start(MODEL, 'http://127.0.0.1:11434')
    thread.return_value.start.assert_called_once()
    return manager


def test_download_catalog_is_unique_and_has_sources():
    catalog = engine_catalog()
    assert len(catalog) == 15
    assert len({item['id'] for item in catalog}) == 15
    assert all(item['source'].startswith('https://ollama.com/huihui_ai/') and item['size_gb'] > 0 for item in catalog)
    assert catalog == sorted(catalog, key=lambda item: item['label'].casefold())


def test_unknown_and_remote_downloads_are_rejected():
    manager = DownloadManager()
    with pytest.raises(ValueError):
        manager.start('arbitrary/model:latest', 'http://localhost:11434')
    with pytest.raises(ValueError):
        manager.start(MODEL, 'https://remote.example')
    assert manager.status() is None


def test_only_one_download_runs_and_same_request_is_reused(monkeypatch):
    manager = manager_with_job(monkeypatch)
    first = manager.status()
    assert manager.start(MODEL, 'http://localhost:11434')['id'] == first['id']
    with pytest.raises(RuntimeError):
        manager.start('huihui_ai/qwen3-abliterated:8b', 'http://localhost:11434')
    snapshot = manager.status()
    snapshot['state'] = 'changed'
    assert manager.status()['state'] == 'running'


def fake_client(monkeypatch, lines):
    response = MagicMock()
    response.iter_lines.return_value = lines
    context = MagicMock()
    context.__enter__.return_value = response
    client = MagicMock()
    client.stream.return_value = context
    factory = MagicMock()
    factory.return_value.__enter__.return_value = client
    monkeypatch.setattr('backend.model_downloads.httpx.Client', factory)
    return client


def test_download_tracks_stream_and_never_uses_chat(monkeypatch):
    manager = manager_with_job(monkeypatch)
    client = fake_client(monkeypatch, [json.dumps({'status':'pulling', 'total':100, 'completed':75, 'digest':'sha256:test'}), json.dumps({'status':'success'})])
    manager._pull(MODEL, 'http://localhost:11434')
    assert manager.status()['state'] == 'completed'
    assert manager.status()['completed'] == 75
    assert manager.status()['total'] == 100
    client.stream.assert_called_once_with('POST', 'http://localhost:11434/api/pull', json={'model':MODEL, 'stream':True})
    client.post.assert_not_called()


@pytest.mark.parametrize('lines', [[], ['not json'], ['[]'], ['{"error":"disk full"}'], ['{"status":"pulling"}']])
def test_failed_or_incomplete_stream_can_be_retried(monkeypatch, lines):
    manager = manager_with_job(monkeypatch)
    original = manager.status()['id']
    fake_client(monkeypatch, lines)
    manager._pull(MODEL, 'http://localhost:11434')
    assert manager.status()['state'] == 'failed'
    assert manager.status()['error']
    assert manager.start(MODEL, 'http://localhost:11434')['id'] != original


def test_network_failure_is_reported(monkeypatch):
    manager = manager_with_job(monkeypatch)
    client = fake_client(monkeypatch, [])
    client.stream.side_effect = httpx.ConnectError('offline')
    manager._pull(MODEL, 'http://localhost:11434')
    assert manager.status()['state'] == 'failed'
