#Ingresar, Leer y segmentar archivo

class SistemaArchivos:
    def __init__(self, rutadelarchivo):
        self.rutadelarchivo = rutadelarchivo

    def leerArchivo(self):
        try:
            pass
        except Exception as e:
            print(f"Ocurrió un error al leer el archivo. \n {e}")