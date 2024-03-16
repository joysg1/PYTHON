def multiplicar(num1, num2):
    '''
    
    Funcion que multiplica dos numeros
    Argumentos:
    numero1 (int)
    numero2 (int)
    Retorna la multiplicacion de los parametros dados
    
    
    >>> multiplicar(2,3)
    6
    >>> multiplicar(2,4)
    5
    >>> multiplicar(7,1)
    8
    
    '''
    
    return num1 * num2


# La seccion en donde se coloca los >>> permite realizar una prueba
# de la funcion, donde debajo se colca el resultado segun los parametros

# Para realizar el test debemos coloca el siguiente comando en la terminal:
# python -m doctest Test.py

# Cuando realizamos el test, si se encuentra un fallo en el este saldra
# tras ejecutar el comando anterior 



# Prueba de la funcion multiplicar

print(f"La multiplicacion de 4 x 4 es igual a = {multiplicar(4,4)}")
 
 
# Para ver la ayuda de la funcion ejecutamos en terminal lo siguiente:

# 0. python

# 1. import Test

# 2. help(Test.multiplicar) 