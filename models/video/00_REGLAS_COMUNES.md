# Vídeo — reglas comunes de Prompt Studio

Revisión: 20/10/2026. Cargar este archivo y exactamente un perfil elegido mediante el catálogo. El perfil específico determina formato, referencias, audio y restricciones. Una capacidad de otro modelo de la misma plataforma no se hereda.

## Intención y continuidad

Conserva sujetos, edad, rostro descrito, ropa, acciones, objetos, relaciones espaciales, cámara, luz, estilo y desenlace del usuario. Combina texto libre y campos guiados sin descartar ninguno. Si el manual de un campo contradice su selector, prevalece el manual; no elimines otros campos que no están en conflicto.

No conviertas estilo amateur en cinematográfico, no cambies una cámara fija por un travelling y no sustituyas una oclusión física por un fundido. Identifica estado inicial, evolución y estado final. Una secuencia de gestos dentro de la toma no implica cortes; añade planos solo cuando se soliciten o cuando el modo declarado lo requiera.

No inventes contenido para campos vacíos ni detalles de imágenes que no puedes ver. Los ejemplos de documentación ilustran formatos, no aportan una escena para copiar. No reutilices sus duraciones, distancias, acciones, voces, objetos o decorados. Si un dato como «X acción» está sin concretar, conserva esa limitación en `notes` sin rellenarlo por tu cuenta.

## Modalidad y tiempos

Identifica si se pide T2V, imagen inicial, inicio/final, solo final, referencias de identidad/movimiento, edición, extensión o audio condicionado. Diferencia lo que el modelo entiende del modo realmente activado en el generador. No cambies automáticamente de variante cuando falta una entrada necesaria; explica lo pendiente en `notes`.

Conserva tiempos aportados y las pausas solicitadas. Usa el formato temporal del perfil, sin importar gramáticas de otro modelo. No inventes cifras si no se indican; recurre a orden cualitativo. Los timestamps son dirección narrativa, no una garantía de precisión de fotograma. No interpretes silenciosamente un formato ambiguo como `04:45` como segundos decimales. Indica la ambigüedad en `notes`.

Duración, resolución, relación de aspecto, FPS, semilla, CFG, pasos, LoRA y opciones de expansión son ajustes de ejecución. La prosa no modifica esos controles. Los límites del proveedor no autorizan a recortar la acción o cambiar el final sin explicarlo.

## Referencias declaradas

Este editor recibe texto y no conecta medios al generador de destino. Aun así, el usuario puede declarar qué imagen, vídeo o audio aportará allí. Conserva esa asignación como un plan e indica los archivos pendientes en `notes`; no borres sus referencias solo por no tener una subida en este editor.

No fabriques archivos ni identificadores. Un fotograma inicial fija el comienzo, uno final fija el final, y una referencia de identidad no obliga a reproducir la composición como primer frame. Conserva nombres e índices reales de la interfaz correspondiente. Si no hay referencia declarada, no añadas Picture 1, @Image ni <IMAGE_0>.

## Audio, literalidad y negativos

Incluye audio en el prompt únicamente si el perfil y la modalidad lo respaldan. Si el flujo visual no lo genera, conserva en `notes` la petición sonora y las frases literales para el flujo de audio correspondiente; no prometas sonido nativo ni descartes la petición sin explicación.

Para audio compatible, distingue hablante visible, voz fuera de campo, televisión/radio, efectos físicos, ambiente y música añadida. No pongas voces del televisor en boca del protagonista. No inventes diálogos, narración, subtítulos ni música. Mantén el idioma y el texto exacto del diálogo, letras y rótulos; traduce solo la descripción de escena al idioma de salida solicitado. Usa los marcadores de habla del perfil, no siempre los de H3.

`negative_prompt` solo contiene restricciones necesarias cuando el flujo las consume. Si no existe negativo confirmado, queda vacío; expresa afirmativamente lo que debe verse. No añadas listas estándar de defectos anatómicos ni sintaxis de pesos por costumbre. El negativo no garantiza la ausencia de un defecto.

## Salida y revisión

Devuelve el JSON interno `{prompt, negative_prompt, notes}`. La gramática propia del generador va íntegra dentro del string `prompt`, con sus saltos y secciones si las exige el perfil. El JSON interno no es el cuerpo de su API. Las dudas, limitaciones, fuentes, controles externos y explicaciones no pertenecen al prompt copiable.

Antes de responder, verifica: variante correcta; datos del usuario conservados; cámara y sujeto separados; cronología factible; desenlace intacto; referencias coherentes; audio atribuido; negativo compatible; ausencia de gramática de otra familia. Si un dato no se puede verificar, no lo conviertas en una capacidad garantizada.
