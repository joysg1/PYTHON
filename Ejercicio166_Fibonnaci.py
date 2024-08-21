# Generar la secuencia de Fibonnaci de un numero dado por el usuario
def fibonacci(n):
  a, b = 0, 1
  sequence = []
  for i in range(n):
    sequence.append(a)
    a, b = b, a + b
  return sequence


num = int(input("Ingrese un numero: "))
print(fibonacci(num))
