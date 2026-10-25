"""Windows desktop entry point; bundles the existing React/FastAPI application."""
from __future__ import annotations

import ctypes
from contextlib import closing
import json
import logging
from logging.handlers import RotatingFileHandler
import os
from pathlib import Path
import socket
import sqlite3
import sys
import threading
import time
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parent
TITLE = 'promptstudio'


def user_directory() -> Path:
    override = os.environ.get('PROMPT_STUDIO_DATA_DIR')
    location = Path(override) if override else Path(os.environ.get('LOCALAPPDATA', Path.home() / 'AppData/Local')) / 'promptstudio'
    location = location.resolve()
    location.mkdir(parents=True, exist_ok=True)
    return location


def import_existing_database(destination: Path, candidates: list[Path]) -> bool:
    """One-time consistent backup; never replace an existing desktop database."""
    if destination.exists():
        return False
    for source in candidates:
        if source.is_file() and source.resolve() != destination.resolve():
            destination.parent.mkdir(parents=True, exist_ok=True)
            temporary = destination.with_suffix('.importing')
            try:
                with closing(sqlite3.connect(source.as_uri() + '?mode=ro', uri=True)) as original:
                    with closing(sqlite3.connect(temporary)) as copy:
                        original.backup(copy)
                temporary.replace(destination)
                return True
            finally:
                temporary.unlink(missing_ok=True)
    return False


def configure(data: Path) -> None:
    from dotenv import load_dotenv
    load_dotenv(data / 'settings.env', override=False)
    if not getattr(sys, 'frozen', False):
        load_dotenv(ROOT / '.env', override=False)
    os.environ.setdefault('PROMPT_STUDIO_SETTINGS_DIR', str(data))
    if 'PROMPT_STUDIO_DB' not in os.environ:
        destination = data / 'prompts.sqlite3'
        if not os.environ.get('PROMPT_STUDIO_DATA_DIR'):
            executable = Path(sys.executable).resolve().parent
            import_existing_database(destination, [ROOT / 'data/prompts.sqlite3', executable / 'data/prompts.sqlite3', executable.parent / 'data/prompts.sqlite3'])
        os.environ['PROMPT_STUDIO_DB'] = str(destination)
    elif not Path(os.environ['PROMPT_STUDIO_DB']).is_absolute():
        os.environ['PROMPT_STUDIO_DB'] = str(data / os.environ['PROMPT_STUDIO_DB'])
    handler = RotatingFileHandler(data / 'desktop.log', maxBytes=1_000_000, backupCount=2, encoding='utf-8')
    logging.basicConfig(level=logging.INFO, handlers=[handler], force=True)
    # Windowed executables have no console streams; some dependencies expect one.
    if sys.stdout is None:
        sys.stdout = open(os.devnull, 'w', encoding='utf-8')
    if sys.stderr is None:
        sys.stderr = open(os.devnull, 'w', encoding='utf-8')


class InstanceLock:
    def __init__(self, data: Path):
        self._path = data / 'desktop.lock'
        self._file = None

    def acquire(self) -> bool:
        import msvcrt
        self._file = self._path.open('a+b')
        try:
            if os.fstat(self._file.fileno()).st_size == 0:
                self._file.write(b'0')
                self._file.flush()
            self._file.seek(0)
            msvcrt.locking(self._file.fileno(), msvcrt.LK_NBLCK, 1)
            return True
        except OSError:
            self._file.close()
            self._file = None
            return False

    def close(self):
        if self._file:
            self._file.close()
            self._file = None


def copy_to_clipboard(text: str) -> None:
    """Unicode clipboard, independent of WebView browser permissions."""
    from ctypes import wintypes
    user = ctypes.WinDLL('user32', use_last_error=True)
    kernel = ctypes.WinDLL('kernel32', use_last_error=True)
    kernel.GlobalAlloc.argtypes = [wintypes.UINT, ctypes.c_size_t]
    kernel.GlobalAlloc.restype = wintypes.HGLOBAL
    kernel.GlobalLock.argtypes = [wintypes.HGLOBAL]
    kernel.GlobalLock.restype = ctypes.c_void_p
    kernel.GlobalUnlock.argtypes = [wintypes.HGLOBAL]
    kernel.GlobalFree.argtypes = [wintypes.HGLOBAL]
    user.SetClipboardData.argtypes = [wintypes.UINT, wintypes.HANDLE]
    user.SetClipboardData.restype = wintypes.HANDLE
    raw = (text + '\0').encode('utf-16-le')
    handle = kernel.GlobalAlloc(0x0042, len(raw))
    if not handle:
        raise ctypes.WinError(ctypes.get_last_error())
    try:
        address = kernel.GlobalLock(handle)
        if not address:
            raise ctypes.WinError(ctypes.get_last_error())
        ctypes.memmove(address, raw, len(raw))
        kernel.GlobalUnlock(handle)
        if not user.OpenClipboard(None):
            raise ctypes.WinError(ctypes.get_last_error())
        try:
            if not user.EmptyClipboard() or not user.SetClipboardData(13, handle):
                raise ctypes.WinError(ctypes.get_last_error())
            handle = None  # Windows owns the allocation after SetClipboardData.
        finally:
            user.CloseClipboard()
    finally:
        if handle:
            kernel.GlobalFree(handle)


class DesktopBridge:
    def __init__(self, data: Path):
        self._data = data
        self._window = None
        self._preference_lock = threading.Lock()

    def get_interface_language(self):
        value = self._read_preferences().get('interface_language')
        return value if value in ('es', 'en') else None

    def get_theme(self):
        value = self._read_preferences().get('theme')
        return value if value in ('system', 'light', 'dark') else None

    def _read_preferences(self):
        try:
            value = json.loads((self._data / 'preferences.json').read_text(encoding='utf-8'))
            return value if isinstance(value, dict) else {}
        except (OSError, ValueError):
            return {}

    def set_interface_language(self, language):
        if language not in ('es', 'en'):
            return False
        return self._set_preference('interface_language', language)

    def set_theme(self, theme):
        if theme not in ('system', 'light', 'dark'):
            return False
        return self._set_preference('theme', theme)

    def _set_preference(self, key, value):
        with self._preference_lock:
            target = self._data / 'preferences.json'
            temporary = target.with_suffix('.tmp')
            preferences = self._read_preferences()
            preferences[key] = value
            temporary.write_text(json.dumps(preferences, ensure_ascii=False) + '\n', encoding='utf-8')
            temporary.replace(target)
        return True

    def copy_text(self, text):
        try:
            copy_to_clipboard(str(text))
            return {'ok':True}
        except Exception:
            logging.exception('Clipboard failed')
            return {'ok':False}

    def open_models_folder(self):
        from backend.local_models import models_directory
        try:
            os.startfile(str(models_directory()))
            return {'ok': True}
        except OSError:
            logging.exception('Cannot open models folder')
            return {'ok': False}

    def export_json(self, filename, content):
        import webview
        try:
            value = json.loads(content)
            paths = self._window.create_file_dialog(webview.FileDialog.SAVE, save_filename=Path(filename).name, file_types=('JSON (*.json)',))
            if not paths:
                return {'ok':True, 'cancelled':True}
            destination = Path(paths[0] if isinstance(paths, (tuple,list)) else paths)
            destination.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
            return {'ok':True, 'cancelled':False}
        except Exception:
            logging.exception('Export failed')
            return {'ok':False}


def listener_socket() -> socket.socket:
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Stable origin for browser storage; occupied ports fall back to an OS choice.
    try:
        listener.bind(('127.0.0.1', 18763))
    except OSError:
        listener.bind(('127.0.0.1', 0))
    listener.listen(128)
    return listener


def main() -> int:
    data = user_directory()
    lock = InstanceLock(data)
    if not lock.acquire():
        existing = ctypes.windll.user32.FindWindowW(None, TITLE)
        if existing:
            ctypes.windll.user32.ShowWindow(existing, 9)
            ctypes.windll.user32.SetForegroundWindow(existing)
        return 0
    listener = None
    server = None
    worker = None
    runtime = data / 'runtime.json'
    try:
        configure(data)
        import uvicorn
        import webview
        from backend.main import app
        if not (ROOT / 'frontend/dist/index.html').is_file():
            raise RuntimeError('Falta la interfaz compilada. Ejecuta scripts/empaquetar_windows.ps1.')
        listener = listener_socket()
        port = listener.getsockname()[1]
        url = f'http://127.0.0.1:{port}'
        server = uvicorn.Server(uvicorn.Config(app, host='127.0.0.1', port=port, log_config=None, access_log=False, loop='asyncio', http='h11', ws='none', lifespan='on'))
        worker = threading.Thread(target=server.run, kwargs={'sockets':[listener]}, daemon=True, name='promptstudioAPI')
        worker.start()
        deadline = time.monotonic() + 20
        while not server.started:
            if not worker.is_alive() or time.monotonic() > deadline:
                raise RuntimeError('No se pudo iniciar el servicio interno. Revisa desktop.log.')
            time.sleep(0.05)
        with urlopen(url + '/api/health', timeout=5) as response:
            if not json.load(response).get('ok'):
                raise RuntimeError('El servicio interno no responde correctamente.')
        runtime.write_text(json.dumps({'pid':os.getpid(), 'url':url, 'data_directory':str(data)}, indent=2), encoding='utf-8')
        bridge = DesktopBridge(data)
        window = webview.create_window(TITLE, url, js_api=bridge, width=1440, height=900, min_size=(980,680), background_color='#101318', text_select=True)
        bridge._window = window
        webview.start(gui='edgechromium', debug=False, private_mode=False, storage_path=str(data / 'webview'), icon=str(ROOT / 'recursos/promptstudio.ico'))
        return 0
    except Exception as exc:
        logging.exception('Desktop startup failed')
        ctypes.windll.user32.MessageBoxW(None, f'No se pudo abrir promptstudio.\n\n{exc}\n\nRegistro: {data / "desktop.log"}', TITLE, 0x10)
        return 1
    finally:
        if server:
            server.should_exit = True
        if worker:
            worker.join(timeout=5)
        if listener:
            listener.close()
        runtime.unlink(missing_ok=True)
        lock.close()


if __name__ == '__main__':
    raise SystemExit(main())
