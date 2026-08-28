import math
print("Calculadora Matematica")
print("----------------------------")

while True:
    print ("1.Suma")
    print ("2.Resta")
    print ("3.Multiplicacion")
    print ("4.Division")
    print ("5.Potencia")
    print ("6.Raiz")
    print ("7.Modulo")
    print ("8.Promedio")
    #suma
    opcion = int(input("Seleccione la operacion: "))

    if opcion == 1:
        num1 = int(input("Digite el primer numero: "))
        num2 = int(input("Digite el segundo numero: "))
        num3 = int(input("Digite el tercer numero: "))
        print("La suma es: ", num1 + num2 + num3)
    #resta
    elif opcion == 2:
        num1 = int(input("Digite el primer numero: "))
        num2 = int(input("Digite el segundo numero: "))
        num3 = int(input("Digite el tercer numero: "))
        print("La resta es: ", num1 - num2 - num3)
    #multiplicacion 
    elif opcion == 3:
        num1 = int(input("Digite el primer numero: "))
        num2 = int(input("Digite el segundo numero: "))
        num3 = int(input("Digite el tercer numero: "))
        print("La multiplicacion es: ", num1 * num2 * num3)
    #division
    elif opcion == 4:
        num1 = int(input("Digite el primer numero: "))
        num2 = int(input("Digite el segundo numero: "))
        if num2 == 0 :
            print("No se puede dividir por cero")
        else:
            print("La division es: ", num1/num2)
    elif opcion == 5:
        num1 = int(input("Digite el primer numero: "))
        num2 = int(input("Digite el segundo numero: "))
        print("La potencia es: ", num1 ** num2)
    #raiz
    elif opcion == 6:
        num1 = int(input("Digite el primer numero: "))
        num2 = int(input("Digite el segundo numero: "))
        num3 = int(input("Digite el tercer numero: "))
    # Verificamos y calculamos num1
        if num1 >= 0:
            print(f"Raíz cuadrada de {num1}: {math.sqrt(num1):.2f}")
        else:
            print(f"Raíz cuadrada de {num1}: No existe en números reales (es negativo)")
    # Verificamos y calculamos num2
        if num2 >= 0:
            print(f"Raíz cuadrada de {num2}: {math.sqrt(num2):.2f}")
        else:
            print(f"Raíz cuadrada de {num2}: No existe en números reales (es negativo)")
    # Verificamos y calculamos num3
        if num3 >= 0:
            print(f"Raíz cuadrada de {num3}: {math.sqrt(num3):.2f}")
        else:
            print(f"Raíz cuadrada de {num3}: No existe en números reales (es negativo)")
    #Modulo        
    elif opcion == 7:
        num1 = int(input("Digite el primer numero: "))
        num2 = int(input("Digite el segundo numero: "))
        if num2 == 0:
            print(f"ZeroDivisionError {num2} no es valido")
        else:
            print("El modulo es: ", num1 % num2)
    #promedio
    elif opcion == 8:
        num1 = int(input("Digite el primer numero: "))
        num2 = int(input("Digite el segundo numero: "))
        num3 = int(input("Digite el tercer numero: "))
        print("El promedio es: ", (num1 + num2 + num3) / 3)
    else:
        print("Opcion no valida")
