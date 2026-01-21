from funciones_proyecto.funciones import *

salir = False
estado = "principal"
menu_opciones = ()

while not salir:
    while estado == "principal":
        cabecera = getHeader("Menú Principal",70)
        menu_opciones = ("Login", "Create User", "Replay Adventure", "Reports", "Exit")
        print(cabecera + menu_opc(menu_opciones))
        opc = validar_opcion(menu_opciones)
        if opc == 1:
            estado = "Login"
        elif opc == 2:
            estado = "Create User"
        elif opc == 3:
            estado = "Replay Adventure"
        elif opc == 4:
            estado = "Reports"
        elif opc == 5: # Exit
            print("Chau")
            estado = ""
            salir = True

    while estado == "Login":
        cabecera = getHeader("Iniciando Sesión", 70)
        print(cabecera)
        login()
        input("Enter para volver")
        estado = "principal"
    while estado == "Create User":
        cabecera = getHeader("Creando Usuario", 70)
        print(cabecera)
        nombre = input("Introduce un nombre de usuario: ")
        create_user_nombre(nombre)
        password = input("Introduce la contraseña: ")
        create_user_password(password)
        input("Enter para volver")
        estado = "principal"
    while estado == "Replay Adventure":
        cabecera = getHeader("Replay Adventure", 70)
        print(cabecera)
        input("Enter para volver")
        estado = "principal"
    while estado == "Reports":
        cabecera = getHeader("Replay Adventure", 70)
        print(cabecera)
        input("Enter para volver")
        estado = "principal"
