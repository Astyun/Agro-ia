"""
====================================================
Proyecto : Agro-IA
Autor    : Juan Ortiz
Versión  : 1.0
====================================================
"""

def mostrar_menu():
    print("\n" + "=" * 50)
    print("            AGRO-IA")
    print(" Sistema de Gestión Agrícola")
    print("=" * 50)
    print("1. Registrar cultivo")
    print("2. Registrar parcela")
    print("3. Registrar fertilización")
    print("4. Registrar cosecha")
    print("5. Ver registros")
    print("6. Salir")
    print("=" * 50)


def main():
    mostrar_menu()

    opcion = input("Seleccione una opción: ")

    print(f"\nHas seleccionado la opción {opcion}")


if __name__ == "__main__":
    main()
