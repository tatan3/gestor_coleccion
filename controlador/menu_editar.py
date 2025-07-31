"""
EDITAR ELEMENTOS - MODIFICAR DATOS
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
    """Interfaz de edición"""
    datos = cargar_datos()
    limpiar_pantalla()
    mostrar_encabezado("EDITAR ELEMENTO")
    
    id_buscar = input("Ingrese el ID del elemento a editar: ").strip()
    elemento = next((item for item in datos if item['id'] == id_buscar), None)
    
    if not elemento:
        print("\nError: ID no encontrado")
        input("Presione Enter para continuar...")
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
        print("\n¡Cambios guardados exitosamente!")
    
    input("Presione Enter para continuar...")
    return False