from utils.terminal import mostrar_encabezado, pausar

def manejar_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            mostrar_encabezado("ERROR")
            print(f"Ocurrió un error: {str(e)}")
            pausar()
            return False
    return wrapper