from ListaSimple import ListaSimple


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
        print(f'- Estacion>> ID: {self.idE}  |  Nombre: {self.nombreE}')
    
    def EsIgualALLave(self, id):
        return self.idE == id
    


############################################################


class Frecuencia(InfoNodo):
    def __init__(self, id, valor):
        self.idF = id
        self.valorF = int(valor.strip())
    
    def desplegar(self):
        print(f'- Frecuencia>> ID: {self.idF}  |  Valor: {self.valorF}')

    def EsIgualALLave(self, id):
        return self.idF == id
    

############################################################



class SensorSuelo(InfoNodo):
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.lecturas = ListaSimple()
    
    def EsIgualALLave(self, id):
        return self.id == id
    
    def desplegar(self):
        print(f'>>> Sensor Suelo>> ID: {self.id}  |  Nombre: {self.nombre}')
        print(f'>>> Lecturas Sensor Suelo>>')
        self.lecturas.desplegar()

        

    def agregarLectura(self, lectura):
        self.lecturas.agregar(lectura)

############################################################

class SensorCultivo(InfoNodo):
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.lecturas = ListaSimple()
    
    def EsIgualALLave(self, id):
        return self.id == id

    def desplegar(self):
        print(f'>>> Sensor Cultivo>> ID: {self.id}  |  Nombre: {self.nombre}')
        print(f'>>> Lecturas Sensor Cultivo>>')
        self.lecturas.desplegar()

        

    def agregarLectura(self, lectura):
        self.lecturas.agregar(lectura)