# Presets e idiomas

## Biblioteca incluida

Hay seis presets por cada uno de los 43 perfiles del catálogo: **258 en total**, 132 de imagen y 126 de vídeo. Las seis escenas base se comparten para evitar duplicación y se adaptan al medio y a las modalidades que requieren una entrada declarada.

| Escena | Personas | Acción y contexto |
|---|---|---|
| Ceramista en su taller | Mujer de 35 años | Modela un cuenco de barro con luz de ventana. |
| Cocinero veterano al amanecer | Hombre de 68 años | Dobla masa en una panadería. |
| Corredora en la costa | Mujer negra de 24 años | Empieza a trotar en un paseo marítimo. |
| Dos mecánicos en el taller | Hombres de 30 y 45 años | Se entregan una herramienta sin duplicarla. |
| Abuela y nieta en el jardín | Mujer de 72 años y niña de 9 | Riegan una planta juntas. |
| Retrato con flash tras el ensayo | Dos mujeres y dos hombres adultos | Retrato y saludo breve con luz frontal en una sala oscura. |

Los presets de imagen incluyen de 41 a 48 campos relevantes: identidad, rasgos, pelo, prendas, expresión, acción, objetos, entorno, cámara, luz y restricciones. Los de vídeo incluyen de 56 a 63, con duración objetivo, modalidad, estados inicial y final, cronología, continuidad y plan sonoro. No es necesario rellenar todos los campos opcionales del editor para definir una escena completa.

Vidu declara una imagen inicial pendiente de adjuntar en el generador y conserva Q4 Preview I2V. Kontext declara una imagen base y la transformación de vestuario, conservando los demás elementos. Los demás presets de vídeo usan dirección desde texto; MiniMax H3 declara T2VA. Las duraciones son objetivos que deben confirmarse en la interfaz del generador. El audio sigue la política del perfil seleccionado.

Acceso: **Presets → Ejemplos por modelo**. Se puede filtrar por modelo y buscar por nombre, persona, contexto o acción. Cargar un ejemplo rellena el editor guiado y permite cambiar cualquier valor. Para conservar una versión propia, se guarda en **Mis presets**.

La biblioteca se distribuye con el proyecto (`backend/preset_scenes.json` y `backend/preset_library.py`). No se inserta en SQLite, no consume el límite del listado de presets personales y no altera los registros existentes. Los IDs de biblioteca son estables: `builtin:<modelo>:<escena>`.

## Español e inglés

El selector de **Configuración → Idioma de la interfaz** cambia navegación, botones, ayudas, mensajes, campos, opciones, buscadores y biblioteca. La elección se recuerda en este navegador. Las cadenas del editor tienen traducción inglesa local; términos ambiguos, como «Liso» en pelo frente a estampados, tienen traducciones por contexto.

Los valores internos de selectores e IDs se conservan para recuperar presets e historial anteriores. Cambiar de idioma no traduce ni modifica el texto del usuario, los valores manuales ni la salida ya generada. Los ejemplos nuevos se cargan en el idioma activo de la biblioteca; un ejemplo cargado pasa a ser texto editable y se conserva al cambiar la interfaz.

**Idioma de la interfaz** e **Idioma del prompt** son ajustes independientes. Cargar un ejemplo conserva el modelo Ollama y el idioma de salida elegidos por el usuario. En nuevas peticiones se solicita que las notas se redacten en el idioma de la interfaz y la escena en el idioma del prompt, conservando diálogos literales y cabeceras nativas. La fidelidad de la redacción depende del LLM.

Todas las traducciones son archivos incluidos en el frontend. No hay llamadas a servicios de traducción ni conexiones externas en ejecución.

## Género, edad y orden de opciones

El campo `tipo_persona` conserva su ID por compatibilidad, pero ahora es **Género / identidad** y sus opciones no contienen edades. La edad se especifica exclusivamente en **Edad aparente**. Los ejemplos incluidos separan ambos datos. Al cargar presets o historial antiguos se normalizan las categorías conocidas: «Mujer anciana» se convierte en género femenino; si ya existe una edad explícita, se respeta. Si no existe, se conserva la categoría de edad original en el campo de edad, sin inventar una cifra precisa. La misma adaptación se aplica en el backend, sin reescribir los registros SQLite ni descripciones manuales arbitrarias.

Complexión sigue una escala de muy delgada a muy corpulenta. Musculatura y estructura corporal tienen campos propios; una constitución atlética no implica una cantidad de grasa corporal. Las antiguas opciones compuestas se trasladan al campo correspondiente, conservando los valores explícitos que ya hubiera en él.

Modelos, presets y categorías sin escala se ordenan por nombre con el idioma activo. Edades, duraciones y focales numéricas se ordenan de menor a mayor; las proporciones de formato, por su cociente. Estatura, complexión, longitud de cabello, épocas, horas, intensidad de luz y otras escalas siguen una progresión semántica. En listas mixtas, las opciones de escala preceden a las categorías ordenadas por nombre. El historial conserva su orden temporal.

## Comprobación

15 tests automatizados correctos, incluidas las 516 configuraciones de biblioteca (258 por idioma), validación de formularios, referencias, selección de guía y separación de presets personales. Compilación de producción y cobertura de traducciones correctas. Comprobados en navegador el cambio de idioma, su persistencia tras recargar, la conservación de selecciones y texto manual, carga de ejemplo y búsqueda de acciones en inglés.

Las pruebas de redacción que ya estaban lanzadas terminaron antes del aviso de no utilizar el modelo. Después del aviso, la verificación continuó sin nuevas llamadas de generación a Ollama ni cambios en sus modelos en ejecución.
