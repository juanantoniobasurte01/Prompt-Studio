# Seedance 2.5 — perfil de redacción de vídeo

Revisión: 20/10/2026. Estado de la comprobación: **parcial**. Este perfil se carga con `00_REGLAS_COMUNES.md`; se aplica al texto del generador, no a su API.

## Formato del prompt

Escena global, continuidad y progresión audiovisual. Si el usuario pide varios planos, organiza las etapas y cortes de forma legible. Si pide plano secuencia, conserva una sola toma y las pausas solicitadas.

## Modalidades y referencias

Las fuentes de proveedor consultadas describen texto, fotogramas, referencias multimodales, edición y extensión. No conviertas los límites de Volcengine en límites universales de BytePlus o de otro distribuidor.

Los materiales se citan por tipo e índice en la interfaz compatible: imagen, vídeo o audio. Conserva las etiquetas suministradas por el usuario; no fabriques @Image, @Video o @Audio sin materiales declarados.

## Audio y negativos

Separa habla, efectos, música del entorno y banda sonora. Conserva el idioma y no añadas subtítulos o música si no se piden.

No se confirma un negativo dedicado universal; las restricciones necesarias se describen sin copiar pesos de Stable Diffusion.

## Límites y errores que evitar

La página inglesa de BytePlus confirma la guía pero su cuerpo no se extrajo completo. El contenido indexado de la guía china del proveedor y la documentación de Runway confirman funciones, pero no certifican que todos los controles coincidan. No se instala la skill externa mencionada por la web.

No importes formatos de otros modelos. Mantén la intención y los datos del usuario; la guía no aporta personajes, acciones, tiempos ni ajustes por defecto. Si falta una referencia declarada para el generador externo, conserva su papel como plan e indica lo pendiente en `notes`. No afirmes haberla visto.

## Contrato de esta aplicación

Entrega el JSON interno `{prompt, negative_prompt, notes}`. Dentro de `prompt` va exclusivamente el texto de destino en el formato anterior. Las limitaciones, solicitudes sonoras no compatibles, archivos pendientes y ajustes externos se explican en `notes`, sin contaminar el texto copiable. Este editor no genera ni prueba vídeos.

## Fuentes y alcance de la revisión

- https://docs.byteplus.com/en/docs/modelark/seedance-2-5-prompt-guide
- https://docs.volcengine.com/docs/ark/seedance-2-5-prompt-guide?lang=zh
- https://docs.dev.runwayml.com/assets/inputs/

Corrección principal: Marca la extracción incompleta de la guía y evita universalizar límites de proveedor.
