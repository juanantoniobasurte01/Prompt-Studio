# Pony Diffusion XL V6 — instrucciones de prompting

Revisión documental: 2026-10-23. Estado: parcial. Aplicar también `00_REGLAS_COMUNES.md`.

## Alcance y evidencia parcial
Estas reglas se limitan a V6 XL. La ficha original de Civitai y el repositorio del autor no pudieron recuperarse durante esta revisión. Hay copias públicas de la ficha: se identifican como copias, no como una comprobación directa del original. No extrapoles estas reglas a V7 ni a un merge desconocido.

## Redacción
La ficha reproducida describe entrenamiento mixto de lenguaje natural y tags, no un formato exclusivamente Danbooru. Para V6 original su prefijo recomendado es score_9, score_8_up, score_7_up, score_6_up, score_5_up, score_4_up. Después describe la escena, con tags pertinentes opcionales. No reduzcas el prefijo a dos scores como si fuera la recomendación completa.

source_anime, source_cartoon, source_furry y source_pony solo proceden cuando coinciden con el medio solicitado. No inventes un personaje o cambies una fotografía a ilustración por el checkpoint.

## Negativos y ejecución
El canal negativo existe en pipelines SDXL compatibles, pero la ficha V6 reproducida no exige usarlo habitualmente. No añadas listas genéricas ni masterpiece por rutina. Clip skip es un ajuste externo de la implementación, no un token visual. Los forks necesitan su propia ficha.

## Fuentes y alcance

- <https://civitai.com/models/257749/pony-diffusion-v6-xl>
- <https://huggingface.co/Snupihog/Pony_Diffusion_V6_XL>
- <https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion/stable_diffusion_xl>

La revisión comprueba compatibilidad documental; no es una prueba de imágenes generadas.
