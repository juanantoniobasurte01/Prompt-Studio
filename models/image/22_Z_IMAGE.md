# Z-Image — instrucciones de prompting

Revisión documental: 2026-10-23. Estado: documentada. Aplicar también `00_REGLAS_COMUNES.md`.

## Redacción
Escribe una caption visual precisa con sujetos, atributos y relaciones. Conserva el texto que deba dibujarse en su idioma. No copies score tags ni un esquema de pesos ajeno.

## Turbo frente a Base
La ejecución oficial de Turbo usa guidance_scale 0.0. No presentes un negativo de CFG como eficaz en ese flujo; devuelve el negativo vacío y formula las restricciones compatibles en positivo. Que una interfaz muestre un textbox no demuestra que el sampler lo utilice.

La base Z-Image, sin Turbo, documenta CFG y un negative_prompt eficaz. Para esa variante confirmada conserva las exclusiones en su campo separado. Sin versión o workflow confirmado no asumas que Base y Turbo comparten ajustes.

## Edición y otras revisiones
Una variante de edición u Omni debe identificarse por su checkpoint y documentación exactos. No atribuyas imagen de entrada a un checkpoint T2I solo por su marca. Cualquier edición requiere adjuntar los archivos necesarios en la herramienta de destino.

## Configuración
Los valores de resolución, pasos y guidance se aplican en el generador, no en la descripción. No añadas parámetros porque aparezcan en una receta de otro modelo. Las restricciones del usuario se conservan incluso cuando no exista un canal negativo independiente.

## Fuentes y alcance

- <https://raw.githubusercontent.com/Tongyi-MAI/Z-Image/main/README.md>
- <https://huggingface.co/Tongyi-MAI/Z-Image-Turbo>

La revisión comprueba compatibilidad documental; no es una prueba de imágenes generadas.
