inventario = {
    1: {"Nombre": "Laptop", "Precio": 1400, "Cantidad":10},
    2: {"Nombre": "Mouse", "Precio": 90, "Cantidad":15},
    3: {"Nombre": "Silla", "Precio": 500, "Cantidad":12},
    4: {"Nombre": "Teclado", "Precio": 400, "Cantidad":20},
    5: {"Nombre": "Luces", "Precio": 40, "Cantidad":16},
}

while True:
    print("1. Registar nuevo producto ")    
    print("2. Listar productos existentes con formato de tabla")   
    print("3. Actualizar precio o stock de un producto por ID")   
    print("4. Eliminar producto por ID")   
    print("5. Salir ")   

    opcion = input("Escoje la opcion: ")
    
    if opcion =="1":  # Pedir ID Nombre, Precio, Cantidad 
        Id = int(input("Ingrese el ID del producto: ")) 
        Nombre = (input("Ingrese el nombre del producto: "))
        Precio = int(input("Ingrese el precio del producto: "))
        Cantidad = int(input("Ingrese la cantida del producto: "))
        if Id in inventario:
            print("Ese ID ya existe")
        else:    
            inventario[Id] = { 
                "Nombre": Nombre, 
                "Precio": Precio, 
                "Cantidad": Cantidad
            }
            print("Producto Registrado")
        
    elif opcion == "2":
        print("\nID   Nombre             Precio      Stock")
        print("-"*40)
        
        for id_producto, producto in inventario.items():
            print(
                f"{id_producto:<6} "
                f"{producto['Nombre']:<18} "
                f"{producto['Precio']:<9} "
                f"{producto['Cantidad']} "
            )
            
    elif opcion == "3":
        print ("A que producto le quiere cambiar el precio y stock")
        Id = int(input("Ingrese el ID: "))
        if Id in inventario:
            Precio = int(input("Ingrese el nuevo precio: "))
            Cantidad = int(input("Ingrese el nuevo stock del producto: "))
            
            inventario[Id]["Precio"] = Precio
            inventario[Id]["Cantidad"] = Cantidad
            
            print(
            f"Producto actualizado\n"
            f"Precio: {Precio}\n"
            f"Stock: {Cantidad}"
            )
        else:
         print ("Producto no encontrado")
            
    elif opcion == "4":
        try:
            id_borrar = int(input("Ingrese el ID del producto que desea eliminar: "))
        
            if id_borrar in inventario:
                del inventario[id_borrar]
                print("Producto eliminado correctamente")
            else:
                print("No existe un producto con ese ID")
        except ValueError: 
            print("Escribiste mal el id")
          
    elif opcion == "5":
        print("Gracias por usar el sistema de inventario")
        break