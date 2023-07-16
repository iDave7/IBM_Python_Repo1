def descomponer_en_factores_primos(numero):
    factores_primos = []
    divisor = 2

    while divisor * divisor <= numero:
        if numero % divisor == 0:
            exp = 0
            while numero % divisor == 0:
                numero //= divisor
                exp += 1
            factores_primos.append((divisor, exp))

        divisor += 1

    if numero > 1:
        factores_primos.append((numero, 1))

    return factores_primos

def imprimir_factores_primos(numero, factores_primos):
    print(f"Los factores primos de {numero} son:", end=" ")
    for factor, exp in factores_primos:
        if exp == 1:
            print(factor, end=" ")
        else:
            print(f"{factor}^{exp}", end=" ")
    print()

# Prueba del programa
numero = int(input("Ingresa un número entero positivo: "))
if numero <= 0:
    print("El número debe ser mayor que cero.")
else:
    factores_primos = descomponer_en_factores_primos(numero)
    imprimir_factores_primos(numero, factores_primos)

