# Intercambio de valores entre dos variables sin usar variable temporal
a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
print("-"*80)
print("Valor original de a: ",a)
print("Valor original de b: ", b)
a, b = b, a
print("-"*80)
print("Valor nuevo de a: ", a)
print("Valor nuevo de b: ", b)


