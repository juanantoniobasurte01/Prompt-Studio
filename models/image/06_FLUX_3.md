# FLUX 3 Image — instrucciones de prompting

Revisión documental: 2026-10-23. Estado: documentada. Aplicar también `00_REGLAS_COMUNES.md`.

## Generación y referencias
Describe una imagen estática con sus sujetos y relaciones. Conserva los textos literales entre comillas. Las referencias se nombran por su orden de entrada: image 1, image 2, etc.; el modelo de imagen admite hasta diez. Identifica qué aporta cada una y qué se conserva. No confundas este modelo con FLUX 3 Video.

## Layout, solo cuando se solicita
El formato nativo combina una descripción con identificadores <id> y, al final, una lista JSON de elementos con id, bbox y desc. Las cajas siguen [top,left,bottom,right], con enteros de 0 a 1000. No son el JSON semántico de FLUX.2. Usa cajas solo con posiciones realmente proporcionadas; sin geometría suficiente, entrega prosa y explica el dato pendiente en notes.

## Klein y parámetros
FLUX 3 Image Klein se entrena con captions completas; su documentación recomienda el prompt upsampler. Preparar una caption aquí no significa haber ejecutado ese modelo auxiliar. No añadas el mismo requisito a FLUX.2 Klein.

La API de FLUX 3 Image no expone negative_prompt, guidance ni seed. Aspect ratio y resolución se configuran aparte. No trasplantes esa ausencia de seed a todos los workflows locales Klein.

## Fuentes y alcance

- <https://docs.bfl.ai/guides/prompting_unified_basics>
- <https://docs.bfl.ai/guides/prompting_layout>
- <https://docs.bfl.ai/flux_3/flux3_image_layout>
- <https://docs.bfl.ai/flux_3/flux3_image_klein>

La revisión comprueba compatibilidad documental; no es una prueba de imágenes generadas.
