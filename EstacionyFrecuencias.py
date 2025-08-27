

class Estacion:
    def __init__(self, id, nombre):
        self.idE = id
        self.nombreE = nombre

class Frecuencia:
    def __init__(self, id, valor):
        self.idF = id
        self.valorF = int(valor.strip())