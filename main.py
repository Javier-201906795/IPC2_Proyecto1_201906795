
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
        elif ingreseopcion == 6:
            print(">> Saliendo del programa...")
            break
        
        print("_"*25)
        print()
    except Exception:
        print("¡¡ Ingrese una opción válida. !!")