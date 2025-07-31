"""
VER ELEMENTOS - LISTA COMPLETA
"""
import json
from pathlib import Path
from utils.terminal import limpiar_pantalla, mostrar_encabezado, mostrar_tabla

RUTA_DATOS = Path(__file__).parent.parent / "datos/coleccion.json"

def cargar_datos():
    """Carga los datos desde JSON"""
    try:
        with open(RUTA_DATOS, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def mostrar():
    """Muestra todos los elementos en tabla"""
    datos = cargar_datos()
    limpiar_pantalla()
    mostrar_encabezado("LISTA DE ELEMENTOS")
    
    if not datos:
        print("No hay elementos para mostrar.")
    else:
        tabla = []
        for item in datos:
            tabla.append([
                item['id'],
                item['tipo'],
                item['titulo'],
                item['autor'],
                item.get('genero', 'N/A')
            ])
        mostrar_tabla(tabla, ["ID", "Tipo", "Título", "Autor", "Género"])
    
    input("\nPresione Enter para continuar...")
    return False