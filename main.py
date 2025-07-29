"""
ENTRADA PRINCIPAL - COORDINA TODOS LOS MÓDULOS
"""
from controlador.menu_principal import mostrar_menu_principal
from utils.terminal import limpiar_pantalla, mostrar_mensaje
from utils.errores import manejar_error

@manejar_error
def main():
    """Bucle principal que maneja el flujo de la aplicación"""
    while True:
        limpiar_pantalla()
        if mostrar_menu_principal():  # Retorna True al salir
            mostrar_mensaje("¡Programa finalizado!", "éxito")
            break

if __name__ == "__main__":
    main()