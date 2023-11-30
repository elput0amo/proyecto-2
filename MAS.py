import math
import recursos as rec
import numpy as np
from matplotlib import pyplot as plt
#ya se que algunas de estas librerias no se usan directamente en esta parte del codigo pero me gusta tenerlas para saber que he usado en general

bucle=True
contador=0
basura=[]
nbasura=0
#aqui es donde estan ciertas variables que voy a usar en un futuro, como todo esta dentro de un bucle aqui es donde tengo que especificarlas

#y aqui es donde comienza la magia
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
        funcion=input().lower()
        contador=1
#aqui es donde te dicen lo que puedes hacer, una introduccion
#siempre que pido cualquier variable la transformo en minusculas para que de igual si la metes en minusculas o mayusculas
#lo del contador es para que esto solo ocurra una vez, hay maneras mejores de hacerlo, pero esta funciona y mlp


    if funcion=="soy subnormal":
        print()
        print(f"X: se refiere a la posicion actual de la masa unida al muelle, su unidad en S.I son los metros")
        print(f"M: se refiere a la masa del cuerpo unido al extremo del muelle, su unidad en S.I son los kilogramos")
        print(f"K: se refiere a la constante elastica del muelle calculada al dividir la fuerza aplicada entre su desplazamiento, su unidad en S.I son los Newtons/metro")
        print(f"A: se refiere a la distancia inicial de la masa al punto de equilibrio de esta, esta coincide con la X maxima, su unidad en el S.I son los metros ")
        print(f"T: se refiere al tiempo transcurrido desde que el movimiento empezo, que es cuando la masa se dejo completamente bajo la influencia del muelle, su unidad en S.I es segundos")
        print()
        incognita=input(f"Ahora que estas educado, introduce la incognita que quieras calcular (X,M,K,A,T) o  (Comandos) si quieres ver tus opciones:").lower()
#pequeña explicacion fisica y te dice en que unidades hay que meter todo, esto es conocimiento comun, pero x si alguien no lo sabe
#perdon por el nombre de algunas cosas, necesito hacer estas bromas para mantenerme despierto

    if funcion =="calculadora":
        incognita=input(f"Por favor, introduce la incognita que quieras calcular (X,M,K,A,T) o (Comandos) para volver atras: ").lower()
#aqui es donde esta la funcion principal de todo, las formulas cambian dependiendo de la incognita, no queda otra que usar varias variables

    if incognita=="x":
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
        incognita=input(f"Si quieres seguir calculando escribe la incognita a calcular (X,M,K,A,T) o (Comandos) para volver atras: ")
#esto en verdad no tiene mucha chicha, es parecido pero ligeramente diferente para cada una de las variables
#se podria optimizar, pero la carga de el programa tampoco lo requiere y asi es mas facil de entender a primera vista

    if incognita== "m":
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
        incognita=input(f"Si quieres seguir calculando escribe la incognita a calcular (X,M,K,A,T) o (Comandos) para volver atras: ")
#no hace falta comentarlas todas

    if incognita =="k":
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
        incognita=input(f"Si quieres seguir calculando escribe la incognita a calcular (X,M,K,A,T) o (Comandos) para volver atras: ")
#de verdad, esto no tiene mucho que ver, es mas interesante las funciones que uso en el codigo de recursos

    if incognita=="a":
        valores=input(f"Por favor introduce las variables, en las unidades del S.I, separadas por una coma en el siguiente orden (M,K,X,T): ")
        M,K,X,T=valores.split(",")
        X=float(X)
        K=float(K)
        M=float(M)
        T=float(T)
        p1=rec.CalculadoraAmplitud(M,K,X,T)
        M,W= p1.amplitud()
        p1=rec.Grafica(X,A,W,T)
        p1.Representacion()
        print(f"La posicion de la masa en el momento {T} es de {X:.2f} metros")
        incognita=input(f"Si quieres seguir calculando escribe la incognita a calcular (X,M,K,A,T) o (Comandos) para volver atras: ")
#leer el comentario de arriba

    if incognita=="t":
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
        incognita=input(f"Si quieres seguir calculando escribe la incognita a calcular (X,M,K,A,T) o (Comandos) para volver atras: ")
#la verdad es que todo este codigo podria haberlo copiado y pegado para el proyecto grupal y habria quedado d locos, pero era abusar

    elif incognita not in ["x", "m", "k", "a", "t", "comandos"]:
        print(f"Esta incognita no esta reconocida, porfavor escribe correctamente")
        print(f"Si quieres volver a la calculadora, introduce tu incognita (X,M,K,A,T), de lo contrario escribe (Comandos) para ver las opciones")
        incognita=input(f"").lower()
        print()
#esto es cuando la incognita no coincide con ninguna de las variables o con nada en general, vamos, que el usuario es dislexico

    if incognita=="Comandos":
        print(f"Si quieres una breve explicacion de los valores que hay que introducir escribe (Soy subnormal)")
        print(f"Si quieres usar la calculadora para calcular incognitas escribe (Calcular)")
        print(f"Si quieres crear la grafica de un MAS sin necesidad de clacular nada escribe (Grafica)")
        print(f"Si tienes alguna sugerencia para mejorar la calculadora, escribe (Sugerencias)")
        print(f"Si quieres salir de la calculadora, escribe (Finalizar)")
        funcion= input().lower()
#esto es el menu principal

    if funcion=="sugerencias":
#esta parte es un poco vacile

        f=True
        while f:
            print(f"Porfavor, escribe tus sugerencias y/o problemas que hallas encontrado a continuación: ")
            basura.append(input())
            nbasura+=1
            repeat=input(f"Si tienes mas sugerencias escribe (Mas), si quieres volver a menu, escribe (Atras): ").lower()
            #ya se que las sugerencias no sirven para nada, esa es la gracia, te estoy tratando como la corporacion promedio
    
            if repeat!="mas" and repeat!= "atras" :
                repeat=input(f"Ese comando no existe, porfavor escribe (Mas) si tienes mas sugerencias, escribe (Ver) o (Atras)")
            if repeat=="mas":
                pass
            if repeat=="atras":
                f=False
                incognita="comandos"
            #esto es para lidiar con las diferentes situaciones 

    
    if funcion=="grafica":
        valores=input(f"Por favor introduce los datos separados por una coma en el orden (X,A,W,T):")
        X,A,W,T=valores.split(",")
        p1=rec.Grafica(X,A,W,T)
        p1.RepresentacionSin()
        funcion=input(f"Si quieres representar otra grafica escribe (grafica), si quieres volver atras escribe (Comandos) ").lower()
#literalmente la funcion que uso para la calculadora pero mas facil

    elif funcion not in ["soy subnormal", "calculadora", "grafica", "sugerencias", "finalizar"]:
        print("Esta función no está reconocida. Por favor, elige una opción válida: ")
        print("Si quieres ver las opciones disponibles, escribe (Comandos):")
        funcion = input().lower()
        print()
#para los dislexicos

    if funcion =="finalizar":
        ip=rec.obtener_ip()
        print("Muchas gracias por usar nuestros servicios")
        print(f"Estashan sido tus sugerencias: {basura}, no haremos caso a ninguna")
        print(f"Ah, y por cierto, has vendido tu metaforica alma virtual al usar este programa, tenemos tu ip, sabemos donde vives y vamos a por ti")
        print(f"Gracias por su colaboracion {ip}")
        bucle=False
#pequeña bromita para el final


    

