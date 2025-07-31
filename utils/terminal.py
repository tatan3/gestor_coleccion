"""
UTILIDADES DE TERMINAL - FUNCIONES BÁSICAS
"""
import os
import platform
from tabulate import tabulate

def limpiar_pantalla():
    """Limpia la pantalla según el SO"""
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def mostrar_encabezado(texto):
    """Muestra un encabezado centrado"""
    print("\n" + "=" * 50)
    print(f"{texto:^50}")
    print("=" * 50 + "\n")

def mostrar_tabla(datos, encabezados):
    """Muestra datos en formato de tabla"""
    print(tabulate(datos, headers=encabezados, tablefmt="grid"))