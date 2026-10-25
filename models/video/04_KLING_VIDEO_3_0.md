# Kling VIDEO 3.0 y Omni — perfil de redacción de vídeo

Revisión: 20/10/2026. Estado de la comprobación: **contrastado**. Este perfil se carga con `00_REGLAS_COMUNES.md`; se aplica al texto del generador, no a su API.

## Formato del prompt

Una toma: escena y acción continua en prosa. Varios planos pedidos: ancla de continuidad y planos numerados con encuadre, acción y duración aportada. No fuerces cortes ni una estructura H3.

## Modalidades y referencias

VIDEO 3.0 distingue Multi-Shot y Custom Multi-Shot. El segundo requiere habilitar el primero. Omni añade entradas y referencias multimodales propias; no todos sus controles se trasladan al modo básico.

Usa los nombres @ de elementos creados o declarados para la interfaz de destino. No inventes nombres de Elements ni copies @Image de Seedance. Si un elemento tiene voz vinculada, evita redefinir un timbre contradictorio.

## Audio y negativos

La familia 3.0 documenta audio nativo y atribución de hablantes. Conserva idioma y texto literal; identifica quién habla y quién permanece en silencio. El silencio solicitado excluye música añadida.

Sin un campo negativo verificado para todas las variantes; deja negative_prompt vacío salvo que se indique una integración que lo soporte.

## Límites y errores que evitar

La guía de 3.0 describe 3–15 s. Describir Shot 1 no habilita el switch Multi-Shot ni configura las duraciones de Custom Multi-Shot. El guion debe corresponder a los controles usados.

No importes formatos de otros modelos. Mantén la intención y los datos del usuario; la guía no aporta personajes, acciones, tiempos ni ajustes por defecto. Si falta una referencia declarada para el generador externo, conserva su papel como plan e indica lo pendiente en `notes`. No afirmes haberla visto.

## Contrato de esta aplicación

Entrega el JSON interno `{prompt, negative_prompt, notes}`. Dentro de `prompt` va exclusivamente el texto de destino en el formato anterior. Las limitaciones, solicitudes sonoras no compatibles, archivos pendientes y ajustes externos se explican en `notes`, sin contaminar el texto copiable. Este editor no genera ni prueba vídeos.

## Fuentes y alcance de la revisión

- https://kling.ai/quickstart/klingai-video-3-model-user-guide
- https://kling.ai/quickstart/klingai-video-3-omni-model-user-guide

Corrección principal: Distingue modo básico, Omni, Elements y activación real de Multi-Shot.
