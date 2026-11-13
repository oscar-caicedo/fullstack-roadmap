"""Menú de consola para organizar tareas personales."""

from datetime import datetime

from stats import mostrar_estadisticas
from storage import cargar_tareas, guardar_tareas
from tasks import (
    buscar_tarea_por_titulo,
    buscar_tareas_por_palabra_clave,
    filtrar_tareas,
)

CATEGORIAS = ("Personal", "Estudio", "Trabajo")
PRIORIDADES = ("Alta", "Media", "Baja")


def pedir_texto_no_vacio(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print("Escribe algo para continuar; este campo no puede quedar vacío.")


def pedir_opcion_valida(mensaje, opciones):
    opciones_por_nombre = {opcion.casefold(): opcion for opcion in opciones}
    opciones_texto = ", ".join(opciones)

    while True:
        respuesta = input(f"{mensaje} ({opciones_texto}): ").strip().casefold()
        if respuesta in opciones_por_nombre:
            return opciones_por_nombre[respuesta]
        print(f"Elige una de estas opciones: {opciones_texto}.")


def pedir_fecha_valida(mensaje):
    while True:
        fecha = input(f"{mensaje} (AAAA-MM-DD): ").strip()
        try:
            fecha_valida = datetime.strptime(fecha, "%Y-%m-%d")
        except ValueError:
            print("Esa fecha no parece válida. Prueba, por ejemplo, 2026-10-16.")
            continue

        if fecha_valida.strftime("%Y-%m-%d") == fecha:
            return fecha
        print("Usa el formato AAAA-MM-DD, por ejemplo, 2026-10-16.")


def pedir_confirmacion(mensaje):
    while True:
        respuesta = input(f"{mensaje} (s/n): ").strip().casefold()
        if respuesta in ("s", "si", "sí"):
            return True
        if respuesta in ("n", "no"):
            return False
        print("Responde «s» para sí o «n» para no.")


def mostrar_tareas(lista_tareas):
    if not lista_tareas:
        print("No hay tareas que coincidan. ¡Todo despejado por aquí!")
        return

    for indice, tarea in enumerate(lista_tareas, start=1):
        estado = "Completada" if tarea["completada"] else "Pendiente"
        print(f"\n{indice}. {tarea['titulo']} — {estado}")
        print(f"   Descripción: {tarea['descripcion']}")
        print(
            f"   Categoría: {tarea['categoria']} | "
            f"Prioridad: {tarea['prioridad']}"
        )
        print(f"   Fecha límite: {tarea['fecha']}")


def crear_tarea(tareas):
    print("\nVamos a agregar una tarea. Puedes cambiarla más adelante.")
    tarea = {
        "titulo": pedir_texto_no_vacio("¿Qué tienes que hacer? "),
        "descripcion": pedir_texto_no_vacio("Agrega un poco de contexto: "),
        "categoria": pedir_opcion_valida("¿En qué categoría va?", CATEGORIAS),
        "fecha": pedir_fecha_valida("¿Para qué día?"),
        "prioridad": pedir_opcion_valida("¿Qué prioridad tiene?", PRIORIDADES),
        "completada": False,
    }
    tareas.append(tarea)
    guardar_tareas(tareas)
    print(f"¡Listo! «{tarea['titulo']}» ya está en tu lista.")


def listar_tareas(tareas, filtro="todas", categoria=None):
    mostrar_tareas(filtrar_tareas(tareas, filtro, categoria))


def seleccionar_tarea(tareas, mensaje):
    titulo = input(f"{mensaje} (Enter para cancelar): ").strip()
    if not titulo:
        print("De acuerdo, no hice cambios.")
        return None

    tarea = buscar_tarea_por_titulo(tareas, titulo)
    if tarea is None:
        print(f"No encontré una tarea llamada «{titulo}». Revisa el título e inténtalo.")
    return tarea


def pedir_campo_actualizable(mensaje, valor_actual, opciones=None, es_fecha=False):
    while True:
        valor = input(f"{mensaje} [{valor_actual}]: ").strip()
        if not valor:
            return valor_actual

        if opciones is not None:
            opciones_por_nombre = {opcion.casefold(): opcion for opcion in opciones}
            opcion = opciones_por_nombre.get(valor.casefold())
            if opcion is not None:
                return opcion
            print(f"Elige una de estas opciones: {', '.join(opciones)}.")
        elif es_fecha:
            try:
                fecha_valida = datetime.strptime(valor, "%Y-%m-%d")
            except ValueError:
                print("Usa una fecha válida con el formato AAAA-MM-DD.")
                continue
            if fecha_valida.strftime("%Y-%m-%d") == valor:
                return valor
            print("Usa una fecha con el formato AAAA-MM-DD.")
        else:
            return valor


def modificar_tarea(tareas):
    tarea = seleccionar_tarea(tareas, "¿Qué tarea quieres actualizar?")
    if tarea is None:
        return

    print("Puedes dejar un campo vacío para conservarlo como está.")
    tarea["titulo"] = pedir_campo_actualizable("Título", tarea["titulo"])
    tarea["descripcion"] = pedir_campo_actualizable(
        "Descripción", tarea["descripcion"]
    )
    tarea["categoria"] = pedir_campo_actualizable(
        "Categoría", tarea["categoria"], opciones=CATEGORIAS
    )
    tarea["fecha"] = pedir_campo_actualizable(
        "Fecha límite (AAAA-MM-DD)", tarea["fecha"], es_fecha=True
    )
    tarea["prioridad"] = pedir_campo_actualizable(
        "Prioridad", tarea["prioridad"], opciones=PRIORIDADES
    )
    guardar_tareas(tareas)
    print(f"Actualicé «{tarea['titulo']}».")


def cambiar_estado_tarea(tareas, completada):
    accion = "completar" if completada else "reactivar"
    tarea = seleccionar_tarea(tareas, f"¿Qué tarea quieres {accion}?")
    if tarea is None:
        return
    if tarea["completada"] == completada:
        estado = "ya está completada" if completada else "ya está pendiente"
        print(f"«{tarea['titulo']}» {estado}.")
        return

    tarea["completada"] = completada
    guardar_tareas(tareas)
    mensaje = "¡Bien hecho! Tarea completada." if completada else "La tarea volvió a pendientes."
    print(f"{mensaje} ({tarea['titulo']})")


def eliminar_tarea(tareas):
    tarea = seleccionar_tarea(tareas, "¿Qué tarea quieres eliminar?")
    if tarea is None:
        return
    if not pedir_confirmacion(f"¿Seguro que quieres eliminar «{tarea['titulo']}»?"):
        print("No la eliminé.")
        return

    tareas.remove(tarea)
    guardar_tareas(tareas)
    print(f"Eliminé «{tarea['titulo']}».")


def buscar_tareas(tareas):
    palabra = input("¿Qué palabra quieres buscar? (Enter para cancelar): ").strip()
    if not palabra:
        print("Búsqueda cancelada.")
        return
    mostrar_tareas(buscar_tareas_por_palabra_clave(tareas, palabra))


def menu_listar_tareas(tareas):
    print("\n¿Cómo quieres ver tus tareas?")
    print("1. Todas")
    print("2. Solo pendientes")
    print("3. Solo completadas")
    print("4. Por categoría")
    opcion = input("Elige una opción (1-4): ").strip()

    if opcion == "1":
        listar_tareas(tareas)
    elif opcion == "2":
        listar_tareas(tareas, "pendientes")
    elif opcion == "3":
        listar_tareas(tareas, "completadas")
    elif opcion == "4":
        categoria = pedir_opcion_valida("¿Qué categoría?", CATEGORIAS)
        listar_tareas(tareas, categoria=categoria)
    else:
        print("Esa opción no está en el menú. Elige un número del 1 al 4.")


def menu(tareas):
    opciones = {
        "1": lambda: crear_tarea(tareas),
        "2": lambda: menu_listar_tareas(tareas),
        "3": lambda: modificar_tarea(tareas),
        "4": lambda: cambiar_estado_tarea(tareas, True),
        "5": lambda: cambiar_estado_tarea(tareas, False),
        "6": lambda: eliminar_tarea(tareas),
        "7": lambda: buscar_tareas(tareas),
        "8": lambda: mostrar_estadisticas(tareas),
    }

    while True:
        print("\n=== Tu lista de tareas ===")
        print("1. Agregar una tarea")
        print("2. Ver tareas")
        print("3. Actualizar una tarea")
        print("4. Marcar como completada")
        print("5. Volver a pendientes")
        print("6. Eliminar una tarea")
        print("7. Buscar")
        print("8. Ver resumen")
        print("9. Salir")
        opcion = input("¿Qué te gustaría hacer? ").strip()

        if opcion == "9":
            print("¡Hasta luego! Tus tareas quedan guardadas.")
            return
        accion = opciones.get(opcion)
        if accion is None:
            print("No reconocí esa opción. Elige un número del 1 al 9.")
            continue
        accion()


def main():
    try:
        tareas = cargar_tareas()
    except (OSError, ValueError) as error:
        print(f"No pude abrir tus tareas: {error}")
        raise SystemExit(1) from error

    try:
        menu(tareas)
    except OSError as error:
        print(f"No pude guardar tus cambios: {error}")
        raise SystemExit(1) from error


if __name__ == "__main__":
    main()
