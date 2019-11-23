from math import ceil
import unittest

from dominio_tsp import DominioTSP
from levenshtein import levenshtein


class PruebaDominioTSP(unittest.TestCase):
    __tsp = None

    @classmethod
    def setUpClass(cls):
        cls.__tsp = DominioTSP('datos/ciudades_cr.csv', 'Liberia')

    def test_constructor(self):
        tsp = DominioTSP('datos/ciudades_cr.csv', 'Liberia')
        self.assertIsNotNone(tsp)

    def test_validar_correcta(self):
        self.assertTrue(self.__tsp.validar([2, 4, 1, 3, 6, 7, 5, 8, 9, 10, 11, 13, 12, 15, 14, 16]))

    def test_validar_más_ciudades(self):
        self.assertTrue(self.__tsp.validar([2, 4, 1, 3, 6, 7, 5, 8, 9, 10, 11, 13, 12, 15, 14, 16, 17]) == False)

    def test_validar_ciudad_inexistente(self):
        self.assertTrue(self.__tsp.validar([2, 4, 1, 3, 6, 7, 5, 8, 9, 10, 11, 13, 12, 15, 14, 17]) == False)

    def test_validar_con_ciudad_inicial(self):
        self.assertTrue(self.__tsp.validar([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == False)

    def test_validar_menos_ciudades(self):
        self.assertTrue(self.__tsp.validar([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == False)

    def test_validar_ciudades_repetidas(self):
        self.assertTrue(self.__tsp.validar([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 16]) == False)

    def test_texto(self):
        self.assertEqual(self.__tsp.texto([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) ==
                         "Liberia -> Santa Cruz -> Nicoya -> Ciudad Quesada -> Alajuela -> Heredia -> Puerto Viejo Sarapiquí -> San José -> San Isidro del General -> Puntarenas -> Quepos -> Golfito -> Cartago -> Turrialba -> Guápiles -> Limón -> Puerto Viejo Talamanca-> Liberia")

    def test_generar(self):
        n = 10
        repetidos = 0
        sol = self.__tsp.generar()
        for _ in range(n):
            self.assertTrue(self.__tsp.validar(sol))
            nueva_sol = self.__tsp.generar()
            if (sol == nueva_sol):
                repetidos += 1

        self.assertNotEqual(n, repetidos)

    def test_fcosto(self):
        costo = self.__tsp.fcosto([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
        # print("Soy el costo",costo)

        self.assertEqual(costo, 2201.7)  # ESTA

    def test_vecino(self):
        sol = self.__tsp.generar()
        vecino = self.__tsp.vecino(sol)
        distancia = levenshtein(sol, vecino)
        # las soluciones no deben ser iguales
        self.assertGreater(distancia, 0)
