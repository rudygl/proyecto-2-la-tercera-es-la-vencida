import csv
import math
import random

from dominio import Dominio


class DominioTSP(Dominio):
    """
    Esta clase modela el dominio del problema del Vendedor Viajero para su resolución
    con algoritmos probabilísticos.

    Las soluciones se modelan como listas de enteros, donde cada número representa
    una ciudad específica. Si el grafo contiene n ciudades, la lista siempre contiene
    (n-1) elementos. La lista nunca contiene elementos repetidos y nunca contiene la 
    ciudad de inicio y fin del circuito.

    Métodos:
    generar()
        Construye aleatoriamente una lista que representa una posible solución al problema.

    fcosto(sol)
        Calcula el costo asociado con una solución dada.

    vecino(sol)
        Calcula una solución vecina a partir de una solución dada.

    validar(sol)
        Valida que la solución dada cumple con los requisitos del problema.

    texto(sol)
        Construye una representación en hilera legible por humanos de la solución
        con el fin de reportar resultados al usuario final.
    """

    def __init__(self, ciudades_rutacsv, ciudad_inicio):
        """Construye un objeto de modelo de dominio para una instancia
        específica del problema del vendedor viajero.

        Entradas:
        ciudades_rutacsv (str)
            Ruta al archivo csv que contiene la matriz de pesos entre las ciudades
            para las que se quiere resolver el problema del vendedor viajero.

        ciudad_inicio (str)
            Nombre de la ciudad que será el inicio y fin del circuito a calcular.

        Salidas:
            Una instancia de DominioTSP correctamente inicializada.
        """
        super(DominioTSP, self).__init__()

        filas_csv = self._abrir_csv(ciudades_rutacsv)
        # tomamos la primera linea del csv, la cual contiene los nombres de todas las ciudades
        self._nombre_ciudades = filas_csv[0]
        # quitamos la primera posición ya que es el nombre de la columna 'km/min'
        self._nombre_ciudades = self._nombre_ciudades[1:]
        # para inicializar la matriz con un tamaño de nxn
        self._cant_ciudades = len(self._nombre_ciudades)
        self._dict_ciudades = {}
        self._crear_dict_ciudades()
        self._matriz_ciudades = [[0 for col in range(self._cant_ciudades)] for row in range(self._cant_ciudades)]
        self._llenar_matriz(filas_csv)
        self._ciudad_inicio = self._dict_ciudades[ciudad_inicio]
        pass

    def _crear_dict_ciudades(self):
        """
        Método que llena el diccionario de ciudades donde la key es el nombre de la ciudad
        y el valor el indice (0...n) al que corresponde.
        :return:
        """
        for i in range(0, self._cant_ciudades):
            self._dict_ciudades[self._nombre_ciudades[i]] = i

    def _abrir_csv(self, ruta_csv):
        """
        Crea un arreglo con las lineas dentro de un csv
        :param ruta_csv: es un string que indica la ruta donde se encuentra el archivo csv
        :return: una lista con todas las lineas del archivo csv
        """
        filas = []
        with open(ruta_csv, 'r') as archivo_csv:
            reader_csv = csv.reader(archivo_csv, delimiter=',')
            for fila in reader_csv:
                filas.append(fila)
        return filas

    def _llenar_matriz(self, filas_csv):
        """
        Este método llena la matriz de ciudades con los datos dados en el csv
        :param cant_ciudades: total de ciudades encontrados dentro del csv
        :param filas_csv: lineas(filas) con los datos del csv
        :return:
        """
        # llenamos la matriz con los datos del archivo csv, cada posición i y j representa la ciudad y la ciudad con la que está conectada
        for i in range(0, self._cant_ciudades):
            pesos_i = filas_csv[i + 1]
            # quitamos el nombre de la ciudad
            pesos_i = pesos_i[1:]
            for j in range(0, self._cant_ciudades):
                # guardamos la distancia que hay entre la ciudad i actual y la ciudad j
                self._matriz_ciudades[i][j] = float(pesos_i[j])

    def validar(self, sol):
        """Valida que la solución dada cumple con los requisitos del problema.

        Si n es el número de ciudades en el grafo, la solución debe:
        - Tener tamaño (n-1)
        - Contener sólo números enteros menores que n (las ciudades se numeran de 0 a (n-1))
        - No contener elementos repetidos
        - No contener la ciudad de inicio/fin del circuito

        Entradas:
        sol (list)
            La solución a validar.

        Salidas:
        (bool) True si la solución es válida, False en cualquier otro caso
        """

        # Validamos que el tamaño de la solución sea menor a la cantidad total de ciudades
        if (len(sol) != self._cant_ciudades - 1):
            return False

        # Validamos que no existan ciudades repetidas y que la ciudad de inicio/fin no esté contemplada dentro de la
        # solución
        sol_set = set(sol)
        if (len(sol_set) != len(sol) or self._ciudad_inicio in sol_set):
            return False

        # Validamos que los números que representan a las ciudades sean menores que la cantidad total de ciudades
        for ciudad in sol:
            if (ciudad > self._cant_ciudades - 1):
                return False

        # solo sí cumple con todas las restricciones
        return True

    def texto(self, sol):
        """Construye una representación en hilera legible por humanos de la solución
        con el fin de reportar resultados al usuario final.

        La hilera cumple con el siguiente formato:
        Nombre ciudad inicio -> Nombre ciudad 1 -> ... -> Nombre ciudad n -> Nombre ciudad inicio

        Entradas:
        sol (list)
            Solución a representar como texto legible

        Salidas:
        (str) Hilera en el formato mencionado anteriormente.
        """
        ciudades_a_mostrar = []
        # agregamos la ciudad de inicio a la hilera
        ciudades_a_mostrar.append(self._nombre_ciudades[self._ciudad_inicio])
        # añadimos todas las demás ciudades dentro de la solución
        for i in range(0, len(sol)):
            ciudades_a_mostrar.append(self._nombre_ciudades[sol[i]])
        # volvemos a agregar la ciudad de inicio/fin
        ciudades_a_mostrar.append(self._nombre_ciudades[self._ciudad_inicio])
        # pegamos todas las ciudades separadas por un ' -> ' como el formato mencionado
        hilera_final = ' -> '.join(ciudades_a_mostrar)
        return hilera_final

    def generar(self):
        """Construye aleatoriamente una lista que representa una posible solución al problema.

        Entradas:
        ninguna

        Salidas:
        (list) Una lista que representa una solución válida para esta instancia del vendedor viajero
        """
        sol = []
        # hacemos un recorrido de o hasta n (tamaño de una solución)
        for i in range(0, self._cant_ciudades):
            if (i != self._ciudad_inicio):
                sol.append(i)
        random.shuffle(sol)
        return sol

    def fcosto(self, sol):
        """Calcula el costo asociado con una solución dada.

        Entradas:
        sol (list)
            Solución cuyo costo se debe calcular

        Salidas:
        (float) valor del costo asociado con la solución
        """

        sol_costo = 0
        # agregamos la ciudad de inicio para obtener el costo de la solución
        curr_ciudad = self._ciudad_inicio
        # llegamos hasta n con el for sumando la ciudad de fin(inicio)
        for i in range(0, len(sol)+1):
            if(i == len(sol)):
                sol_costo += self._matriz_ciudades[curr_ciudad][self._ciudad_inicio]
            else:
                sol_costo += self._matriz_ciudades[curr_ciudad][sol[i]]
                curr_ciudad = sol[i]
        return sol_costo

    def vecino(self, sol):
        """Calcula una solución vecina a partir de una solución dada.

        Una solución vecina comparte la mayor parte de su estructura con 
        la solución que la origina, aunque no son exactamente iguales. El 
        método transforma aleatoriamente algún aspecto de la solución
        original.

        Entradas:
        sol (list)
            Solución a partir de la cual se originará una nueva solución vecina

        Salidas:
        (list) Solución vecina
        """
        sol_vecino = sol[:]
        mitad_cant_ciudades = math.floor((self._cant_ciudades / 4) - 1)
        i_random1 = random.randint(0, self._cant_ciudades - 1)
        i_random2 = random.randint(0, self._cant_ciudades - 1)
        if (i_random1 > i_random2):
            i_random1, i_random2 = i_random2, i_random1

        while i_random2 - i_random1 >= mitad_cant_ciudades or i_random2 - i_random1 == 0:
            i_random2 = random.randint(0, self._cant_ciudades - 1)
            if (i_random1 > i_random2):
                i_random1, i_random2 = i_random2, i_random1

        reverse_part = sol_vecino[i_random1:i_random2 + 1]
        reverse_part.reverse()
        sol_vecino_tmp = sol_vecino[i_random2 + 1:]
        sol_vecino = sol_vecino[0:i_random1]
        sol_vecino += reverse_part + sol_vecino_tmp

        return sol_vecino
