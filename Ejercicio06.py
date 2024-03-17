edad = 0

while edad <=0:
 edad = int(input('Por favor ingrese su edad: '))
if edad >=18:
     print(f"Usted es mayor de edad, edad introducida = {edad}")
elif edad <18:
    print(f"Usted no es mayor de edad, edad introducida = {edad}")