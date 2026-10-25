# HiDream — instrucciones de prompting

Revisión documental: 2026-10-23. Estado: documentada. Aplicar también `00_REGLAS_COMUNES.md`.

## I1: crear imágenes
Full, Dev y Fast reciben descripciones visuales, no tags exclusivos. Sus configuraciones no son intercambiables: el ejemplo I1 oficial usa guidance en Full y lo desactiva para Dev/Fast. No prometas un canal negativo eficaz en esas variantes sin CFG; el pipeline Full compatible sí puede aceptar negativos separados.

## E1: editar imágenes
E1-Full requiere la estructura Editing Instruction: seguida de la transformación, y Target Image Description: seguida de la descripción del resultado esperado. No lo reduzcas a una orden genérica. E1.1, en cambio, admite instrucciones directas y ya no necesita ese refinamiento.

Ambas ediciones necesitan la imagen real. Si se adjuntará después, nombra el cambio y los invariantes conocidos; no inventes una descripción de píxeles para rellenar el formato. Explica en notes cualquier referencia o contenido objetivo pendiente.

## Límites
La marca HiDream por sí sola no identifica I1 o E1. Sin tarea de edición explícita, conserva el flujo I1. Pasos, guidance, refine_strength y resolución son ajustes externos. No insertes esas claves ni supuestos sobre descarga de encoders dentro de la escena. Conserva contenido y estilo del usuario sin añadir una estética de demostración.

## Fuentes y alcance

- <https://raw.githubusercontent.com/HiDream-ai/HiDream-I1/main/README.md>
- <https://raw.githubusercontent.com/HiDream-ai/HiDream-E1/main/README.md>
- <https://huggingface.co/docs/diffusers/api/pipelines/hidream>

La revisión comprueba compatibilidad documental; no es una prueba de imágenes generadas.
