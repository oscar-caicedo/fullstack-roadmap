def ejecutar_conversor(): 
    try: 
        print("---------------------------------")
        print("Bienvenido al conversor de divisas con tasas de cambio")
        print("--------------------------------")    
        monto = float(input("1. Cuánto es el monto a convertir: "))
        moneda_origen = input("2. Cuál es la moneda de origen (USD, EUR, COP, MXN): ").upper()
        moneda_destino = input("3. Cuál es la moneda de destino (USD, EUR, COP, MXN): ").upper()
        
        tasas = {
            "USD": 4000,    # 1USD = 4000 COP
            "EUR": 4300,    # 1EUR = 4300 COP
            "COP": 1,       # 1 COP (REFERENCIA BASE)
            "MXN": 220      # 1 MXN = 220 COP 
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
        
        print(f"Resultado: {resultado:.2f}")
        
    except KeyError:
        print("Escribiste una moneda no válida")
    except ValueError:
        print("Error: El monto debe ser un número válido")
    except Exception:
        print("Ocurrió algo inesperado.")
        
    continuar = input("¿Desea seguir haciendo conversiones? (S/N): ").upper()
    
    # CORRECCIÓN DE IDENTACIÓN AQUÍ
    if continuar == "S":
        ejecutar_conversor()
    else:
        print("Muchas Gracias por haber usado el conversor de monedas!")

ejecutar_conversor()