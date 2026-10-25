# FLUX.1 / FLUX1.1 — instrucciones de prompting

Revisión documental: 2026-10-23. Estado: documentada. Aplicar también `00_REGLAS_COMUNES.md`.

## Redacción
Usa frases descriptivas claras, no una lista obligatoria de tags. Vincula sujeto, acción, estética, entorno y detalles relevantes. Conserva el texto de rótulos entre comillas. No añadas nombres de cámaras, marcas ni una iluminación distinta por rutina.

## Alcance
Esta ficha corresponde a T2I de FLUX.1 dev/schnell/pro y FLUX1.1 pro. Kontext y Fill tienen otro perfil. Schnell, dev y servicios pro no comparten necesariamente configuración de muestreo; tampoco se heredan referencias o controles de Ultra a todos ellos.

## Negativos y controles
En el flujo oficial de prompting FLUX no hay negativo independiente: formula el estado visual deseado y deja negative_prompt vacío. Un workflow modificado puede incorporar CFG u otros mecanismos, pero no los presentes como capacidades nativas del endpoint original.

Pesos de atención, BREAK y sintaxis LoRA pertenecen al parser del workflow. Conserva únicamente disparadores aportados por el usuario y confirmados para ese LoRA. Tamaño, seed, pasos y guidance son ajustes externos, no palabras del prompt. El resultado describe una imagen fija, sin tiempos de vídeo.

## Fuentes y alcance

- <https://raw.githubusercontent.com/black-forest-labs/skills/master/skills/flux-image-best-practices/rules/flux1-models.md>
- <https://raw.githubusercontent.com/black-forest-labs/skills/master/skills/flux-image-best-practices/rules/core-principles.md>

La revisión comprueba compatibilidad documental; no es una prueba de imágenes generadas.
