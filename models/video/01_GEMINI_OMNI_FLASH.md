# Gemini Omni Flash 1.1 — perfil de redacción de vídeo

Revisión: 20/10/2026. Estado de la comprobación: **contrastado**. Este perfil se carga con `00_REGLAS_COMUNES.md`; se aplica al texto del generador, no a su API.

## Formato del prompt

Redacta una instrucción natural: escena, acción que cambia, cámara y continuidad. En edición separa el cambio solicitado de lo que debe permanecer. No existe el esquema de tres bloques de H3 ni se requiere un JSON dentro del texto.

## Modalidades y referencias

La documentación de Gemini Omni 1.1 Flash incluye generación audiovisual, entradas multimodales, edición y extensión. Distingue generar un plano de editar o continuar un vídeo existente.

Identifica qué imagen, vídeo o audio aporta identidad, composición, actuación o sonido. Mantén sus papeles declarados; no inventes identificadores @Image ni afirmes que este editor conectó medios.

## Audio y negativos

Describe el sonido pedido y atribuye el habla a su fuente. Una televisión audible pertenece a la escena; no conviertas sus voces en diálogo del protagonista. No añadas música por defecto.

Sin campo negativo universal documentado para este perfil; usa condiciones positivas y deja negative_prompt vacío.

## Límites y errores que evitar

Los ejemplos de SDK y REST muestran mecanismos de transporte; response_format, configuración de vídeo e historial conversacional no son sintaxis del prompt. Conservar la continuidad en texto no reemplaza enviar el vídeo o el contexto previo.

No importes formatos de otros modelos. Mantén la intención y los datos del usuario; la guía no aporta personajes, acciones, tiempos ni ajustes por defecto. Si falta una referencia declarada para el generador externo, conserva su papel como plan e indica lo pendiente en `notes`. No afirmes haberla visto.

## Contrato de esta aplicación

Entrega el JSON interno `{prompt, negative_prompt, notes}`. Dentro de `prompt` va exclusivamente el texto de destino en el formato anterior. Las limitaciones, solicitudes sonoras no compatibles, archivos pendientes y ajustes externos se explican en `notes`, sin contaminar el texto copiable. Este editor no genera ni prueba vídeos.

## Fuentes y alcance de la revisión

- https://ai.google.dev/gemini-api/docs/omni

Corrección principal: Separa redacción conversacional de transporte y no confunde Omni con Veo.
