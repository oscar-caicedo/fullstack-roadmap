saldo = 100000
intentos_fallidos = 0
historial = []
pin_correcto = 123 #Guardar el PIN como numero entero

#Ciclo para permitir hasta 3 intentos de PIN
while intentos_fallidos < 3:
    ingreso = int(input("Ingrese su pin: "))
    if ingreso == pin_correcto:
        print("PIN CORRECTO")
        while True:
            print("\n1.Consultar Dinero")
            print("2.Depositar Dinero")
            print("3.Retirar Dinero")
            print("4.Ver Historial")
            print("5.Salir y expulsar tarjeta")
            opcion = int(input("Ingrese la opcion: "))
        
            if opcion == 1:
                print(F"Su saldo actual es de: {saldo}")
                
            elif opcion == 2:
                try:
                    monto = int(input("Ingrese el monto a depositar: "))
                    if monto > 0:
                        saldo += monto
                        historial.append(f"Deposito: +{monto}")
                        print(f"Saldo en {saldo}, deposito exitoso")
                    else:
                        print("ERROR: Cantidad tiene que ser mayor a 0")
                except ValueError:
                    print("ERROR: Debe ingresar un numero valido")
                    
            elif opcion == 3:
                try:
                    monto = int(input("Ingrese el monto a retirar: "))
                    if monto > 0 and monto <= saldo:
                        saldo -= monto
                        historial.append(f"Retiro: -{monto}")
                        print("Retiro Exitoso")
                        print(f"Saldo que queda en la cuenta {saldo}")
                    else:
                        print("Retiro mayor al saldo que tiene en su cuenta")
                except ValueError:
                    print("ERROR: Debe ingresar un numero valido") 
                    
            elif opcion == 4:
                print ("-" * 45)
                print("Historial de la sesion:")
                for item in historial:
                    print(item)
                print("-"*45)
                
            elif opcion == 5:
                print("Tarjeta Expulsada")
                break
        break #Romper ciclo del PIN
    else:
        intentos_fallidos += 1
        print(f"Incorrecto. Te quedan {3 - intentos_fallidos} intentos.")

#Si se superan los 3 intentos
if intentos_fallidos >= 3:
    print("Intentos maximos alcanzados, cuenta bloqueada temporalmente.")