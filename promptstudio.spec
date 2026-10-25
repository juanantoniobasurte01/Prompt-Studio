# Windows one-file build. Runtime data is stored in LOCALAPPDATA, never here.
from pathlib import Path
from PyInstaller.utils.hooks import collect_data_files

root = Path(SPECPATH)
data = [(str(root / 'LICENSE'), '.'), (str(root / 'NOTICE.md'), '.'), (str(root / 'frontend/dist'), 'frontend/dist'),
        (str(root / 'models'), 'models'),
        (str(root / 'recursos/identity_legacy.json'), 'recursos'),
        (str(root / 'recursos/promptstudio.ico'), 'recursos'),
        (str(root / 'backend/preset_scenes.json'), 'backend')]
data += collect_data_files('webview')
a = Analysis([str(root / 'desktop.py')], pathex=[str(root)], binaries=[], datas=data,
             hiddenimports=['uvicorn.logging','uvicorn.loops.asyncio','uvicorn.protocols.http.h11_impl','uvicorn.lifespan.on','webview.platforms.edgechromium','webview.platforms.winforms'],
             hookspath=[], hooksconfig={}, runtime_hooks=[],
             excludes=['pytest','tkinter','PyQt5','PyQt6','PySide2','PySide6','IPython','matplotlib','numpy'], noarchive=False)
pyz = PYZ(a.pure)
exe = EXE(pyz, a.scripts, a.binaries, a.datas, [], name='promptstudio',
          debug=False, bootloader_ignore_signals=False, strip=False, upx=False,
          console=False, disable_windowed_traceback=False,
          icon=str(root / 'recursos/promptstudio.ico'))
