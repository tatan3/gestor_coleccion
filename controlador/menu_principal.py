"""
MENÚ PRINCIPAL - CENTRO DE NAVEGACIÓN
"""
from controlador import (
    menu_agregar, menu_ver, menu_buscar, 
    menu_editar, menu_eliminar, menu_categorias, 
    menu_archivos
)
from utils.terminal import mostrar_encabezado

def mostrar_menu_principal():
    """Muestra y dirige a los submenús"""
    mostrar_encabezado("GESTOR DE COLECCIÓN")
    
    print("1. Añadir elemento")
    print("2. Ver elementos")
    print("3. Buscar elementos")
    print("4. Editar elemento")
    print("5. Eliminar elemento")
    print("6. Filtrar por categoría")
    print("7. Gestionar archivos")
    print("8. Salir")
    
    opcion = input("\nSeleccione (1-8): ").strip()
    
    acciones = {
        '1': menu_agregar.mostrar,
        '2': menu_ver.mostrar,
        '3': menu_buscar.mostrar,
        '4': menu_editar.mostrar,
        '5': menu_eliminar.mostrar,
        '6': menu_categorias.mostrar,
        '7': menu_archivos.mostrar,
        '8': lambda: True  # Salir
    }
    
    return acciones.get(opcion, lambda: False)()