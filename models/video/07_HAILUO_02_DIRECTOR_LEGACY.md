# Hailuo 02 / 2.3 / Director (MiniMax legado) — perfil de redacción de vídeo

Revisión: 20/10/2026. Estado de la comprobación: **contrastado**. Este perfil se carga con `00_REGLAS_COMUNES.md`; se aplica al texto del generador, no a su API.

## Formato del prompt

Describe sujeto y acción en prosa; sitúa el comando de cámara cuando se aplica. Los comandos válidos incluyen [Truck left], [Truck right], [Pan left], [Pan right], [Push in], [Pull out], [Pedestal up], [Pedestal down], [Tilt up], [Tilt down], [Zoom in], [Zoom out], [Shake], [Tracking shot] y [Static shot].

## Modalidades y referencias

La API T2V confirma comandos para MiniMax-Hailuo-2.3, MiniMax-Hailuo-02 y T2V-01-Director. I2V y start/end tienen rutas y listas de modelos propias; no basta el nombre Director.

Las imágenes de inicio/final se envían por los argumentos correspondientes. No uses la cabecera Picture 1/Picture 2 de H3 ni sus tres bloques de audio.

## Audio y negativos

No hay audio nativo confirmado para estas rutas antiguas. Conserva las peticiones sonoras en notes para otro flujo.

La ruta consultada no documenta un negativo dedicado. Deja negative_prompt vacío.

## Límites y errores que evitar

Límite documentado: 2.000 caracteres en el prompt T2V. Los comandos en el mismo corchete son simultáneos; separados a lo largo del texto pueden secuenciarse. El optimizador del proveedor puede cambiar el texto: se configura fuera del prompt.

No importes formatos de otros modelos. Mantén la intención y los datos del usuario; la guía no aporta personajes, acciones, tiempos ni ajustes por defecto. Si falta una referencia declarada para el generador externo, conserva su papel como plan e indica lo pendiente en `notes`. No afirmes haberla visto.

## Contrato de esta aplicación

Entrega el JSON interno `{prompt, negative_prompt, notes}`. Dentro de `prompt` va exclusivamente el texto de destino en el formato anterior. Las limitaciones, solicitudes sonoras no compatibles, archivos pendientes y ajustes externos se explican en `notes`, sin contaminar el texto copiable. Este editor no genera ni prueba vídeos.

## Fuentes y alcance de la revisión

- https://platform.minimax.io/docs/api-reference/video-generation-t2v
- https://platform.minimax.io/docs/api-reference/video-generation-fl2v

Corrección principal: Confirma que los comandos también se documentan para 02 y 2.3, no solo Director.
