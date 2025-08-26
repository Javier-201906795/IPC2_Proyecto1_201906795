

from SistemaArchivos import SistemArchivos

class Sistema:
    def CargarArchivos(self, rutacompleta):
        print(">> Cargando archivos...")
        print(rutacompleta)
        #Leer archivo
        SA = SistemArchivos()
        #Recivir lectura
        campos = SA.leerArchivo(rutacompleta)
        print(campos)
        

        
