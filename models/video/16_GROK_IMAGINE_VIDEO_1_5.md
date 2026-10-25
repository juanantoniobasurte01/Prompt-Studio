# Grok Imagine Video 1.5 — perfil de redacción de vídeo

Revisión: 20/10/2026. Estado de la comprobación: **contrastado**. Este perfil se carga con `00_REGLAS_COMUNES.md`; se aplica al texto del generador, no a su API.

## Formato del prompt

Describe plano, acciones, cámara y sonido en lenguaje natural. En T2V no introduzcas tokens de imágenes inexistentes. No fuerces un guion H3.

## Modalidades y referencias

La documentación separa T2V, I2V, R2V, fotograma final y keyframes. La referencia de identidad no fija por sí sola el primer frame.

En R2V, las referencias comienzan en <IMAGE_0>; si se añade image para fijar el inicio, este ocupa <IMAGE_0> y las referencias empiezan en <IMAGE_1>. Conserva el mapeo declarado: no renumeres a ciegas.

## Audio y negativos

Las voces de reference_audios se referencian como <AUDIO_0>, etc. El acceso general documenta presets por voice_id; los archivos de voz propios requieren acceso de trusted partner. No prometas clonar cualquier archivo. El audio generado puede desactivarse mediante configuración externa.

No se confirma negativo dedicado; negative_prompt vacío.

## Límites y errores que evitar

image, last_frame y keyframes son entradas diferentes. Los keyframes interiores y sus tiempos se configuran externamente, no mediante etiquetas de texto. Las resoluciones y límites de I2V/T2V no se extrapolan a R2V.

No importes formatos de otros modelos. Mantén la intención y los datos del usuario; la guía no aporta personajes, acciones, tiempos ni ajustes por defecto. Si falta una referencia declarada para el generador externo, conserva su papel como plan e indica lo pendiente en `notes`. No afirmes haberla visto.

## Contrato de esta aplicación

Entrega el JSON interno `{prompt, negative_prompt, notes}`. Dentro de `prompt` va exclusivamente el texto de destino en el formato anterior. Las limitaciones, solicitudes sonoras no compatibles, archivos pendientes y ajustes externos se explican en `notes`, sin contaminar el texto copiable. Este editor no genera ni prueba vídeos.

## Fuentes y alcance de la revisión

- https://docs.x.ai/developers/model-capabilities/video/reference-to-video
- https://docs.x.ai/developers/model-capabilities/video/generation

Corrección principal: Corrige el desplazamiento de índices y el alcance de referencias de voz.
