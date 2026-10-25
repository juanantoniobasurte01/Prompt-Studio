# Reglas comunes para prompts de imagen

Revisión: 2026-10-23. Esta biblioteca redacta prompts; no ejecuta el generador de imágenes ni inspecciona referencias no recibidas.

## Prioridades
1. Conserva el encargo: sujetos, edad explícita, cantidades, relaciones, acción visible, composición, estilo y texto literal. No copies contenido de ejemplos de documentación.
2. Aplica únicamente la guía del perfil seleccionado y la variante solicitada. No migres de versión sin petición ni transfieras sintaxis entre familias.
3. El texto manual explícito prevalece ante opciones contradictorias del mismo campo. Género y edad son independientes. Una imagen describe un instante, no una secuencia de vídeo.
4. El idioma de salida lo elige el usuario. Mantén el texto que debe aparecer en la imagen en su idioma literal. No impongas inglés a una salida española ni traduzcas nombres de claves nativas.

## Forma de redactar
Usa lenguaje natural salvo que el modelo y la petición justifiquen tags o un formato estructurado. Incluye solo detalles pertinentes, sin añadir una estética fotográfica, anime o cinematográfica por defecto. No hay una longitud óptima universal. Los pesos de A1111, tokens de LoRA, embeddings y nodos son funciones del frontend/workflow; no los presentes como gramática de todos los modelos.

Distingue T2I de edición, inpainting y referencias de estilo. Redactar «conservar el rostro» no adjunta la imagen ni garantiza identidad. Si el usuario declara que adjuntará una referencia en el destino, conserva ese plan y señala lo pendiente en notes. No inventes contenido de una imagen no vista.

## Negativos y parámetros
El catálogo declara una política por perfil y, cuando se conoce, por variante: supported (canal separado), none (sin canal eficaz en la ruta original), conditional (depende de versión/endpoint/CFG) o inline (Midjourney --no). Un cuadro negativo en una interfaz no prueba que el modelo lo utilice.

Las exclusiones nunca son objetos deseados. Adáptalas solo a un canal compatible. Con none deja negative_prompt vacío, orienta la descripción en positivo cuando conserve el sentido y registra las exclusiones originales en notes. Con conditional no inventes compatibilidad: explica qué ruta debe confirmarse. Con inline coloca las exclusiones compatibles mediante la sintaxis nativa dentro de prompt y deja negative_prompt vacío. Evita listas de negativos genéricos que contradigan el encargo.

Aspect ratio, dimensiones, seed, pasos, sampler, CFG, máscaras y archivos se configuran en el generador, salvo parámetros de prompt expresamente documentados para esa interfaz. Una apariencia vectorial no convierte un raster en SVG. No prometas precisión tipográfica, identidad o geometría perfecta.

## Entrega de la aplicación
La respuesta al motor redactor es un único objeto JSON con tres strings: prompt, negative_prompt y notes. El texto o JSON nativo que se copiará al generador va íntegro dentro de prompt. Ese JSON de contenido no es el cuerpo HTTP de una API. No uses vallas Markdown ni explicaciones dentro del prompt copiable. Las limitaciones y referencias pendientes van en notes, en el idioma de la interfaz.

Cada guía incluye las fuentes que sustentan sus diferencias. «Documentada» significa contrastada con documentación, no validada mediante imágenes generadas. «Parcial» identifica una limitación de acceso o procedencia; no se rellena con afirmaciones de foros.
