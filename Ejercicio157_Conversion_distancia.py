# Programa con menu para convertir de kilometros a millas y viceverza
def km_millas():
    km = float(input("Ingrese la cantidad de kilómetros: "))
    millas = km * 0.62137
    # Que la impresion de las millas sea a 3 decimales
    millas = round(millas, 3)
    print(f"{km} kilómetros equivalen a {millas} millas.")

def millas_km():
    millas = float(input("Ingrese la cantidad de millas: "))
    km = millas / 0.62137
    # Que la impresion de los kilometros sea a 3 decimales
    km = round(km, 3)
    print(f"{millas} millas equivalen a {km} kilómetros.")

# Menu para elegir que opcion de conversion usar
def menu():
    print("-"*80)
    print("1. Convertir de kilómetros a millas")
    print("2. Convertir de millas a kilómetros")
    print("-"*80)
    opcion = int(input("Ingrese su opción: "))
    if opcion == 1:
        km_millas()
    elif opcion == 2:
        millas_km()
    else:
        print("Opción inválida.")
    print("\n")

# Llamada a la funcion menu
menu()


