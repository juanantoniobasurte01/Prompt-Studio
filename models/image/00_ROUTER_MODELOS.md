# Selección de la guía de imagen

El perfil elegido por el usuario determina la guía. No deduzcas otra familia por su estética ni cambies de versión por disponibilidad comercial. El catálogo conserva IDs estables para presets e historial.

| Perfil | Forma inicial | Negativos | Revisión |
| --- | --- | --- | --- |
| [Krea 2](01_KREA_2.md) | natural | none | documentada |
| [Krea 2 Turbo](02_KREA_2_TURBO.md) | natural | none | documentada |
| [FLUX.1 / FLUX1.1](03_FLUX_1.md) | natural | none | documentada |
| [FLUX.1 Kontext / Fill](04_FLUX_1_KONTEXT.md) | edit | none | documentada |
| [FLUX.2](05_FLUX_2.md) | natural | none | documentada |
| [FLUX 3 Image](06_FLUX_3.md) | natural | none | documentada |
| [Midjourney](07_MIDJOURNEY.md) | midjourney | inline | documentada |
| [Stable Diffusion 1.5](08_STABLE_DIFFUSION_1_5.md) | hybrid | supported | documentada |
| [Stable Diffusion XL](09_STABLE_DIFFUSION_XL.md) | hybrid | supported | documentada |
| [Stable Diffusion 3.5](10_STABLE_DIFFUSION_3_5.md) | natural | conditional | documentada |
| [Pony Diffusion XL V6](11_PONY_DIFFUSION_XL.md) | hybrid | supported | parcial |
| [Illustrious XL](12_ILLUSTRIOUS_XL.md) | hybrid | supported | documentada |
| [NoobAI XL](13_NOOBAI_XL.md) | tags | supported | documentada |
| [Qwen-Image](14_QWEN_IMAGE.md) | natural | conditional | documentada |
| [Nano Banana / Gemini Image](15_NANO_BANANA_GEMINI.md) | natural | none | documentada |
| [GPT Image](16_GPT_IMAGE.md) | natural | none | documentada |
| [Ideogram](17_IDEOGRAM.md) | natural | conditional | documentada |
| [Seedream](18_SEEDREAM.md) | natural | conditional | documentada |
| [Recraft](19_RECRAFT.md) | natural | none | documentada |
| [Adobe Firefly](20_ADOBE_FIREFLY.md) | natural | conditional | documentada |
| [HiDream](21_HIDREAM.md) | natural | conditional | documentada |
| [Z-Image](22_Z_IMAGE.md) | natural | conditional | documentada |

La forma inicial puede cambiar por petición explícita: FLUX.2 JSON semántico, FLUX 3 layout, Ideogram 4/4.5 JSON o HiDream E1-Full con sus dos secciones. La palabra JSON impresa en un cartel no solicita un formato de salida.

Para variantes concretas aplica las reglas de su guía: Kontext frente a Fill; HiDream I1 frente a E1/E1.1 y Full frente a Dev/Fast; Z-Image Base frente a Turbo; Recraft V3 frente a V4. No supongas compatibilidad de edición porque la familia genere imágenes.

La aplicación carga 00_REGLAS_COMUNES.md y solo el MD numerado del perfil seleccionado. Este router y 23_FLUX_PROMPT_ENGINE_COMPLETO.md son índices de consulta, no instrucciones adicionales inyectadas a todos los modelos. Sin perfil se emplea lenguaje natural universal, sin sintaxis específica.
