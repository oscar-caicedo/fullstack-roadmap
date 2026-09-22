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

#Gestion de tareas

from datetime import date

tarea = {
    "titulo": "titulo", 
    "descripcion": "descripcion",
    "categoria": "categoria",
    "fecha_limite": "fecha_limite", 
    "prioridad": "prioridad"
}

def crear_tareas(tarea):
    titulo = input("Agrega el titulo: ").strip().capitalize()
    descripcion = input("Agregue la descripcion: ").capitalize()
    categoria = ("Personal", "Estudio", "Trabajo")
    categoria = input("Agregue la categoria(Personal, Estudio, Trabajo): ").capitalize()
    fecha_limite = date(input("En que fecha inicio a programar: ", ))
    prioridad = input("Prioridad(Alta/Media/Baja): ").capitalize()

while True:
    print("===Gestion De Tareas===")
    print("1. Crear tareas")
    print("2. Listar tareas por filtros")
    print("3. Modificar datos de una tarea existente")
    print("4. Marcar tarea completada o reactivarla")
    print("5. Eliminar tareas")
    print("6. Busqueda por palabra clave")
    print("7. Salir")
    opcion = int(input(("Ingrese la opcion: ")))

    if opcion == "1":
        print(crear_tareas)
        print("Tarea creada")
        
    if opcion == 2:
        for tareas in tarea:
            print(tarea)
            
    if opcion == 3:
        for tareas in tarea:
            print(tarea)
            
        modificar = input("Ingrese el numero de la tarea a modificar")
        
        if modificar not in tareas:
            print ("Tarea no se ha encontrado")
        else:
                titulo = input("Titulo a modificar: ").strip().capitalize()
                descripcion = input("Agregue la descripcion a modificar: ").capitalize()
                categoria = input("Nueva categoria(Personal, Estudio, Trabajo): ".categoria).capitalize()
                fecha_limite = date(input("En que fecha inicio a programar: ", ))
                prioridad = input("Prioridad(Alta/Media/Baja): ").capitalize()
        



    

    
    
     