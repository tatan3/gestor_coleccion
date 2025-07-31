import os
import platform
from tabulate import tabulate

def limpiar_pantalla():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def mostrar_encabezado(texto):
    print("\n" + "=" * 50)
    print(f"{texto:^50}")
    print("=" * 50 + "\n")

def mostrar_tabla(datos, encabezados):
    print(tabulate(datos, headers=encabezados, tablefmt="grid"))

def pausar():
    input("\nPresione Enter para continuar...")