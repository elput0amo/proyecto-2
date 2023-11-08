import math
import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(0, 100, 10)
plt.xticks(range(0,100,10))
y = np.cos(x)
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('cos(x)')
plt.title('Grafico de la funcion coseno')
plt.show()
  
              
