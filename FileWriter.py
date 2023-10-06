class FileWriter:
    def __init__(self, filename):
        self.filename = filename

    def crear_txt(self, contenido):
        with open(self.filename, 'w') as f:
            f.write('\n'.join(map(str, contenido)))

        print(f'Se ha creado el archivo {self.filename}')

