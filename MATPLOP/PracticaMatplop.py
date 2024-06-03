import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

x = np.linspace(1, 150, 200)
y = x + x**2
print(x)
print(y)

plt.plot(x,y,"blue")
plt.title('Mi grafica')
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.show()


# Video 98 min 5