# HunyuanVideo 1.5 — perfil de redacción de vídeo

Revisión: 20/10/2026. Estado de la comprobación: **contrastado**. Este perfil se carga con `00_REGLAS_COMUNES.md`; se aplica al texto del generador, no a su API.

## Formato del prompt

Combina sujeto, movimiento y escena con encuadre, cámara, luz y estilo cuando estén definidos. Los corchetes de la fórmula del manual señalan componentes opcionales; no son comandos literales. Usa conectores temporales para acciones sucesivas.

## Modalidades y referencias

Distingue T2V e I2V y los checkpoints de resolución correspondientes. Prompt rewriting puede refinar vocabulario, no cambiar identidad, vestuario o desenlace.

I2V arranca de una imagen real; prioriza dinámica de sujeto, entorno y cámara. No transformes una referencia de identidad en un sistema de R2V no configurado.

## Audio y negativos

No se confirma audio nativo del checkpoint base. Conserva sonido y diálogos en notes para el pipeline de audio, sin fingir sincronización generada.

La inferencia oficial expone --negative_prompt; solo se usa separado, en un flujo que lo consuma.

## Límites y errores que evitar

El manual documenta chino e inglés. Resolución, frames, sampler y extensión son controles del pipeline. Descripción detallada no equivale a acumular etiquetas genéricas ni prometer multi-shot estricto.

No importes formatos de otros modelos. Mantén la intención y los datos del usuario; la guía no aporta personajes, acciones, tiempos ni ajustes por defecto. Si falta una referencia declarada para el generador externo, conserva su papel como plan e indica lo pendiente en `notes`. No afirmes haberla visto.

## Contrato de esta aplicación

Entrega el JSON interno `{prompt, negative_prompt, notes}`. Dentro de `prompt` va exclusivamente el texto de destino en el formato anterior. Las limitaciones, solicitudes sonoras no compatibles, archivos pendientes y ajustes externos se explican en `notes`, sin contaminar el texto copiable. Este editor no genera ni prueba vídeos.

## Fuentes y alcance de la revisión

- https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5
- https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5/blob/main/assets/HunyuanVideo_1_5_Prompt_Handbook_EN.md

Corrección principal: No interpreta la fórmula del manual como comandos y separa vídeo base de audio/Avatar.
