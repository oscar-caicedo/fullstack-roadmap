"""Lectura y escritura del archivo local de tareas."""

import json
import tempfile
from datetime import datetime
from pathlib import Path

RUTA_ARCHIVO = Path(__file__).parent / "tareas.json"
CATEGORIAS_VALIDAS = {"Personal", "Estudio", "Trabajo"}
PRIORIDADES_VALIDAS = {"Alta", "Media", "Baja"}
CAMPOS_TEXTO = ("titulo", "descripcion", "categoria", "fecha", "prioridad")


def cargar_tareas():
    if not RUTA_ARCHIVO.exists():
        return []

    try:
        with RUTA_ARCHIVO.open("r", encoding="utf-8") as archivo:
            tareas = json.load(archivo)
    except json.JSONDecodeError as error:
        raise ValueError("El archivo tareas.json contiene datos que no son JSON válido.") from error

    if not isinstance(tareas, list):
        raise ValueError("El archivo tareas.json debe contener una lista de tareas.")

    for numero, tarea in enumerate(tareas, start=1):
        if not isinstance(tarea, dict):
            raise ValueError(f"La tarea {numero} debe ser un objeto.")
        if any(campo not in tarea for campo in (*CAMPOS_TEXTO, "completada")):
            raise ValueError(f"A la tarea {numero} le faltan campos obligatorios.")
        if any(
            not isinstance(tarea[campo], str) or not tarea[campo].strip()
            for campo in CAMPOS_TEXTO
        ):
            raise ValueError(f"La tarea {numero} contiene un campo de texto vacío o inválido.")
        if not isinstance(tarea["completada"], bool):
            raise ValueError(f"El estado de la tarea {numero} debe ser verdadero o falso.")
        if tarea["categoria"] not in CATEGORIAS_VALIDAS:
            raise ValueError(f"La categoría de la tarea {numero} no es válida.")
        if tarea["prioridad"] not in PRIORIDADES_VALIDAS:
            raise ValueError(f"La prioridad de la tarea {numero} no es válida.")

        try:
            fecha = datetime.strptime(tarea["fecha"], "%Y-%m-%d")
        except ValueError as error:
            raise ValueError(f"La fecha de la tarea {numero} no es válida.") from error
        if fecha.strftime("%Y-%m-%d") != tarea["fecha"]:
            raise ValueError(f"La fecha de la tarea {numero} debe usar el formato AAAA-MM-DD.")

    return tareas


def guardar_tareas(tareas):
    ruta_temporal = None
    try:
        with tempfile.NamedTemporaryFile(
            "w",
            encoding="utf-8",
            dir=RUTA_ARCHIVO.parent,
            delete=False,
        ) as archivo:
            ruta_temporal = Path(archivo.name)
            json.dump(tareas, archivo, ensure_ascii=False, indent=4)
            archivo.write("\n")
        ruta_temporal.replace(RUTA_ARCHIVO)
    finally:
        if ruta_temporal is not None:
            try:
                ruta_temporal.unlink()
            except FileNotFoundError:
                pass
