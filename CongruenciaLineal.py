from GeneradorNumerosAleatorios import GeneradorNumerosAleatorios

class CongruenciaLineal(GeneradorNumerosAleatorios):
    def __init__(self, semilla, a, c, m):
        super().__init__(semilla)
        self.a = a
        self.c = c
        self.m = m

    def generar_numeros_aleatorios(self, n):
        secuencia = [self.semilla]
        for _ in range(n):
            Xi = (self.a * secuencia[-1] + self.c) % self.m
            secuencia.append(Xi)
        return secuencia[1:]
