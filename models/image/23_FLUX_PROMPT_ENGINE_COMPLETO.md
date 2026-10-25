# Referencia de las familias FLUX

Revisión: 2026-10-23. Este índice sustituye la anterior receta extensa. Las guías operativas enlazadas contienen las fuentes y evitan introducir escenas de ejemplo en los prompts del usuario.

| Ruta | Guía operativa | Diferencia que debe conservarse |
| --- | --- | --- |
| FLUX.1 / FLUX1.1 | [03_FLUX_1.md](03_FLUX_1.md) | Caption visual; parámetros externos; sin negativos separados en la ruta original. |
| FLUX.1 Kontext | [04_FLUX_1_KONTEXT.md](04_FLUX_1_KONTEXT.md) | Edición con imagen de entrada, transformación e invariantes. |
| FLUX.1 Fill | [04_FLUX_1_KONTEXT.md](04_FLUX_1_KONTEXT.md) | Inpainting/outpainting con máscara o transparencia; no equivale a Kontext. |
| FLUX.2 | [05_FLUX_2.md](05_FLUX_2.md) | Prosa por defecto; JSON semántico opcional, sin esquema API obligatorio. |
| FLUX 3 Image | [06_FLUX_3.md](06_FLUX_3.md) | Layout opcional con IDs y cajas; diferente del JSON de FLUX.2. |
| FLUX 3 Image Klein | [06_FLUX_3.md](06_FLUX_3.md) | Caption completa y recomendación de upsampler propia de esta variante. |

No mezcles FLUX 3 Image con Video. No añadas parámetros de Midjourney ni pesos de A1111. Describe las referencias por su función y orden sin fingir que se han adjuntado. Si faltan posiciones o imágenes, consérvalo como dato pendiente en notes.

Las opciones ofrecidas por una API alojada no describen automáticamente todos los pipelines locales. Por ejemplo, no extrapoles la ausencia de seed en la API FLUX 3 Image a la inferencia local Klein. Consulta la fuente de la ruta exacta antes de prometer un control.
