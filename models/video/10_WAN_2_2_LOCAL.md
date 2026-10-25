# Wan 2.2 (local / ComfyUI) — perfil de redacción de vídeo

Revisión: 20/10/2026. Estado de la comprobación: **contrastado**. Este perfil se carga con `00_REGLAS_COMUNES.md`; se aplica al texto del generador, no a su API.

## Formato del prompt

Un párrafo descriptivo con sujeto, movimiento, entorno y cámara. La expansión de prompt puede precisar lo pedido, pero no añadir otra acción ni convertirlo en un guion H3.

## Modalidades y referencias

El repositorio diferencia T2V-A14B, I2V-A14B y TI2V-5B. S2V-14B es una variante guiada por audio; no añade por sí sola sonido nativo a los checkpoints base.

I2V requiere el checkpoint y una imagen real. Keyframes, identidad o control temporal adicional dependen del workflow; escribir Image 1 no crea esos nodos.

## Audio y negativos

Para T2V/I2V base redacta contenido visual. Si se pide voz o música, conserva la petición en notes para un flujo de audio; si se declara S2V, explica que requiere su audio de entrada y su modelo específico.

El condicionamiento negativo depende del sampler y de sus nodos. Úsalo separado cuando el usuario declare un flujo compatible.

## Límites y errores que evitar

Idioma, número de frames, resolución, CFG, pasos y LoRAs se ajustan al pipeline. No extrapoles límites de Wan 3.0 API ni de un wrapper a todos los checkpoints locales.

No importes formatos de otros modelos. Mantén la intención y los datos del usuario; la guía no aporta personajes, acciones, tiempos ni ajustes por defecto. Si falta una referencia declarada para el generador externo, conserva su papel como plan e indica lo pendiente en `notes`. No afirmes haberla visto.

## Contrato de esta aplicación

Entrega el JSON interno `{prompt, negative_prompt, notes}`. Dentro de `prompt` va exclusivamente el texto de destino en el formato anterior. Las limitaciones, solicitudes sonoras no compatibles, archivos pendientes y ajustes externos se explican en `notes`, sin contaminar el texto copiable. Este editor no genera ni prueba vídeos.

## Fuentes y alcance de la revisión

- https://github.com/Wan-Video/Wan2.2

Corrección principal: Separa S2V de generación base y evita atribuir controles API al checkpoint local.
