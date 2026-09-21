#Cuenta regresiva con despliegue

vo = 6

while vo > 0:
    vo -= 1
    print(vo)
    
print("¡Despegue!")

#Adivine el numero secreto

secreto = "1"

while True:
    user = input("Escribe un numero:")
    if secreto == user:
        print("¡FELICITACIONES!")
        break
    else:
        print("Vuelve a intentarlo")