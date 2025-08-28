from ListaSimple import ListaSimple
from NodosSistema import *

class Matriz:
    def __init__(self, numfilas, numcolumnas):
        self.numero_filas = numfilas
        self.numero_columnas = numcolumnas
        self.matriz = ListaSimple()

        #Crear matriz vacia
        for i in range(self.numero_columnas):
            fila = ListaSimple()
            #Llenar Fila
            for h in range(self.numero_filas):
                valor = ValorMatriz("0","0")
                fila.agregar(valor)
            #Agregar a columna
            self.matriz.agregar(fila)
    
    def datocasilla(self, n_fila, n_columna):
        fila = self.matriz.obtener(n_fila)
        if fila:
            return fila.obtener(n_columna)
        return None

    def desplegar(self):
        print("-"*10+"[Matriz]"+"-"*10)

        for i in range(self.matriz.tamano()):
            print("Columna", (i+1),"-"*10)
            for j in range(self.numero_filas):
                dato = self.datocasilla(i,j)
                dato.desplegar()


        
        

        
    
    