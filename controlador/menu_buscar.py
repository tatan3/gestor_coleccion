"""
BUSCAR ELEMENTOS - POR CRITERIOS
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
    """Interfaz de búsqueda"""
    datos = cargar_datos()
    
    while True:
        limpiar_pantalla()
        mostrar_encabezado("BUSCAR ELEMENTOS")
        
        print("1. Buscar por título")
        print("2. Buscar por autor")
        print("3. Buscar por género")
        print("4. Volver")
        
        opcion = input("\nSeleccione criterio (1-4): ").strip()
        
        if opcion == '4':
            return False
        
        criterios = {'1': 'titulo', '2': 'autor', '3': 'genero'}
        if opcion in criterios:
            termino = input(f"Ingrese {criterios[opcion]}: ").lower()
            resultados = [
                item for item in datos 
                if termino in item[criterios[opcion]].lower()
            ]
            
            if resultados:
                tabla = [[item['id'], item['tipo'], item['titulo']] for item in resultados]
                mostrar_tabla(tabla, ["ID", "Tipo", "Título"])
            else:
                print("\nNo se encontraron coincidencias.")
            
            input("\nPresione Enter para continuar...")