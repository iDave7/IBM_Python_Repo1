def descomponer_en_factores_primos(numero):
    factores_primos = []
    divisor = 2

    while divisor * divisor <= numero:
        if numero % divisor == 0:
            factores_primos.append(divisor)
            numero //= divisor
        else:
            divisor += 1

    if numero > 1:
        factores_primos.append(numero)

    return factores_primos

# Prueba del programa
numero = int(input("Ingresa un número entero positivo: "))
if numero <= 0:
    print("El número debe ser mayor que cero.")
else:
    factores_primos = descomponer_en_factores_primos(numero)
    print(f"Los factores primos de {numero} son: {factores_primos}")
