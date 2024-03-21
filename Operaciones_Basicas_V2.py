def sumar(num1, num2):
    return num1 + num2


def restar(num1, num2):
    return num1 - num2


def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    try:
     return num1 / num2
    except ZeroDivisionError:
       return "Indeterminado"
       
          



a = int(input("Por favor ingrese el 1er numero: "))
b = int(input("Por favor ingrese el 2do numero: "))
print("\n")
print("*"*80)

opcion = 0
repetir = "s"
contador = 0

while repetir == "s" or repetir =="S":
 
 while opcion <=0 or opcion > 4:
  print("1. Suma")
  print("2. Resta")
  print("3. Multiplicacion")
  print("4. Dividir")
  opcion = int(input("Por favor ingrese que opcion desea realizar (1-4): "))
  if opcion == 1:
     resultado_sumar = sumar(a,b)
     print(f"{a} + {b} = {resultado_sumar}")
  elif opcion ==2:
     resultado_restar = restar(a,b)
     print(f"{a} - {b} = {resultado_restar}")
  elif opcion ==3:
    resultado_multiplicar = multiplicar(a,b)
    print(f"{a} * {b} = {resultado_multiplicar}")
  elif opcion ==4:
    resultado_dividir = dividir(a,b) 
    print(f"{a} / {b} = {resultado_dividir}") 
  contador = contador + 1
  print(f"Veces que el programa se ha ejecutado = {contador}")
  print("\n")
  opcion = 0
  repetir = str(input("Desea repetir la ejecucion del programa (s/n): "))
  if repetir =="n" or repetir =="N":
   break
  print("\n")
  print("*"*80)

"""
if opcion == 1:
 resultado_sumar = sumar(a,b)
 print(f"{a} + {b} = {resultado_sumar}")
elif opcion ==2:
 resultado_restar = restar(a,b)
 print(f"{a} - {b} = {resultado_restar}")
elif opcion ==3:
 resultado_multiplicar = multiplicar(a,b)
 print(f"{a} * {b} = {resultado_multiplicar}")
elif opcion ==4:
  resultado_dividir = dividir(a,b) 
  print(f"{a} / {b} = {resultado_dividir}")
"""







