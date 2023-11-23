import math
import recursos as rec
import numpy as np
from matplotlib import pyplot as plt

valores=input(f"Por favor introduce los datos separados por una coma en el orden (X,A,W,T):")
X,A,W,T=valores.split(",")
X=float(X)
A=float(A)
W=float(W)
T=float(T)
p1=rec.Grafica(X,A,W,T)
p1.Representacion()