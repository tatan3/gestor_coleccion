"""
GESTIÓN DE ARCHIVOS - RESPALDOS Y CARGA DE DATOS
"""
import json
import shutil
from pathlib import Path
from datetime import datetime
from utils.terminal import limpiar_pantalla, mostrar_encabezado, mostrar_mensaje

RUTA_DATOS = Path(__file__).parent.parent / "datos/coleccion.json"
RUTA_RESPALDO = Path(__file__).parent.parent / "datos/respaldo.json"

def crear_respaldo():
    """Crea una copia de seguridad con timestamp"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    ruta_respaldo = RUTA_DATOS.parent / f"respaldo_{timestamp}.json"
    shutil.copy(RUTA_DATOS, ruta_respaldo)
    return ruta_respaldo

def mostrar():
    """Menú de gestión de archivos"""
    while True:
        limpiar_pantalla()
        mostrar_encabezado("GESTIÓN DE ARCHIVOS")
        
        print("1. Crear respaldo")
        print("2. Restaurar respaldo")
        print("3. Volver")
        
        opcion = input("\nSeleccione opción (1-3): ").strip()
        
        if opcion == '3':
            return False
            
        if opcion == '1':
            ruta = crear_respaldo()
            mostrar_mensaje(f"Respaldo creado: {ruta.name}", "éxito")
            input("Presione Enter...")
        
        elif opcion == '2':
            if RUTA_RESPALDO.exists():
                shutil.copy(RUTA_RESPALDO, RUTA_DATOS)
                mostrar_mensaje("Respaldo restaurado", "éxito")
            else:
                mostrar_mensaje("No existe respaldo", "error")
            input("Presione Enter...")