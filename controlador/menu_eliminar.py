"""
ELIMINAR ELEMENTOS - REMOVER DE LA COLECCIÓN
"""
import json
from pathlib import Path
from utils.terminal import limpiar_pantalla, mostrar_encabezado

RUTA_DATOS = Path(__file__).parent.parent / "datos/coleccion.json"

def cargar_datos():
    """Carga los datos desde JSON"""
    try:
        with open(RUTA_DATOS, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def guardar_datos(datos):
    """Guarda los datos en JSON"""
    with open(RUTA_DATOS, 'w', encoding='utf-8') as f:
        json.dump(datos, f, indent=2)

def mostrar():
    """Interfaz de eliminación"""
    datos = cargar_datos()
    limpiar_pantalla()
    mostrar_encabezado("ELIMINAR ELEMENTO")
    
    id_eliminar = input("Ingrese el ID del elemento a eliminar: ").strip()
    nuevos_datos = [item for item in datos if item['id'] != id_eliminar]
    
    if len(nuevos_datos) == len(datos):
        print("\nError: ID no encontrado")
    else:
        guardar_datos(nuevos_datos)
        print("\n¡Elemento eliminado exitosamente!")
    
    input("Presione Enter para continuar...")
    return False