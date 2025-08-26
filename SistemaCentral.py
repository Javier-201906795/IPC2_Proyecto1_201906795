

from SistemaArchivos import SistemArchivos

class Sistema:
    def CargarArchivos(self, rutacompleta):
        print(">> Cargando archivos...")
        print(rutacompleta)
        #Leer archivo
        SA = SistemArchivos()
        #Ruta para TESTEOS
        rutacompleta = "G:\\2020\\2020_USAC\\Semestre14(2025)\\IPC2\\1_Laboratorio\\4_PROYECTO1\\IPC2_Proyecto1_201906795\\archivoejemplo.xml"
        print(rutacompleta)
        #Recivir lectura
        campos = SA.leerArchivo(rutacompleta)
        print(campos)


        
