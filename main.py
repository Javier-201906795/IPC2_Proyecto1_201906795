
from Menutexto import Menu
from SistemaCentral import Sistema
from SistemaArchivos import SistemArchivos

#> [Clase Texto Menus]
txt = Menu()
#> [Clase Sistema]
Sys = Sistema()


print("Proyecto IPC2")
print("Javier Ricardo Yllescas Barrios")
print("201906795")

while True:
    try:
        
        #>Menu Principal
        txt.MenuPrincipal()
        #> Opción ingresada
        ingreseopcion = int(input("Ingrese una opción: "))

        #Opicones
        if ingreseopcion == 1:
            print(">> Menu Cargar un archivo.")
            #Obtener Ruta
            rutacompleta = txt.CargarArchivo()
            #Cargar Archivos al Sistema
            Sys.CargarArchivos(rutacompleta)

        elif ingreseopcion == 2:
            print(">> Procesar el Archivo.")
            #Segmentar el archivo en categorias (sensores)
            Sys.SegmentarDatos()
            #Imprimir Campos de Cultivo
            Sys.desplegar()
            #Optimizar


        elif ingreseopcion == 3:
            print(">> Menu Escribir archivo de salida.")
            ruta, nombre = txt.EscribirSalida()
            print(ruta, " - ",nombre)
            ruta_junta = ruta + "\\"+ nombre
            #Obtener Lista campos de cultivo
            print(">>> Obtener campos de cultivo")
            campos_cultivo = Sys.obtenercamposcultivo()
            #Guardar Archivo
            print(">>>> Procesar informacion para guardar.")
            Archivo = SistemArchivos()
            Archivo.asignarrutaarchivo(ruta_junta)
            Archivo.guardarArchivo(campos_cultivo)

        elif ingreseopcion == 4:
            print(">> Menu Mostrar datos del estudiante")
            txt.DatosEstudiante()

        elif ingreseopcion == 5:
            print(">> Generar grafica")
            Sys.creargrafica()

        elif ingreseopcion == 6:
            print(">> Saliendo del programa...")
            break
        else:
            print(">> Ingrese una opcion dentro del rango de opciones")
        
        print()
    except Exception:
        print("¡¡ Ingrese una opción válida. !!")