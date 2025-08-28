from NodosSistema import *
from ListaSimple import ListaSimple 


class CampoAgricola:
    def __init__(self, id, nombre):
        self.idC = id
        self.nombre = nombre
        self.estaciones_base = ListaSimple()
        self.sensores_suelo = ListaSimple()
        self.sensores_cultivo = ListaSimple()

    def desplegar(self):
        print(f'>>> Campo Agricola>> ID: {self.idC}  |  Nombre: {self.nombre}')
    
    
    



