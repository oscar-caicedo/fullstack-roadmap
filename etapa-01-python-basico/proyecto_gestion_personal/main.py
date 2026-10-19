"""
1. Gestión de Tareas y Actividades
- [ ] Crear tareas con título, descripción, categoría (Personal, Estudio, Trabajo), fecha límite y prioridad.
- [ ] Listar tareas con filtros (todas, pendientes, completadas, por categoría).
- [ ] Modificar datos de una tarea existente.
- [ ] Marcar tarea como completada o reactivarla.
- [ ] Eliminar tareas.
- [ ] Búsqueda por palabra clave en título y descripción.
"""

#Gestion de Tareas y Actividades
from datetime import datetime
from storage import cargar_tareas, guardar_tareas    
from stats import mostrar_estadisticas
from tasks import buscar_tarea_por_titulo, buscar_tareas_por_palabra_clave, filtrar_tareas

    
    
try:
    tareas = cargar_tareas()
except ValueError as error:  
    print(error) 
    raise SystemExit(1) 

def pedir_fecha_valida(mensaje):

    while True:
        fecha = input(mensaje).strip()
        
        try:
            datetime.strptime(fecha, "%Y-%m-%d")
            return fecha
        except ValueError:
            print("Fecha inválida. Usa el formato AAAA-MM-DD, por ejemplo 2026-10-16.")
            
def pedir_opcion_valida(mensaje, opciones):

    while True:
        valor = input(mensaje).strip().title()

        if valor in opciones:
            return valor

        print(f"Valor no válido. Opciones permitidas: {', '.join(opciones)}")
        
def pedir_texto_no_vacio(mensaje):
    while True:
        texto = input(mensaje).strip()

        if texto:
            return texto

        print("Este campo no puede quedar vacío.")

def crear_tarea():
    titulo = pedir_texto_no_vacio("Titulo: ")
    descripcion = pedir_texto_no_vacio("Descripcion: ")
    categoria = pedir_opcion_valida(
    "Categoría (Personal, Estudio, Trabajo): ",
    ["Personal", "Estudio", "Trabajo"]
)
    fecha = pedir_fecha_valida("Fecha (AAAA-MM-DD): ")
    prioridad = pedir_opcion_valida(
    "Prioridad (Alta, Media, Baja): ",
    ["Alta", "Media", "Baja"]
)    
    tarea = {
        "titulo" : titulo,
        "descripcion" : descripcion,
        "categoria": categoria,
        "fecha": fecha,
        "prioridad": prioridad,
        "completada": False
    }
    tareas.append(tarea)
    guardar_tareas(tareas)
    
def listar_tareas(filtro="todas", categoria=None):
    tareas_a_mostrar = filtrar_tareas(tareas, filtro, categoria)
    if not tareas_a_mostrar:
        print("No hay tareas para mostrar con ese filtro.")
        return

    for indice, tarea in enumerate(tareas_a_mostrar, start=1):
        print(f"\n{indice}. Título: {tarea['titulo']}")
        print(f"Descripción: {tarea['descripcion']}")
        print(f"Categoría: {tarea['categoria']}")
        print(f"Fecha: {tarea['fecha']}")
        print(f"Prioridad: {tarea['prioridad']}")
        print("Estado: Completada" if tarea["completada"] else "Estado: Pendiente")   
            
def modificar_tarea():
    titulo = input("Ingrese el titulo de la tarea a modificar: ") 
    tarea = buscar_tarea_por_titulo(tareas, titulo)
    if tarea:
        print("Ingrese los nuevos datos de la tarea: " )
        titulo = pedir_texto_no_vacio("Titulo: ")
        descripcion = pedir_texto_no_vacio("Descripcion: ")
        categoria = pedir_opcion_valida(
    "Categoría (Personal, Estudio, Trabajo): ",
    ["Personal", "Estudio", "Trabajo"]
)
        fecha = pedir_fecha_valida("Fecha (AAAA-MM-DD): ")
        prioridad = pedir_opcion_valida(
    "Prioridad (Alta, Media, Baja): ",
    ["Alta", "Media", "Baja"]
)
        
        tarea["titulo"] = titulo
        tarea["descripcion"] = descripcion
        tarea["categoria"] = categoria
        tarea["fecha"] = fecha
        tarea["prioridad"] = prioridad
        guardar_tareas(tareas)
        print("Tarea modificada exitosamente.")
    else:
        print("Tarea no encontrada.")
        
def marcar_completada():
    titulo = input("Ingrese el titulo de la tarea a marcar como completada: ")
    tarea = buscar_tarea_por_titulo(tareas, titulo)
    if tarea:
        tarea["completada"] = True
        guardar_tareas(tareas)
        print("Tarea marcada como completada.")
    else:
        print("Tarea no encontrada.")
        
def reactivar_tarea():
    titulo = input("Ingrese el titulo de la tarea a reactivar: ")
    tarea = buscar_tarea_por_titulo(tareas, titulo)
    if tarea:
        tarea["completada"] = False
        guardar_tareas(tareas)
        print("Tarea reactivada.")
    else:
        print("Tarea no encontrada.")
        
def eliminar_tarea():
    titulo = input("Ingrese el titulo de la tarea a eliminar: ")
    tarea = buscar_tarea_por_titulo(tareas, titulo)
    if tarea:
        tareas.remove(tarea)
        guardar_tareas(tareas)
        print("Tarea eliminada exitosamente.")
    else:
        print("Tarea no encontrada.")

def mostrar_resultados_busqueda():
    palabra = input("Escribe una palabra para buscar: ").strip()

    if palabra == "":
        print("La búsqueda no puede estar vacía.")
        return

    resultados = buscar_tareas_por_palabra_clave(tareas, palabra)

    if not resultados:
        print("No se encontraron tareas.")
        return

    print("Tareas encontradas:")

    for indice, tarea in enumerate(resultados, start=1):
        print(f"\n{indice}. Título: {tarea['titulo']}")
        print(f"   Descripción: {tarea['descripcion']}")
        print(f"   Categoría: {tarea['categoria']}")
        print(f"   Fecha: {tarea['fecha']}")
        print(f"   Prioridad: {tarea['prioridad']}")

        if tarea["completada"]:
            print("   Estado: Completada")
        else:
            print("   Estado: Pendiente")

def menu_listar_tareas():
    print("\n--- Filtrar tareas ---")
    print("1. Todas")
    print("2. Pendientes")
    print("3. Completadas")
    print("4. Por categoría")

    opcion = input("Elige un filtro: ").strip()

    if opcion == "1":
        listar_tareas()
    elif opcion == "2":
        listar_tareas("pendientes")
    elif opcion == "3":
        listar_tareas("completadas")
    elif opcion == "4":
        categoria = input("Categoría (Personal, Estudio, Trabajo): ").strip()
        listar_tareas(categoria=categoria)
    else:
        print("Opción no válida.")
 


def menu():
    while True:
        print("\n--- Gestión de tareas ---")
        print("1. Crear tarea")
        print("2. Listar tareas")
        print("3. Modificar tarea")
        print("4. Marcar como completada")
        print("5. Reactivar tarea")
        print("6. Eliminar tarea")
        print("7. Buscar tareas")
        print("8. Mostrar estadísticas")
        print("9. Salir")
        
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            crear_tarea()
        elif opcion == "2":
            menu_listar_tareas()
        elif opcion == "3":
            modificar_tarea()
        elif opcion == "4":
            marcar_completada()
        elif opcion == "5":
            reactivar_tarea()
        elif opcion == "6":
            eliminar_tarea()
        elif opcion == "7":
            mostrar_resultados_busqueda()
        elif opcion == "8":
            mostrar_estadisticas(tareas)
        elif opcion == "9":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Elige un número del 1 al 9.")


if __name__ == "__main__":
    menu()