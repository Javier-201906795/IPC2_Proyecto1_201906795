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
        self.matriz_suelo_Patron = None
        self.matriz_cultivo_Patron = None
        self.matrizReducida = None

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

        print()
        print("\\/"*25)
        print()
        print(">>>> Matriz Suelo PATRON")
        if self.matriz_suelo_Patron != None:
            self.matriz_suelo_Patron.desplegar()
        
        print(">>>> Matriz Cultivo PATRON")
        if self.matriz_cultivo_Patron != None:
            self.matriz_cultivo_Patron.desplegar()
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
            #Crear Matrices PATRON
            self.matriz_suelo_Patron = Matriz(numero_estaciones, numero_sensores_suelo)
            self.matriz_cultivo_Patron = Matriz(numero_estaciones, numero_sensores_cultivo)

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
    

    def desplegarMatrices(self):
        #Imprimir
        print()
        print(">>>> Matriz Suelo")
        self.matriz_suelo.desplegar()
        
        print(">>>> Matriz Cultivo")
        self.matriz_cultivo.desplegar()

        #Imprimir
        print()
        print(">>>> Matriz Suelo PATRON")
        self.matriz_suelo_Patron.desplegar()
        
        print(">>>> Matriz Cultivo PATRON")
        self.matriz_cultivo_Patron.desplegar()

    
    
    def CrearMatricesPatron(self):
        try:
            print(">>>> tomando datos.")
            #Imprimir para ver las matrices vacias
            print(">> Matriz Suelo PATRON")
            self.matriz_suelo_Patron.desplegar()
            print(">> Matriz Cultivo PATRON")
            self.matriz_cultivo_Patron.desplegar()

            #Obtener datos de las matrices
            #################################################
            #>Cultivo
            max_columna = self.matriz_cultivo.numero_columnas
            max_fila = self.matriz_cultivo.numero_filas
            print("-"*5+"[Matriz Cultivo PATRON]")
            for i in range(max_columna):
                for j in range(max_fila):
                    print(f'[{i},{j}]')
                    self.matriz_cultivo.datocasilla(i,j).desplegar()
                    #Obtener Valor casilla
                    casilla = self.matriz_cultivo.datocasilla(i,j)
                    valor = casilla.valor
                    #Convertir a numero
                    try:
                        valornumero = int(valor)
                        #convertir
                        if valornumero != 0:
                            print("cambiar -> 1")
                            datonuevo = Frecuencia(casilla.id,"1")
                            #Rempalzar
                            self.matriz_cultivo_Patron.asignarValor(j,i,datonuevo)
                        else:
                            datonuevo = Frecuencia(casilla.id,"0")
                            #Rempalzar
                            self.matriz_cultivo_Patron.asignarValor(j,i,datonuevo)
                    except:
                        print(f"¡¡¡ No se pudo convertir en valor la casilla [{i},{j}] !!!")
                    
            print("-"*10+"[ Matriz Patron Cultivo ]"+"-"*10)
            self.matriz_cultivo_Patron.desplegar()
            
            #################################################
            #>Suelo
            max_columna = self.matriz_suelo.numero_columnas
            max_fila = self.matriz_suelo.numero_filas
            print("-"*5+"[Matriz Suelo PATRON]")
            for i in range(max_columna):
                for j in range(max_fila):
                    print(f'[{i},{j}]')
                    self.matriz_suelo.datocasilla(i,j).desplegar()
                    #Obtener Valor casilla
                    casilla = self.matriz_suelo.datocasilla(i,j)
                    valor = casilla.valor
                    #Convertir a numero
                    try:
                        valornumero = int(valor)
                        #convertir
                        if valornumero != 0:
                            print("cambiar -> 1")
                            datonuevo = Frecuencia(casilla.id,"1")
                            #Rempalzar
                            self.matriz_suelo_Patron.asignarValor(j,i,datonuevo)
                        else:
                            datonuevo = Frecuencia(casilla.id,"0")
                            #Rempalzar
                            self.matriz_suelo_Patron.asignarValor(j,i,datonuevo)
                    except:
                        print(f"¡¡¡ No se pudo convertir en valor la casilla [{i},{j}] !!!")
                    
            print("-"*10+"[ Matriz Patron Suelo ]"+"-"*10)
            self.matriz_suelo_Patron.desplegar()



        except:
            print("¡¡¡ Ocurrio un error al formar Matrices Patron !!!")


    def CrearMatricesReducidas(self):
        try:
            print("\n>>> Procesando Matrices Reducidas...\n")
            
            
            print("\n>>>> Procesadno Matriz PATRON Sensores")
            
            #Inicio_#################### [ BUSCAR FILAS REPETIDAS ] #########################
            #-----------------------------
            #>Obtener Valores Fila
            max_colum = self.matriz_suelo_Patron.numero_columnas
            max_fila = self.matriz_suelo_Patron.numero_filas
            print(f'columnas: {max_colum} y filas: {max_fila}')
            #Almacenar FILAS
            ListaFilas = ListaSimple()
            FilaValores = ""
            contador = 0
            indicadorfila = 0
            #Recorrer matriz
            for h in range(max_fila):
                for i in range(max_colum):
                    for j in range(max_fila):
                        # print(f'[{i},{j}]')
                        #Obtener primero
                        if j == indicadorfila:
                            print(f"----> [{i},{j}]")
                            valoractual = self.matriz_suelo_Patron.datocasilla(i,j).valor
                            print(valoractual)
                            FilaValores += str(valoractual)+","
                
                #Almacenar Fila
                print(f'Filavalores = {FilaValores}')
                nuevaFila = FilaD(indicadorfila,FilaValores)
                ListaFilas.agregar(nuevaFila)
                #Reiniciar Fila
                FilaValores = ""
                indicadorfila +=1

            print("\n>> Resumen ListaFilas\n")  
            ListaFilas.desplegar()
            print("\n>> Fin Resumen ListaFilas\n")  

            #-----------------------------
            ListaFilasRepetidas = ListaSimple()
            print(">> Comparando Valores")
            max_tamano = ListaFilas.tamano() - 1
            #Primer dato a comparar
            dato = ListaFilas.obtenerprimero()
            contador = 0
            #CICLO 1
            max_ciclo = ListaFilas.tamano() - 1
            print(f'tamaño lista y ciclos = {max_ciclo}')
            for i in range(max_ciclo):
                print("-> contador: ", contador)
                #Obtener Primer dato si es segunda vez
                if contador >= 1:
                    dato = dato.siguiente
                    if dato == None:
                        break
                # dato.valor.desplegar()
                datovalor = dato.valor.obtenervalor()
                # print(datovalor)
                #Obtener siguiente dato
                dato2 = dato
                for i in range(max_tamano):
                    #siguiente
                    dato2 = dato2.siguiente
                    if dato2 != None:
                        # dato2.valor.desplegar()
                        dato2valor = dato2.valor.obtenervalor()
                        print(f'Comparara {datovalor} es =  a {dato2valor}')
                        #Comparar
                        if datovalor == dato2valor:
                            print(f">>>>> Se encontraron dos patrones iguales")
                            print(f'>>>>> Fila {dato.valor.obtenerfila()} = Fila {dato2.valor.obtenerfila()}')
                            #Guardar valores
                            filaReptida = FilasRepetidas(datovalor,dato2.valor.obtenerfila(),dato.valor.obtenerfila())
                            ListaFilasRepetidas.agregar(filaReptida)
                    else:
                        break
                
                contador += 1

            #Imprimir
            print("\n"+"-"*10+"[ Lista Filas Repetidas ]" + "-"*10)
            ListaFilasRepetidas.desplegar()
            print()
            #-----------------------------
            #Fin_#################### [ FIN buscar filas repetidas ] #########################
            
            
            
            #Inicio_#################### [ CREAR MATRIZ REDUCIDA ] #########################
            print("\n >Creando Matriz Reducida")
            num_columnas = self.matriz_suelo_Patron.numero_columnas
            #por cada fila repetida es 1 fila menos
            num_filas = self.matriz_suelo_Patron.numero_filas - ListaFilasRepetidas.tamano()
            print(f"filas totales: {self.matriz_suelo_Patron.numero_filas} - {ListaFilasRepetidas.tamano()} = {num_filas}")

            #Crear Matriz
            self.matrizReducida = Matriz(num_filas,num_columnas)

            #Imprimir
            self.matrizReducida.desplegar()
            print("\n\n")

            # #Imprimir matriz sensores
            # print("\n\n")
            # self.matriz_suelo.desplegar()
            # print("\n\n")

            #Llenar Matriz
            print(">Llenando Matrices Reducidas")
            #Obtner filas que se repiten
            casilla = ListaFilasRepetidas.obtenerprimero()
            for i in range(ListaFilasRepetidas.tamano()):
                #Pasar al siguiente
                if i >= 1:
                    casilla = casilla.siguiente
                #Obtener filas
                fila1 = casilla.valor.obtenerfila1()
                fila2 = casilla.valor.obtenerfila2()
                print(f'Fila{fila1} = Fila{fila2}')
                #Obtener valores filas
                print(f'---[ Fila{fila1} ]---')
                for j in range(self.matriz_suelo.numero_columnas):
                    #Fila1
                    fila1_casillamatriz = self.matriz_suelo.datocasilla(j,fila1)
                    fila1_casillamatriz_valor = fila1_casillamatriz.valor
                    print(f'F{fila1}-> [{j},{fila1}] -> {fila1_casillamatriz_valor}')
                    #Fila2
                    fila2_casillamatriz = self.matriz_suelo.datocasilla(j,fila2)
                    fila2_casillamatriz_valor = fila2_casillamatriz.valor
                    print(f'F{fila2}-> [{j},{fila2}] -> {fila2_casillamatriz_valor}')
                    #Sumar
                    try:
                        dato_1 = int(fila1_casillamatriz_valor)
                        dato_2 = int(fila2_casillamatriz_valor)
                        suma = dato_1 + dato_2
                    except:
                        print("Error al convertir a nuemro valores")
                    print("suma = ",suma)
                    print("\n\n")
                    #Guardar Valor en Matriz Reducida
                    dato = self.matrizReducida.datocasilla(0,0)
                    dato.desplegar()
                    

                print("---------------")

            


        except Exception as e:
            print("\n¡¡¡ Ocurrio un error al crear matrices Reducidas !!!")
