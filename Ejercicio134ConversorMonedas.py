DOLAREURO = 0.92


def cambiarDolares(dolares):
    euros = dolares * DOLAREURO
    return euros


def cambiarEuros(euros):
    dolares = euros / DOLAREURO
    return dolares


def solicitarCantidad(tipo):
    cantidad = float(input(f"Monto de {tipo} a cambiar = "))
    return cantidad



menu = """
      Cambio de moneda
Selecciona una opción:
1. Dolares a euros
2. Euros a dolares
3. Salir
"""


if __name__ == "__main__":
    while True:
        print(menu)
        opcion = input("Ingresa una opción: ")
        if opcion == "1":
            cantidad = solicitarCantidad("dolares")
            euros = round(cambiarDolares(cantidad),2)
            print(f"{cantidad} dolares = {euros} euros")
        elif opcion == "2":
            cantidad = solicitarCantidad("euros")
            dolares = round(cambiarEuros(cantidad),2)
            print(f"{cantidad} euros = {dolares} dolares")
            
        elif opcion == "3":
            break
        else:
            print("Opción inválida")


       