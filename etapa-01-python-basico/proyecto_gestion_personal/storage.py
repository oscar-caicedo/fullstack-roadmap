from datetime import datetime
import json
from pathlib import Path

RUTA_ARCHIVO = Path(__file__).parent / "tareas.json"

#importar los archibos
def cargar_tareas():
    if not RUTA_ARCHIVO.exists():
        return []

    try:
        with RUTA_ARCHIVO.open("r", encoding="utf-8") as archivo:
            tareas = json.load(archivo)
    except json.JSONDecodeError as error:
        raise ValueError("El archivo tareas.json tiene contenido inválido.") from error 
            
    if not isinstance(tareas, list):
        raise ValueError("tareas.json debe contener una lista de tareas.")

    campos_texto = ("titulo", "descripcion", "categoria", "fecha", "prioridad")
    categorias_validas = {"Personal", "Estudio", "Trabajo"}
    prioridades_validas = {"Alta", "Media", "Baja"}

    for numero, tarea in enumerate(tareas, start=1):
        if not isinstance(tarea, dict):
            raise ValueError(f"La tarea {numero} debe ser un objeto.")

        if any(campo not in tarea for campo in (*campos_texto, "completada")):
            raise ValueError(f"Faltan campos en la tarea {numero}.")

        if any(not isinstance(tarea[campo], str) for campo in campos_texto):
            raise ValueError(f"Hay campos de texto inválidos en la tarea {numero}.")

        if not isinstance(tarea["completada"], bool):
            raise ValueError(f"El estado de la tarea {numero} debe ser verdadero o falso.")

        if tarea["categoria"] not in categorias_validas:
            raise ValueError(f"La categoría de la tarea {numero} no es válida.")

        if tarea["prioridad"] not in prioridades_validas:
            raise ValueError(f"La prioridad de la tarea {numero} no es válida.")

        try:
            datetime.strptime(tarea["fecha"], "%Y-%m-%d")
        except ValueError as error:
            raise ValueError(f"La fecha de la tarea {numero} no es válida.") from error

    return tareas    


def guardar_tareas(tareas):
    with RUTA_ARCHIVO.open("w", encoding="utf-8") as archivo:
        json.dump(tareas, archivo, ensure_ascii=False, indent=4)