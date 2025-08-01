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
    
    while True:
        limpiar_pantalla()
        mostrar_encabezado("FILTRAR POR CATEGORÍA")
        
        print("1. Libros")
        print("2. Películas")
        print("3. Música")
        print("4. Volver")
        
        opcion = input("\nSeleccione categoría (1-4): ").strip()
        
        if opcion == '4':
            return False
        
        categorias = {'1': 'libro', '2': 'película', '3': 'música'}
        if opcion in categorias:
            elementos = [item for item in datos if item['tipo'] == categorias[opcion]]
            
            if elementos:
                tabla = [[item['id'], item['titulo'], item['autor']] for item in elementos]
                mostrar_tabla(tabla, ["ID", "Título", "Autor"])
            else:
                print(f"\nNo hay {categorias[opcion]}s en la colección")
            
            pausar()