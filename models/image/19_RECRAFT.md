# Recraft — instrucciones de prompting

Revisión documental: 2026-10-23. Estado: documentada. Aplicar también `00_REGLAS_COMUNES.md`.

## Redacción
Define el tipo de pieza y su sistema visual: contenido, jerarquía, composición, paleta y tratamiento gráfico. Una idea breve permite explorar; un brief largo sirve para restricciones concretas, no para añadir objetos ajenos. Para texto conserva literales y ubicación.

## Versiones y capacidades
El perfil genérico adopta la ruta V4 documentada, sin forzar una migración de V3 ni inferir V4.1 por la marca. La API distingue variantes raster y vectoriales; pedir apariencia vectorial no genera por sí solo un SVG. El resultado vectorial depende de elegir un modelo _vector y el formato externo correspondiente.

## Negativos
V4 no admite negative_prompt ni el text_layout de V3. Deja el negativo vacío y describe afirmativamente las restricciones. Si el usuario indica explícitamente V3, su API sí admite negativo separado, estilos curados y controles de texto propios. No copies esos campos a V4 ni uses sus coordenadas como bbox de Ideogram.

## Edición
Image-to-image, inpainting y controles de estilos tienen rutas y modelos compatibles específicos. No prometas que todas las operaciones funcionen con toda revisión. Define referencias e invariantes y deja el envío de imágenes y configuración a la herramienta externa.

## Fuentes y alcance

- <https://www.recraft.ai/blog/prompt-engineering-guide>
- <https://www.recraft.ai/docs/api-reference/models/recraft-v4>
- <https://www.recraft.ai/docs/api-reference/models/recraft-v3>

La revisión comprueba compatibilidad documental; no es una prueba de imágenes generadas.
