from GeneradorNumerosAleatorios import GeneradorNumerosAleatorios
from TransformadaInversa import TransformadaInversa
import random
import math

class DistribucionExponencial(TransformadaInversa):
    def __init__(self, lambd, generador_aleatorios):
        self.lambd = lambd
        self.generador_aleatorios = generador_aleatorios

    def generar_variables_aleatorias(self, n):
        var_exp = []
        for _ in range(n):
            R = random.random()
            x = -1 / self.lambd * math.log(1 - R)
            var_exp.append(x)
        return var_exp

