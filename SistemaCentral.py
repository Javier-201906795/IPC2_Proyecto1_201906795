
from ListaSimple import ListaSimple
from NodosSistema import Estacion, Frecuencia, SensorSuelo, SensorCultivo
from CampoAgricola import CampoAgricola


from SistemaArchivos import SistemArchivos

class Sistema:
    def __init__(self):
        self.archivo = None
        self.camposcultivo = ListaSimple()
        

    def CargarArchivos(self, rutacompleta):
        print(">> Cargando archivos...")
        print(rutacompleta)
        #Leer archivo
        SA = SistemArchivos()
        #Ruta para TESTEOS
        rutacompleta = "G:\\2020\\2020_USAC\\Semestre14(2025)\\IPC2\\1_Laboratorio\\4_PROYECTO1\\IPC2_Proyecto1_201906795\\archivoejemplo2.xml"
        print(rutacompleta)
        #Recivir lectura
        self.archivo = SA.leerArchivo(rutacompleta)
        print("Archivo: ",self.archivo)
        #Validar
        if self.archivo != None:
            print(">>> Archivo cargado correctamente.")
        else:
            print("¡¡¡ Ocurio un error al cargar los archivos !!!")
            print("Intente nuevamente.")
    



    def Buscarcampo(self, elemento,segmentoArchivo):
        print(">>>> Buscando: ", elemento)
        
        try:
            estacionebaseitem = segmentoArchivo.getElementsByTagName(str(elemento))
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

        #Obtener campos
        campos_item = self.archivo.getElementsByTagName('campo')
        # #imprimir
        # for nodo in campos_item:
        #     print(nodo.toprettyxml())

        if campos_item != None:
            print(">>> Procesando datos...")
            #Recorrer datos
            for campo in campos_item:
                try:
                    #Obtener ID
                    id = campo.getAttribute('id')
                    #Obtener Nombre
                    nombre = campo.getAttribute('nombre')
                    #Crear Campo
                    campo_Agricola = CampoAgricola(id,nombre)
                    campo_Agricola.desplegar()


            #############################################################################
                    #> Cargar Estaciones Base
                    estacionbaseitem = self.Buscarcampo('estacionesBase', campo)
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
                            estacion_nodo = Estacion(estacion_id, estacion_nombre)
                            estacion_nodo.desplegar()
                            #>>>>> Guardar estacion
                            campo_Agricola.estaciones_base.agregar(estacion_nodo)
                            
                        #Imprimir valores
                        print()
                        print("°"+"-"*10 + " Estaciones Base " + "-"*10)
                        campo_Agricola.estaciones_base.desplegar()
                        print("-"*30)
                        print()
                    
            #############################################################################
                    #> Cargar sensor Suelo
                    buscar = 'sensoresSuelo'
                    buscar2 = 'sensorS'
                    SensorSuelo_item = self.Buscarcampo(buscar,campo)
                    print("Sensores Suelo: ", SensorSuelo_item)
                    #>> Validar 
                    if SensorSuelo_item == None:
                        print(f">>>> No se encontro {buscar}. Cargue otro documento.")
                        break
                    #>>> Obtener items medianos
                    for it in SensorSuelo_item:
                        sensorS = it.getElementsByTagName(buscar2)
                        #>> Validar
                        if sensorS == None:
                            print(f">>>> No hay {buscar2}. cargue otro documento.")
                            break
                        #>>>> Obtener Atributos     
                        for it2 in sensorS:
                            id = it2.getAttribute('id')
                            nombre = it2.getAttribute('nombre')
                            Sensor_Suelo = SensorSuelo(id, nombre)
                            Sensor_Suelo.desplegar()
                            #> Obtener items pequeños
                            frecuencia_item = it2.getElementsByTagName('frecuencia')
                            for frecu in frecuencia_item:
                                id2 = frecu.getAttribute('idEstacion')
                                valor2 = frecu.firstChild.data
                                frecuencia_nodo = Frecuencia(id2, valor2)
                                frecuencia_nodo.desplegar()
                                #>>>>> Guardar Lectura
                                Sensor_Suelo.agregarLectura(frecuencia_nodo)
                            #Guardar Sensor
                            campo_Agricola.sensores_suelo.agregar(Sensor_Suelo)
                        #Imprimir valores sensor
                        print()
                        print("°°"+"-"*10 + " Sensores Suelo " + "-"*10)
                        campo_Agricola.sensores_suelo.desplegar()
                        print("-"*30)
                        print()

                #############################################################################
                    #> Cargar Sensores Cultivo
                    sensorcultivoitem = self.Buscarcampo('sensoresCultivo', campo)
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
                            #Crear Nodo Sensor T
                            Sensor_Cultivo = SensorCultivo(sensorT_id, sensorT_nombre)
                            Sensor_Cultivo.desplegar()
                            #>>>>> Obtener Elemento frecuencia
                            frecuencia_item = sensorT.getElementsByTagName('frecuencia')
                            for frecuencia in frecuencia_item:
                                idfrecuencia = frecuencia.getAttribute('idEstacion')
                                valorfrecuencia = frecuencia.firstChild.data
                                frecuencia_nodo = Frecuencia(idfrecuencia, valorfrecuencia)
                                frecuencia_nodo.desplegar()
                                #>>>>> Guardar Lectura
                                Sensor_Cultivo.agregarLectura(frecuencia_nodo)
                            #Guardar Sensor
                            campo_Agricola.sensores_cultivo.agregar(Sensor_Cultivo)    
                            
                        #Imprimir valores
                        print()
                        print("°°°"+"-"*10 + " Sensores Cultivo " + "-"*10)
                        campo_Agricola.sensores_cultivo.desplegar()
                        print("-"*30)
                        print()
                    
                    #imprimir Resumen
                    print("\n \n")
                    print("°"*10+" [ Resumen Campo Agricola ] "+"°"*10)
                    campo_Agricola.desplegar()

                    #Crear Matrices
                    print(">>> Agrupando en Matrices")
                    campo_Agricola.RealizarMatrices()

                    #Alamacenar Campo
                    self.camposcultivo.agregar(campo_Agricola)

                except Exception as e:
                    print("¡¡¡ Error al segmentar los datos !!!")
                    print(e)
        else:
            print("¡¡¡ No hay datos para segmentar !!!")



    def desplegar(self):
        print("/"*10+" [ Lista Campos de Cultivo ] " + "/"*10)
        self.camposcultivo.desplegar()

    