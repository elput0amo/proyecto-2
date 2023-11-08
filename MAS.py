import math
import recursos as rec
import numpy as np
from matplotlib import pyplot as plt
bucle=True
contador=0
while bucle==True:
    if contador==0:
        print(f"Bienvenido a la Calculadora Original de Movimiento Armonico Simple (COMAS)")
        print(f"Esta calculadora simula un MAS dado por un muelle unido a un peso en la tierra, cacula y representa la posicion de este a lo largo del tiempo")
        print(f"COMAS puede calcular cualquier variable de este tipo de MAS siempre y cuando le suministres el resto de variables")
        print(f"Si quieres una breve explicacion de los valores que hay que introducir escribe (Soy subnormal), de lo contrario;")
        print()
        incognita=input(f"Por favor introduce la incognita que quieras calcular en S.I (X,M,K,A,T):")
        contador=1
        

    if incognita=="Soy subnormal":
        print()
        print(f"X: se refiere a la posicion actual de la masa unida al muelle, su unidad en S.I son los metros")
        print(f"M: se refiere a la masa del cuerpo unido al extremo del muelle, su unidad en S.I son los kilogramos")
        print(f"K: se refiere a la constante elastica del muelle calculada al dividir la fuerza aplicada entre su desplazamiento, su unidad en S.I son los Newtons/metro")
        print(f"A: se refiere a la distancia inicial de la masa al punto de equilibrio de esta, esta coincide con la X maxima, su unidad en el S.I son los metros ")
        print(f"T: se refiere al tiempo transcurrido desde que el movimiento empezo, que es cuando la masa se dejo completamente bajo la influencia del muelle, su unidad en S.I es segundos")
        print()
        incognita=input(f"Ahora que estas educado, introduce la incognita que quieras calcular en S.I (X,M,K,A,T):")

    if incognita=="X":
        valores=input(f"Por favor introduce las variables separadas por una coma en el siguiente orden (M,K,A,T): ")
        M,K,A,T=valores.split(",")
        M=float(M)
        K=float(K)
        A=float(A)
        T=float(T)
        p1=rec.CalculadoraPosicion(M,K,A,T)
        X,W=p1.posicion()
        p1=rec.Grafica(X,A,W,T)
        p1.Representacion()
        print(f"La posicion de la masa en el momento {T} es de {X:.2f} metros")





  
              
