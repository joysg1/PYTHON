# Generar tabla de multiplicar de un numero solicitado al usuario
def tabla_multiplicar(num):
    print(f"Tabla de multiplicar del {num}")
    for i in range(1, 13):
        print(f"{num} x {i} = {num * i}")

num = int(input("Ingrese un numero: "))
tabla_multiplicar(num)
