import random

print("Bienvenido a adivina el numero")
print("------------------------------")

while True:       
    print("1.Nivel Bajo")
    print("2.Nivel Medio")
    print("3.Nivel Alto")
    opcion = int(input("Que nivel quieres jugar: "))

    intentos = 0

    if opcion == 1:            
        bajo = random.randint(1, 50)
        while True:
            if intentos == 51:
                print("INTENTO MAXIMOS, INTENTALO DE NUEVO")
                break
            else:
                jugador = int(input("Adivina el numero entre el 1 y 50: "))
                intentos = intentos + 1
                print ("Intento numero: ", intentos)
                if jugador < 1 or jugador > 50:
                    print("Numero fuera de los rangos permitidos (1-50)")
                else:
                    if jugador == bajo:
                        print("Acertaste")
                        break   
                    elif jugador < bajo:
                        print("Demasiado Bajo")
                    elif jugador > bajo:
                        print("Demasiado alto")
        si = (input("Quieres jugar otra partida? S/N"))
        if si == "S": 
            print ("Listo, empecemos", opcion)
        else:
            break

    if opcion == 2:            
        medio = random.randint(1, 75)
        while True:
            if intentos == 75:
                print("INTENTO MAXIMOS, INTENTALO DE NUEVO")
                break
            else:
                jugador = int(input("Adivina el numero entre el 1 y 75: "))
                intentos = intentos + 1
                print ("Intento numero: ", intentos)
                if jugador < 1 or jugador > 75:
                    print("Numero fuera de los rangos permitidos (1-50)")
                else:
                    if jugador == medio:
                        print("Acertaste")
                        break
                    elif jugador < medio:
                        print("Demasiado Bajo")
                    elif jugador > medio:
                        print("Demasiado alto")
        si = (input("Quieres jugar otra partida? S/N"))
        if si == "S": 
            print ("Listo, empecemos", opcion)
        else:
            break

    if opcion == 3:            
        alto = random.randint(1, 100)
        while True:
            if intentos == 100:
                print("INTENTO MAXIMOS, INTENTALO DE NUEVO")
                break
            else:
                jugador = int(input("Adivina el numero entre el 1 y 100: "))
                intentos = intentos + 1
                print ("Intento numero: ", intentos)
                if jugador < 1 or jugador > 100:
                    print("Numero fuera de los rangos permitidos (1-100)")
                else:
                    if jugador == alto:
                        print("Acertaste")
                        break
                    elif jugador < alto:
                        print("Demasiado Bajo")
                    elif jugador > alto:
                        print("Demasiado alto")
        si = (input("Quieres jugar otra partida? S/N"))
        if si == "S": 
            print ("Listo, empecemos", opcion)
        else:
            break