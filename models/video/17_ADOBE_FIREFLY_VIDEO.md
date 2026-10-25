# Adobe Firefly Video — perfil de redacción de vídeo

Revisión: 20/10/2026. Estado de la comprobación: **contrastado**. Este perfil se carga con `00_REGLAS_COMUNES.md`; se aplica al texto del generador, no a su API.

## Formato del prompt

Describe encuadre, sujeto, acción, lugar y estilo de forma directa. Coordina el texto con los controles de cámara y composición seleccionados; no añadas instrucciones opuestas.

## Modalidades y referencias

Distingue Firefly Video de Veo, Kling u otros modelos disponibles en la misma web. Las herramientas de composición y referencia de movimiento tienen controles propios.

Declara imagen inicial y referencia de movimiento/composición por su función. No fabriques tokens propietarios ni prometas que nombrar una referencia la conecta.

## Audio y negativos

Las herramientas de efectos, música, voz o traducción son productos distintos. No atribuyas su audio al generador visual base; conserva la petición sonora y los diálogos en notes para ese flujo.

No se confirma un campo negativo universal; negative_prompt vacío.

## Límites y errores que evitar

Enhance prompt es una reescritura opcional que puede alterar un prompt ya preciso. Los presets, referencias de movimiento y cámara se configuran en la interfaz; no son comandos de Hailuo ni parámetros que active la prosa.

No importes formatos de otros modelos. Mantén la intención y los datos del usuario; la guía no aporta personajes, acciones, tiempos ni ajustes por defecto. Si falta una referencia declarada para el generador externo, conserva su papel como plan e indica lo pendiente en `notes`. No afirmes haberla visto.

## Contrato de esta aplicación

Entrega el JSON interno `{prompt, negative_prompt, notes}`. Dentro de `prompt` va exclusivamente el texto de destino en el formato anterior. Las limitaciones, solicitudes sonoras no compatibles, archivos pendientes y ajustes externos se explican en `notes`, sin contaminar el texto copiable. Este editor no genera ni prueba vídeos.

## Fuentes y alcance de la revisión

- https://helpx.adobe.com/firefly/web/work-with-audio-and-video/work-with-video/writing-effective-text-prompts-for-video-generation.html
- https://helpx.adobe.com/firefly/web/work-with-audio-and-video/work-with-video/enhance-your-prompt-for-video-generation.html

Corrección principal: Separa Firefly Video de los modelos asociados y de sus herramientas sonoras.
