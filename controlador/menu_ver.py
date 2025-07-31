import json
from pathlib import Path
from utils.terminal import limpiar_pantalla, mostrar_encabezado, mostrar_tabla, pausar

RUTA_DATOS = Path(__file__).parent.parent / "datos/coleccion.json"

def cargar_datos():
    try:
        with open(RUTA_DATOS, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def mostrar():
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
    
    pausar()
    return False