def buscar_tareas_por_palabra_clave(tareas, palabra):
    palabra = palabra.casefold().strip()
    resultados = []
    
    for tarea in tareas:
        if (
            palabra in tarea["titulo"].casefold()
            or palabra in tarea["descripcion"].casefold()
        ):
            resultados.append(tarea)
            
    return resultados

def buscar_tarea_por_titulo(tareas, titulo_buscado):
    for tarea in tareas:
        if tarea["titulo"].casefold() == titulo_buscado.casefold():
            return tarea
    return None 

def filtrar_tareas(tareas, filtro="todas", categoria=None):
    if filtro == "pendientes":
        return [tarea for tarea in tareas if not tarea["completada"]]

    if filtro == "completadas":
        return [tarea for tarea in tareas if tarea["completada"]]

    if categoria is not None:
        return [
            tarea for tarea in tareas
            if tarea["categoria"].casefold() == categoria.casefold()
        ]

    return tareas