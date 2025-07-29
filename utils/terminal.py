"""
INTERFAZ DE CONSOLA - MANEJA LA VISUALIZACIÓN
"""
import os
import platform
from tabulate import tabulate

def limpiar_pantalla():
    """Limpia la pantalla (Windows/Linux/macOS)"""
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def mostrar_encabezado(texto):
    """Muestra un encabezado formateado"""
    print("\n" + "=" * 50)
    print(f"{texto:^50}")  # Centrado
    print("=" * 50 + "\n")

def mostrar_mensaje(texto, tipo="info"):
    """Muestra mensajes con colores según tipo"""
    colores = {
        "éxito": "\033[92m",  # Verde
        "error": "\033[91m",   # Rojo
        "info": "\033[94m"     # Azul
    }
    print(f"{colores[tipo]}{texto}\033[0m")  # \033[0m resetea el color

def mostrar_tabla(datos, encabezados):
    """Muestra datos en formato de tabla"""
    print(tabulate(datos, headers=encabezados, tablefmt="grid"))