# Stable Diffusion XL — instrucciones de prompting

Revisión documental: 2026-10-23. Estado: documentada. Aplicar también `00_REGLAS_COMUNES.md`.

## Redacción
Describe contenido y estilo mediante lenguaje natural o frases cortas compatibles con el checkpoint. Relaciona atributos, posiciones y acciones con sus sujetos. SDXL original no impone la gramática de Pony, Illustrious o NoobAI: sus perfiles se consultan aparte.

## Arquitectura y pipeline
La base de SDXL puede utilizarse sola; el refiner es opcional y no es una fase que este editor haya ejecutado. SDXL usa dos encoders y algunas interfaces exponen prompts separados para ellos. No inventes un reparto entre encoders si el usuario no lo solicita ni lo proporciona su workflow.

## Negativos
El pipeline documenta negative_prompt separado y variantes de entrada para sus encoders cuando se usa guidance. Devuelve únicamente exclusiones pertinentes al encargo; no presupongas que todas las versiones destiladas usan el mismo CFG o conservan ese comportamiento.

## Controles externos
Resolución, recorte, seed, guidance, sampler, refiner y adaptadores no son texto de la escena. La sintaxis de ponderación depende del parser; no generes (tag:1.2), BREAK o llamadas LoRA por defecto. Los modelos de edición necesitan sus imágenes o máscaras en la herramienta de destino.

## Fuentes y alcance

- <https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0>
- <https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion/stable_diffusion_xl>

La revisión comprueba compatibilidad documental; no es una prueba de imágenes generadas.
