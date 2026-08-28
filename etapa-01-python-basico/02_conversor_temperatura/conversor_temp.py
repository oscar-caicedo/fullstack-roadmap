
while True:
    print("1. Celsius a Fahrenheit")
    print("2. Celsius a Kelvin")
    print("3. Fahrenheit a Celsius")
    print("4. Fahrenheit a Kelvin")
    print("5. Kelvin a Celsius")
    print("6. Kelvin a Fahrenheit")
    print("7. Salir")
    try:
        opcion = int(input("Escoja una opcion (1-7): ")) 
        if opcion == 1:
            try:
                celsius = float(input("Digite la temperatura: "))
                if celsius < -273.15:
                    print ("La temperatura minima es -273.15, es el valor absoluto")
                else:
                    fahrenheit = (celsius * 9/5) + 32
                    print(f"La temperatura {celsius}  grados celsius a fahrenheit es: {fahrenheit:.2f}")
            except:
                print("Error: Dato Invalido")
        if opcion == 2:
            try:
                celsius = float(input("Digite la temperatura: "))
                if celsius <-273.15:
                    print ("La temperatura minima es -273.15, es el valor absoluto")
                else:
                    kelvin = celsius + 273.15
                    if kelvin < 0:
                        print("La temperatura esta por debajo de 0, el valor absoluto")
                    else:
                        print(f"La temperatura {celsius}  grados celsius a grados kelvin es: {kelvin:.2f}")
            except:
                print("Error: Dato Invalido")
        if opcion == 3:
            try:
                fahrenheit = float(input("Digite la temperatura: "))
                celsius = (fahrenheit - 32) * 5/9
                if celsius <-273.15:
                    print("La temperatura minima es -273.15, es el valor absoluto")
                else:
                    print(f"La temperatura {fahrenheit}  grados fahrenheit a grados celsius es: {celsius:.2f}")
            except:
                print("Error: Dato Invalido")
        if opcion == 4:
            try:
                fahrenheit = float(input("Digite la temperatura: "))
                kelvin = (fahrenheit - 32) * 5/9 + 273.15
                if kelvin < 0:
                    print("La temperatura esta por debajo de 0, el valor absoluto")
                else:    
                    print(f"La temperatura {fahrenheit}  grados fahrenheit a grados kelvin es: {kelvin:.2f}")
            except: 
                print("Error: Dato Invalido")
        if opcion == 5:
            try:
                kelvin = float(input("Digite la temperatura: "))
                if kelvin < 0:
                    print("La temperatura esta por debajo de 0, el valor absoluto")
                else:
                    celsius = kelvin - 273.15
                    if celsius <-273.15:
                        print("La temperatura minima es -273.15, es el valor absoluto")
                    else:
                        print(f"La temperatura {kelvin}  grados kelvin a grados celsius es: {celsius:.2f}")
            except:
                print("Error: Dato invalido")
        if opcion == 6:
            try:    
                kelvin = float(input("Digite la temperatura: "))
                if kelvin < 0:
                    print("La temperatura esta por debajo de 0, el valor absoluto")
                else:
                    fahrenheit = (kelvin - 273.15) * 9/5 + 32
                    print(f"La temperatura {kelvin}  grados kelvin a grados fahrenheit es: {fahrenheit:.2f}")
            except:
                print("Error: Dato invalido")
        if opcion == 7:
            break
    except:
        print("Vuelve a digita un numero entre el (1-7)")