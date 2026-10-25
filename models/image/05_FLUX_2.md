# FLUX.2 — instrucciones de prompting

Revisión documental: 2026-10-23. Estado: documentada. Aplicar también `00_REGLAS_COMUNES.md`.

## Redacción
Describe sujeto, acción y contexto con prosa precisa. Para tipografía conserva texto literal y jerarquía. Asocia cada color HEX al elemento al que pertenece; no prometas coincidencia colorimétrica exacta.

## Variantes
No intercambies pro/max/flex/dev/klein. Las referencias y el upsampling dependen de la variante y la ruta concreta. Klein de FLUX.2 no equivale a Klein de FLUX 3. Los ajustes de resolución, pasos, seed y expansión se configuran fuera del texto.

## JSON semántico
La guía pro/max admite organizar el contenido del prompt como un objeto JSON. Es una forma de describir la imagen, no un cuerpo HTTP ni un esquema obligatorio de claves de API. Usa prosa por defecto; cambia a JSON solo por petición explícita de formato. No actives ese modo porque una inscripción de la escena contenga la palabra JSON. Tampoco pegues cajas de FLUX 3 en este formato.

## Negativos y edición
El flujo oficial no admite negative prompts. Deja el campo negativo vacío y conserva las exclusiones mediante dirección positiva o notas. Para editar, distingue cambios e invariantes y asigna una función a cada referencia realmente prevista.

## Fuentes y alcance

- <https://docs.bfl.ai/guides/prompting_guide_flux2>
- <https://docs.bfl.ai/flux_2/flux2_text_to_image>

La revisión comprueba compatibilidad documental; no es una prueba de imágenes generadas.
