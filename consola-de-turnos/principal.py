import numeros

#MENU DE INTERACCION PARA EL USUARIO


def menu():

    print("Menú de opciones\nPorfavor elija el sector donde deseé un turno:")

    while True:
        print("[P]-Perfumería\n[F]-Farmacia\n[C]-Cosmetica")
        try:
            mi_sector = input("Ingrese su sector: ").upper()
            ["P","F","C"].index(mi_sector)
        except:
            print("Por favor elija entre las opciones correctas")
        else:
            break
    numeros.decorar_generador(mi_sector)


def inicio():

    while True:
        menu()
        try:
            otro_turno = input("Quieres sacar otro turno? [S]/[N]").upper()
            ["S","N"].index(otro_turno)
        except:
            print("Porfavor ingrese 'S' para SI y 'N' para NO")
            otro_turno = input("Quieres sacar otro turno? [S]/[N]").upper()
            ["S", "N"].index(otro_turno)
            if otro_turno == "N":
                print("Gracías por su visita.")
                break

        else:
            if otro_turno == "N":
                print("Gracías por su visita.")
                break


inicio()

