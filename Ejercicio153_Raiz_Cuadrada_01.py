# Realiza un programa que calcule la raiz cuadrada de un numero sin usar la libreria math
def sqrt(num):
    """
    Calcula la raiz cuadrada de un numero sin usar la libreria math
    """
    raiz = num ** 0.5
    return raiz


num1= int(input("Introduce un numero: "))
# Imprime el resultado redondeado a 2 decimales
print("La raiz cuadrada de", num1, "es:", round(sqrt(num1), 2))

