# Motores de IA locales

promptstudio usa Ollama para redactar los prompts. El motor de IA y el perfil de destino son selecciones independientes: puedes cambiar entre modelos de conversación sin cambiar las guías de MiniMax, Kling, FLUX u otros generadores.

## Elegir un motor instalado

Abre **Configuración → Motor de IA**. Pulsa **Actualizar modelos** y selecciona uno de la lista, ordenada por nombre. La elección se guarda en `engine-settings.json`, dentro de `%LOCALAPPDATA%\promptstudio` en escritorio o `data` al ejecutar la API desde código.

Abrir presets o historial conserva el motor actual. Elegir un modelo o actualizar la lista no genera texto ni lo carga en memoria. El modelo se utiliza cuando pulsas **Generar prompt**. Si ya existe `OLLAMA_MODEL` en tu configuración anterior, se conserva como selección inicial hasta que elijas otro motor; una instalación nueva no fuerza Qwen.

## Añadir un archivo GGUF

1. Abre la carpeta desde **Abrir carpeta de modelos**. En escritorio es `ai-models` junto a `promptstudio.exe`; desde código está en la raíz del proyecto.
2. Copia allí un modelo de conversación en un único archivo `.gguf`, con una arquitectura compatible con tu versión de Ollama.
3. Pulsa **Actualizar modelos**, elige el archivo y escribe un nombre para Ollama. La aplicación propone uno a partir del nombre del archivo.
4. Pulsa **Importar en Ollama** y espera a que termine. Después selecciónalo en la lista de motores instalados.

La importación usa `ollama create` con un Modelfile que apunta únicamente al archivo elegido. No hereda los pesos ni la plantilla de Qwen, no descarga otro modelo y no realiza una generación de prueba. Ollama interpreta la arquitectura y la plantilla que admite para esos pesos. La cabecera GGUF válida no garantiza compatibilidad: utiliza modelos de conversación soportados por tu versión de Ollama.

Los modelos divididos en varias partes GGUF deben importarse mediante Ollama fuera de la aplicación. Una vez registrados, aparecen en la misma lista de motores. Otros formatos, como Safetensors, pueden importarse también por los medios que ofrezca Ollama; no se importan desde este selector de archivos.

Ollama debe estar instalado y abierto en este equipo para importar archivos. La aplicación no reemplaza un modelo que ya tenga el mismo nombre. Ollama puede conservar otra copia de los pesos en su almacén: comprueba que tienes espacio suficiente. Los archivos GGUF se mantienen fuera del EXE y de Git.

## Configurar rutas

En escritorio, añade estas opciones a `%LOCALAPPDATA%\promptstudio\settings.env` y reinicia la aplicación si necesitas cambiarlas:

```dotenv
OLLAMA_URL=http://127.0.0.1:11434
PROMPT_STUDIO_MODELS_DIR=D:/Modelos
```

`PROMPT_STUDIO_MODELS_DIR` es opcional. Permite guardar los archivos en otro disco o usar una carpeta escribible si el EXE está en un directorio protegido. Desde código, utiliza `.env` o variables de entorno. `OLLAMA_MODEL` sigue disponible para establecer la elección inicial, pero una elección guardada en Configuración tiene prioridad.

El importador no admite servidores Ollama remotos. Los modelos que ya estén instalados en un servidor configurado mediante `OLLAMA_URL` se pueden seleccionar sin importar archivos.

Fuentes: [importación de modelos](https://docs.ollama.com/import), [Modelfile](https://docs.ollama.com/modelfile), [lista de modelos instalados](https://docs.ollama.com/api/tags).


## Descargar desde el catálogo

En **Configuración → Motor de IA → Descargar motores abiertos** hay 15 variantes comunitarias de DeepSeek R1, Dolphin 3, Gemma 3, Llama 3.2 y Qwen 3, publicadas por huihui_ai como uncensored/abliterated. Cada entrada muestra un tamaño de descarga aproximado, su estado de instalación y un enlace a la ficha del autor. Las licencias son las de cada modelo; pesos abiertos no implica que todos tengan licencia MIT.

Selecciona una entrada y pulsa **Descargar modelo**. La aplicación solicita a Ollama la descarga y muestra el progreso del archivo actual. No realiza inferencia ni cambia el motor activo. Al terminar, pulsa **Usar este motor**, o elígelo en la lista de modelos instalados. La descarga continúa al cerrar el panel de Configuración; mantén la aplicación abierta hasta que termine.

Los pesos se guardan en el almacén de Ollama, separado de la carpeta `ai-models` destinada a importar archivos GGUF. Si se interrumpe una descarga puedes repetirla; Ollama reutiliza los datos disponibles. Solo se inicia una descarga a la vez. Si un modelo ya está instalado, se ofrece seleccionarlo y no se vuelve a descargar.

Las etiquetas del catálogo reflejan las fichas de sus autores y no garantizan que cada solicitud obtenga respuesta. Los tamaños publicados son aproximados y no representan la memoria necesaria para ejecutar el modelo.

Fuentes del catálogo, revisadas el 23 de octubre de 2026:

- [DeepSeek R1 Abliterated](https://ollama.com/huihui_ai/deepseek-r1-abliterated)
- [Dolphin 3 Abliterated](https://ollama.com/huihui_ai/dolphin3-abliterated)
- [Gemma 3 Abliterated](https://ollama.com/huihui_ai/gemma3-abliterated)
- [Llama 3.2 Abliterated](https://ollama.com/huihui_ai/llama3.2-abliterate)
- [Qwen 3 Abliterated](https://ollama.com/huihui_ai/qwen3-abliterated)
- [API de descarga de Ollama](https://docs.ollama.com/api/pull)
