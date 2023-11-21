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
        print(f"Si quieres una breve explicacion de los valores que hay que introducir escribe (Soy subnormal)")
        print(f"Si quieres usar la calculadora para calcular incognitas escribe (Calcular)")
        print(f"Si quieres crear la grafica de un MAS sin necesidad de clacular nada escribe (Grafica)")
        print(f"Si tienes alguna sugerencia para mejorar la calculadora, escribe (Sugerencias)")
        print(f"Si quieres salir de la calculadora, escribe (Finalizar)")
        print()
        funcion=input()
        contador=1

    if funcion=="Soy subnormal":
        print()
        print(f"X: se refiere a la posicion actual de la masa unida al muelle, su unidad en S.I son los metros")
        print(f"M: se refiere a la masa del cuerpo unido al extremo del muelle, su unidad en S.I son los kilogramos")
        print(f"K: se refiere a la constante elastica del muelle calculada al dividir la fuerza aplicada entre su desplazamiento, su unidad en S.I son los Newtons/metro")
        print(f"A: se refiere a la distancia inicial de la masa al punto de equilibrio de esta, esta coincide con la X maxima, su unidad en el S.I son los metros ")
        print(f"T: se refiere al tiempo transcurrido desde que el movimiento empezo, que es cuando la masa se dejo completamente bajo la influencia del muelle, su unidad en S.I es segundos")
        print()
        incognita=input(f"Ahora que estas educado, introduce la incognita que quieras calcular (X,M,K,A,T):")

    if  funcion =="Calculadora":
        incognita=input(f"Por favor, introduce la incognita que quieras calcular (X,M,K,A,T): ")

    if incognita=="X":
        valores=input(f"Por favor introduce las variables, en las unidades del S.I, separadas por una coma en el siguiente orden (M,K,A,T): ")
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

    if incognita== "M":
        valores=input(f"Por favor introduce las variables, en las unidades del S.I, separadas por una coma en el siguiente orden (X,K,A,T): ")
        X,K,A,T=valores.split(",")
        X=float(X)
        K=float(K)
        A=float(A)
        T=float(T)
        p1=rec.CalculadoraMasa(X,K,A,T)
        M,W= p1.masa()
        p1=rec.Grafica(X,A,W,T)
        p1.Representacion()
        print(f"La posicion de la masa en el momento {T} es de {X:.2f} metros")

    if incognita =="K":
        valores=input(f"Por favor introduce las variables, en las unidades del S.I, separadas por una coma en el siguiente orden (M,X,A,T): ")
        M,X,A,T=valores.split(",")
        X=float(X)
        M=float(M)
        A=float(A)
        T=float(T)
        p1=rec.CalculadoraConstanteElastica(M,X,A,T)
        M,W= p1.constante()
        p1=rec.Grafica(X,A,W,T)
        p1.Representacion()
        print(f"La posicion de la masa en el momento {T} es de {X:.2f} metros")

    if incognita=="A":
        valores=input(f"Por favor introduce las variables, en las unidades del S.I, separadas por una coma en el siguiente orden (M,K,X,T): ")
        M,K,X,T=valores.split(",")
        X=float(X)
        K=float(K)
        M=float(B)
        T=float(T)
        p1=rec.CalculadoraAmplitud(M,K,X,T)
        M,W= p1.amplitud()
        p1=rec.Grafica(X,A,W,T)
        p1.Representacion()
        print(f"La posicion de la masa en el momento {T} es de {X:.2f} metros")

    if incognita=="T":
        valores=input(f"Por favor introduce las variables, en las unidades del S.I, separadas por una coma en el siguiente orden (M,K,A,X): ")
        M,K,A,X=valores.split(",")
        X=float(X)
        K=float(K)
        A=float(A)
        M=float(M)
        p1=rec.CalculadoraTiempo(M,K,A,X)
        M,W= p1.tiempo()
        p1=rec.Grafica(X,A,W,T)
        p1.Representacion()
        print(f"La posicion de la masa en el momento {T} es de {X:.2f} metros")
        print(f"Si quieres volver a la calculadora, introducela variable que quieres calcular (X,M,K,A,T) o escribe (Soy subnormal) para una explicacion de las variables")
        print(f"Si quieres realizar otra acción, escribe (Comandos)")
        incognita=input(f"")

    elif incognita!="X"or"M"or"K"or"A"or"T"or"Comandos":
        print(f"Esta incognita no esta reconocida, porfavor asegurate de usar mayusculas correctamente")
        print(f"Si quieres volver a la calculadora, introduce tu incognita (X,M,K,A,T), de lo contrario escribe (Comandos) para ver las opciones")
        incognita=input(f"")
        print()

    if incognita=="Comandos":
        print(f"Si quieres una breve explicacion de los valores que hay que introducir escribe (Soy subnormal)")
        print(f"Si quieres usar la calculadora para calcular incognitas escribe (Calcular)")
        print(f"Si quieres crear la grafica de un MAS sin necesidad de clacular nada escribe (Grafica)")
        print(f"Si tienes alguna sugerencia para mejorar la calculadora, escribe (Sugerencias)")
        print(f"Si quieres salir de la calculadora, escribe (Finalizar)")

    
        

    






  
              
