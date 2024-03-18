def bis(a):
    if a%4 == 0 and a%100 !=0:
        return True
    elif a%100 ==0 and a%400 ==0:
        return True
    else:
        return False
    
a = 0   
while a <=0:
 a = int(input("Por favor ingrese un año: "))
 
 
result = bis(a) 

print(f"El {a} es bisiesto? = {result}")
    