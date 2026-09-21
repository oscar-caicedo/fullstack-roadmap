tareas = []
siguiente_id = 1

def mostrar_menu():
    while True:
        
        print("\n=== GESTION DE TAREAS ===")
        print("1. Agregar Tarea")
        print("2. Listar Tareas")
        print("3. Completar Tareas")
        print("4. Eliminar Tareas")
        print("5. Filtrar Tareas")
        print("6. Salir")
        
def buscar_tarea_por_id(id_tarea):
    for tarea in tareas:
        if tarea["id"] == id_tarea:
            return tarea
    return None
    
def agregar_tarea():
    global siguiente_id
    
    titulo = input("Titulo de la tarea: ").strip()
    if not titulo:
        print("El titulo no puede estar vacio")
        return
    
    prioridad = input("Prioridad (Alta/Media/Baja): ").strip().title()
    if prioridad not in ["Alta", "Media", "Baja"]:
        print("Prioridad inválida. Usa Alta, Media o Baja.")
        return
    
    tarea = {
        "id": siguiente_id,
        "titulo": titulo,
        "prioridad": prioridad,
        "estado": "Pendiente"
    }
    
    tareas.append(tarea)
    print(f"Tarea '{titulo}' agregada correctamente.")
    siguiente_id += 1
    
def listar_tareas():
    if not tareas:
        print("No hay tareas registradas.")
        return
    for tarea in tareas:
        if tarea["estado"] == "Pendiente":
            estado_motrar = "[ ]"
        else:
            estado_mostrar = "[X]"

        print(f"{estado_mostrar} ID {tarea['id']}")

def completar_tareas():
    id_tarea = int(input("Ingrese el ID de la tarea: "))
    
    tarea = buscar_tarea_por_id(id_tarea)
    for tarea in tareas:
        if tarea["id"] == id_tarea:
            tarea["estado"] = "Completado"
        else:
            print("Tarea con ID inexistente")
            return            
    
def eliminar_tareas():
    id_tarea = int(input("Ingrese el ID de la tarea a eliminar: "))
    
    for tarea in tareas:
        if tarea["id"] == id_tarea:
            tareas.remove(tarea)
            return

def filtrar_tareas():
    tipo = input("Filtrar tarea por estado o prioridad").lower()
        
    if tipo == "estado":
        estado = input("Ingrese estado(Pendiente/Completada): ").title()
        for tarea in tareas:
            if tarea["estado"] == estado:
                print(tarea)
    elif tipo == "prioridad":
        prioridad = input("Ingrese prioridad(Alta/Media/Baja)")
        for tarea in tareas:
            if tarea["prioridad"]:
                print(tarea)
                
                
while True:
    mostrar_menu()
    opcion = input("Elige una opcion:")
    
    if opcion == "1":
        agregar_tarea()
    elif opcion == "2":
        listar_tareas()
    elif opcion == "3":
        completar_tareas()
    elif opcion == "4":
        eliminar_tareas()
    elif opcion == "5":
        filtrar_tareas()
    elif opcion == "6":
        break