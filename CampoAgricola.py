from NodosSistema import *
from ListaSimple import ListaSimple 


class CampoAgricola:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.estaciones_base = ListaSimple()
        self.sensores_suelo = ListaSimple()
        self.sensores_cultivo = ListaSimple()

    def desplegar(self):
        print()
        print("#"*50)
        print(f'>>> Campo Agricola>> ID: {self.id}  |  Nombre: {self.nombre}')
        print("°"+"-"*10 + " [ Estaciones Base ]"+"-"*10)
        self.estaciones_base.desplegar()
        print("°°"+"-"*10 + " [ Sensores Suelo ]"+"-"*10)
        self.sensores_suelo.desplegar()
        print("°°°"+"-"*10 + " [ Sensores Cultivo ]"+"-"*10)
        self.sensores_cultivo.desplegar()
        print("#"*50)
        print()
    
    
    
    



