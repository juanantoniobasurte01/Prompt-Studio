# Luma Ray3.14 (compatibilidad) — perfil de redacción de vídeo

Revisión: 20/10/2026. Estado de la comprobación: **contrastado**. Este perfil se carga con `00_REGLAS_COMUNES.md`; se aplica al texto del generador, no a su API.

## Formato del prompt

Prosa con sujeto, acción, entorno y cámara. En I2V desarrolla movimiento desde el encuadre inicial; en Modify describe cambios y conservación de lo no editado.

## Modalidades y referencias

La guía específica incluye T2V, I2V, keyframes y Modify Video. No deben heredarse automáticamente las funciones posteriores de Ray3.2.

No confundir un fotograma de I2V o keyframe con referencias de identidad: la guía de Ray3.14 declara que no admite reference images ni character consistency. Si el usuario pide R2V de identidad, indícalo en notes sin fingir soporte.

## Audio y negativos

No hay generación sonora nativa confirmada en esta revisión. La petición sonora permanece en notes para otra herramienta.

Sin negativo dedicado confirmado; negative_prompt vacío.

## Límites y errores que evitar

La guía lista T2V de 5/10 s, I2V de 5 s y Modify hasta 18 s. También indica que no puede utilizarse con Reframe. Son límites de esa guía/producto, no parámetros que active el texto.

No importes formatos de otros modelos. Mantén la intención y los datos del usuario; la guía no aporta personajes, acciones, tiempos ni ajustes por defecto. Si falta una referencia declarada para el generador externo, conserva su papel como plan e indica lo pendiente en `notes`. No afirmes haberla visto.

## Contrato de esta aplicación

Entrega el JSON interno `{prompt, negative_prompt, notes}`. Dentro de `prompt` va exclusivamente el texto de destino en el formato anterior. Las limitaciones, solicitudes sonoras no compatibles, archivos pendientes y ajustes externos se explican en `notes`, sin contaminar el texto copiable. Este editor no genera ni prueba vídeos.

## Fuentes y alcance de la revisión

- https://lumalabs.ai/learning-hub/ray314-user-guide

Corrección principal: Corrige la falsa equivalencia entre keyframes y referencias de identidad; registra Reframe no compatible.
