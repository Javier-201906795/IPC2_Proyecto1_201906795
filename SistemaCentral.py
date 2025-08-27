

from SistemaArchivos import SistemArchivos

class Sistema:
    def __init__(self):
        self.campos = None
        self.estacionesbase = []
        self.sensoresSuelo = [] 

    def CargarArchivos(self, rutacompleta):
        print(">> Cargando archivos...")
        print(rutacompleta)
        #Leer archivo
        SA = SistemArchivos()
        #Ruta para TESTEOS
        rutacompleta = "G:\\2020\\2020_USAC\\Semestre14(2025)\\IPC2\\1_Laboratorio\\4_PROYECTO1\\IPC2_Proyecto1_201906795\\archivoejemplo.xml"
        print(rutacompleta)
        #Recivir lectura
        self.campos = SA.leerArchivo(rutacompleta)
        print(self.campos)
        #Validar
        if self.campos != None:
            print(">>> Archivo cargado correctamente.")
        else:
            print("¡¡¡ Ocurio un error al cargar los archivos !!!")
            print("Intente nuevamente.")
    



    def Buscarcampo(self, elemento):
        print(">>>> Buscando: ", elemento)
        for campo in self.campos:
            try:
                estacionebaseitem = campo.getElementsByTagName(str(elemento))
                #>> Verificar si hay estaciones base
                if estacionebaseitem:
                    return estacionebaseitem
                else:
                    print(f"¡¡¡ No se encontro: {elemento} en el documento. !!!")
                    print(">>> No se puede procesar intenta cargar un archivo nuevo")
                    return None
            except Exception as e:
                    print(f"¡¡¡ Error al procesar datos, Error buscando {elemento} !!!")
                    print(e)


    def ProcesarDatos(self):
        if self.campos != None:
            print(">>> Procesando datos...")
            #Recorrer datos
            for campo in self.campos:
                try:
                    #Obtener ID
                    id = campo.getAttribute('id')
                    #Obtener Nombre
                    nombre = campo.getAttribute('nombre')
                    print("ID: ", id, " - Nombre: ", nombre)


                    #> Cargar Estaciones Base
                    estacionbaseitem = self.Buscarcampo('estacionesBase')
                    print("Estaciones Base: ", estacionbaseitem)
                    #>> Validar Estacion Base
                    if estacionbaseitem == None:
                        print(">>>> No hay estaciones base. cargue otro documento.")
                        break
                    #>>> Obtener estaciones
                    for estacionbase in estacionbaseitem:
                        estaciones = self.Buscarcampo('estacion')
                        #>> Validar estaciones
                        if estaciones == None:
                            print(">>>> No hay estaciones. cargue otro documento.")
                            break
                        #>>>> Obtener Atributos estaciones    
                        for estacion in estaciones:
                            estacion_id = estacion.getAttribute('id')
                            estacion_nombre = estacion.getAttribute('nombre')
                            print(">>> Estacion ID: ", estacion_id, " - Nombre: ", estacion_nombre)
                            #>>>>> Guardar estacion
                            self.estacionesbase.append([estacion_id, estacion_nombre])
                        print(self.estacionesbase)
                    

                    #> Cargar sensor Suelo
                    buscar = 'sensoresSuelo'
                    buscar2 = 'sensorS'
                    SensorSuelo = self.Buscarcampo(buscar)
                    print("Sensores Suelo: ", SensorSuelo)
                    # for nodo in SensorSuelo:
                    #     print(nodo.toprettyxml())
                    #>> Validar 
                    if SensorSuelo == None:
                        print(f">>>> No se encontro {buscar}. Cargue otro documento.")
                        break
                    #>>> Obtener items medianos
                    for it in SensorSuelo:
                        # print("-*-"*10)
                        # print(it.toprettyxml())
                        # print("-*-"*10)
                        sensorS = self.Buscarcampo(buscar2)
                        print("/*/"*10)
                        for nodo in sensorS:
                            print(nodo.toprettyxml())
                        print("/*/"*10)
                        #>> Validar
                        if sensorS == None:
                            print(f">>>> No hay {buscar2}. cargue otro documento.")
                            break
                        #>>>> Obtener Atributos     
                        for it2 in sensorS:
                            print("###"*5)
                            print(it2.toprettyxml())
                            print("###"*5)
                            id = it2.getAttribute('id')
                            nombre = it2.getAttribute('nombre')
                            print(">>> SensorS ID: ", id, " - Nombre: ", nombre)
                            #>>>>> Guardar estacion
                            self.sensoresSuelo.append([id, nombre])
                            #> Obtener items pequeños
                            buscar3 = 'frecuencia'
                            frecuencias = self.Buscarcampo(buscar3)
                            # for nodo in frecuencias:
                            #     print(nodo.toprettyxml())

                        print(self.sensoresSuelo)
                    
                        


                    


                except Exception as e:
                    print("¡¡¡ Error al procesar datos !!!")
                    print(e)
        else:
            print("¡¡¡ No hay datos para procesar !!!")
