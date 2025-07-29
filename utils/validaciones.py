"""
VALIDACIONES - CHECKS PARA DATOS DE ENTRADA
"""
from utils.terminal import mostrar_mensaje

def validar_opcion(opcion, minimo, maximo):
    """Valida que una opción esté dentro de un rango"""
    if not opcion.isdigit():
        mostrar_mensaje("Debe ingresar un número", "error")
        return False
    if not minimo <= int(opcion) <= maximo:
        mostrar_mensaje(f"Opción fuera de rango ({minimo}-{maximo})", "error")
        return False
    return True