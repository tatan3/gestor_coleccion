from controlador.menu_agregar import mostrar as menu_agregar
from controlador.menu_ver import mostrar as menu_ver
from controlador.menu_buscar import mostrar as menu_buscar
from controlador.menu_editar import mostrar as menu_editar
from controlador.menu_eliminar import mostrar as menu_eliminar
from controlador.menu_categorias import mostrar as menu_categorias
from controlador.menu_archivos import mostrar as menu_archivos
from utils.terminal import mostrar_encabezado, pausar

def mostrar_menu_principal():
    mostrar_encabezado("GESTOR DE COLECCIÓN CULTURAL")
    
    print("1. Añadir elemento")
    print("2. Ver elementos")
    print("3. Buscar elementos")
    print("4. Editar elemento")
    print("5. Eliminar elemento")
    print("6. Filtrar por categoría")
    print("7. Gestionar archivos")
    print("8. Salir")
    
    opcion = input("\nSeleccione una opción (1-8): ").strip()
    
    acciones = {
        '1': menu_agregar,
        '2': menu_ver,
        '3': menu_buscar,
        '4': menu_editar,
        '5': menu_eliminar,
        '6': menu_categorias,
        '7': menu_archivos,
        '8': lambda: True
    }
    
    resultado = acciones.get(opcion, lambda: False)()
    if not resultado:
        pausar()
    return resultado