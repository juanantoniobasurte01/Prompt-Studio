# GPT Image — instrucciones de prompting

Revisión documental: 2026-10-23. Estado: documentada. Aplicar también `00_REGLAS_COMUNES.md`.

## Redacción
Indica qué imagen se necesita, su contenido, composición, estilo y restricciones. Para editar delimita cambio e invariantes; asigna una función a cada referencia. Conserva el texto visible literalmente, sin traducirlo por el idioma de la interfaz.

## Versión concreta
La documentación consultada distingue GPT Image 2.5 Flare y Sunburst, GPT Image 2 y versiones anteriores. Mantén la versión elegida: no migres ni agregues sufijos por decisión propia. Los controles y límites de una revisión no son intercambiables.

## API frente a prompt
model, size, quality, background y output_format pertenecen a la configuración externa. Una petición de transparencia necesita el canal alfa y un formato compatible; describir un damero no crea transparencia. input_fidelity no debe enviarse a GPT Image 2, que procesa sus entradas en alta fidelidad.

## Edición y exclusiones
Una máscara orienta la edición, no garantiza un límite exacto de píxeles. La continuidad requiere conservar y reenviar las referencias o el estado necesario. No afirmes haber adjuntado imágenes desde este editor.

No hay un campo negativo separado en el flujo aquí documentado: redacta restricciones dentro de la instrucción y deja negative_prompt vacío. El JSON interno de promptstudio es transporte de texto, no el cuerpo de la solicitud de imágenes de OpenAI.

## Fuentes y alcance

- <https://developers.openai.com/api/docs/guides/image-prompting>
- <https://developers.openai.com/api/docs/guides/image-generation>

La revisión comprueba compatibilidad documental; no es una prueba de imágenes generadas.
