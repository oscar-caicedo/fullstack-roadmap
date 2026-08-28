import math

num1 = int(input("Digite el primer numero: "))
num2 = int(input("Digite el segundo numero: "))
num3 = int(input("Digite el tercer numero: "))

print("Vas a escojer una de estas operaciones: ")
print ("Ten en cuenta si escojes division  ")
opcion = (input("Escriba una opcion de operacion (suma, resta, multi, divi, potencia, raiz, modulo, promedio: )")).lower().strip()
#suma
if opcion == "suma":
    print("La suma es: ", num1 + num2 + num3)
#resta
elif opcion == "resta":
    print("La resta es: ", num1 - num2 - num3)
#multiplicacion
elif opcion == "multi":
    print("La multiplicacion es: ", num1 * num2 * num3)
#division
elif opcion == "divi":
    if num2 == 0 or num3 == 0:
        print("No se puede dividir por cero")
    else:
        print("La division es: ", num1/num2/num3)
elif opcion == "potencia":
    print("La potencia es: ", num1 ** num2 ** num3)
#raiz
elif opcion == "raiz":
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
elif opcion == "modulo":
    if num2 == 0 or num3 == 0:
        print("No se puede dividir por cero")
    else:
        print("El modulo es: ", num1 % num2 % num3)
#promedio
elif opcion == "promedio":
    print("El promedio es: ", (num1 + num2 + num3) / 3)
else:
    print("Opcion no valida")
