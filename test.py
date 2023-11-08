from matplotlib import pyplot as plt
import numpy as np
import math

class Grafica:
    def __init__(self,X,A,W,T):
        self.X=X
        self.A=A
        self.W=W
        self.T=T
    def Representacion(self):

        x = np.linspace(0,math.ceil(4/3*self.T), 10000)
        y = self.A*np.cos(self.W*x)
        x2=self.T
        y2=self.X
        fig, ax = plt.subplots(1)
        ax.set_xticks(range(0,math.ceil( 4/3*self.T), math.ceil(self.T/5)))
        ax.plot(x, y)
        ax.plot(x2, y2,marker="o",color="red",label=f"Tu posicion({self.X},{self.T})")
        ax.set_xlabel("Tiempo (s)")
        ax.set_ylabel("Amplitud (m)")
        ax.set_title("Movimiento Armonico Simple")
        ax.legend()
        fig.tight_layout()
        plt.show()

p1=Grafica(0,3,4,2.5)
p1.Representacion()