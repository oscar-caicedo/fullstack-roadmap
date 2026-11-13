# Sistema de gestión personal

Una aplicación de consola para organizar tareas de estudio, trabajo y vida personal. Está hecha con Python y guarda tus cambios en un archivo JSON local.

## Empezar

1. Abre una terminal en esta carpeta.
2. Ejecuta:

   ```bash
   python main.py
   ```

3. Elige una opción del menú y sigue las indicaciones. No necesitas instalar paquetes.

## Qué puedes hacer

- Agregar tareas con título, descripción, categoría, fecha límite y prioridad.
- Ver todas las tareas o filtrarlas por estado o categoría.
- Actualizar una tarea. Si dejas un campo vacío, conserva su valor actual.
- Marcarla como completada o devolverla a pendientes.
- Buscar palabras en títulos y descripciones; la búsqueda no distingue mayúsculas ni tildes.
- Consultar un resumen de avance, prioridades y categorías.
- Eliminar una tarea después de confirmar la acción.

Las fechas se escriben como `AAAA-MM-DD` (por ejemplo, `2026-10-16`). Las categorías disponibles son Personal, Estudio y Trabajo; las prioridades son Alta, Media y Baja.

## Datos y archivos

El programa crea `tareas.json` junto a `main.py` cuando guardas tu primera tarea. Tus datos permanecen en ese archivo local; no se envían a ningún servicio. Si el archivo no existe, la aplicación empieza con una lista vacía. Si sus datos no son válidos, el programa avisa y evita sobrescribirlos.

## Estructura

```text
proyecto_gestion_personal/
├── main.py       # Menú e interacción con la persona usuaria
├── tasks.py      # Búsqueda y filtros
├── stats.py      # Resumen de tareas
├── storage.py    # Lectura y guardado de JSON
└── tareas.json   # Se crea al guardar la primera tarea
```
