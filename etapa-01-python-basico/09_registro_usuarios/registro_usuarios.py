def contraseña_segura(contraseña):
    tiene_numero = any(caracter.isdigit() for caracter in contraseña)
    tiene_mayuscula = any(caracter.isupper() for caracter in contraseña)
    
    return(
        len(contraseña) >= 6
        and tiene_numero
        and tiene_mayuscula
    )

registro = {
    "Oscar": "1010_Oscar"
    }

while True:
    intentos_fallidos = 0
    print("1. Registro de usuario ")
    print("2. Inicio de sesion ")
    print("3. Cerrar Sesion")
    try:
        opcion = int(input("Ingrese la opcion a realizar: "))
    
        if opcion == 1:
            usuario = input("Ingrese el nombre de usuario: ")
            if usuario in registro:
                print("Usuario ya registrado")
            else: 
                pin = input(
               "Cree su contraseña(longitud mínima de 6 caracteres, un número y una mayúscula): " 
               )
                if contraseña_segura(pin):
                    registro[usuario] = pin
                    print("Usuario Registrado")
                else:
                    print("La contraseña no cumple los requisitos")
        elif opcion == 2:
            while intentos_fallidos < 3:
                usuario = input("Ingrese su nombre de usuario: ")
                if usuario in registro:
                    pin = input("Ingrese su contraseña: ")
                    print("Bienvenido")
                    break
                else:
                    print("El usuario no existe")
                    if registro[usuario] == pin:
                        #Menu post login
                        print("Bienvenido ", usuario, "a su menu post login")
                        while True:
                            print()
                            print("1. Ver Perfil")
                            print("2. Cambiar Contraseña")
                            print("3. Cerrar Sesion")
                            try:
                                opcion = int(input("Que desea hacer:"))
                                if opcion == 1:
                                    print("Usuario: ", usuario)
                                    print("Contraseña por seguridad")
                                elif opcion == 2:
                                    nueva_contraseña = input(
                                        "Ingrese su nueva contraseña"
                                    )
                                    if contraseña_segura(nueva_contraseña):
                                        registro[usuario] = nueva_contraseña
                                        print("Contraseña cambiada")
                                    else:
                                        print(
                                            "La contraseña necesita 6 caracteres, "
                                            "un número y una mayúscula"
                                        )
                                elif opcion == 3:
                                    print("Sesion Cerrada")
                                    break
                            except ValueError:
                                print("Tienes que escojer un numero")    
                    else :
                        intentos_fallidos += 1
                        print("Contraseña Incorrecta")
            if intentos_fallidos == 3:
                print("Demasiados intentos")        
        elif opcion == 3:
            print("Sesion Cerrada")
            break
    except ValueError:
        print("Tienes que escojer un numero")
        