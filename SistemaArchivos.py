#Ingresar, Leer y segmentar archivo
from xml.dom.minidom import Document, parse

class SistemArchivos:
    def __init__(self):
        self.rutadelarchivo = None

    def leerArchivo(self, ruta):
            try:
                Dom = parse(ruta)
                # campos_xml = Dom.getElementsByTagName('campo')
                return Dom
                
            except Exception as e:
                print("¡¡¡ Error al cargar archivos !!!")
                print(e)
    
    def asignarrutaarchivo(self, ruta):
         self.rutadelarchivo = ruta
         print(">> ruta: ", self.rutadelarchivo)

    def guardarArchivo(self,Lista_campos):
        self.rutadelarchivo = "G:\\2020\\2020_USAC\\Semestre14(2025)\\IPC2\\1_Laboratorio\\4_PROYECTO1\\IPC2_Proyecto1_201906795\\archivosalida.xml"
        try:
            print(">>>> Leyendo archivo.")
            print(self.rutadelarchivo," -> ",Lista_campos)
            print(">>>>> Creando Archivo")
            try:
                doc = Document()
                root = doc.createElement("camposAgricolas")
                doc.appendChild(root)

                nodocampo = Lista_campos.obtenerprimero()
                
                numerocampos = Lista_campos.tamano()

                for i in range(numerocampos):
                    #Obtener siguiente
                    if i >= 1 :
                        nodocampo = nodocampo.siguiente
                        if nodocampo == None:
                            break
                    # Crear un campo
                    print(">Creando campo",i)
                    nodocampo_valor = nodocampo.valor
                    print("campo-> id:",nodocampo_valor.id,"nombre:", nodocampo_valor.nombre)
                    campo = doc.createElement("campo")
                    campo.setAttribute("id", nodocampo_valor.id)
                    campo.setAttribute("nombre", nodocampo_valor.nombre)
                    root.appendChild(campo)
                    

                    # ==============================
                    # Estaciones Base Reducidas SUELO
                    # ==============================
                    matrizSueloReducida = nodocampo_valor.matrizReducida
                    estaciones = doc.createElement("estacionesSueloReducidas")
                    campo.appendChild(estaciones)

                    #Recorrer matriz
                    print(f"Matriz tamaño columnas: {matrizSueloReducida.numero_columnas} , filas: {matrizSueloReducida.numero_filas}")
                    for i in range(matrizSueloReducida.numero_columnas):
                        for j in range(matrizSueloReducida.numero_filas):
                            print(f"[{i},{j}]")
                            matriz_casilla = matrizSueloReducida.datocasilla(i,j)
                            if matriz_casilla and hasattr(matriz_casilla, 'id') and hasattr(matriz_casilla, 'valor'):
                                estacion1 = doc.createElement("estacion")
                                estacion1.setAttribute("id", str(matriz_casilla.id))
                                estacion1.setAttribute("valor", str(matriz_casilla.valor))
                                estaciones.appendChild(estacion1)
                            else:
                                print(f"Casilla vacía o inválida en [{i},{j}]")
                    
                    # ==============================
                    # Estaciones Base Reducidas CULTIVO
                    # ==============================
                    matrizCultivoReducida = nodocampo_valor.matrizReducida_Cultivo
                    estaciones = doc.createElement("estacionesCultivoReducidas")
                    campo.appendChild(estaciones)

                    #Recorrer matriz
                    print(f"Matriz tamaño columnas: {matrizCultivoReducida.numero_columnas} , filas: {matrizCultivoReducida.numero_filas}")
                    for i in range(matrizCultivoReducida.numero_columnas):
                        for j in range(matrizCultivoReducida.numero_filas):
                            print(f"[{i},{j}]")
                            matriz_casilla = matrizCultivoReducida.datocasilla(i,j)
                            if matriz_casilla and hasattr(matriz_casilla, 'id') and hasattr(matriz_casilla, 'valor'):
                                estacion1 = doc.createElement("estacion")
                                estacion1.setAttribute("id", str(matriz_casilla.id))
                                estacion1.setAttribute("valor", str(matriz_casilla.valor))
                                estaciones.appendChild(estacion1)
                            else:
                                print(f"Casilla vacía o inválida en [{i},{j}]")


                    # ==============================
                    # Sensores de Suelo
                    # ==============================
                    Lista_sensores_suelo = nodocampo_valor.sensores_suelo
                    sensores_suelo = doc.createElement("sensoresSuelo")
                    campo.appendChild(sensores_suelo)

                    sensor = Lista_sensores_suelo.obtenerprimero()
                    

                    for i in range(Lista_sensores_suelo.tamano()):
                        if i >=1:
                            sensor = sensor.siguiente
                        sensor_valor = sensor.valor
                        # Sensor S01
                        sensorS1 = doc.createElement("sensorS")
                        sensorS1.setAttribute("id", sensor_valor.id)
                        sensorS1.setAttribute("nombre", sensor_valor.nombre)
                        #Frecuencias
                        Lista_frecuencias = sensor_valor.lecturas
                        datof = Lista_frecuencias.obtenerprimero()
                        for j in range(Lista_frecuencias.tamano()):
                            if j >= 1:
                                datof.siguiente
                            datof_valor = datof.valor
                            f1 = doc.createElement("frecuencia")
                            f1.setAttribute("idEstacion", datof_valor.id)
                            f1.appendChild(doc.createTextNode(str(datof_valor.valor)))
                            sensorS1.appendChild(f1)

                        sensores_suelo.appendChild(sensorS1)


                    # ==============================
                    # Sensores de Cultivo
                    # ==============================
                    Lista_sensores_suelo = nodocampo_valor.sensores_cultivo
                    sensores_cultivo = doc.createElement("sensoresCultivo")
                    campo.appendChild(sensores_cultivo)

                    sensor = Lista_sensores_suelo.obtenerprimero()

                    for i in range(Lista_sensores_suelo.tamano()):
                        if i >=1:
                            sensor = sensor.siguiente
                        sensor_valor = sensor.valor
                        for j in range(Lista_sensores_suelo.tamano()):
                            # Sensor T01
                            sensorT1 = doc.createElement("sensorT")
                            sensorT1.setAttribute("id", sensor_valor.id)
                            sensorT1.setAttribute("nombre", sensor_valor.nombre)
                            #Frecuencias
                            Lista_frecuencias = sensor_valor.lecturas
                            datof = Lista_frecuencias.obtenerprimero()
                            for j in range(Lista_frecuencias.tamano()):
                                if j >= 1:
                                    datof.siguiente
                                datof_valor = datof.valor
                                f6 = doc.createElement("frecuencia")
                                f6.setAttribute("idEstacion", datof_valor.id)
                                f6.appendChild(doc.createTextNode(str(datof_valor.valor)))
                                sensorT1.appendChild(f6)
                            sensores_cultivo.appendChild(sensorT1)
                    
                    
             

                    

                    

                
            except:
                print("¡¡¡ Ocurrio un error al segmentar el archivo!!!")
            
            try:
                # ==============================
                # Guardar en archivo XML
                # ==============================
                xml_str = doc.toprettyxml(indent=" ", encoding="UTF-8")
                # Guardar en la ruta especificada
                with open(self.rutadelarchivo, "wb") as f:
                    f.write(xml_str)

                print(f"Archivo XML guardado en: {self.rutadelarchivo}")
            except:
                print("¡¡¡ Ocurrio un error al Crear el Archivo!!!")
        except:
            print("¡¡¡ Ocurrio un error al Guardar Archivo !!!")
            