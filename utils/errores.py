"""
MANEJO DE ERRORES - DECORADOR BÁSICO
"""
from utils.terminal import mostrar_encabezado

def manejar_error(func):
    """Decorador para capturar errores y mostrar mensaje"""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            mostrar_encabezado("ERROR")
            print(f"Ocurrió un error: {str(e)}")
            input("\nPresione Enter para continuar...")
            return False
    return wrapper