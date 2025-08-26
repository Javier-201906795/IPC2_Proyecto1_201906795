

from SistemaArchivos import SistemArchivos

class Sistema:
    def CargarArchivos(self, rutacompleta):
        print(">> Cargando archivos...")
        print(rutacompleta)
        SA = SistemArchivos()
        campos = SA.leerArchivo(rutacompleta)
        print(campos)

        
