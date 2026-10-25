# Google Veo 3.1 (legado) — perfil de redacción de vídeo

Revisión: 20/10/2026. Estado de la comprobación: **contrastado**. Este perfil se carga con `00_REGLAS_COMUNES.md`; se aplica al texto del generador, no a su API.

## Formato del prompt

Describe sujeto, acciones, lugar, encuadre, cámara, luz y audio en prosa. No importes etiquetas H3 o tokens de otros modelos. Las comillas delimitan diálogo o texto literal, no una instrucción de API.

## Modalidades y referencias

T2V, I2V, referencias, primer/último fotograma y extensión dependen de la variante y del servicio. No prometas que una única llamada combina todas las modalidades.

Distingue imagen inicial, imagen final y referencia de identidad. Su papel se configura mediante entradas reales; el texto explica movimiento y conservación.

## Audio y negativos

Veo 3.1 documenta audio nativo. Atribuye cada frase al hablante y conserva el idioma. Describe ambiente y efectos solicitados sin añadir una banda sonora.

La documentación de Veo incluye negativePrompt; mantenlo separado del positivo cuando se utilice ese endpoint. No añadas un catálogo genérico de defectos.

## Límites y errores que evitar

La retirada anunciada para el 22/10/2026 afecta a los modelos Preview indicados de Gemini API; no equivale a afirmar que todo Veo 3.1 desaparece de Vertex/otros servicios. La duración, resolución y ratio se ajustan fuera del prompt.

No importes formatos de otros modelos. Mantén la intención y los datos del usuario; la guía no aporta personajes, acciones, tiempos ni ajustes por defecto. Si falta una referencia declarada para el generador externo, conserva su papel como plan e indica lo pendiente en `notes`. No afirmes haberla visto.

## Contrato de esta aplicación

Entrega el JSON interno `{prompt, negative_prompt, notes}`. Dentro de `prompt` va exclusivamente el texto de destino en el formato anterior. Las limitaciones, solicitudes sonoras no compatibles, archivos pendientes y ajustes externos se explican en `notes`, sin contaminar el texto copiable. Este editor no genera ni prueba vídeos.

## Fuentes y alcance de la revisión

- https://ai.google.dev/gemini-api/docs/veo

Corrección principal: Precisa el alcance de la retirada; deja de declarar obsoleto todo Veo 3.1.
