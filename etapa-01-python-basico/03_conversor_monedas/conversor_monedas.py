try: 
    print("-------------------------------------------")
    print("Bienvenido a el conversor de divisas con tasas de cambio")
    print("-------------------------------------------")
    monto = (float(input("1.Cuanto es el monto a convertir: ")))
    moneda_origen = input("Cual es la moneda de origen (USD, EUR, COP, MXN): ").upper()
    moneda_destino = input("Cual es la moneda de destino (USD, EUR, COP, MXN): ").upper()

    tasas = {
    "USD": 4000,    # 1USD = 4000 COP
    "EUR": 4300,    # 1EUR = 4300 COP
    "COP": 1,       #1 COP (REFERENCIA BASE)
    "MXN": 220      #1 MXN = 220 COP
    }

    def convertir(monto, moneda_origen, moneda_destino, tasas):
        monto_en_cop = monto * tasas[moneda_origen]
        resultado = monto_en_cop / tasas[moneda_destino]
        return resultado    

    resultado = convertir(
        monto, 
        moneda_origen, 
        moneda_destino,  
        tasas
        )
    print(f"Resultado: {resultado: .2f}")
except:
    print("Escribiste una opcion no valida")

# resultado= convertir(100, "USD", "COP", tasas)
#resultado= convertir(100, "USD", "dfsMEX", tasas)
#resultado= convertir(100, "EUR", "USD", tasas)
#resultado= convertir(100, "EUR", "COP", tasas)
#resultado= convertir(100, "EUR", "MEX", tasas)
#resultado= convertir(100, "USD", "EUR", tasas)
#resultado= convertir(100, "USD", "EUR", tasas)
#resultado= convertir(100, "USD", "EUR", tasas)
