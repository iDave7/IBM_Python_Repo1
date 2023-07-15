# En Python disponemos de 4 sentencias que podemos utilizar para manejar excepciones:
# • try/except: Intercepta y recupera excepciones disparadas por Python o por nuestro código.
# • try/finally: Realiza tareas de limpieza ocurran las excepciones o no.
# • raise: Dispara una excepción manualmente en el código.
# • assert: Dispara una excepción condicionalmente.

# Ejemplo 1
indice = int(input('Introduce el índice deseado para la palabra "Python"'))

def indexador(objeto, indice):
    return objeto[indice]
try:
    print(indexador('Python', indice))
except IndexError: # Captura Indexerror
    print('Has puesto un índice muy grande.')

print('Hemos salido del try-catch')

# Ejemplo 2 - Todos los errores en el except
indice = input('Introduce el índice deseado para la palabra "Python"') 

def indexador(objeto, indice):
    
    return objeto[indice]
try:
    print(indexador('Python', indice))
except (IndexError, TypeError): # Captura Indexerror y TypeError (se puede no poner nada pero es no recomendado)
    print("Error")
print('Hemos salido del try-catch')

# Ejemplo 2 - Un except por error
indice = input('Introduce el índice deseado para la palabra "Python"')

def indexador(objeto, indice):
    return objeto[indice]
try:
    print(indexador('Python', indice))
except (IndexError): # Captura Indexerror
    print('Has puesto un índice muy grande.')
except (TypeError):
    print('Has puesto una letra.')
print('Hemos salido del try-catch')

# Lanzado y captura de excepciones manuales
try:
    raise IndexError('Excepción lanzada manualmente')
except:
    print('He capturado mi pripia excepción')

 # Sentencia assert para lanzar excepciones condicionales    
a = 10
b=0
c=5
assert(a > b), 'A tiene que ser mayor que B!' # Si se cumple no salta el error
print('Si se muestra esto es que no ha saltado el primer assert')
assert(a == c), 'A y C tienen que ser iguales' # Como no se cumple no salta el error
print('Si se muestra esto es que no ha saltado el primer assert')

# Creación de nuesttas propias excepciones
# Ejemplo 1 (básico)
class miPropiaExcepcion(Exception): #Las excepciones heredan de Exception
    pass 
try:
    raise miPropiaExcepcion
except miPropiaExcepcion:
    print('He capturado mi propia excepción')

 # Ejemplo 2   
class miError(Exception):
    def __init__(self, valor):
        self.valor = valor
    def __str__(self):
        return str(self.valor)
raise(miError('Mensaje de error'))

# Uso de finally 

def indexador(objeto, indice):
    return objeto[indice]
try:
    indexador('Python', 10)
except IndexError:
    print('Capturamos la excepción')
finally:
    print('Esto se ejecuta incluso cuando salta la excepción')
print('Se ejecuta tambien este print')

# Uso de else
def divide(x, y):
    try:
        resultado = x/y
    except ZeroDivisionError:
        print('No se puede dividir por cero')
    else:
        print('El resultado es: ')
    finally:
        print('Ejecutamos el finally')

divide(4, 12)
divide(4, 0)
