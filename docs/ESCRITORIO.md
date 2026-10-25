# promptstudio para Windows

## Abrir la aplicación

Ejecuta **`dist/promptstudio.exe`** con doble clic. Es una aplicación de escritorio con ventana propia, icono, portapapeles y diálogo de exportación JSON de Windows. No abre el navegador, Node, una terminal ni un servidor Vite.

El EXE contiene Python, el backend, la interfaz compilada, las guías de los modelos y los 258 presets incluidos. En el equipo de destino no hace falta instalar Python ni Node. Usa Microsoft Edge WebView2 y .NET del sistema; ambos están disponibles en el equipo donde se ha construido y comprobado. El motor Ollama y sus pesos se mantienen instalados por separado: el EXE no los descarga, inicia ni detiene automáticamente.

## Datos y configuración

Los datos de escritorio se guardan en **`%LOCALAPPDATA%\promptstudio`**, fuera del EXE y de su directorio temporal:

- `prompts.sqlite3`: presets propios e historial.
- `preferences.json`: idioma de la interfaz.
- `webview/`: estado persistente de la ventana integrada.
- `desktop.log`: registro de funcionamiento, con dos copias de rotación como máximo.
- `runtime.json`: dirección interna y PID mientras la aplicación está abierta; desaparece al cerrar.

En el primer inicio se busca la base anterior `data/prompts.sqlite3` junto al proyecto/ejecutable y se importa mediante una copia consistente de SQLite. Una base de escritorio existente nunca se reemplaza. Esto conserva los datos al volver a compilar o mover el EXE.

Opcionalmente se puede crear `settings.env` en esa carpeta para configurar `OLLAMA_URL`, `PROMPT_STUDIO_DB` o `PROMPT_STUDIO_MODELS_DIR`. Ollama se consulta en `http://127.0.0.1:11434` por defecto. El motor de IA se elige en Configuración y se guarda en `engine-settings.json`. Una ruta relativa de base de datos se resuelve dentro de la carpeta de datos.

La carpeta `ai-models` junto al EXE permite añadir archivos GGUF. Configuración incluye un botón para abrirla, actualizar la lista e importar un archivo en Ollama. Los pesos quedan fuera del ejecutable. Consulta [Motores locales](MODELO_LOCAL.md).

El idioma se elige en **Configuración → Idioma de la interfaz**, independientemente del idioma del prompt. También persiste si cambia el puerto interno. Abrir el EXE dos veces recupera la ventana existente. Al cerrar se detiene únicamente su servicio interno; Ollama y otros modelos quedan intactos.

## Empaquetar de nuevo

Desde la raíz del proyecto:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\empaquetar_windows.ps1
```

El script instala las dependencias de `requirements-build.txt`, compila React y ejecuta `promptstudio.spec`. El resultado es un único EXE en `dist`. Los archivos intermedios se escriben en `laboratorio/pyinstaller`; pueden eliminarse después de comprobar el resultado. El logo original está en `recursos/PS.png`; cada compilación regenera `recursos/promptstudio.ico` a partir de él mediante `scripts/generar_icono.ps1`.

La interfaz y la API se ejecutan dentro de pywebview. El servicio interno escucha exclusivamente en loopback y usa su propio puerto, con alternativa libre si está ocupado; no necesita los puertos de desarrollo 5173 ni 8000. La distribución usa modo `onefile` y no incluye `.env`, bases personales, pruebas, `node_modules` ni pesos de modelos.

Referencias técnicas: [empaquetado pywebview](https://pywebview.flowrl.com/guide/freezing.html), [API de pywebview](https://pywebview.flowrl.com/api/), [archivos de datos de PyInstaller](https://pyinstaller.org/en/stable/runtime-information.html).


## Tema y prompt negativo

En **Configuración → Tema de la interfaz** puedes elegir **Sistema**, **Claro** u **Oscuro**. La opción inicial es Sistema y sigue los cambios de apariencia del equipo mientras la ventana está abierta. La elección se conserva en `preferences.json`, junto con el idioma de la interfaz. Cambiar el idioma no reemplaza el tema, ni al revés.

El campo **Prompt negativo**, debajo de **Indicaciones adicionales**, contiene lo que quieres evitar en el resultado. Se guarda al crear presets y se conserva en el historial y las exportaciones JSON. El motor recibe esas exclusiones por separado. Si el modelo de destino no admite un negativo independiente, la salida conserva las exclusiones originales en las notas y adapta las restricciones que sean compatibles con su formato.
