aprobado = True
reprobado = True
estado = 0
contador = 0 #Cuenta estudiantes
prom_grupal = 0
sum_prom = 0


while True:
    nombre_est = input("Nombre del estudiante: ")
    notas = int(input("Cuantas notas son: "))
    
    suma = 0
    prom = 0

    maximo = 0 
    minimo = 5.0 
    
    for i in range(notas):
        nota = float(input(f"Ingrese la {i} nota: "))
    
        if nota <= 0.0:
            print("Nota no valida, mayor a 0")
        elif nota >= 5.0:
            print("Nota no valida, menor a 5.0")
        else:
            suma += nota 
            if nota < minimo:
                minimo = nota
            if nota > maximo:
                maximo = nota
                
    prom = suma / notas 
    sum_prom += prom
    contador += 1
 
    if prom > 3.0:
        estado = aprobado
    else:
        estado = reprobado

  
    print("Estudiante ", nombre_est)
    print("Nota: ", prom)
    print("Estado ", estado)
    otro = input("Desea ingresar otro estudiante? (S/N): ").upper()
    if otro == "S":
        continue
    else:    
        print ("---------------------------")
        print ("La nota mas alta es: ", maximo)
        print ("La nota mas baja es: ", minimo)       
        prom_grupal = sum_prom / contador 
        print ("El promedio general del grupo es: ", prom_grupal)
