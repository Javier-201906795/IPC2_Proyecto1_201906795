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
        print()
        print("\\/"*25)
        print()
        print(">>>> Matriz Suelo")
        if self.matriz_suelo != None:
            self.matriz_suelo.desplegar()
        
        print(">>>> Matriz Cultivo")
        if self.matriz_cultivo != None:
            self.matriz_cultivo.desplegar()
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


            #Asignar Valores matriz Suelo
            for n_columna in range(numero_sensores_suelo):
                #Obtener sensor
                sensorsuelo = self.sensores_suelo.obtener(n_columna)
                #Obtener Lista frecuencias
                frecuencias_lista = sensorsuelo.lecturas
                #Obtener primera frecuencia
                frecuencia_actual = frecuencias_lista.obtenerprimero()
                while frecuencia_actual:
                    #Obtener valor frecuencia
                    frecuencia_valor = frecuencia_actual.valor
                    frecuencia_valor.desplegar()
                    #Obtener posicion fila
                    n_fila = self.estaciones_base.buscar_indice(frecuencia_valor.id)
                    #Cambiar posicion fila mandar al fondo

                    n_fila_nueva = numero_estaciones - n_fila - 1
                    if n_fila_nueva != -1:
                        #Guardar en matriz
                        self.matriz_suelo.asignarValor(n_fila_nueva,n_columna,frecuencia_valor)
                    frecuencia_actual = frecuencia_actual.siguiente

            #Asignar Valores matriz Cultivo
            for n_columna in range(numero_sensores_cultivo):
                #Obtener sensor
                sensorcultivo = self.sensores_cultivo.obtener(n_columna)
                #Obtener Lista frecuencias
                frecuencias_lista = sensorcultivo.lecturas
                #Obtener primera frecuencia
                frecuencia_actual = frecuencias_lista.obtenerprimero()
                while frecuencia_actual:
                    #Obtener valor frecuencia
                    frecuencia_valor = frecuencia_actual.valor
                    frecuencia_valor.desplegar()
                    #Obtener posicion fila
                    n_fila = self.estaciones_base.buscar_indice(frecuencia_valor.id)
                    #Cambiar posicion fila mandar al fondo
                    n_fila_nueva = numero_estaciones - n_fila - 1
                    if n_fila_nueva != -1:
                        #Guardar en matriz
                        self.matriz_cultivo.asignarValor(n_fila_nueva,n_columna,frecuencia_valor)
                    frecuencia_actual = frecuencia_actual.siguiente

                
            #Imprimir
            print()
            print(">>>> Matriz Suelo")
            self.matriz_suelo.desplegar()
            
            print(">>>> Matriz Cultivo")
            self.matriz_cultivo.desplegar()
            

            # #Obtener datos
            # print("casilla [0,0]")
            # self.matriz_suelo.datocasilla(0,0).desplegar()
            
            # print("casilla [0,0]")
            # self.matriz_cultivo.datocasilla(0,0).desplegar()
          

        except Exception as e:
            print("¡¡¡ Error al realizar matrices !!!")
            print(e)
    

    