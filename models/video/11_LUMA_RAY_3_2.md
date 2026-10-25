# Luma Ray3.2 — perfil de redacción de vídeo

Revisión: 20/10/2026. Estado de la comprobación: **contrastado**. Este perfil se carga con `00_REGLAS_COMUNES.md`; se aplica al texto del generador, no a su API.

## Formato del prompt

Escribe en prosa el plano y su evolución. En Modify separa qué se transforma y qué actuación, encuadre o identidad se pretende conservar. No introduzcas esquemas de H3 ni comandos Hailuo.

## Modalidades y referencias

Luma identifica Ray3.2 como su modelo de vídeo actual y describe generación, modificación y control temporal mediante herramientas. La capacidad del producto no fija por sí sola el esquema de todos los endpoints.

Declara roles de keyframes y vídeo de origen solo cuando el usuario los aporte para su flujo. No inventes índices textuales de API ni afirmes tener continuidad de identidad garantizada.

## Audio y negativos

La plataforma integra herramientas de audio separadas. No se confirma aquí que el endpoint Ray3.2 genere habla sincronizada nativa: conserva solicitudes sonoras en notes para el flujo correspondiente.

No hay un negativo universal verificado para este perfil. Usa dirección afirmativa y negative_prompt vacío.

## Límites y errores que evitar

No llamar Dream Machine al nombre de modelo actual ni copiar un JSON de Ray2. Una herramienta de audio alojada en Luma no prueba audio nativo de Ray3.2.

No importes formatos de otros modelos. Mantén la intención y los datos del usuario; la guía no aporta personajes, acciones, tiempos ni ajustes por defecto. Si falta una referencia declarada para el generador externo, conserva su papel como plan e indica lo pendiente en `notes`. No afirmes haberla visto.

## Contrato de esta aplicación

Entrega el JSON interno `{prompt, negative_prompt, notes}`. Dentro de `prompt` va exclusivamente el texto de destino en el formato anterior. Las limitaciones, solicitudes sonoras no compatibles, archivos pendientes y ajustes externos se explican en `notes`, sin contaminar el texto copiable. Este editor no genera ni prueba vídeos.

## Fuentes y alcance de la revisión

- https://lumalabs.ai/llm-info
- https://lumalabs.ai/ray3

Corrección principal: Evita confundir audio de la plataforma con el generador y Ray2 con Ray3.2.
