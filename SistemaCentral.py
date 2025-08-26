

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
    



    def Buscarcampo(self, elemento):
        print(">>>> Buscando: ", elemento)
        for campo in self.campos:
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


    def ProcesarDatos(self):
        if self.campos != None:
            print(">>> Procesando datos...")
            #Recorrer datos
            for campo in self.campos:
                try:
                    #Obtener ID
                    id = campo.getAttribute('id')
                    #Obtener Nombre
                    nombre = campo.getAttribute('nombre')
                    print("ID: ", id, " - Nombre: ", nombre)


                    #> Cargar Estaciones Base
                    estacionbaseitem = self.Buscarcampo('estacionesBase')
                    print("Estaciones Base: ", estacionbaseitem)


                    


                except Exception as e:
                    print("¡¡¡ Error al procesar datos !!!")
                    print(e)
        else:
            print("¡¡¡ No hay datos para procesar !!!")
