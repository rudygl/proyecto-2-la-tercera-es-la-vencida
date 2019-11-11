import math
from random import randint, uniform,random


def optimizar(dominio, tam_pobl, porc_elite, prob_mut, reps):
    """Algoritmo genético para optimización estocástica.

    Entradas:
    dominio (DominioAG)
        Un objeto que modela el dominio del problema que se quiere aproximar.
    
    tam_pobl (int)
        Tamaño de la población.
    
    porc_elite (float)
        Porcentaje de la población que se tomará como elite.
    
    prob_mut (float)
        Probabilidad de mutación, debe estar en el rango [0, 1]
    
    reps (int)
        Número de iteraciones a ejecutar.

    Salidas:
        (estructura de datos) Estructura de datos según el dominio, que representa una
        aproximación a la mejor solución al problema.
    """
    
    #poblacion = dominio.generar(tam_pobl)
    
    while reps > 0:
		for sol in poblacion:
			#sol.aptitud = dominio.fcosto(sol) 
			
		Ordenar(poblacion, llave = aptitud)
		num_padres = math.floor(abs(poblacion) * porc_elite)
		num_hijos = (abs(poblacion) - num_padres
		sig_gen(poblacion[0:num_padres])
		descendencia = 0
		
		while num_hijos > 0:
			randm = randint(1,tam_pobl)
			padreA = sig_gen[randm]
			#while randm1 != randm2
			
			padreB = sig_gen[randm]
			hijo = dominio.cruzar(padreA, padreB)
			p = randint(0,1)
			
			if p <= prob_mut:
				hijo = dominio.mutar(hijo)
				
			descendencia.append(hijo)
			
			num_hijos = num_hijos-1
		
		sig_gen += descendencia	
		poblacion = sig_gen
		
		repeticiones = repeticiones-1
		
    # Pendiente: implementar este método
    pass
