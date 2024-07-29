class Alumno():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def mostrar(self):
        print("Nombre: ", self.nombre)
        print("Nota: ", self.nota)
        
        
        
    def valoracion(self):
        if self.nota >= 61:
            print("Aprobado")
        else:
            print("Suspenso")
     
            
if __name__ == "__main__":
    alumno1 = Alumno("Juan", 75)
    alumno2 = Alumno("Ana", 60)
    alumno3 = Alumno("Pedro", 91)
    alumno1.mostrar()
    alumno1.valoracion()
    alumno2.mostrar()
    alumno2.valoracion()
    alumno3.mostrar()
    alumno3.valoracion()
    
    