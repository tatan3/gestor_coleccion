import json
import shutil
from pathlib import Path
from datetime import datetime
from utils.terminal import limpiar_pantalla, mostrar_encabezado, pausar

RUTA_DATOS = Path(__file__).parent.parent / "datos/coleccion.json"
RUTA_RESPALDO = Path(__file__).parent.parent / "datos/respaldo.json"

def crear_respaldo():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    ruta_nueva = RUTA_DATOS.parent / f"respaldo_{timestamp}.json"
    shutil.copy(RUTA_DATOS, ruta_nueva)
    return ruta_nueva

def mostrar():
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
            print(f"\nRespaldo creado: {ruta.name}")
            pausar()
        
        elif opcion == '2':
            if RUTA_RESPALDO.exists():
                shutil.copy(RUTA_RESPALDO, RUTA_DATOS)
                print("\n¡Respaldo restaurado exitosamente!")
            else:
                print("\nError: No existe archivo de respaldo")
            pausar()