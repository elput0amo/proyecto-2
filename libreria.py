import math

class CalculadoraPosicion:
    def __init__(self,M ,K, A, T):
        self.M=M
        self.K=K
        self.A=A
        self.T=T
        
    def posicion(self):
        relleno=self.K/self.M
        W= (math.sqrt(relleno))
        X=self.A*math.cos(W*self.T)
        return X
    
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
        return M
    
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
        return K
    
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
        return A
    
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
        return T
    


