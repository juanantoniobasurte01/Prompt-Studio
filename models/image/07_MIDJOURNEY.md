# Midjourney — instrucciones de prompting

Revisión documental: 2026-10-23. Estado: documentada. Aplicar también `00_REGLAS_COMUNES.md`.

## Redacción y versión
Escribe la escena en lenguaje descriptivo y añade los parámetros compatibles al final. No impongas una versión distinta de la elegida por el usuario. La documentación consultada sitúa V8.2 como predeterminada; no extrapoles sus opciones a V7 o Niji.

Usa --ar para una proporción solicitada y --stylize/--s solo cuando se pida ese control. No inventes URLs, códigos de estilo ni imágenes de referencia. En V8.2 el Edit Model reemplaza Omni/Character Reference; --q no está admitido. V7 mantiene sus propias referencias y opciones. Los datos de configuración no deben aparecer como prosa de la escena.

## Exclusiones
Midjourney usa --no dentro del prompt; no tiene un segundo campo negativo al estilo SDXL. Integra allí las exclusiones apropiadas y deja negative_prompt vacío. Los términos de --no se interpretan por separado: una frase compuesta puede excluir conceptos no deseados. Si hace falta, describe afirmativamente el aspecto que sí se quiere.

## Evitar
No uses pesos de A1111 ni score tags. No agregues --q, --oref, --cref o códigos de estilo sin comprobar la versión. Conserva literalmente los rótulos y las cantidades solicitadas.

## Fuentes y alcance

- <https://docs.midjourney.com/hc/en-us/articles/32199405667853-Version>
- <https://docs.midjourney.com/hc/en-us/articles/32859204029709-Parameter-List>
- <https://docs.midjourney.com/hc/en-us/articles/32173351982093-No>

La revisión comprueba compatibilidad documental; no es una prueba de imágenes generadas.
