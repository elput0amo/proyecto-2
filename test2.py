import sympy as sp

def encontrar_puntos_corte():
    while True:
        try:
            # Pedir al usuario que ingrese la función
            expresion = input("Ingresa la función en términos de x: ")

            # Convertir la entrada del usuario en una expresión simbólica
            funcion = sp.sympify(expresion)

            # Definir la variable simbólica
            x = sp.symbols('x')

            # Encontrar puntos de corte reales con el eje x
            puntos_x = [round(sol.evalf(), 2) for sol in sp.solve(funcion, x) if sol.is_real]

            # Evaluar la función en el origen para encontrar el punto de corte con el eje y
            punto_y = round(funcion.subs(x, 0).evalf(), 2)

            # Imprimir los puntos de corte
            print(f"Puntos de corte con el eje x: {puntos_x}")
            print(f"Punto de corte con el eje y: {punto_y}")

            # Si la ejecución llega a este punto, la entrada se procesó correctamente
            break

        except Exception as e:
            print("Error al procesar la entrada:", e)
            print("Inténtalo de nuevo.")

# Llamar a la función para encontrar puntos de corte
encontrar_puntos_corte()
