from sympy import symbols, diff, simplify, pprint

def calcular_derivada():
    # Definir la variable simbólica
    x = symbols('x')

    # Pedir al usuario que ingrese la función
    expresion = input("Ingresa la función en términos de x: ")

    try:
        # Convertir la entrada del usuario en una expresión simbólica
        funcion = simplify(expresion)

        # Calcular la derivada de la función
        derivada = diff(funcion, x)

        # Imprimir la derivada simplificada
        pprint(derivada)

    except Exception as e:
        print("Error al procesar la entrada:", e)

# Llamar a la función para calcular la derivada
calcular_derivada()
