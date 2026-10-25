# Vidu Q4 / Q3 — perfil de redacción de vídeo

Revisión: 20/10/2026. Estado de la comprobación: **contrastado**. Este perfil se carga con `00_REGLAS_COMUNES.md`; se aplica al texto del generador, no a su API.

## Formato del prompt

Escena, acciones, cámara y sonido en texto natural. Mantén los roles de referencias. No sustituyas la descripción por un inventario de sujetos ni por bloques H3.

## Modalidades y referencias

La documentación Q4 Preview distingue I2V con una imagen inicial y R2V con imágenes de referencia. No se confirma ahí T2V puro de Q4. Q3 es otra variante; la ausencia de imágenes no autoriza a cambiar de modelo silenciosamente.

Una imagen inicial declarada para adjuntar después en Vidu es un plan válido de I2V. Conserva I2V y anota únicamente que la imagen debe adjuntarse allí. No cambies a R2V, Q3 o una imagen generada por defecto porque este editor solo reciba texto.

El endpoint R2V muestra @1/@2 en ejemplos y advierte que el método de invocación de subjects no está disponible en Q4 Preview. Usa solo etiquetas realmente declaradas/compatibles; no inventes nombres de subjects de la biblioteca.

## Audio y negativos

Q3 y Q4 Preview documentan salida audiovisual. Q4 permite audio=false para vídeo silencioso. No asumas clonación libre de voz: la gestión de subjects indica restricciones de voice_id para Q3/Q4.

No se confirma un negativo dedicado para estas rutas; negative_prompt vacío.

## Límites y errores que evitar

Q4 Preview documenta prompt hasta 20.000 caracteres e is_rec puede sustituir la redacción por una recomendada. Las voces, idioma y material sonoro deben corresponder al endpoint; la garantía comercial de sincronía no es una prueba de exactitud literal.

No importes formatos de otros modelos. Mantén la intención y los datos del usuario; la guía no aporta personajes, acciones, tiempos ni ajustes por defecto. Si falta una referencia declarada para el generador externo, conserva su papel como plan e indica lo pendiente en `notes`. No afirmes haberla visto.

## Contrato de esta aplicación

Entrega el JSON interno `{prompt, negative_prompt, notes}`. Dentro de `prompt` va exclusivamente el texto de destino en el formato anterior. Las limitaciones, solicitudes sonoras no compatibles, archivos pendientes y ajustes externos se explican en `notes`, sin contaminar el texto copiable. Este editor no genera ni prueba vídeos.

## Fuentes y alcance de la revisión

- https://platform.vidu.com/docs/api-reference/video-models/vidu-q4-preview/image-to-video
- https://platform.vidu.com/docs/api-reference/video-models/vidu-q4-preview/reference-to-video
- https://www.vidu.com/vidu-q3
- https://platform.vidu.com/docs/api-reference/task-management/subjects

Corrección principal: Sustituye una guía inaccesible por API primaria; precisa audio, subjects y ausencia de T2V Q4 confirmado.
