def dividir():
    num1 = int(input("Por favor ingrese el primer numero: "))
    num2 = int(input("Por favor ingrese el segundo numero: "))
    try:
        division = num1 / num2
    except ZeroDivisionError:
        print("La division entre 0 no esta definida") 
        division = 'indeterminado'   
    finally:
        return division  
    
def damePares():
    pares = []
    
    for i in range(1,51):
        if i %3 ==0:        #Error de codigo agrega los elementos impares, en vez de los pares
            pares.append(i)
    return pares


def main():                # Funcion main que imprima el resultado de damePares
    print(damePares())   
          

if __name__ == "__main__":
    # print(f"El resultado de la division es: {dividir()}")
    main()