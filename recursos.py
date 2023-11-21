import math
import numpy as np
from matplotlib import pyplot as plt

class CalculadoraPosicion:
    def __init__(self,M ,K, A, T):
        self.M=float(M)
        self.K=float(K)
        self.A=float(A)
        self.T=float(T)
        
    def posicion(self):
        relleno=float(self.K)/float(self.M)
        W= (math.sqrt(relleno))
        X=self.A*math.cos(W*self.T)
        return X,W
    
class CalculadoraMasa:
    def __init__(self,X,K, A, T):
        self.X=X
        self.K=K
        self.A=A
        self.T=T
        
    def masa(self):
        relleno=self.X/self.A
        inc= (math.acos(relleno))
        M=self.K*(self.T**2)/(inc**2)
        inc2=self.K/M
        W=math.sqrt(inc2)
        return M,W
    
class CalculadoraConstanteElastica:
    def __init__(self,M,X, A, T):
        self.X=X
        self.M=M
        self.A=A
        self.T=T
        
    def constante(self):
        relleno=self.X/self.A
        inc= (math.acos(relleno))
        K=self.M*(inc**2)/(self.T**2)
        inc2=K/self.M
        W=math.sqrt(inc2)
        return K,W
    
class CalculadoraAmplitud:
    def __init__(self,M,K, X, T):
        self.X=X
        self.M=M
        self.T=T
        self.K=K
        
    def amplitud(self):
        relleno=self.K/self.M
        W= (math.sqrt(relleno))
        A=self.X/math.cos(W*self.T)
        return A,W
    
class CalculadoraTiempo:
    def __init__(self,M,K, A, X):
        self.X=X
        self.M=M
        self.K=K
        self.A=A
        
    def tiempo(self):
        relleno=self.X/self.A
        inc= (math.acos(relleno))
        Tsn=self.M*(inc**2)/(self.K)
        T=math.sqrt(Tsn)
        inc2=self.K/self.M
        W=math.sqrt(inc2)
        return T,W
    
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
        ax.plot(x, y,colour="black")
        ax.plot(x2, y2,marker="o",color="red",label=f"Tu posicion({self.X:.2f},{self.T})",linewidth=0)
        ax.set_xlabel("Tiempo (s)")
        ax.set_ylabel("Amplitud (m)")
        ax.set_title("Movimiento Armonico Simple")
        ax.legend()
        fig.tight_layout()
        plt.show()