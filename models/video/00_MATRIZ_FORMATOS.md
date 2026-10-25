# Matriz de formatos de vídeo — revisada el 20/10/2026

El formato textual no activa modos, no adjunta medios y no configura los parámetros del generador. Audio nativo y negativo se interpretan para la variante y el endpoint del perfil, no para toda la plataforma.

| Perfil | Formato / distinción principal | Audio | Negativo | Verificación |
|---|---|---|---|---|
| [Gemini Omni Flash 1.1](./01_GEMINI_OMNI_FLASH.md) | Dirección conversacional y edición con conservación explícita. | Nativo según modalidad | No confirmado: vacío | contrastado |
| [Google Veo 3.1 (legado)](./02_GOOGLE_VEO_3_1_LEGACY.md) | Veo 3.1: descripción audiovisual; retirada de Preview limitada a Gemini API. | Nativo según modalidad | Solo flujo compatible | contrastado |
| [Runway Gen-4.5](./03_RUNWAY_GEN_4_5.md) | Gen-4.5: prosa visual y movimiento; timestamps como guía aproximada. | Flujo sonoro aparte / base visual | No confirmado: vacío | contrastado |
| [Kling VIDEO 3.0 y Omni](./04_KLING_VIDEO_3_0.md) | Kling 3.0: una toma o Multi-Shot; Omni y Elements se declaran expresamente. | Nativo según modalidad | Solo flujo compatible | contrastado |
| [Seedance 2.5](./05_SEEDANCE_2_5.md) | Seedance 2.5: plan audiovisual y roles de referencias; límites por distribuidor. | Nativo según modalidad | No confirmado: vacío | parcial |
| [MiniMax H3 / H3 Max](./06_MINIMAX_H3.md) | H3: formato audiovisual por planos, anclajes de fotogramas y modo Ref2VA con referencias declaradas. | Nativo según modalidad | No confirmado: vacío | contrastado |
| [Hailuo 02 / 2.3 / Director (MiniMax legado)](./07_HAILUO_02_DIRECTOR_LEGACY.md) | Hailuo 02/2.3/Director: prosa y comandos oficiales de cámara compatibles. | Flujo sonoro aparte / base visual | No confirmado: vacío | contrastado |
| [Wan 3.0 Video](./08_WAN_3_0.md) | Wan 3.0: narración, storyboard opcional y referencias por tipo. | Nativo según modalidad | Solo flujo compatible | contrastado |
| [Wan 2.7 (Alibaba API)](./09_WAN_2_7.md) | Wan 2.7: plano único mediante texto; shot_type ya no gobierna el resultado. | Nativo según modalidad | Sí en la ruta documentada | contrastado |
| [Wan 2.2 (local / ComfyUI)](./10_WAN_2_2_LOCAL.md) | Wan 2.2 local: checkpoint de vídeo separado de S2V. | Flujo sonoro aparte / base visual | Solo flujo compatible | contrastado |
| [Luma Ray3.2](./11_LUMA_RAY_3_2.md) | Ray3.2: dirección y edición con fotogramas/control del producto. | Flujo sonoro aparte / base visual | No confirmado: vacío | contrastado |
| [Luma Ray3.14 (compatibilidad)](./12_LUMA_RAY_3_14.md) | Ray3.14: compatibilidad sin referencias de identidad ni Reframe. | Flujo sonoro aparte / base visual | No confirmado: vacío | contrastado |
| [Vidu Q4 / Q3](./13_VIDU_Q4_Q3.md) | Vidu: Q4 Preview requiere imágenes; Q3 se verifica por su propia ruta. | Nativo según modalidad | No confirmado: vacío | contrastado |
| [Pika 2.5 / Pikaframes](./14_PIKA_2_5.md) | Pika 2.5/Pikaframes: movimiento y transiciones de imágenes ordenadas. | Flujo sonoro aparte / base visual | Solo flujo compatible | contrastado |
| [PixVerse](./15_PIXVERSE.md) | PixVerse: endpoint explícito; multi-transition tiene instrucciones por segmento. | Verificar endpoint | Solo flujo compatible | contrastado |
| [Grok Imagine Video 1.5](./16_GROK_IMAGINE_VIDEO_1_5.md) | Grok Imagine Video 1.5: referencias con índices reales y voces compatibles. | Nativo según modalidad | No confirmado: vacío | contrastado |
| [Adobe Firefly Video](./17_ADOBE_FIREFLY_VIDEO.md) | Firefly Video: dirección visual sin confundir modelos asociados. | Flujo sonoro aparte / base visual | No confirmado: vacío | contrastado |
| [LTX-2.5 (API y local ComfyUI)](./18_LTX_2_5.md) | LTX-2.5: prosa cronológica; cortes descritos, no lista aislada de planos. | Nativo según modalidad | Solo flujo compatible | contrastado |
| [HunyuanVideo 1.5](./19_HUNYUANVIDEO_1_5.md) | HunyuanVideo 1.5: descripción dinámica y checkpoint T2V/I2V correcto. | Flujo sonoro aparte / base visual | Solo flujo compatible | contrastado |
| [SkyReels V4](./20_SKYREELS_V4.md) | SkyReels V4: capacidades multimodales confirmadas; contrato de endpoint parcial. | Nativo según modalidad | No confirmado: vacío | parcial |
| [CogVideoX (local)](./21_COGVIDEOX.md) | CogVideoX: texto descriptivo dentro del presupuesto del encoder. | Flujo sonoro aparte / base visual | Solo flujo compatible | contrastado |

MiniMax H3 conserva sus bloques base o Ref2VA; no es prosa genérica ni un esquema universal para el resto. Ray3.14 admite keyframes pero no referencias de identidad según su guía. Un modo no documentado se indica en notes, sin sustituir el modelo en silencio.

