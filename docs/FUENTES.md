# Fuentes y guía de mantenimiento

Los documentos `models/image/*.md` y `models/video/*.md` contienen las instrucciones de cada modelo que utiliza el motor de prompts. Cada perfil contiene sus referencias y advertencias. Para actualizar modelos: 1) verificar la documentación oficial del proveedor; 2) contrastar recomendaciones experimentales (Reddit, ComfyUI) separándolas de sintaxis nativa; 3) editar el MD en su carpeta; 4) actualizar `models/catalog.json` con id/medium/file/label; 5) ejecutar las pruebas de carga.

Fuentes para el motor local:
- <https://docs.ollama.com/import>
- <https://docs.ollama.com/api/tags>
- <https://docs.ollama.com/api/chat>
- <https://docs.ollama.com/capabilities/structured-outputs>

**Regla editorial:** no presentar como comandos del modelo formatos que son solo convenciones de prompting o JSON de una API particular. No asumir que un modelo soporta negativos, multi-shot, audio o imágenes de referencia en todos sus proveedores.
