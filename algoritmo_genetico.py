import math
from random import randint, uniform


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
	poblacion = dominio.generar_n(tam_pobl)
	
	while repeticiones > 0:
		tuplas = []
		for sol in poblacion:
			tuplas.append((sol, dominio.fcosto(sol)))
		
		sorted(tuplas, key=lambda t: t[1])
		num_padres = math.floor(len(tuplas) * porc_elite)
		num_hijos = len(tuplas) - num_padres
		sig_gen_tmp = tuplas[0:num_padres]
		sig_gen = []
		# tomamos los elementos soluciones (tupla[0]) de cada tupla
		for elemento in sig_gen_tmp:sig_gen.append(elemento[0])
		descendencia = []
		
		while num_hijos > 0:
			ran1 = randint(1, len(sig_gen)-1)
			ran2 = randint(1, len(sig_gen)-1)
			while(ran1 == ran2):ran2 = randint(1, len(sig_gen)-1)
			
			padreA = sig_gen[ran1]
			padreB = sig_gen[ran2]
			hijo = dominio.cruzar(padreA, padreB)
			
			# obtenemos un número random entre 0 y 1 (incluido ambos)
			p = uniform(0, 1)
			# p probabilidad
			if p <= prob_mut:
				hijo = dominio.mutar(hijo)
			descendencia.append(hijo)
			
			num_hijos = num_hijos - 1
			
		sig_gen += descendencia
		poblacion = sig_gen
		repeticiones = repeticiones - 1
	
	return poblacion[0]
