from TransformadaInversa import TransformadaInversa
import math

class DistribucionNormal(TransformadaInversa):
    def __init__(self, generador_aleatorios):
        self.generador_aleatorios = generador_aleatorios

    def generar_variables_aleatorias(self, n):
        var_nor = []
        for i in range(n):
            nor = 10 ** (len(str(self.generador_aleatorios[i])))
            bas = 10 ** (len(str(self.generador_aleatorios[-1])))
            P = self.generador_aleatorios[-1] / bas
            R = self.generador_aleatorios[i] / nor
            a = math.sqrt((-2 * math.log(R)))
            b = 2 * math.pi * P
            x = a * math.sin(b)
            var_nor.append(x)
        return var_nor
