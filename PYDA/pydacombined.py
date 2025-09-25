import pydawiki
import pydawolframalpha


def main():
    while True:
        print("\nMenú:")
        print("1. Ejecutar archivo 1 (Wolfram)")
        print("2. Ejecutar archivo 2 (Wiki)")
        print("3. Salir")

        opcion = input("Ingrese su opción: ")

        if opcion == "1":
           
            print("Ejecutando archivo 1 (Wolfram)...")
            pydawolframalpha.buscar_en_wolframalpha()
            
        elif opcion == "2":
            
            print("Ejecutando archivo 2 (Wiki)...")
            pydawiki.buscar_en_wikipedia()

        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    main()
