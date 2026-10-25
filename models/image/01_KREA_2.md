# Krea 2 — instrucciones de prompting

Revisión documental: 2026-10-23. Estado: documentada. Aplicar también `00_REGLAS_COMUNES.md`.

## Redacción
Describe la imagen terminada con lenguaje natural. Explicita sujeto, relaciones, técnica y composición según el encargo. Para texto visible conserva el literal entre comillas. El idioma de salida lo determina la aplicación; inglés es una opción de trabajo, no un requisito universal del checkpoint.

## Variantes y flujo
El repositorio abierto distingue RAW, sin destilación, y Turbo, destilado. No conviertas nombres comerciales Medium/Large de una interfaz en configuraciones del checkpoint abierto. La guía de la aplicación Krea permite explorar con ideas breves, referencias de estilo y moodboards; para un encargo preciso añade los detalles necesarios sin inventar adornos. Una referencia de estilo no equivale a edición localizada ni asegura identidad.

Los controles de estilo, resolución, pasos y CFG pertenecen al generador. El CLI abierto examinado no ofrece un parámetro de negativo separado: devuelve ese campo vacío y expresa las restricciones compatibles en positivo. No trasplantes deslizadores de animación ni pesos de A1111.

## Fidelidad
No introduzcas escenas de demostración, colores, objetos o tratamientos que no estén pedidos. Si se declara una referencia futura, redacta un plan de uso y anota que debe adjuntarse en el destino.

## Fuentes y alcance

- <https://raw.githubusercontent.com/krea-ai/krea-2/main/README.md>
- <https://raw.githubusercontent.com/krea-ai/krea-2/main/inference.py>
- <https://www.krea.ai/blog/krea-2-deep-dive-walkthrough>

La revisión comprueba compatibilidad documental; no es una prueba de imágenes generadas.
