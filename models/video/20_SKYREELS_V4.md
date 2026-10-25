# SkyReels V4 — perfil de redacción de vídeo

Revisión: 20/10/2026. Estado de la comprobación: **parcial**. Este perfil se carga con `00_REGLAS_COMUNES.md`; se aplica al texto del generador, no a su API.

## Formato del prompt

Redacta una descripción audiovisual natural de sujeto, acciones, cámara y continuidad. Si se piden cortes, narra su progresión. No inventes etiquetas nativas ni una estructura supuestamente obligatoria de H3.

## Modalidades y referencias

El artículo de los autores confirma generación conjunta de vídeo/audio, referencias multimodales, inpainting, edición y extensión. Que una capacidad exista en el artículo no confirma que cada producto público la exponga.

Declara por separado el papel de imagen, vídeo, máscara y audio. En edición expresa lo que cambia y lo que se conserva. No inventes una máscara ni archivos ausentes.

## Audio y negativos

El sistema investigado genera vídeo y audio conjuntamente. Describe el sonido solicitado sin añadir música o habla. Para un endpoint comercial no identificado, advierte en notes que debe confirmarse su modalidad.

Sin negativo de endpoint públicamente verificado en esta revisión; negative_prompt vacío.

## Límites y errores que evitar

La página API no expuso un contrato legible. No se certifican nombres de parámetros, tags de referencias ni disponibilidad de pesos locales V4. La existencia de V2 abierto no prueba que V4 funcione en ese workflow.

No importes formatos de otros modelos. Mantén la intención y los datos del usuario; la guía no aporta personajes, acciones, tiempos ni ajustes por defecto. Si falta una referencia declarada para el generador externo, conserva su papel como plan e indica lo pendiente en `notes`. No afirmes haberla visto.

## Contrato de esta aplicación

Entrega el JSON interno `{prompt, negative_prompt, notes}`. Dentro de `prompt` va exclusivamente el texto de destino en el formato anterior. Las limitaciones, solicitudes sonoras no compatibles, archivos pendientes y ajustes externos se explican en `notes`, sin contaminar el texto copiable. Este editor no genera ni prueba vídeos.

## Fuentes y alcance de la revisión

- https://arxiv.org/abs/2602.21818
- https://arxiv.org/html/2602.21818v1
- https://www.skyreels.ai/api-platform

Corrección principal: Limita las afirmaciones al artículo primario; contrato API no verificable.
