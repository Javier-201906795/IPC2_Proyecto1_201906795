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

                # Crear un campo de ejemplo
                campo = doc.createElement("campo")
                campo.setAttribute("id", "01")
                campo.setAttribute("nombre", "Campo agrícola 01")
                root.appendChild(campo)

                # Ejemplo de estación
                estaciones = doc.createElement("estacionesBaseReducidas")
                campo.appendChild(estaciones)

                estacion1 = doc.createElement("estacion")
                estacion1.setAttribute("id", "e01")
                estacion1.setAttribute("nombre", "Estacion 01, Estacion 03")
                estaciones.appendChild(estacion1)

                # Convertir XML a string
                xml_str = doc.toprettyxml(indent=" ", encoding="UTF-8")

                # Guardar en la ruta especificada
                with open(self.rutadelarchivo, "wb") as f:
                    f.write(xml_str)

                print(f"Archivo XML guardado en: {self.rutadelarchivo}")
            except:
                print("¡¡¡ Ocurrio un error al Crear el Archivo!!!")
        except:
            print("¡¡¡ Ocurrio un error al Guardar Archivo !!!")
            