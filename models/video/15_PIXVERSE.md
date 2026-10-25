# PixVerse — perfil de redacción de vídeo

Revisión: 20/10/2026. Estado de la comprobación: **contrastado**. Este perfil se carga con `00_REGLAS_COMUNES.md`; se aplica al texto del generador, no a su API.

## Formato del prompt

T2V/I2V usan texto natural de escena y movimiento. En multi-transition, describe cada transición por separado con su imagen de partida y su intervalo declarado; las instrucciones deben corresponder al segmento correcto.

## Modalidades y referencias

Distingue T2V, I2V, start/end, Fusion, multi-transition y edición/extensión. La disponibilidad cambia según modelo y cuenta; una función del catálogo de PixVerse no está implícita en todas las rutas.

Los medios se suben y se enlazan mediante img_id/media_id en entradas compatibles. No inventes IDs ni conviertas sus números en contenido visual.

## Audio y negativos

Hay soluciones separadas de sonido, TTS/lipsync y opciones de audio según endpoint. No prometas diálogo nativo en una ruta no confirmada; conserva la petición en notes si falta esa confirmación.

Negativo solo donde la ruta publique ese campo; no se infiere por el nombre PixVerse.

## Límites y errores que evitar

La URL antigua de multi-transition devolvió 404; la ruta vigente documenta multi_transition con prompt y duración en cada segmento. El último elemento termina la secuencia: duración ausente/0 y sin nueva transición. No se reutiliza aquí el prompt común de Pikaframes ni se conserva el antiguo límite 2–7 sin verificar.

No importes formatos de otros modelos. Mantén la intención y los datos del usuario; la guía no aporta personajes, acciones, tiempos ni ajustes por defecto. Si falta una referencia declarada para el generador externo, conserva su papel como plan e indica lo pendiente en `notes`. No afirmes haberla visto.

## Contrato de esta aplicación

Entrega el JSON interno `{prompt, negative_prompt, notes}`. Dentro de `prompt` va exclusivamente el texto de destino en el formato anterior. Las limitaciones, solicitudes sonoras no compatibles, archivos pendientes y ajustes externos se explican en `notes`, sin contaminar el texto copiable. Este editor no genera ni prueba vídeos.

## Fuentes y alcance de la revisión

- https://docs.platform.pixverse.ai/text-to-video-generation-13016634e0
- https://docs.platform.pixverse.ai/multi-transition-video-43051215e0
- https://docs.platform.pixverse.ai/

Corrección principal: Actualiza enlace roto y diferencia prompts por transición del prompt común de Pika.
