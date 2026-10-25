import json
from pathlib import Path
import tempfile

from desktop import DesktopBridge


def test_theme_and_language_preserve_each_other_and_other_preferences():
    lab = Path(__file__).resolve().parents[1] / 'laboratorio'
    lab.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(dir=lab) as directory:
        folder = Path(directory)
        path = folder / 'preferences.json'
        path.write_text(json.dumps({'interface_language':'es', 'other':'keep'}), encoding='utf-8')
        bridge = DesktopBridge(folder)
        assert bridge.get_theme() is None
        assert bridge.set_theme('light')
        assert bridge.set_interface_language('en')
        reloaded = DesktopBridge(folder)
        assert reloaded.get_theme() == 'light'
        assert reloaded.get_interface_language() == 'en'
        assert json.loads(path.read_text())['other'] == 'keep'
        assert not reloaded.set_theme('invalid')
        assert reloaded.get_theme() == 'light'
        assert reloaded.set_theme('system')
        assert DesktopBridge(folder).get_theme() == 'system'


def test_invalid_preferences_are_recoverable():
    lab = Path(__file__).resolve().parents[1] / 'laboratorio'
    lab.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(dir=lab) as directory:
        folder = Path(directory)
        (folder / 'preferences.json').write_text('[]', encoding='utf-8')
        bridge = DesktopBridge(folder)
        assert bridge.get_theme() is None
        assert bridge.get_interface_language() is None
        assert bridge.set_theme('dark')
        assert bridge.get_theme() == 'dark'
