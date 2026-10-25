# Seedream — instrucciones de prompting

Revisión documental: 2026-10-23. Estado: documentada. Aplicar también `00_REGLAS_COMUNES.md`.

## Redacción
Usa lenguaje natural preciso: sujeto, acción y entorno, con estética y composición si importan. La guía 4.0/4.5 prefiere instrucciones concisas y coherentes frente a apilar vocabulario ornamental. Más palabras no equivalen a mejor fidelidad.

## Edición y referencias
Identifica el elemento objetivo y lo que debe mantenerse. En composición multiimagen asigna el origen de cada sujeto, estilo o escenario. Una referencia declarada para el workflow posterior no es una imagen que promptstudio ya haya examinado.

## Revisiones
Distingue 4.0, 4.5 y 5.0 Lite. La publicación del fabricante describe razonamiento y búsqueda en 5.0 Lite; no conviertas eso en una instrucción para que el LLM redactor invente resultados actuales. La búsqueda solo existe si se habilita en el generador real. No extrapoles sus funciones a versiones anteriores.

## Controles
Los modelos disponibles, tamaño, número de imágenes y referencias se seleccionan según el endpoint original. No añadas tags Pony ni JSON arbitrario. Para texto renderizado conserva el literal y su ubicación.

El negativo separado debe confirmarse en la API concreta. Si falta ese soporte, integra las exclusiones compatibles en lenguaje natural y conserva cualquier limitación en notes. Las guías de un proveedor intermediario no sustituyen las especificaciones del fabricante.

## Fuentes y alcance

- <https://docs.byteplus.com/en/docs/modelark/seedream-4-0-5-0-prompt-guide?redirect=1>
- <https://seed.bytedance.com/en/blog/deeper-thinking-more-accurate-generation-introducing-seedream-5-0-lite>

La revisión comprueba compatibilidad documental; no es una prueba de imágenes generadas.
