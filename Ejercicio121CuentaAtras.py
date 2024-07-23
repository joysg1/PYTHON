import time

for i in range(10,-1,-1): 
 if i !=0:
    print(f"\r{i}",end="")
    time.sleep(1)
 else:
     print("Fin cuenta atras")
