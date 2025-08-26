#Ingresar, Leer y segmentar archivo
from xml.dom.minidom import parse

class SistemArchivos:
    def __init__(self):
        self.rutadelarchivo = None

    def leerArchivo(self, ruta):
            try:
                Dom = parse(ruta)
                campos_xml = Dom.getElementsByTagName('campo')
                return campos_xml
                
            except Exception as e:
                print("¡¡¡ Error al cargar archivos !!!")
                print(e)