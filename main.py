
from Menutexto import Menu

#> [Clase Texto Menus]
txt = Menu()


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
            ruta, nombre = txt.CargarArchivo()
            print(ruta, " - ",nombre)

        elif ingreseopcion == 2:
            print(">> Procesar el Archivo.")

        elif ingreseopcion == 3:
            print(">> Menu Escribir archivo de salida.")
            ruta, nombre = txt.EscribirSalida()
            print(ruta, " - ",nombre)

        elif ingreseopcion == 4:
            print(">> Menu Mostrar datos del estudiante")
            txt.DatosEstudiante()
        elif ingreseopcion == 5:
            print(">> Generar grafica")
        elif ingreseopcion == 6:
            print(">> Saliendo del programa...")
            break
        else:
            print(">> Ingrese una opcion dentro del rango de opciones")
        
        print()
    except Exception:
        print("¡¡ Ingrese una opción válida. !!")