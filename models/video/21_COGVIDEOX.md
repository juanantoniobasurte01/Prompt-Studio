# CogVideoX (local) — perfil de redacción de vídeo

Revisión: 20/10/2026. Estado de la comprobación: **contrastado**. Este perfil se carga con `00_REGLAS_COMUNES.md`; se aplica al texto del generador, no a su API.

## Formato del prompt

Escribe un párrafo visual preciso con sujeto, entorno, acciones y cámara. Prioriza detalles de la petición; no expandas indefinidamente con adjetivos ni copies escenas de ejemplos.

## Modalidades y referencias

El repositorio distingue 2B, 5B, 5B-I2V y la familia 1.5. Las tareas T2V, I2V y V2V requieren pipeline/checkpoint compatibles.

La imagen inicial o el vídeo se pasan al pipeline. No hay convención universal Image N o Picture N que cree condicionamiento.

## Audio y negativos

El generador base produce frames de vídeo; las solicitudes sonoras y diálogos se conservan en notes para otra herramienta.

No se deduce un negativo del nombre del modelo: depende de Diffusers/ComfyUI. El cli_demo consultado no expone un flag negativo; no inventarlo.

## Límites y errores que evitar

La tabla oficial documenta inglés y presupuestos de 224/226 tokens según variante. Texto largo recomendado significa descriptivo dentro de ese presupuesto; evita que la expansión elimine el final por truncamiento. No confundas el límite de Ollama con el del encoder de CogVideoX.

No importes formatos de otros modelos. Mantén la intención y los datos del usuario; la guía no aporta personajes, acciones, tiempos ni ajustes por defecto. Si falta una referencia declarada para el generador externo, conserva su papel como plan e indica lo pendiente en `notes`. No afirmes haberla visto.

## Contrato de esta aplicación

Entrega el JSON interno `{prompt, negative_prompt, notes}`. Dentro de `prompt` va exclusivamente el texto de destino en el formato anterior. Las limitaciones, solicitudes sonoras no compatibles, archivos pendientes y ajustes externos se explican en `notes`, sin contaminar el texto copiable. Este editor no genera ni prueba vídeos.

## Fuentes y alcance de la revisión

- https://github.com/zai-org/CogVideo
- https://raw.githubusercontent.com/zai-org/CogVideo/main/inference/cli_demo.py

Corrección principal: Añade presupuesto de encoder y evita recomendar expansión ilimitada o flags inexistentes.
