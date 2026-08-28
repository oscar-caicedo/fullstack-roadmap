# 🏆 Proyecto de Etapa 1 — Sistema de Gestión Personal

### 🎯 Objetivo
Integrar todo lo aprendido en la Etapa 1 en una aplicación de consola modular, robusta, con persistencia (archivo JSON) y estadísticas completas.

---

## 📋 Requisitos del Proyecto

### 1. Gestión de Tareas y Actividades
- [ ] Crear tareas con título, descripción, categoría (Personal, Estudio, Trabajo), fecha límite y prioridad.
- [ ] Listar tareas con filtros (todas, pendientes, completadas, por categoría).
- [ ] Modificar datos de una tarea existente.
- [ ] Marcar tarea como completada o reactivarla.
- [ ] Eliminar tareas.
- [ ] Búsqueda por palabra clave en título y descripción.

### 2. Estadísticas y Reportes
- [ ] Total de tareas creadas.
- [ ] Porcentaje de avance / completitud.
- [ ] Tareas pendientes agrupadas por prioridad.
- [ ] Conteo de tareas por categoría.

### 3. Persistencia de Datos
- [ ] Guardar las tareas en un archivo local (`tareas.json`) automáticamente al hacer cambios.
- [ ] Cargar las tareas existentes al iniciar el programa de forma segura.

### 4. Robustez y Calidad de Código
- [ ] Manejo de excepciones (`try/except` para entradas no válidas y archivos corruptos).
- [ ] Estructura modular dividida en funciones limpias y con responsabilidades únicas.
- [ ] Menú interactivo intuitivo y legible.

---

## 📁 Archivos Sugeridos
```text
proyecto_gestion_personal/
├── main.py          # Punto de entrada y menú interactivo
├── storage.py       # Lectura y guardado de JSON
├── tasks.py         # Lógica CRUD y búsqueda de tareas
├── stats.py         # Funciones de cálculo y métricas
├── data/            # Carpeta para tareas.json
└── README.md
```
