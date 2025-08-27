
class InfoNodo():
    
    def desplegar():
        pass
    
    def EsIgualALLave():
        pass


############################################################


class Estacion(InfoNodo):
    def __init__(self, id, nombre):
        self.idE = id
        self.nombreE = nombre
    
    def desplegar(self):
        print(f'Estacion_ID: {self.idE}  |  Estacion_Nombre: {self.nombreE}')
    
    def EsIgualALLave(self, id):
        return self.idE == id
    


############################################################


class Frecuencia(InfoNodo):
    def __init__(self, id, valor):
        self.idF = id
        self.valorF = int(valor.strip())
    
    def desplegar(self):
        print(f'Frecuencia_ID: {self.idF}  |  Frecuencia_Valor: {self.valorF}')

    def EsIgualALLave(self):
        return self.idF == id