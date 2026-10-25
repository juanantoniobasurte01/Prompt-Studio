# Illustrious XL — instrucciones de prompting

Revisión documental: 2026-10-23. Estado: documentada. Aplicar también `00_REGLAS_COMUNES.md`.

## Redacción
La ficha v1.0 admite lenguaje natural junto con tags de Danbooru. Usa el formato que conserve mejor el encargo; no impongas una lista exclusiva de etiquetas. Si no conoces una etiqueta real, escribe una descripción breve en lugar de inventarla.

## Variante y estilo
Este perfil toma v1.0 como referencia documental, no todos los finetunes publicados con su nombre. Evita introducir scores de Pony o una receta de calidad no documentada. Si el usuario pide fotografía, conserva esa intención y no la conviertas por defecto en una ilustración. Explica en notes cualquier límite de especialización del checkpoint.

## Negativos y pipeline
Como derivado SDXL, puede utilizar el canal negativo de un pipeline compatible. Respeta las recomendaciones del checkpoint exacto y excluye únicamente lo pertinente. Los ajustes de clip skip, resolución y pesos no se deducen del nombre Illustrious ni se escriben como contenido visual.

Una LoRA no se activa por mencionar un personaje: debe estar realmente instalada y conectada en el generador. Conserva disparadores facilitados, sin inventarlos. La resolución nativa de una revisión tampoco se hereda automáticamente por todos los derivados.

## Fuentes y alcance

- <https://huggingface.co/OnomaAIResearch/Illustrious-XL-v1.0>
- <https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion/stable_diffusion_xl>

La revisión comprueba compatibilidad documental; no es una prueba de imágenes generadas.
