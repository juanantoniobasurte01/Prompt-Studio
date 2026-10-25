# Adobe Firefly — instrucciones de prompting

Revisión documental: 2026-10-23. Estado: documentada. Aplicar también `00_REGLAS_COMUNES.md`.

## Redacción
Escribe frases descriptivas claras con sujeto, acción, entorno y estilo solicitados. No agregues una técnica fotográfica cuando se pide otro medio. Los controles visuales de estilo y composición son diferentes y se configuran en la interfaz real.

## Modelo frente a aplicación
Firefly puede alojar modelos de terceros. Si se elige FLUX, Gemini u otro partner, sus reglas de generación son las de ese modelo, no una combinación de todas las funciones de Adobe. Distingue además modelos Firefly estándar y Custom Models.

## Referencias y edición
Una referencia de composición orienta estructura; una referencia de estilo orienta apariencia. Describe su función e invariantes sin garantizar conservación exacta. Generative Fill y las otras herramientas necesitan sus selecciones o entradas en el destino. Un texto no configura una máscara.

## Negativos
No presupongas un campo negativo universal. La documentación de Custom Models declara ausencia de negative prompting en Image Model 3 y 4. Para esas rutas devuelve el negativo vacío y conserva las exclusiones en prosa o notes. En otras versiones comprueba su control o esquema exacto antes de prometerlo.

No mezcles parámetros de partner models ni sintaxis Midjourney con el contenido visual. Texto, proporción, referencias y resolución deben respetar lo que permita la modalidad elegida.

## Fuentes y alcance

- <https://helpx.adobe.com/firefly/web/work-with-images/generate-images/writing-effective-text-prompts.html>
- <https://developer.adobe.com/firefly-services/docs/firefly-api/guides/how-tos/cm-generate-image/>

La revisión comprueba compatibilidad documental; no es una prueba de imágenes generadas.
