from NodosSistema import *
from ListaSimple import ListaSimple 
from Matriz import Matriz


class CampoAgricola(InfoNodo):
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.estaciones_base = ListaSimple()
        self.sensores_suelo = ListaSimple()
        self.sensores_cultivo = ListaSimple()
        self.matriz_suelo = None
        self.matriz_cultivo = None

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
    
    def EsIgualALLave(self, id):
        return self.id == id
    
    def RealizarMatrices(self):
        try:
            print(">>> Realizando matrices...")
            #Tamaño Matriz
            numero_estaciones = self.estaciones_base.tamano()
            numero_sensores_suelo = self.sensores_suelo.tamano()
            numero_sensores_cultivo = self.sensores_cultivo.tamano()

            #Crear Matrices
            self.matriz_suelo = Matriz(numero_estaciones, numero_sensores_suelo)
            self.matriz_cultivo = Matriz(numero_estaciones, numero_sensores_cultivo)

            print(">>>> Matrices Vacias Creadas")
            print(">>>> Matriz Suelo")
            self.matriz_suelo.desplegar()
            print(">>>> Matriz Cultivo")    
            self.matriz_cultivo.desplegar()

        except Exception as e:
            print("¡¡¡ Error al realizar matrices !!!")
            print(e)
