class Vehiculo():
    def __init__(self, marca,color):
        self.marca = marca
        self.color = color
    def __str__(self):
        return f"El vehiculo de marca : {self.marca} es de color : {self.color}"    


class Coche(Vehiculo):
    def __init__(self,marca,color,potencia,motor):
        Vehiculo.__init__(self,marca,color)
        self.potencia = potencia
        self.motor = motor   
    def __str__(self):
        return Vehiculo.__str__(self) + f" y tiene una potencia de {self.potencia} con un motor {self.motor}"
miVehiculo = Vehiculo("Seat","Verde")
miCoche = Coche("Toyota","Rojo",1000,"Diesel")

print(miVehiculo) 
print(miCoche)           