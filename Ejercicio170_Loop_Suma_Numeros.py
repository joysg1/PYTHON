# Programa que recibe un numero y realiza la sumatoria de su decremento hasta 0 mostrando el paso a paso
def sumatoria_decremento(numero):    
    resultado = 0
    print(f"Sumando decremento de {numero}")
    while numero > 0:
        resultado += numero
        print(f"{resultado - numero} + {numero} = {resultado}")
        numero -= 1
    print(f"El resultado final es: {resultado}")


numero = int(input("Ingrese un numero: "))
sumatoria_decremento(numero)



