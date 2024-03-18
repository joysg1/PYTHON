
# Clase Padre

class Vehiculo:
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color
 
# Clase Coche hereda de Vehiculo
        
class Coche(Vehiculo):
    def __init__(self, marca, color, potencia, motor): #Constructor de la clase coche
        super().__init__(marca, color) #Constructor de la clase padre
        self.potencia = potencia
        self.motor = motor      
        
        
# Creacion de objeto de la clase Coche

miCoche = Coche('Toyota','Rojo',200,'Diesel') 

# Impresion de los atributos del objeto miCoche
print("-- ATRIBUTOS DEL OBJETO COCHE --- ")
print(f" MARCA: {miCoche.marca} - COLOR: {miCoche.color} - POTENCIA: {miCoche.potencia} - MOTOR: {miCoche.motor}") 
print("*"*80)
print("\n") 
    