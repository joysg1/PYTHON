def sumar(num1, num2):
    return num1 + num2


def restar(num1, num2):
    return num1 - num2


def multi(num1, num2):
    return num1 * num2


def div(num1,num2):
    try:
     resultado = num1/num2
    except ZeroDivisionError:
     resultado = "indeterminado"
    finally:
      return resultado
# Prueba de ejecucion en el propio archivo  
  
if __name__=='__main__':
    print(sumar(4,6))  
    