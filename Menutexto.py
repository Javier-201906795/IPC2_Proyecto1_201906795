


class Menu():

    
    def MenuPrincipal(self):
        print("*"*36)
        print("*"+" "*8 + " Sistema DataAgro " + " "*8 + "*")
        print("*"*36)
        print("* 1."+" Cargar archivo " + " "*15 + "*")
        print("* 2."+" Procesar archivo " + " "*13 + "*")
        print("* 3."+" Escribir archivos salida" + " "*6 + "*")
        print("* 4."+" Mostrar datos del estudiante " + " "*1 + "*")
        print("* 5."+" Generar gráfica " + " "*14 + "*")
        print("* 6."+" Salida " + " "*23 + "*")
        print("*"*36)
        print()

    def DatosEstudiante(self):
        print()
        print("/"*36)
        print("> Nombre: Javier Ricardo Yllescas Barrios")
        print("> Carnet: 201906795")
        print("> Introduccion a la Programación y Computación 2")
        print("> Sección: C")
        print("> 4to. Semestre")
        print("> Documentacion: ")
        print("> Github: https://github.com/Javier-201906795/IPC2_Proyecto1_201906795 ")
        print("/"*36)
    
    
    def MenuCargarArchivo(self):
        print()
        print("*"*34)
        print("*"+" "*8 + " Cargar archivo " + " "*8 + "*")
        print("*"*34)

    def MenuEscribirArchivo(self):
        print()
        print("*"*34)
        print("*"+" "*7 + " Escribir archivo " + " "*7 + "*")
        print("*"*34)
    
    
    def CargarArchivo(self):
        try:
            self.MenuCargarArchivo()
            ruta = str(input("Ingrese la ruta del archivo: "))
            nombre = str(input("Ingrese el nombre del archivo: "))
            print("_"*36)
            return ruta, nombre
        except:
            print("¡¡¡ Ingrese una opción válida. !!!")

    def EscribirSalida(self):
        try:
            self.MenuEscribirArchivo()
            ruta = str(input("Ingrese la ruta del archivo: "))
            nombre = str(input("Ingrese el nombre del archivo: "))
            print("_"*36)
            return ruta, nombre
        except:
            print("¡¡¡ Ingrese una opción válida. !!!")