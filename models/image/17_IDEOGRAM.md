# Ideogram — instrucciones de prompting

Revisión documental: 2026-10-23. Estado: documentada. Aplicar también `00_REGLAS_COMUNES.md`.

## Prosa y versión
Para una imagen normal describe sujeto, composición, medio y tipografía literal. No conviertas toda petición en JSON. Ideogram 4.0 y 4.5 admiten el formato estructurado documentado; no lo atribuyas a versiones anteriores sin comprobarlas.

## JSON de imagen
Solo por petición explícita: high_level_description y compositional_deconstruction son obligatorios. El segundo contiene background como string y elements como lista. Cada elemento lleva type (obj o text) y desc; los de texto incluyen text literal. style_description es opcional: photo o art_style, no ambos.

Una bbox opcional son cuatro enteros [y_min,x_min,y_max,x_max], normalizados 0–1000, con mínimo menor que máximo. La paleta global admite hasta 16 colores #RRGGBB y cada elemento hasta cinco. No inventes cajas si no se proporcionan posiciones. La geometría de otra API no es intercambiable.

## Entrega y controles
Magic Prompt puede reescribir el texto o el JSON; se desactiva cuando se necesita preservar una estructura manual. El objeto de diseño se entrega como contenido de prompt, nunca como cuerpo HTTP ni con vallas Markdown. Ratio y tamaño siguen fuera.

Negativos: depende del modelo y endpoint confirmado. Si no está documentado en la ruta concreta, expresa restricciones en prosa y conserva la incertidumbre en notes.

## Fuentes y alcance

- <https://docs.ideogram.ai/prompting/json-prompting>
- <https://docs.ideogram.ai/create/image-settings>

La revisión comprueba compatibilidad documental; no es una prueba de imágenes generadas.
