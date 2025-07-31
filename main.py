from controlador.menu_principal import mostrar_menu_principal
from utils.terminal import limpiar_pantalla

def main():
    while True:
        limpiar_pantalla()
        if mostrar_menu_principal():
            print("\n¡Programa finalizado!")
            break

if __name__ == "__main__":
    main()