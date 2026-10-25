# Stable Diffusion 3.5 — instrucciones de prompting

Revisión documental: 2026-10-23. Estado: documentada. Aplicar también `00_REGLAS_COMUNES.md`.

## Redacción
Expresa en oraciones claras sujeto, acciones y relaciones espaciales. Asocia la tipografía literal a su posición y conserva su idioma. No sustituyas una escena compleja por una lista de calidad de anime.

## Variantes
Large, Medium y Large Turbo requieren configuraciones diferentes. El modelo emplea encoders CLIP y T5; no asumas las convenciones o la extensión de contexto de SD1.5/SDXL. La longitud efectiva y cualquier prompt múltiple por encoder dependen del pipeline de destino.

## Negativos
En un pipeline SD3 con classifier-free guidance activo se documentan negativos separados. Con guidance desactivado o una variante destilada no deben darse por eficaces. Antes de atribuir un valor de CFG, número de pasos o política de negativos a Turbo, comprueba esa variante exacta. Si no se conoce el workflow, conserva las exclusiones en notes y evita prometer un campo activo.

## Controles
Los cambios de resolución, seed, pasos, guidance y sampler se hacen en el generador. No uses sintaxis Midjourney, score tags Pony ni pesos de atención como si fueran capacidades nativas de SD3.5. Los parámetros de código de la documentación son ejemplos de ejecución, no texto para renderizar.

## Fuentes y alcance

- <https://huggingface.co/stabilityai/stable-diffusion-3.5-large>
- <https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion/stable_diffusion_3>

La revisión comprueba compatibilidad documental; no es una prueba de imágenes generadas.
