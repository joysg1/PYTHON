# Creacion de la clase hucha

class Hucha:
    def __init__(self, importe_inicial=0): #metodo constructor
        self.__importe = importe_inicial   #el atributo importe es privado, por ello se coloca el doble guion bajo
    def obtener_importe(self):
        return self.__importe
    def ingresar(self, cantidad):
        if cantidad >0:
            self.__importe = self.__importe + cantidad   
        else:
            print("La cantidad ingresada debe ser mayor que 0")
    def sacar(self, cantidad):
        if cantidad >0 and cantidad <= self.__importe:
            self.__importe = self.__importe - cantidad
        else:
            print("La cantidad ingresada debe ser mayor que 0 y no puede exceder el importe actual")   
    def mostrar_importe(self):
        print(f"El importe total en la hucha es: {self.__importe}")  
        
# Creacion de una instancia de la clase 

mi_hucha = Hucha(100)

# Uso de metodos para interactuar con la hucha

mi_hucha.ingresar(50)
print(mi_hucha.mostrar_importe())
mi_hucha.sacar(100)
print(mi_hucha.mostrar_importe())

# Tratar de acceder al atributo importe 


# print(mi_hucha.__importe)
    
        
# No es posible el acceso dado que el atributo esta como privado
# y debe accederse por un metodo de la clase no directamente


# Mostrar importe en la hucha como cadena 

print(mi_hucha.obtener_importe())


             
                     