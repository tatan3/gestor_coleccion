"""
EDITAR ELEMENTOS - MODIFICA CAMPOS EXISTENTES
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
    """Menú de edición"""
    datos = cargar_datos()
    if not datos:
        print("\nNo hay elementos para editar")
        input("Presione Enter...")
        return False
    
    limpiar_pantalla()
    mostrar_encabezado("EDITAR ELEMENTO")
    
    id_editar = input("Ingrese ID del elemento: ").strip()
    elemento = next((item for item in datos if item['id'] == id_editar), None)
    
    if not elemento:
        mostrar_mensaje("ID no encontrado", "error")
        input("Presione Enter...")
        return False
    
    print(f"\nEditando: {elemento['titulo']}")
    print("1. Título")
    print("2. Autor")
    print("3. Género")
    print("4. Cancelar")
    
    opcion = input("\nSeleccione campo a editar (1-4): ").strip()
    
    if opcion == '4':
        return False
    
    campos = {'1': 'titulo', '2': 'autor', '3': 'genero'}
    if opcion in campos:
        nuevo_valor = input(f"Nuevo {campos[opcion]}: ").strip()
        elemento[campos[opcion]] = nuevo_valor
        guardar_datos(datos)
        mostrar_mensaje("¡Cambios guardados!", "éxito")
    
    input("Presione Enter...")
    return False