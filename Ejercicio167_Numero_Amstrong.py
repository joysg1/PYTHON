# Solicitar al usuario un numero y determinar si es o no un numero de Amstrong
def is_armstrong_number(num):
  original_num = num
  sum = 0
  num_digits = len(str(num))

  while num > 0:
    digit = num % 10
    sum += digit ** num_digits
    num //= 10

  if sum == original_num:
    msj = "Es un numero de amstrong"
  else:
    msj = "No es un numero de amstrong"
  return msj
  
num = int(input("Ingrese un numero: "))
print(is_armstrong_number(num))

