from TransformadaInversa import TransformadaInversa
import random
import math

class DistribucionTriangular(TransformadaInversa):
    def __init__(self, a, b, c, generador_aleatorios):
        self.a = a
        self.b = b
        self.c = c
        self.generador_aleatorios = generador_aleatorios

    def generar_variables_aleatorias(self, n):
        variables_triangulares = []
        for _ in range(n):
            R = random.random()
            if R < (self.c - self.a) / (self.b - self.a):
                x = self.a + math.sqrt(R * (self.b - self.a) * (self.c - self.a))
            else:
                x = self.b - math.sqrt((1 - R) * (self.b - self.a) * (self.b - self.c))
            variables_triangulares.append(x)
        return variables_triangulares
