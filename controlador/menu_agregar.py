"""
AÑADIR ELEMENTOS - LIBROS, PELÍCULAS O MÚSICA
"""
import json
from pathlib import Path
from utils.terminal import limpiar_pantalla, mostrar_encabezado, mostrar_mensaje
from utils.generadores import generar_id

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
    """Menú para agregar nuevos elementos"""
    while True:
        limpiar_pantalla()
        mostrar_encabezado("AÑADIR ELEMENTO")
        
        print("1. Libro")
        print("2. Película")
        print("3. Música")
        print("4. Volver")
        
        opcion = input("\nSeleccione tipo (1-4): ").strip()
        
        if opcion == '4':
            return False
            
        tipos = {'1': 'libro', '2': 'película', '3': 'música'}
        if opcion in tipos:
            datos = cargar_datos()
            datos.append(crear_elemento(tipos[opcion]))
            guardar_datos(datos)
            mostrar_mensaje("¡Elemento añadido!", "éxito")
            input("Presione Enter...")

def crear_elemento(tipo):
    """Solicita datos y retorna un nuevo elemento"""
    limpiar_pantalla()
    mostrar_encabezado(f"NUEVO {tipo.upper()}")
    
    titulo = input("Título: ").strip()
    while not titulo:
        mostrar_mensaje("El título es obligatorio", "error")
        titulo = input("Título: ").strip()
    
    autor = input("Autor/Director/Artista: ").strip()
    genero = input("Género: ").strip()
    
    return {
        'id': generar_id(),
        'tipo': tipo,
        'titulo': titulo,
        'autor': autor,
        'genero': genero
    }