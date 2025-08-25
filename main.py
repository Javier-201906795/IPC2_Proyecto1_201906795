
from Menutexto import Menu

#> [Clase Texto Menus]
txt = Menu()


while True:
    try:
        #>Menu Principal
        txt.MenuPrincipal()
        #> Opción ingresada
        ingreseopcion = input("Ingrese una opción: ")

        #Opicones
        if ingreseopcion == "1":
            print("Opción 1")
        elif ingreseopcion == "2":
            print("Opción 2")
        elif ingreseopcion == "9":
            print("Saliendo del programa...")
            break
        
        print("_"*25)
        print()
    except Exception:
        print("Ingrese una opción válida.")