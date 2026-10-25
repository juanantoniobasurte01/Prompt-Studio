# Perfiles de vídeo de Prompt Studio

Los 21 perfiles se cargan individualmente desde el catálogo. Se redactan prompts; no se generan vídeos ni se envían medios a proveedores.

La salida pública de la aplicación es `{prompt, negative_prompt, notes}`. Dentro de prompt va el texto nativo del destino; el JSON interno no se pega en su API como si fuera un contrato de ese proveedor. Las referencias pueden declararse para conectarlas después en el generador externo.

- [Reglas comunes](./00_REGLAS_COMUNES.md)
- [Router por ID](./00_ROUTER_MODELOS.md)
- [Matriz por perfil](./00_MATRIZ_FORMATOS.md)

«Contrastado» significa que se consultaron las fuentes primarias citadas; no garantiza precisión semántica de Qwen ni resultados del vídeo final. Seedance y SkyReels tienen comprobaciones parciales documentadas. La retirada de Veo Preview indicada por Google afecta a Gemini API y no demuestra retirada de todos los despliegues Veo 3.1.
