
from ListaSimple import ListaSimple



from SistemaArchivos import SistemArchivos

class Sistema:
    def __init__(self):
        self.archivo = None
        self.estacionesbase = []
        self.sensoresSuelo = [] 
        self.sensoresCultivo = []

    def CargarArchivos(self, rutacompleta):
        print(">> Cargando archivos...")
        print(rutacompleta)
        #Leer archivo
        SA = SistemArchivos()
        #Ruta para TESTEOS
        rutacompleta = "G:\\2020\\2020_USAC\\Semestre14(2025)\\IPC2\\1_Laboratorio\\4_PROYECTO1\\IPC2_Proyecto1_201906795\\archivoejemplo.xml"
        print(rutacompleta)
        #Recivir lectura
        self.archivo = SA.leerArchivo(rutacompleta)
        print(self.archivo)
        #Validar
        if self.archivo != None:
            print(">>> Archivo cargado correctamente.")
        else:
            print("¡¡¡ Ocurio un error al cargar los archivos !!!")
            print("Intente nuevamente.")
    



    def Buscarcampo(self, elemento):
        print(">>>> Buscando: ", elemento)
        for campo in self.archivo:
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


    def SegmentarDatos(self):
        if self.archivo != None:
            print(">>> Procesando datos...")
            #Recorrer datos
            for campo in self.archivo:
                try:
                    #Obtener ID
                    id = campo.getAttribute('id')
                    #Obtener Nombre
                    nombre = campo.getAttribute('nombre')
                    print("ID: ", id, " - Nombre: ", nombre)

            #############################################################################
                    #> Cargar Estaciones Base
                    estacionbaseitem = self.Buscarcampo('estacionesBase')
                    print("Estaciones Base: ", estacionbaseitem)
                    #>> Validar Estacion Base
                    if estacionbaseitem == None:
                        print(">>>> No hay estaciones base. cargue otro documento.")
                        break
                    #>>> Obtener estaciones
                    for estacionbase in estacionbaseitem:
                        estaciones = estacionbase.getElementsByTagName('estacion')
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
                        #Imprimir valores
                        print()
                        print("-"*10 + " Estaciones Base " + "-"*10)
                        print(self.estacionesbase)
                        print("-"*30)
                        print()
                    
            #############################################################################
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
                        sensorS = it.getElementsByTagName(buscar2)
                        #>> Validar
                        if sensorS == None:
                            print(f">>>> No hay {buscar2}. cargue otro documento.")
                            break
                        #>>>> Obtener Atributos     
                        for it2 in sensorS:
                            id = it2.getAttribute('id')
                            nombre = it2.getAttribute('nombre')
                            print(">>> SensorS ID: ", id, " - Nombre: ", nombre)
                            # #>>>>> Guardar estacion
                            # self.sensoresSuelo.append([id, nombre])
                            #> Obtener items pequeños
                            frecuencia_item = it2.getElementsByTagName('frecuencia')
                            for frecu in frecuencia_item:
                                id2 = frecu.getAttribute('idEstacion')
                                valor2 = frecu.firstChild.data
                                print(f"ID: {id2} - Valor: {valor2}")
                                #>>>>> Guardar estacion
                                self.sensoresSuelo.append([id, nombre,id2, valor2])
                        #Imprimir valores
                        print()
                        print("-"*10 + " Sensores Suelo " + "-"*10)
                        print(self.sensoresSuelo)
                        print("-"*30)
                        print()

                #############################################################################
                    #> Cargar Sensores Cultivo
                    sensorcultivoitem = self.Buscarcampo('sensoresCultivo')
                    print("sensoresCultivo: ", sensorcultivoitem)
                    #>> Validar
                    if sensorcultivoitem == None:
                        print(">>>> No hay sensores de cultivo. cargue otro documento.")
                        break
                    #>>> Obtener sensores T
                    for estacionbase in sensorcultivoitem:
                        sensorT_item = estacionbase.getElementsByTagName('sensorT')
                        #>> Validar 
                        if sensorT_item == None:
                            print(">>>> No hay sensores T. cargue otro documento.")
                            break
                        #>>>> Obtener Atributos     
                        for sensorT in sensorT_item:
                            sensorT_id = sensorT.getAttribute('id')
                            sensorT_nombre = sensorT.getAttribute('nombre')
                            print(">>> SensorT ID: ", sensorT_id, " - Nombre: ", sensorT_nombre)
                            #>>>>> Obtener Elemento frecuencia
                            frecuencia_item = sensorT.getElementsByTagName('frecuencia')
                            for frecuencia in frecuencia_item:
                                idfrecuencia = frecuencia.getAttribute('id')
                                valorfrecuencia = frecuencia.firstChild.data
                                print(f"ID: {idfrecuencia} - Valor: {valorfrecuencia}")
                                #>>>>> Guardar Sensor T
                                self.sensoresCultivo.append([sensorT_id, sensorT_nombre, idfrecuencia, valorfrecuencia])
                        #Imprimir valores
                        print()
                        print("-"*10 + " Sensores Cultivo " + "-"*10)
                        print(self.sensoresCultivo)
                        print("-"*30)
                        print()

                except Exception as e:
                    print("¡¡¡ Error al segmentar los datos !!!")
                    print(e)
        else:
            print("¡¡¡ No hay datos para segmentar !!!")
