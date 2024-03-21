distancia = float(input("Por favor ingrese la distancia en metros: "))
tiempo = int(input("Por favor ingrese el tiempo en segundos: "))


try:
 velocidad = distancia / tiempo
except ZeroDivisionError:
    print("Ha ingresado un tiempo de 0s la operacion no puede llevarse a cabo") 
    velocidad = "Indeterminado"
    
print(f"Velocidad = {velocidad} m/s")
print("*"*80)