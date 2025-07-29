"""
ELIMINAR ELEMENTOS - BORRA ELEMENTOS POR ID
"""
import json
from pathlib import Path
from utils.terminal import limpiar_pantalla, mostrar_encabezado, mostrar_mensaje

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
    """Menú de eliminación"""
    datos = cargar_datos()
    if not datos:
        print("\nNo hay elementos para eliminar")
        input("Presione Enter...")
        return False
    
    limpiar_pantalla()
    mostrar_encabezado("ELIMINAR ELEMENTO")
    
    id_eliminar = input("Ingrese ID del elemento: ").strip()
    nuevos_datos = [item for item in datos if item['id'] != id_eliminar]
    
    if len(nuevos_datos) == len(datos):
        mostrar_mensaje("ID no encontrado", "error")
    else:
        guardar_datos(nuevos_datos)
        mostrar_mensaje("¡Elemento eliminado!", "éxito")
    
    input("Presione Enter...")
    return False