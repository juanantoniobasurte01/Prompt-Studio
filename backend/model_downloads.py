"""Background Ollama pulls with progress. Does not load or generate with a model."""
from __future__ import annotations

import json
import threading
from urllib.parse import urlparse
from uuid import uuid4

import httpx
from .engine_catalog import engine_catalog


class DownloadManager:
    def __init__(self):
        self._lock = threading.Lock()
        self._job = None

    def status(self):
        with self._lock:
            return dict(self._job) if self._job else None

    def _update(self, **values):
        with self._lock:
            self._job.update(values)

    def start(self, model: str, url: str):
        if model not in {entry['id'] for entry in engine_catalog()}:
            raise ValueError('El modelo no pertenece al catálogo de descargas.')
        if urlparse(url).hostname not in ('127.0.0.1', 'localhost', '::1'):
            raise ValueError('La descarga requiere Ollama en este equipo.')
        with self._lock:
            if self._job and self._job['state'] == 'running':
                if self._job['model'] == model:
                    return dict(self._job)
                raise RuntimeError('Ya hay una descarga en curso.')
            self._job = {'id': uuid4().hex, 'model': model, 'state': 'running',
                         'completed': 0, 'total': 0, 'digest': '', 'error': ''}
            result = dict(self._job)
        threading.Thread(target=self._pull, args=(model, url), daemon=True, name='model-download').start()
        return result

    def _pull(self, model: str, url: str):
        try:
            success = False
            with httpx.Client(timeout=httpx.Timeout(60.0, connect=5.0)) as client:
                with client.stream('POST', url + '/api/pull', json={'model': model, 'stream': True}) as response:
                    response.raise_for_status()
                    for line in response.iter_lines():
                        if not line.strip():
                            continue
                        event = json.loads(line)
                        if not isinstance(event, dict):
                            raise ValueError('Ollama devolvió un progreso de descarga no válido.')
                        if event.get('error'):
                            raise RuntimeError(str(event['error'])[:300])
                        if event.get('total') is not None:
                            self._update(total=max(0, int(event['total'])), completed=max(0, int(event.get('completed', 0))), digest=str(event.get('digest', '')))
                        if event.get('status') == 'success':
                            success = True
            if not success:
                raise RuntimeError('Ollama cerró la descarga antes de completarla.')
            self._update(state='completed')
        except (httpx.HTTPError, RuntimeError, ValueError, TypeError, OSError) as exc:
            self._update(state='failed', error=str(exc)[:300])


downloads = DownloadManager()
