from utils.terminal import pausar

def validar_opcion(opcion, minimo, maximo):
    if not opcion.isdigit():
        print("\nError: Debe ingresar un número")
        pausar()
        return False
    if not minimo <= int(opcion) <= maximo:
        print(f"\nError: Opción debe estar entre {minimo} y {maximo}")
        pausar()
        return False
    return True