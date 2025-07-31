"""
VALIDACIONES - CHECKS BÁSICOS
"""
def validar_opcion(opcion, minimo, maximo):
    """Valida que una opción esté en rango numérico"""
    if not opcion.isdigit():
        print("\nError: Debe ingresar un número")
        return False
    if not minimo <= int(opcion) <= maximo:
        print(f"\nError: Opción debe estar entre {minimo} y {maximo}")
        return False
    return True