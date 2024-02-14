def Suma(num1, num2):
    result = num1 + num2
    return result


numero1 = int(input("Por favor ingrese el primer numero: \n"))
numero2 = int(input("Por favor ingrese el segundo numero: \n"))

print("------------------------- \n")


resultado = Suma(numero1, numero2)
print(f"{numero1} + {numero2} = {resultado}\n")

