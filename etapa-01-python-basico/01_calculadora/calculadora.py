import math

num1 = int(input("Digite el primer numero: "))
num2 = int(input("Digite el segundo numero: "))
num3 = int(input("Digite el tercer numero: "))

print("Vas a escojer una de estas operaciones: ")
print ("Ten en cuenta si escojes division  ")
opcion = (input("Escriba una opcion de operacion (suma, resta, multi, divi, potencia, raiz, modulo, promedio: )"))

if opcion == "suma":
    print(num1 + num2 + num3)
elif opcion == "resta":
    print(num1 - num2 - num3)
elif opcion == "multi":
    print(num1 * num2 * num3)
elif opcion == "divi":
    print(num1 / num2 / num3)
elif opcion == "potencia":
    print(num1 ** num2 ** num3)
elif opcion == "raiz":
    print(math.sqrt(num1) or math.sqrt(num2) or math.sqrt(num3))
elif opcion == "modulo":
    print(num1 % num2 % num3)
elif opcion == "promedio":
    print((num1 + num2 + num3) / 3)
else:
    print("Opcion no valida")
