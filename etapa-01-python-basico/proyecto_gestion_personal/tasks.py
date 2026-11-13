"""Consultas y filtros para las tareas."""

import unicodedata


def _normalizar(texto):
    sin_acentos = "".join(
        caracter
        for caracter in unicodedata.normalize("NFD", texto.casefold())
        if unicodedata.category(caracter) != "Mn"
    )
    return sin_acentos.strip()


def buscar_tareas_por_palabra_clave(tareas, palabra):
    palabra = _normalizar(palabra)
    if not palabra:
        return []

    return [
        tarea
        for tarea in tareas
        if palabra in _normalizar(tarea["titulo"])
        or palabra in _normalizar(tarea["descripcion"])
    ]


def buscar_tarea_por_titulo(tareas, titulo_buscado):
    titulo_buscado = _normalizar(titulo_buscado)
    for tarea in tareas:
        if _normalizar(tarea["titulo"]) == titulo_buscado:
            return tarea
    return None


def filtrar_tareas(tareas, filtro="todas", categoria=None):
    if filtro == "pendientes":
        return [tarea for tarea in tareas if not tarea["completada"]]

    if filtro == "completadas":
        return [tarea for tarea in tareas if tarea["completada"]]

    if categoria is not None:
        categoria_buscada = _normalizar(categoria)
        return [
            tarea
            for tarea in tareas
            if _normalizar(tarea["categoria"]) == categoria_buscada
        ]

    return list(tareas)
