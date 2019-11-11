import math

def optimizar(dominio, temperatura = 10e32, tasa_enfriamiento = 0.95):

    
    solucionA = dominio.generar()
    costoA = dominio.fcosto(solucionA)

    while (temperatura > 0.01):

        solucionB = dominio.vecino(solucionA)
        costoB = dominio.fcosto(solucionB)
        p = math.exp(-abs(costoB - costoA)/temperatura)
        pAzar = random.randint(0, 1)

        if (costoB < costoA) or pAzar <= p:
            costoA = costoB
            solucionA = solucionB

    temperatura = temperatura * tasa_enfriamiento

    return solucionA

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

    # Pendiente: implementar esta función
    pass
