# Router de perfiles de vídeo

La resolución real se hace por `id` de `models/catalog.json`, no por similitud de nombres ni por rutas recibidas del usuario. Cargar reglas comunes y un solo perfil. Un nombre manual sin ID no autoriza leer un MD ni escoger una versión automáticamente.

| ID persistente | Perfil | Dirección de prompting |
|---|---|---|
| `video_gemini_omni_flash` | [Gemini Omni Flash 1.1](./01_GEMINI_OMNI_FLASH.md) | Dirección conversacional y edición con conservación explícita. |
| `video_google_veo_3_1_legacy` | [Google Veo 3.1 (legado)](./02_GOOGLE_VEO_3_1_LEGACY.md) | Veo 3.1: descripción audiovisual; retirada de Preview limitada a Gemini API. |
| `video_runway_gen_4_5` | [Runway Gen-4.5](./03_RUNWAY_GEN_4_5.md) | Gen-4.5: prosa visual y movimiento; timestamps como guía aproximada. |
| `video_kling_video_3_0` | [Kling VIDEO 3.0 y Omni](./04_KLING_VIDEO_3_0.md) | Kling 3.0: una toma o Multi-Shot; Omni y Elements se declaran expresamente. |
| `video_seedance_2_5` | [Seedance 2.5](./05_SEEDANCE_2_5.md) | Seedance 2.5: plan audiovisual y roles de referencias; límites por distribuidor. |
| `video_minimax_h3` | [MiniMax H3 / H3 Max](./06_MINIMAX_H3.md) | H3: formato audiovisual por planos, anclajes de fotogramas y modo Ref2VA con referencias declaradas. |
| `video_hailuo_02_director_legacy` | [Hailuo 02 / 2.3 / Director (MiniMax legado)](./07_HAILUO_02_DIRECTOR_LEGACY.md) | Hailuo 02/2.3/Director: prosa y comandos oficiales de cámara compatibles. |
| `video_wan_3_0` | [Wan 3.0 Video](./08_WAN_3_0.md) | Wan 3.0: narración, storyboard opcional y referencias por tipo. |
| `video_wan_2_7` | [Wan 2.7 (Alibaba API)](./09_WAN_2_7.md) | Wan 2.7: plano único mediante texto; shot_type ya no gobierna el resultado. |
| `video_wan_2_2_local` | [Wan 2.2 (local / ComfyUI)](./10_WAN_2_2_LOCAL.md) | Wan 2.2 local: checkpoint de vídeo separado de S2V. |
| `video_luma_ray_3_2` | [Luma Ray3.2](./11_LUMA_RAY_3_2.md) | Ray3.2: dirección y edición con fotogramas/control del producto. |
| `video_luma_ray_3_14` | [Luma Ray3.14 (compatibilidad)](./12_LUMA_RAY_3_14.md) | Ray3.14: compatibilidad sin referencias de identidad ni Reframe. |
| `video_vidu_q4_q3` | [Vidu Q4 / Q3](./13_VIDU_Q4_Q3.md) | Vidu: Q4 Preview requiere imágenes; Q3 se verifica por su propia ruta. |
| `video_pika_2_5` | [Pika 2.5 / Pikaframes](./14_PIKA_2_5.md) | Pika 2.5/Pikaframes: movimiento y transiciones de imágenes ordenadas. |
| `video_pixverse` | [PixVerse](./15_PIXVERSE.md) | PixVerse: endpoint explícito; multi-transition tiene instrucciones por segmento. |
| `video_grok_imagine_video_1_5` | [Grok Imagine Video 1.5](./16_GROK_IMAGINE_VIDEO_1_5.md) | Grok Imagine Video 1.5: referencias con índices reales y voces compatibles. |
| `video_adobe_firefly_video` | [Adobe Firefly Video](./17_ADOBE_FIREFLY_VIDEO.md) | Firefly Video: dirección visual sin confundir modelos asociados. |
| `video_ltx_2_5` | [LTX-2.5 (API y local ComfyUI)](./18_LTX_2_5.md) | LTX-2.5: prosa cronológica; cortes descritos, no lista aislada de planos. |
| `video_hunyuanvideo_1_5` | [HunyuanVideo 1.5](./19_HUNYUANVIDEO_1_5.md) | HunyuanVideo 1.5: descripción dinámica y checkpoint T2V/I2V correcto. |
| `video_skyreels_v4` | [SkyReels V4](./20_SKYREELS_V4.md) | SkyReels V4: capacidades multimodales confirmadas; contrato de endpoint parcial. |
| `video_cogvideox` | [CogVideoX (local)](./21_COGVIDEOX.md) | CogVideoX: texto descriptivo dentro del presupuesto del encoder. |

Distingue explícitamente Gemini Omni/Veo, H3/Hailuo antiguo, Wan API/Wan local, Ray3.2/Ray3.14 y Q4/Q3. No conviertas el nombre de una plataforma en la versión concreta del motor. Si el usuario no conoce la variante, explica la incertidumbre sin prometer la unión de capacidades de todas ellas.
