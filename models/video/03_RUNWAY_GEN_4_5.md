# Runway Gen-4.5 — perfil de redacción de vídeo

Revisión: 20/10/2026. Estado de la comprobación: **contrastado**. Este perfil se carga con `00_REGLAS_COMUNES.md`; se aplica al texto del generador, no a su API.

## Formato del prompt

En T2V combina contenido visual y movimiento. En I2V prioriza cómo se mueve lo establecido por la imagen. Una toma continua no se convierte en varios planos porque existan etapas de acción.

## Modalidades y referencias

Gen-4.5 admite T2V e I2V. No le atribuyas edición Aleph, actuación Act-Two ni los controles de otro modelo de la plataforma Runway.

La imagen inicial determina apariencia y composición. No inventes una imagen final ni una librería de referencias de personajes para una ruta que no las expone.

## Audio y negativos

No está confirmado aquí un canal de generación sonora nativa de Gen-4.5. Guarda solicitudes de diálogo, música y ambiente en notes como necesidades del flujo de audio, sin prometer que el clip visual las produce.

Redacta de forma afirmativa; no hay negativo dedicado confirmado en este perfil. Cámara inmóvil se expresa como cámara fija, no como una lista de prohibiciones.

## Límites y errores que evitar

La guía oficial permite timestamps asociados a acciones junto con prosa y advierte que su precisión no es exacta. No los prohíbas ni los conviertas en parámetros de API. La API documenta duración de 2–10 s, pero el texto no modifica el selector.

No importes formatos de otros modelos. Mantén la intención y los datos del usuario; la guía no aporta personajes, acciones, tiempos ni ajustes por defecto. Si falta una referencia declarada para el generador externo, conserva su papel como plan e indica lo pendiente en `notes`. No afirmes haberla visto.

## Contrato de esta aplicación

Entrega el JSON interno `{prompt, negative_prompt, notes}`. Dentro de `prompt` va exclusivamente el texto de destino en el formato anterior. Las limitaciones, solicitudes sonoras no compatibles, archivos pendientes y ajustes externos se explican en `notes`, sin contaminar el texto copiable. Este editor no genera ni prueba vídeos.

## Fuentes y alcance de la revisión

- https://help.runwayml.com/hc/en-us/articles/42460036199443-Text-to-Video-Prompting-Guide
- https://docs.dev.runwayml.com/api-details/api_changelog/

Corrección principal: Admite timestamps documentados; separa Gen-4.5 de otros productos Runway.
