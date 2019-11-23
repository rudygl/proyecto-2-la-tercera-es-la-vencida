import random

from dominio_ag import DominioAG
from dominio_tsp import DominioTSP
from random import randint


class DominioAGTSP(DominioAG, DominioTSP):
    """
    Representa el objeto de dominio que conoce los detalles de implementación y modelamiento
    del problema del vendedor viajero para ser resuelto con algoritmos genéticos.

    Las soluciones se modelan como listas de enteros, donde cada número representa
    una ciudad específica. Si el grafo contiene n ciudades, la lista siempre contiene
    (n-1) elementos. La lista nunca contiene elementos repetidos y nunca contiene la 
    ciudad de inicio y fin del circuito.

    Métodos:
    generar(n)
        Construye aleatoriamente una lista de listas que representa n 
        posibles soluciones al problema.

    cruzar(sol_a, sol_b)
        Produce una nueva posible solución cruzando las dos soluciones dadas por parámetro.

    mutar(sol)
        Produce una nueva solución aplicando un ligero cambio a la solución dada por
        parámetro.
    """
    
    def __init__(self, ciudades_rutacsv, ciudad_inicio):
        """Construye un objeto de modelo de dominio para una instancia
        específica del problema del vendedor viajero para ser resuelto
        con algoritmos genéticos.

        Entradas:
        ciudades_rutacsv (str)
            Ruta al archivo csv que contiene la matriz de pesos entre las ciudades
            para las que se quiere resolver el problema del vendedor viajero.

        ciudad_inicio (str)
            Nombre de la ciudad que será el inicio y fin del circuito a calcular.

        Salidas:
            Una instancia de DominioAGTSP correctamente inicializada.
        """
        super(DominioAGTSP, self).__init__(ciudades_rutacsv, ciudad_inicio)
        self.dominioTSP = DominioTSP(ciudades_rutacsv, ciudad_inicio)
    
    def generar_n(self, n):
        """Construye aleatoriamente una lista de listas que representa n
        posibles soluciones al problema.

        Entradas:
        n (int)
            Número de soluciones aleatorias a generar.

        Salidas:
        (list) Lista que contiene n listas, cada una representando
        una posible solución al problema modelado por el objeto de dominio.
        """
        SolucionesAG = []
        
        for i in range(0, n):
            temporal = self.dominioTSP.generar()
            SolucionesAG.append(temporal)
        
        return SolucionesAG
    
    def cruzar(self, sol_a, sol_b):
        """Produce una nueva posible solución cruzando las dos soluciones dadas por parámetro.

        Entradas:
        sol_a (estructura de datos)
            Estructura de datos que modela la solución antecesora A que será cruzada con la B

        sol_b (estructura de datos)
            Estructura de datos que modela la solución antecesora B que será cruzada con la A

        Salidas:
        (estructura de datos) Una nueva solución producto del cruzamiento entre las soluciones A y B
        """
        if(self.dominioTSP.fcosto(sol_a) < self.dominioTSP.fcosto(sol_b)):
            hijo = sol_a[:(len(sol_a) - 1) // 2]
            segundo_padre = sol_b
        else:
            hijo = sol_b[:(len(sol_b) - 1) // 2]
            segundo_padre = sol_a
            
        for i in segundo_padre:
            if i not in hijo:
                hijo.append(i)
        
        return hijo
    
    def mutar(self, sol):
        """Produce una nueva solución aplicando un ligero cambio a la solución dada por
        parámetro.
        
        Entradas:
        sol (estructura de datos)
            La solución a mutar.
        
        Salidas:
        (estructura de datos) Una nueva solución que refleja un ligero cambio con respecto
        a la solución dada por parámetro
        """
        mutada = sol[:]
        largo = len(mutada)
        x = randint(0, largo - 1) 
        y = randint(0, largo - 1)
        while(x==y):
            y = randint(0, largo - 1)
        mutada[x],mutada[y] = mutada[y],mutada[x]
        
        return mutada
