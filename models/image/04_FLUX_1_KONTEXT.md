# FLUX.1 Kontext / Fill — instrucciones de prompting

Revisión documental: 2026-10-23. Estado: documentada. Aplicar también `00_REGLAS_COMUNES.md`.

## Elegir la tarea
Kontext y Fill son modelos distintos, aunque este perfil conserve un identificador común por compatibilidad. Si no se especifica Fill, trata la petición como una edición Kontext. No inventes una modalidad a partir de una palabra de la escena.

## Kontext
Redacta el cambio solicitado y los rasgos que deben mantenerse. Una instrucción concreta suele ser preferible a redescribir toda la imagen. Para texto, identifica el literal anterior y su sustituto. Kontext puede editar sin una máscara de Fill; no le exijas una por defecto. Tampoco atribuyas referencias múltiples de FLUX.2 al Kontext original.

## Fill
Requiere imagen y zona editable mediante máscara o alfa. En la máscara oficial, blanco se regenera y negro se conserva; con alfa, se rellenan las partes transparentes. Describe el contenido final de la zona y su continuidad con el entorno. El texto no sustituye esos archivos.

## Límites
Ambos flujos usan prosa y no un negativo separado. Imagen, máscara y ajustes van fuera del prompt. Este editor prepara texto: si los archivos se aportarán después, conserva el plan y señala el adjunto pendiente en notes; nunca inventes su contenido.

## Fuentes y alcance

- <https://docs.bfl.ai/kontext/kontext_image_editing>
- <https://docs.bfl.ai/flux_1_fill>

La revisión comprueba compatibilidad documental; no es una prueba de imágenes generadas.
