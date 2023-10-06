import random
import math
from GeneradorNumerosAleatorios import GeneradorNumerosAleatorios
from CongruenciaLineal import CongruenciaLineal
from TransformadaInversa import TransformadaInversa
from DistribucionExponencial import DistribucionExponencial
from DistribucionNormal import DistribucionNormal
from FileWriter import FileWriter
from Menu import Menu
from DistribucionTriangular import DistribucionTriangular

if __name__ == '__main__':
    semilla = 37

    menu = Menu()

    n = menu.obtener_variables()
    lambd = menu.obtener_valor_lambd()
    c = menu.obtener_valor_c()
    m = menu.obtener_valor_m()
    a = menu.obtener_valor_a()

    generador_cong_lineal = CongruenciaLineal(semilla, a, c, m)

    U = generador_cong_lineal.generar_numeros_aleatorios(n)

    opcion = menu.obtener_distribucion()

    if opcion == "exponencial":
        distribucion = DistribucionExponencial(lambd, generador_cong_lineal)
    elif opcion == "normal":
        distribucion = DistribucionNormal(U)
    elif opcion == "triangular":
        a = float(input("Ingresa el valor de 'a' para la distribución triangular: "))
        b = float(input("Ingresa el valor de 'b' para la distribución triangular: "))
        c = float(input("Ingresa el valor de 'c' para la distribución triangular: "))
        distribucion = DistribucionTriangular(a, b, c, generador_cong_lineal)

    else:
        print("Intenta entre exponencial, normal o triangular")

    prob = distribucion.generar_variables_aleatorias(n)
    filename = menu.obtener_nombre_archivo()


    escritor = FileWriter(filename)
    escritor.crear_txt(prob)
