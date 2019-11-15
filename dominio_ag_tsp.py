import random

from dominio_ag import DominioAG
from dominio_tsp import DominioTSP

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
        self.dominioTSP = DominioTSP(ciudades_rutacsv, ciudad_inicio)
        SolucionesAG = []
		
        # Pendiente: implementar este constructor
        pass

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
        
        x=0
		
        while(x<=n):
		
            temporal = dominioTSP.generar()
            self.SolucionesAG.append(temporal)
        
        # Pendiente: implementar este método
        pass

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
        hijo = []
        n = len(sol_a)
		
        while(n>0):
			
            hijo+=[sol_a[n-1]]
            hijo+=[sol_b[n-1]]
            n-=1
		
		
        bandera = 0
        n=len(hijo)
        resultado = []
		
        for x in range (0, n):
            j=x+1
            while(j< n):
			
                if(hijo[j]==hijo[x]):
					
                    j = n
                    bandera = 1
                else:
					
                    j+=1
            if(bandera == 1):
                bandera = 0
			
            else:
				
                resultado += [hijo[x]]
		
        return resultado
        # Pendiente: implementar este método
        pass

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
        largo = len(sol)
        x = randint(1,largo)-1
        y = randint(1,largo)-1
        temporal = sol[x]
        sol[x] = sol[y]
        sol[y] = temporal
        return sol

        # Pendiente: implementar este método
        pass
