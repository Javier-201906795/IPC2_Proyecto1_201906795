

from SistemaArchivos import SistemArchivos

class Sistema:
    def __init__(self):
        self.campos = None

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
    





    def ProcesarDatos(self):
        if self.campos != None:
            print(">>> Procesando datos...")
            #Recorrer datos
            for campo in self.campos:
                #Obtener ID
                id = campo.getAttribute('id')
                #Obtener Nombre
                nombre = campo.getAttribute('nombre')
                print("ID: ", id, " - Nombre: ", nombre)

                #> Cargar Estaciones Base
                
            
        else:
            print("¡¡¡ No hay datos para procesar !!!")
