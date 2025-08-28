from ListaSimple import ListaSimple


class InfoNodo():
    
    def desplegar():
        pass
    
    def EsIgualALLave():
        pass


############################################################


class Estacion(InfoNodo):
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
    
    def desplegar(self):
        print(f'- Estacion>> ID: {self.id}  |  Nombre: {self.nombre}')
    
    def EsIgualALLave(self, id):
        return self.id == id
    


############################################################


class Frecuencia(InfoNodo):
    def __init__(self, id, valor):
        self.id = id
        self.valor = int(valor.strip())
    
    def desplegar(self):
        print(f'- Frecuencia>> ID: {self.id}  |  Valor: {self.valor}')

    def EsIgualALLave(self, id):
        return self.id == id
    
    def cambiarvalor(self, valor):
        self.valor = valor
    

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

    


############################################################

class FilaD(InfoNodo):
    def __init__(self, fila, valor):
        self.fila = fila
        self.valor = valor
    
    def desplegar(self):
        print(f'- Fila>> : {self.fila}  |  Valor: {self.valor}')

    def EsIgualALLave(self, valor):
        return self.valor == valor
    
    def cambiarvalor(self, valor):
        self.valor = valor
    