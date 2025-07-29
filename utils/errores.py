"""
MANEJO DE ERRORES - DECORADORES PARA CAPTURAR EXCEPCIONES
"""
from utils.terminal import mostrar_mensaje

def manejar_error(func):
    """Decorador para manejar errores genéricos"""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            mostrar_mensaje(f"Error: {str(e)}", "error")
            return False
    return wrapper