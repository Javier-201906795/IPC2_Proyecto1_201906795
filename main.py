
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
            print("Opción 1")
        elif ingreseopcion == 2:
            print("Opción 2")
        elif ingreseopcion == 4:
            print("Opción 4")
            txt.DatosEstudiante()
        elif ingreseopcion == 5:
            print("opcion 5")
        elif ingreseopcion == 6:
            print(">> Saliendo del programa...")
            break
        else:
            print(">> Ingrese una opcion dentro del rango de opciones")
        
        print()
    except Exception:
        print("¡¡ Ingrese una opción válida. !!")