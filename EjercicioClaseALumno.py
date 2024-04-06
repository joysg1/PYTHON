class Alumno():
    def __init__(self,nombre,cal):
        self.nombre = nombre
        self.cal = cal
    def __str__(self):
        return f"El alumno {self.nombre } ha obtenido {self.cal}" 
    def aprobado(self):
        if self.cal <5:
            False
        else:
            return True  
        
jose = Alumno("Jose",3)  
print(jose) 
aprobadoJose = jose.aprobado()
if aprobadoJose:  
    print("Esta aprobado") 
else:
    print("No esta aprobado")
    
print("\n")   
print("*"*80) 
print("\n")        

maria = Alumno("Maria",5)
print(maria)
aprobadoMaria = maria.aprobado()
if aprobadoMaria:  
    print("Esta aprobada") 
else:
    print("No esta aprobada")

