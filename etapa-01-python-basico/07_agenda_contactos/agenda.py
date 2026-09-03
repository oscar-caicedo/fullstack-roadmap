Categoria = {"familia" : "family", "trabajo" : "Work", "amigos" : "Friends"}

contactos = {
    1: {"Nombre" : "Andres"},
    2: {"Telefono" : "3123529960"},
    3: {"Correo" : "andrescastañeda@gmail.com"},
    4: {"Categoria" : "amigos"}
}

while True:
    print("1. Agregar contacto")
    print("2. Listar todos los contactos")
    print("3. Buscar contacto por nombre (búsqueda parcial insensible a mayúsculas/minúsculas)")
    print("4. Editar teléfono o correo.")
    print("5. Eliminar contacto.")
    opcion = int(input("Que opcion:"))
    
    if opcion == 1:
        try:
            Nombre = input("Nombre del contacto: ")
            Telefono = int(input("Telefono del contacto: "))
            Correo = input("Correo del contacto: ")
            Categoria = input("Categoria del contacto (familia, trabajo, amigos): ")
        except ValueError:
            print("vuelve a intentarlo, algo mal digitado")    
        
        if Telefono in contactos:
            print("Numero ya registrado")
        else:
            contactos = {"Nombre ": Nombre,
                        "Telefono ": Telefono,
                        "Correo ": Correo,
                        "Categoria": Categoria
                        } 
            print("Contacto registrado")
    
    elif opcion == 2:
        print("\nTelefono        Nombre       Categoria      Correo                        ")
        print("-"* 45) 
        
        for agenda in contactos.items():
            print (
            f"{contactos ['Nombre']}:"
            f"{contactos ['Telefono']:<10}"
            f"{contactos ['Correo']:<40}"
            f"{contactos ['Categoria']}"
            )
            
    elif opcion == 3:
        buscar = print("Escribe el nombre del contacto".Upper().Lower())
        if buscar in contactos:
            print(
                f"Los datos del contacto son\n"
                f"Nombre: {Nombre}\n"
                f"Telefono: {Telefono}\n"
                f"Correo: {Correo}\n"
                f"Categoria: {Categoria}"    
                )
        else:
            print("Contacto no encontrado")
            
    elif opcion == 4:
        editar = int(input("Escribe el numero del telefono:"))
        if editar in contactos:
            try:
                user = input("Editar telefono o Correo(TEL/CORREO): ".Upper().Lower())
                if user == "TEL":
                    Telefono = int(input("Ingrese el nuevo telefono: "))
                    Telefono [Nombre]["Telefono"] = Telefono 
                elif user == "CORREO":
                    Correo = int(input("Ingrese el nuevo correo"))
                    Correo [Nombre]["Correo"] = Correo
            except ValueError:
                print("Vuelve a intentar, Solo se valen NUMEROS")
        else: 
            print("Numero no registrado")
        
    elif opcion == 5: 
        try:
            nombre_borrar = input("Ingrese el nombre del contacto que quiere eliminar")
            if nombre_borrar in contactos:
                del contactos[nombre_borrar]
                print("Contacto eliminado")
            else:
                print("Nombre no registrado")
        except ValueError:
            print("Escribiste un numero, es un nombre")
            
    elif opcion == 6:
        print("Gracias por usar su agenda")
        break