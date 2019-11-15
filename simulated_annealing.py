import math
import random

def optimizar(dominio, temperatura = 10e32, tasa_enfriamiento = 0.95):
    """Algoritmo de optimización estocástica simulated annealing.
    Entradas:
    dominio (Dominio)
        Un objeto que modela el dominio del problema que se quiere aproximar.
    temperatura (float/int)
        Temperatura inicial del algoritmo, se recomienda un número alto
    tasa_enfriamiento (float)
        Porcentaje de enfriamiento de la temperatura durante cada iteración, el valor
        por defecto es 0.95, lo que indica una tasa de enfriamiento del 5%.
    Salidas:
        (estructura de datos) Estructura de datos según el dominio, que representa una
        aproximación a la mejor solución al problema.
    """
    sol = dominio.generar()
    costo_sol = dominio.fcosto(sol)

    while (temperatura > 0.01):

        vecino = dominio.vecino(sol)
        costo_vecino = dominio.fcosto(vecino)
        p = math.exp(-abs(costo_vecino - costo_sol)/temperatura)
        Pazar = random.uniform(0, 1)

        if (costo_vecino < costo_sol) or Pazar <= p:
            sol = vecino
            costo_sol = costo_vecino

        temperatura = temperatura * tasa_enfriamiento

    return sol
