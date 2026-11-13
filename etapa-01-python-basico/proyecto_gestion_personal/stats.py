"""Resumen sencillo del estado de las tareas."""


def mostrar_estadisticas(tareas):
    total = len(tareas)
    if total == 0:
        print("\nTodavía no tienes tareas. Cuando agregues alguna, aquí verás tu resumen.")
        return

    completadas = sum(tarea["completada"] for tarea in tareas)
    pendientes = total - completadas
    porcentaje = completadas / total * 100
    pendientes_por_prioridad = {"Alta": 0, "Media": 0, "Baja": 0}
    tareas_por_categoria = {"Personal": 0, "Estudio": 0, "Trabajo": 0}

    for tarea in tareas:
        tareas_por_categoria[tarea["categoria"]] += 1
        if not tarea["completada"]:
            pendientes_por_prioridad[tarea["prioridad"]] += 1

    print("\n=== Tu resumen ===")
    print(f"Tareas en total: {total}")
    print(f"Completadas: {completadas} ({porcentaje:.1f} %)")
    print(f"Pendientes: {pendientes}")

    print("\nPendientes por prioridad:")
    for prioridad, cantidad in pendientes_por_prioridad.items():
        print(f"- {prioridad}: {cantidad}")

    print("\nTareas por categoría:")
    for categoria, cantidad in tareas_por_categoria.items():
        print(f"- {categoria}: {cantidad}")
