"""
AÑADIR ELEMENTOS - LIBROS, PELÍCULAS O MÚSICA
"""
import json
from pathlib import Path
from utils.generadores import generar_id
from utils.terminal import limpiar_pantalla, mostrar_encabezado

RUTA_DATOS = Path(__file__).parent.parent / "datos/coleccion.json"

def cargar_datos():
    """Carga los datos existentes desde JSON"""
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
    """Interfaz para agregar nuevos elementos"""
    datos = cargar_datos()
    
    limpiar_pantalla()
    mostrar_encabezado("AÑADIR NUEVO ELEMENTO")
    
    print("1. Libro")
    print("2. Película")
    print("3. Música")
    print("4. Volver")
    
    opcion = input("\nSeleccione tipo (1-4): ").strip()
    
    if opcion == '4':
        return False
    
    tipos = {'1': 'libro', '2': 'película', '3': 'música'}
    if opcion in tipos:
        tipo = tipos[opcion]
        titulo = input("Título: ").strip()
        autor = input("Autor/Director/Artista: ").strip()
        genero = input("Género: ").strip()
        
        nuevo_elemento = {
            'id': generar_id(),
            'tipo': tipo,
            'titulo': titulo,
            'autor': autor,
            'genero': genero
        }
        
        datos.append(nuevo_elemento)
        guardar_datos(datos)
        print(f"\n¡{tipo.capitalize()} agregado con éxito! ID: {nuevo_elemento['id']}")
        input("Presione Enter para continuar...")
    
    return False