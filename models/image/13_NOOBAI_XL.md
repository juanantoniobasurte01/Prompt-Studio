# NoobAI XL — instrucciones de prompting

Revisión documental: 2026-10-23. Estado: documentada. Aplicar también `00_REGLAS_COMUNES.md`.

## Redacción
Respeta el captionado de la familia: sujeto, personaje y serie si proceden, artista/estilo solicitado, tags especiales y tags generales. Emplea palabras naturales donde no haya un tag conocido. No inventes triggers ni personajes.

## Tags aprendidos
La ficha original relaciona calidad con masterpiece, best quality y otros niveles; newest es una etiqueta de período del dataset, no la fecha de hoy. No trasplantes scores ni source_anime de Pony. Calidad, fecha y rating son dimensiones distintas.

Los ejemplos oficiales incluyen safe y una lista negativa orientada a ciertos contenidos. Son ejemplos, no una receta para toda tarea. No añadas safe, nsfw o negativos de especie que contradigan la petición. La exclusión de furry o mammal destruiría una escena que los requiera.

## Epsilon frente a V-Pred
La variante V-Pred necesita un workflow de v-prediction y ajustes propios. El texto del prompt no cambia esa configuración. No prometas que un cargador epsilon o cualquier sampler funcionará igual. Usa el canal negativo documentado del pipeline, adaptándolo al contenido y a la revisión exacta.

No fuerces una estética o un rating no solicitado. Conserva cantidades, atributos y relaciones entre sujetos.

## Fuentes y alcance

- <https://huggingface.co/Laxhar/noobai-XL-1.0/raw/main/README.md>
- <https://huggingface.co/Laxhar/noobai-XL-Vpred-1.0/raw/main/README.md>

La revisión comprueba compatibilidad documental; no es una prueba de imágenes generadas.
