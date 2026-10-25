# Guías de generación de imagen

22 perfiles de imagen. Cada guía distingue redacción, variantes, restricciones y fuentes originales. Incluyen modelos alojados y checkpoints abiertos; los controles de una interfaz no son universales.

- [Reglas comunes](00_REGLAS_COMUNES.md): fidelidad, idioma, exclusiones y transporte de respuesta.
- [Índice por modelo](00_ROUTER_MODELOS.md): formato inicial y política de negativos de los 22 perfiles.
- [Referencia FLUX](23_FLUX_PROMPT_ENGINE_COMPLETO.md): diferencias entre generación, edición y layout.

El backend carga únicamente las reglas comunes y el archivo numerado del perfil seleccionado. El catálogo añade contratos específicos y selecciona variantes explícitas; no cambia el modelo de destino por su cuenta. Los presets utilizan los mismos IDs.

La revisión es documental y las comprobaciones de software usan respuestas simuladas. No se han generado imágenes ni descargado pesos. El resultado visual depende del modelo, su versión y el workflow real. Pony V6 mantiene verificación parcial porque la ficha original no estuvo accesible; su guía explica la procedencia secundaria disponible.
