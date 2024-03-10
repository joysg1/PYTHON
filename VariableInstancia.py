# Las variables de instancias pertenecen a cada instancia individual de 
# una clase, cada instancia tiene su copia de estas variables y los valores
# de las variables de instancias pueden ser diferentes entre diferentes 
# instancias de la misma clase

# Las variables de instancias se definen dentro del metodo init
# o en otros metodos de las clases utilizando self 

class MiClase:
    def __init__(self,valor):
        self.valor = valor
        
# Instanciar la clase, creando los objetos

objeto1 = MiClase(1)
objeto2 = MiClase(2)  


# Impresion del atributo valor de cada objeto

print(f"Valor del atributo valor del objeto1 = {objeto1.valor}") 
print(f"Valor del atributo valor del objeto2 = {objeto2.valor}")  
print("\n")
print("*"*80)   

# Diferencias entre variables de clase y variables de instancia

# -- Ambito de acceso

# Las variables de clase se pueden acceder tanto a traves de la clase
# como de las instancias, pero generalmente se acceden a traves de la clase

# Las variables de instancias solo se pueden acceder a traves de las
# instancias de las clases 

# Para compartir datos las variables de clase son compartidas por 
# todas las instancias de las clases, lo que significa que tienen el
# mismo valor para todas las instancias

# Las variables de instancia son unicas para cada instancia
# Lo que permite que cada instancia tenga sus propios valores independientes

# -- Como uso

# Las variables de clase se utilizan para almacenar valores que son comunes a
# todas las instancias de las clases, como constantes que se comparten entre 
# todas las instancias

# Las variables de instancias se utilizan para almacenar datos que son 
# especificos de cada instancia y pueden variar entre ellas

# En resumen las variables de clase son compartidas entre todas las instancias
# de una clase y se utilizan para almacenar datos comunes 

# Mientras que las variables de instancias son especificas de cada instancia
# y se utilizan para almacenar datos individuales 


# La eleccion entre una y otra depende de las necesidades especificas del
# programa 

