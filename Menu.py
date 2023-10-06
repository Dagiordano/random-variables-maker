class Menu:
    @staticmethod
    def obtener_variables():
        num = int(input("Ingresa el número de variables (Defecto = 12): ") or "12")
        return num

    @staticmethod
    def obtener_distribucion():
        dist = input("Ingresa la distribución a usar: ")
        return dist

    @staticmethod
    def obtener_valor_lambd():
        lambd = float(input("Ingresa el valor de LAMBDA (Defecto = 0.5): ") or "0.5")
        return lambd

    @staticmethod
    def obtener_valor_a():
        a = float(input("Ingresa el valor de 'a' (Defecto = 19): ") or "19")
        return a

    @staticmethod
    def obtener_valor_c():
        c = float(input("Ingresa el valor de 'c' (Defecto = 33): ") or "33")
        return c

    @staticmethod
    def obtener_valor_m():
        m = float(input("Ingresa el valor de 'm'  (Defecto = 100): ") or "100")
        return m

                        
    @staticmethod
    def obtener_nombre_archivo():
        filename = input("Ingresa nombre del archivo a crear (añadir '.txt'): ")
        return filename