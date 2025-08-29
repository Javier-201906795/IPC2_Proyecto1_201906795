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

                # Crear un campo
                campo = doc.createElement("campo")
                campo.setAttribute("id", "01")
                campo.setAttribute("nombre", "Campo agrícola 01")
                root.appendChild(campo)

                # ==============================
                # Estaciones Base Reducidas
                # ==============================
                estaciones = doc.createElement("estacionesBaseReducidas")
                campo.appendChild(estaciones)

                estacion1 = doc.createElement("estacion")
                estacion1.setAttribute("id", "e01")
                estacion1.setAttribute("nombre", "Estacion 01, Estacion 03")
                estaciones.appendChild(estacion1)

                estacion2 = doc.createElement("estacion")
                estacion2.setAttribute("id", "e02")
                estacion2.setAttribute("nombre", "Estacion 02, Estacion 05")
                estaciones.appendChild(estacion2)

                estacion4 = doc.createElement("estacion")
                estacion4.setAttribute("id", "e04")
                estacion4.setAttribute("nombre", "Estacion 04")
                estaciones.appendChild(estacion4)

                # ==============================
                # Sensores de Suelo
                # ==============================
                sensores_suelo = doc.createElement("sensoresSuelo")
                campo.appendChild(sensores_suelo)

                # Sensor S01
                sensorS1 = doc.createElement("sensorS")
                sensorS1.setAttribute("id", "s01")
                sensorS1.setAttribute("nombre", "Sensor S01")

                f1 = doc.createElement("frecuencia")
                f1.setAttribute("idEstacion", "e01")
                f1.appendChild(doc.createTextNode("700"))
                sensorS1.appendChild(f1)

                f2 = doc.createElement("frecuencia")
                f2.setAttribute("idEstacion", "e04")
                f2.appendChild(doc.createTextNode("1500"))
                sensorS1.appendChild(f2)

                sensores_suelo.appendChild(sensorS1)

                # Sensor S02
                sensorS2 = doc.createElement("sensorS")
                sensorS2.setAttribute("id", "s02")
                sensorS2.setAttribute("nombre", "Sensor S02")

                f3 = doc.createElement("frecuencia")
                f3.setAttribute("idEstacion", "e01")
                f3.appendChild(doc.createTextNode("8300"))
                sensorS2.appendChild(f3)

                sensores_suelo.appendChild(sensorS2)

                # Sensor S03
                sensorS3 = doc.createElement("sensorS")
                sensorS3.setAttribute("id", "s03")
                sensorS3.setAttribute("nombre", "Sensor S03")

                f4 = doc.createElement("frecuencia")
                f4.setAttribute("idEstacion", "e02")
                f4.appendChild(doc.createTextNode("8000"))
                sensorS3.appendChild(f4)

                f5 = doc.createElement("frecuencia")
                f5.setAttribute("idEstacion", "e04")
                f5.appendChild(doc.createTextNode("1500"))
                sensorS3.appendChild(f5)

                sensores_suelo.appendChild(sensorS3)

                # ==============================
                # Sensores de Cultivo
                # ==============================
                sensores_cultivo = doc.createElement("sensoresCultivo")
                campo.appendChild(sensores_cultivo)

                # Sensor T01
                sensorT1 = doc.createElement("sensorT")
                sensorT1.setAttribute("id", "t01")
                sensorT1.setAttribute("nombre", "Sensor T01")

                f6 = doc.createElement("frecuencia")
                f6.setAttribute("idEstacion", "e01")
                f6.appendChild(doc.createTextNode("4500"))
                sensorT1.appendChild(f6)

                f7 = doc.createElement("frecuencia")
                f7.setAttribute("idEstacion", "e02")
                f7.appendChild(doc.createTextNode("5200"))
                sensorT1.appendChild(f7)

                f8 = doc.createElement("frecuencia")
                f8.setAttribute("idEstacion", "e04")
                f8.appendChild(doc.createTextNode("950"))
                sensorT1.appendChild(f8)

                sensores_cultivo.appendChild(sensorT1)

                # ==============================
                # Guardar en archivo XML
                # ==============================
                xml_str = doc.toprettyxml(indent=" ", encoding="UTF-8")
            except:
                print("¡¡¡ Ocurrio un error al segmentar el archivo!!!")
            
            try:
                # Guardar en la ruta especificada
                with open(self.rutadelarchivo, "wb") as f:
                    f.write(xml_str)

                print(f"Archivo XML guardado en: {self.rutadelarchivo}")
            except:
                print("¡¡¡ Ocurrio un error al Crear el Archivo!!!")
        except:
            print("¡¡¡ Ocurrio un error al Guardar Archivo !!!")
            