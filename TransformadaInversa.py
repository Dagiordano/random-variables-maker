from abc import ABC, abstractmethod

class TransformadaInversa(ABC):
    @abstractmethod
    def generar_variables_aleatorias(self, n):
        pass
