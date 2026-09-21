#Funciones con Parametro
def operacion(num1=1, num2=1):
    multiplicacion = num1 * num2
    return multiplicacion

print(operacion(4,4))

#Calculadora de area con valor por defecto
def calcular_area_rectangulo(base, altura=5):
    resultado = base * altura
    return resultado

print (calcular_area_rectangulo(10))

#Validador de mayoria de edad
def es_mayor_de_edad(edad):
    if edad >= 18:
        return True
    return False

resultado = (es_mayor_de_edad(10))
print(resultado)
