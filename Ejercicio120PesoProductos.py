peso_01 = 1.5
peso_02 = 1.7
peso_03 = 2.1

cantidad_01 = int(input("Ingrese la cantidad de producto 1  (peso 1.5 kg): "))
cantidad_02 = int(input("Ingrese la cantidad de producto 2  (peso 1.7 kg): "))
cantidad_03 = int(input("Ingrese la cantidad de producto 3  (peso 2.1 kg): "))

peso_enviado_01 = cantidad_01 * peso_01
peso_enviado_02 = cantidad_02 * peso_02
peso_enviado_03 = cantidad_03 * peso_03


print("El peso total del producto 1 es de: ", round(peso_enviado_01,2), "kg")
print("El peso total del producto 2 es de: ", round(peso_enviado_02,2), "kg")
print("El peso total del producto 3 es de: ", round(peso_enviado_03,2), "kg")
peso_total = peso_enviado_01 + peso_enviado_02 + peso_enviado_03
print("El peso total enviado es: ", round(peso_total,2), "kg")