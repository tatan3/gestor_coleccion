import json
from pathlib import Path
from utils.terminal import limpiar_pantalla, mostrar_encabezado, pausar

RUTA_DATOS = Path(__file__).parent.parent / "datos/coleccion.json"

def cargar_datos():
    try:
        with open(RUTA_DATOS, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def guardar_datos(datos):
    with open(RUTA_DATOS, 'w', encoding='utf-8') as f:
        json.dump(datos, f, indent=2)

def mostrar():
    datos = cargar_datos()
    limpiar_pantalla()
    mostrar_encabezado("EDITAR ELEMENTO")
    
    id_buscar = input("Ingrese el ID del elemento a editar: ").strip()
    elemento = next((item for item in datos if item['id'] == id_buscar), None)
    
    if not elemento:
        print("\nError: ID no encontrado")
        pausar()
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
        pausar()
    
    return False