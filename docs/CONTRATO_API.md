# Contrato interno de datos y API

Base: `http://127.0.0.1:8000`; en Vite `/api` se redirige al backend local.

## `GET /api/health`
`{"ok":true,"app":"promptstudio","offline":true}`.

## `GET /api/models`
`{"profiles":[{"id":"video_minimax_h3","label":"MiniMax H3 / H3 Max","medium":"video","file":"06_MINIMAX_H3.md","legacy":false}],"default_ollama_model":"my-local-model:latest"}`. El catálogo procede de `models/catalog.json`, archivo local y bajo control del proyecto.

## `POST /api/generate`
Ejemplo **sin ninguna selección**:

```json
{
  "medium":"auto",
  "model_id":null,
  "manual_model":"",
  "mode":"free",
  "free_prompt":"A black dragon over a medieval cathedral at night",
  "fields":{},
  "extra_instructions":"",
  "output_language":"English",
  "ollama_model":"my-local-model:latest",
  "temperature":0.45
}
```

Ejemplo **con combinación de los dos modos**:

```json
{
  "medium":"video",
  "model_id":"video_minimax_h3",
  "mode":"guided",
  "free_prompt":"Un dragón negro aterriza en una catedral al anochecer",
  "fields":{
    "iluminacion":{"selected":"Cinematográfica","manual":"destellos rojos intermitentes desde la izquierda"},
    "movimiento_camara":{"selected":"Push in","manual":"la cámara mantiene una trayectoria suave y termina en primer plano"},
    "dialogo":{"selected":"","manual":"El caballero dice exactamente: «No te acerques»"}
  },
  "ollama_model":"my-local-model:latest"
}
```

Salida:

```json
{
  "prompt":"Cinematic video of ...",
  "negative_prompt":"",
  "notes":"Conservado el diálogo literal...",
  "medium":"video",
  "profile_id":"video_minimax_h3",
  "ollama_model":"my-local-model:latest"
}
```

`negative_prompt` vacío si el perfil no garantiza campo negativo. Errores: HTTP 400 para validación; HTTP 503 para Ollama sin conexión, timeout o errores de inferencia.

## Gestión de Ollama
- `GET /api/ollama/status`: `{online:boolean, installed:[...], default:string}` consultando `/api/tags` local.
- Endpoint Ollama: `POST /api/chat`, `stream:false`, `think:false`, `format:JSON_SCHEMA`, `options.temperature`, `options.num_ctx`.
- Si el modelo no respeta JSON, se aplica parser de texto como fallback y se preserva la salida en prompt.

## SQLite
- `GET /api/presets`; `POST /api/presets` `{name,content}`; `PUT /api/presets/{id}`; `DELETE /api/presets/{id}`.
- `GET /api/history`; `DELETE /api/history/{id}`.
- `content` contiene el estado entero del formulario; historial contiene `input` + `result`. Sin usuarios ni cloud.

## Biblioteca de presets incluida

`GET /api/preset-library?language=es&model_id=video_minimax_h3` devuelve los seis ejemplos de ese perfil. `language` admite `es` (predeterminado) o `en`; omitir `model_id` devuelve los 258 ejemplos de los 43 perfiles. Un ID desconocido devuelve 400; un idioma no admitido, 422.

Cada registro contiene `id`, `name`, `source: "builtin"`, `model_id`, `model_label`, `medium`, `description` y `content` (formulario completo). La biblioteca no modifica SQLite. El frontend carga el ejemplo como formulario editable; el usuario puede guardar una copia mediante el CRUD de `/api/presets`.

`POST /api/generate` admite `interface_language: "es" | "en"` (predeterminado `es`) para el idioma solicitado de `notes`. `output_language` sigue controlando el idioma solicitado de la escena. Los diálogos literales y las cabeceras nativas se conservan. El idioma de interfaz se persiste únicamente en el navegador, sin cambiar IDs ni valores de presets e historial.

## Formato nativo dentro de la salida

El contrato público sigue devolviendo `prompt` como string. Sus saltos de línea y secciones pertenecen al texto copiable del generador de destino. En MiniMax H3 se conservan los bloques base o Ref2VA según la modalidad declarada; una respuesta genérica sin sus secciones se rechaza con HTTP 503 para permitir reintentar. Las notas sobre referencias pendientes se mantienen fuera del string `prompt`.

El catálogo puede definir `max_output_tokens`, `prompt_contract`, `prompt_contracts` y `prompt_layouts`. Son metadatos locales: el primero ajusta el presupuesto de salida; los contratos y layouts especifican el formato. La modalidad manual de `fields.modalidad_video` prevalece sobre el selector; si no se declara en ese campo, se consulta el texto libre. No se cargan MD adicionales ni se llaman servicios externos. Una respuesta que Ollama marque como truncada no se persiste como un resultado completo.

## Reglas de prioridad
Campos vacíos se omiten. `manual` contradice a `selected` -> prevalece `manual`, pero ambos se transmiten al LLM para interpretación. `model_id` se resuelve mediante lista blanca; `manual_model` solo menciona el destino, **no** autoriza a cargar archivos por nombre. Al no haber modelo específico, no se introducen flags o tokens de modelo.


## Motores de IA

`GET /api/local-models` devuelve `directory`, `files` (nombre, tamaño y nombre sugerido), `installed`, `online` y `selected`. Consulta `/api/tags` de Ollama y la carpeta local; no ejecuta inferencia. `default_ollama_model` en `/api/models` refleja la elección guardada o la configuración inicial.

`PUT /api/local-models/selection` recibe `{"model":"my-local-model:latest"}`. El nombre debe existir en Ollama. Guarda la selección en `engine-settings.json`; devuelve `{"selected":"my-local-model:latest"}`. Si no se envía `ollama_model` al generar, el backend usa esa elección.

`POST /api/local-models/import` recibe `{"filename":"my-model.gguf","model":"promptstudio/my-model:latest"}`. Solo permite un archivo GGUF dentro de la carpeta configurada y un servidor Ollama de este equipo. Rechaza nombres existentes con 409 y archivos inválidos con 400. Registra el modelo mediante `ollama create` y devuelve `{"ok":true,"model":"promptstudio/my-model:latest"}`. No selecciona el motor automáticamente ni llama a `/api/chat`. Puede tardar hasta 30 minutos; solo se ejecuta una importación simultánea.


`GET /api/local-models` incluye también `catalog`: motores descargables, con identificador, nombre, tamaño aproximado y ficha del autor. `POST /api/local-models/download` recibe `{"model":"huihui_ai/qwen3-abliterated:4b"}` y devuelve `job` e `installed`. Solo admite entradas del catálogo y Ollama en este equipo. Un modelo ya instalado no inicia otra descarga. Otra descarga simultánea devuelve 409; repetir la del mismo modelo devuelve su estado actual.

`GET /api/local-models/download` devuelve el último `job`, o null. Sus campos son `id`, `model`, `state` (running/completed/failed), `completed`, `total`, `digest` y `error`. El progreso en bytes corresponde al archivo actual, no a la suma de capas. El trabajo usa `/api/pull` de Ollama y no llama a `/api/chat` ni cambia la selección guardada.


`POST /api/generate` acepta `negative_prompt`, un string opcional de hasta 5000 caracteres. Se transmite al motor como exclusiones del usuario, separado del prompt positivo y de las instrucciones adicionales. Si falta, equivale a un string vacío para mantener la compatibilidad con presets anteriores. El historial guarda este campo en `content.input`; la respuesta mantiene `negative_prompt` como negativo generado. Los perfiles con `negative_prompt_policy: none` devuelven ese campo vacío y conservan las exclusiones solicitadas en `notes`.

En imagen, el catálogo distingue `supported`, `none`, `conditional` e `inline`. Las variantes explícitas pueden ajustar la política del perfil: por ejemplo, Z-Image Base frente a Turbo o Recraft V3 frente a V4. `conditional` exige confirmar el endpoint o pipeline; no garantiza compatibilidad universal. Midjourney usa `inline`: las exclusiones compatibles van mediante `--no` dentro de `prompt` y `negative_prompt` queda vacío.

Los formatos JSON de imagen se entregan serializados dentro del string `prompt`, conservando el objeto exterior de respuesta. Cuando se solicita JSON explícito, se comprueba que sea un objeto; Ideogram comprueba además sus campos esenciales, elementos y cajas. E1-Full exige sus dos secciones en orden. Una respuesta que incumple esos formatos genera un error, en lugar de guardarse como un prompt válido. Las comprobaciones estructurales no certifican fidelidad visual.
