# Stable Diffusion 1.5 — instrucciones de prompting

Revisión documental: 2026-10-23. Estado: documentada. Aplicar también `00_REGLAS_COMUNES.md`.

## Redacción
El modelo original recibe texto descriptivo; no exige etiquetas Danbooru, score tags ni un orden ritual. Usa una descripción compacta y atribuible a cada sujeto. Un checkpoint derivado puede preferir tags o triggers: solo adopta los de su ficha exacta.

## Encoder y frontend
Prioriza el contenido esencial al principio. El encoder CLIP tiene contexto limitado; los mecanismos para superar sus bloques dependen del software. No equipares un límite de tokens a un número fijo de palabras ni prometas que cualquier interfaz conservará texto ilimitado.

Los pesos (término:valor), BREAK y llamadas LoRA son funciones del parser de A1111 u otro frontend, no del checkpoint original. Sin una interfaz confirmada entrega texto normal, sin esas marcas.

## Negativos y edición
En los pipelines con CFG, las exclusiones van al campo negativo separado. No añadas una lista genérica de defectos ni negativos que contradigan la escena. Img2img e inpainting necesitan entradas y un pipeline apropiado: el prompt no sustituye la imagen ni la máscara.

## Evidencia
La ficha v1.5 accesible es una copia que se identifica expresamente como espejo, no el repositorio original de Runway. Las reglas de parser se verifican por separado en el software que las implementa.

## Fuentes y alcance

- <https://huggingface.co/stable-diffusion-v1-5/stable-diffusion-v1-5>
- <https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Features>

La revisión comprueba compatibilidad documental; no es una prueba de imágenes generadas.
