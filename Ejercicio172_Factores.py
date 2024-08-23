#Programa que calcule los factores de un numero ingresado por el usuario
def factors(num):
    """
    This function takes a number as input and returns a list of its factors.
    """
    factor_list = []
    for i in range(1, num + 1):
        if num % i == 0:
            factor_list.append(i)
    return factor_list


numero = int(input("Ingrese un numero: "))
print(f"Los factores de {numero} son: {factors(numero)}")

