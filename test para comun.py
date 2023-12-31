import math
import recursos as rec
import numpy as np
from matplotlib import pyplot as plt


class Grafica:
    def __init__(self,X,A,W,T):
        self.X=X
        self.A=A
        self.W=W
        self.T=T
    def RepresentacionSin(self):

        x = np.linspace(0,math.ceil(4/3*self.T), 10000)
        y = self.A*np.cos(self.W*x)
        fig, ax = plt.subplots(1)
        ax.set_xticks(range(0,math.ceil( 4/3*self.T), math.ceil(self.T/5)))
        ax.plot(x, y,color="black")
        ax.set_xlabel("Tiempo (s)")
        ax.set_ylabel("Amplitud (m)")
        ax.set_title("Movimiento Armonico Simple")
        ax.legend()
        fig.tight_layout()
        plt.show()

p1=Grafica(2,3,4,5)
p1.Representacion()