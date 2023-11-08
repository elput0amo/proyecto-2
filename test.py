from matplotlib import pyplot as plt
import numpy as np
x = np.linspace(0, 10, 10000)
plt.xticks(range(0,100,10))
y = np.cos(x)
x2=5
y2=0.5
fig = plt.figure()
fig.clear()
ax = fig.subplots(1,1)

ax.plot(x, y)
ax.plot(x2, y2,marker="o",color="red",label="Tu posicion")


plt.plot(x, y)
plt.xlabel("Tiempo")
plt.ylabel("Amplitud")
plt.title("Movimiento Armonico Simple")
ax.legend()
fig.tight_layout()
fig.show() 