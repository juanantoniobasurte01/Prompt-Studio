# Qwen-Image — instrucciones de prompting

Revisión documental: 2026-10-23. Estado: documentada. Aplicar también `00_REGLAS_COMUNES.md`.

## Generación y edición
Distingue Qwen-Image T2I, Image-Edit y sus revisiones de los modelos Prompt Enhancer de 2.1. Redacta el resultado visible con lenguaje natural. En edición precisa cambios, invariantes y papel de cada referencia. Conserva texto literal, idioma y jerarquía.

## Prompt Enhancer 2.1
Los enhancers T2I e I2I son checkpoints distintos. Su formato de respuesta incluye rewritten_prompt y datos de lienzo; la herramienta normaliza el resultado como positive_prompt. No pegues el JSON completo del enhancer en una API de imagen cualquiera. En edición multiimagen, <image1>, <image2> y ratio_follow pertenecen a ese flujo y no son sintaxis universal del Qwen original.

El slot negative_prompt del enhancer 2.1 se documenta vacío: no produce un negativo independiente. Eso no demuestra que todos los pipelines Qwen-Image ignoren el negative_prompt de CFG; el ejemplo oficial del generador y el reescritor son componentes diferentes.

## Límites
Este editor no ejecuta el enhancer ni adjunta referencias. No simules que has analizado píxeles o calculado la proporción de una imagen ausente. Los parámetros de lienzo se configuran en el destino; escribir una proporción en una descripción no redimensiona un archivo.

## Fuentes y alcance

- <https://raw.githubusercontent.com/QwenLM/Qwen-Image/main/README.md>
- <https://raw.githubusercontent.com/QwenLM/Qwen-Image-2.1/main/prompt_rewrite/README.md>

La revisión comprueba compatibilidad documental; no es una prueba de imágenes generadas.
