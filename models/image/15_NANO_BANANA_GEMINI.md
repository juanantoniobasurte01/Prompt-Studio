# Nano Banana / Gemini Image — instrucciones de prompting

Revisión documental: 2026-10-23. Estado: documentada. Aplicar también `00_REGLAS_COMUNES.md`.

## Redacción
Comunica una escena coherente, no una acumulación de palabras de calidad. Conserva elementos, composición y texto literal. Para editar identifica el cambio y los rasgos que quedan fijos; en una serie, una modificación concreta por turno facilita comprobar el efecto.

## Modelos diferentes
Nano Banana 2.1, Nano Banana 2, Pro, Lite y 2.5 Flash Image no comparten todos los límites. Lite no está optimizado para múltiples referencias o edición secuencial multivuelta. No le atribuyas automáticamente las capacidades de Pro o 2.1.

Las imágenes y el historial necesarios para una edición se suministran realmente al generador. Este editor solo prepara las instrucciones. Define la función de cada referencia declarada; no inventes archivos, IDs ni análisis visual.

## Configuración y negativos
Los controles de aspecto, tamaño, modalidad y herramientas se configuran según la API de la versión. No mezcles sintaxis generateContent con Interactions ni copies campos de Imagen a Gemini Image. El esquema de generación de imagen aquí revisado no usa un negativo separado: incluye las restricciones de forma semántica en la instrucción y deja negative_prompt vacío. No prometas que un texto active búsqueda si la herramienta no está habilitada.

## Fuentes y alcance

- <https://ai.google.dev/gemini-api/docs/image-generation>
- <https://ai.google.dev/gemini-api/docs/models/gemini-nano-banana-2.1>

La revisión comprueba compatibilidad documental; no es una prueba de imágenes generadas.
