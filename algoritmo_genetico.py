import math
from random import randint, uniform,random


def optimizar(dominio, tam_pobl, porc_elite, prob_mut, repeticiones):
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
    
	poblacion = dominio.generar(tam_pobl)
    
	while repeticiones > 0:
		
		tuplas = []
		for sol in poblacion:
			tuplas.append((sol, dominio.fcosto(sol))) 
			
		sorted(tuplas, key = lambda t:t[1])
		num_padres = math.floor(abs(poblacion) * porc_elite)
		num_hijos = (abs(poblacion)) - num_padres
		sig_gen = poblacion[0:num_padres]
		descendencia = 0
		
		while num_hijos > 0:
			randm1, randm2 = randint(1,tam_pobl)
			
			if randm1 == randm2:
				randm1 += 1
			
			while randm1 != randm2:
				padreA = sig_gen[randm1]	
				padreB = sig_gen[randm2]
				hijo = dominio.cruzar(padreA, padreB)
				p = randint(0,1)
				
				#p probabilidad
				if p <= prob_mut:
					hijo = dominio.mutar(hijo)
				
				descendencia.append(hijo)
				num_hijos = num_hijos-1
		
		sig_gen += descendencia	
		poblacion = sig_gen
		
		repeticiones = repeticiones-1
		
