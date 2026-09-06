categorias = {"familia" : "family", "trabajo" : "Work", "amigos" : "Friends"}


contactos = {
    1: {
        "Nombre": "Andres",
        "Telefono": "3123529960",
        "Correo": "andrescastañeda@gmail.com",
        "Categoria": "amigos"
    }
}

while True:
    print("1. Agregar contacto")
    print("2. Listar todos los contactos")
    print("3. Buscar contacto por nombre (búsqueda parcial insensible a mayúsculas/minúsculas)")
    print("4. Editar teléfono o correo.")
    print("5. Eliminar contacto.")
    print("6. Salir")
    try:
        opcion = int(input("Que opcion:"))
    except ValueError:
        print("Error: Debes escribir un numero:")
        continue
    
    if opcion == 1:
        try:
            Nombre = input("Nombre del contacto: ")
            Telefono = int(input("Telefono del contacto: "))
            Correo = input("Correo del contacto: ")
            Categoria = input("Categoria del contacto (familia, trabajo, amigos): ")
        except ValueError:
            print("ERROR : vuelve a intentarlo, algo mal digitado")
            continue    
        
        nuevo_id = max(contactos, default=0)+1
            
        contactos[nuevo_id] = {
            "Nombre": Nombre,
            "Telefono": Telefono,
            "Correo": Correo,
            "Categoria": Categoria
        } 
        print("Contacto registrado")
    
    elif opcion == 2:
        print("\nTelefono        Nombre       Categoria      Correo                        ")
        print("-"* 45) 
        
        for id_contacto, contacto in contactos.items():
            print(
                f"ID: {id_contacto}\n"
                f"Nombre: {contacto['Nombre']}\n"
                f"Telefono: {contacto['Telefono']}\n"
                f"Correo: {contacto['Correo']}\n"
                f"Categoria: {contacto['Categoria']}\n"
            )
            
    elif opcion == 3:
        buscar = input("Escribe el nombre del contacto".lower())
        encontrado = False

        for contacto in contactos.values():
            if buscar in contacto["Nombre"].lower():
                print(contacto)
                encontrado = True

        if not encontrado:
            print("Contacto no encontrado")
            
    elif opcion == 4:
        try:
            editar = int(input("Ingrese el ID:"))
        except:
            print("ERROE: El ID debe ser un numero")
            continue
        if editar in contactos:
            try:
                tipo = input("Editar telefono o Correo(TEL/CORREO): ".upper())
                if tipo == "TEL":
                    Telefono = int(input("Ingrese el nuevo telefono: "))
                    contactos [editar]["Telefono"] = Telefono
                    print("Contacto Actualizado") 
                elif tipo == "CORREO": 
                    Correo = (input("Ingrese el nuevo correo"))
                    contactos [editar]["Correo"] = Correo
                    print("Contacto Actualizado") 
            except ValueError:
                print("Vuelve a intentar, Solo se valen NUMEROS")
        else: 
            print("Numero no registrado")
        
    elif opcion == 5: 
        try:
            id_borrar = int(input("Ingrese el Id que quiere eliminar"))
            if id_borrar in contactos:
                del contactos[id_borrar] 
                print("Contacto eliminado")
            else:
                print("Nombre no registrado")
        except ValueError:
            print("Escribiste un numero, es un nombre")
            
    elif opcion == 6:
        print("Gracias por usar su agenda")
        break