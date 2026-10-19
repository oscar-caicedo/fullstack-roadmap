def mostrar_estadisticas(tareas):
    total = len(tareas)
    
    if total == 0:
        print("Todavia no hay tareas para calcular estadisticas.")
        return 
    
    completadas = sum(1 for tarea in tareas if tarea["completada"])
    porcentaje = completadas / total *100
    
    pendientes_por_prioridad = {
        "Alta": 0,
        "Media": 0,
        "Baja": 0
    }
    
    tareas_por_categoria = {
        "Personal": 0,
        "Estudio": 0,
        "Trabajo": 0    
    }
    
    for tarea in tareas:
        tareas_por_categoria[tarea["categoria"]] += 1
        
        if not tarea["completada"]:
            pendientes_por_prioridad[tarea["prioridad"]] += 1
            
    print("\n--- Estadisticas ---")
    print(f"Total de tareas: {total}")
    print(f"Completadas: {completadas} ({porcentaje:.2f}%)")
    print(f"Pendientes: {total - completadas}")
    
    print("\nPendientes por prioridad:")
    for prioridad, cantidad in pendientes_por_prioridad.items():
        print(f"- {prioridad}: {cantidad}")
        
    print("\nTareas por categoria: ")
    for categoria, cantidad in tareas_por_categoria.items():
        print(f"- {categoria}: {cantidad}")
    