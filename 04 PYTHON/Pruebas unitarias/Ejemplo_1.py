# Creamos una función para calcular el área de un círculo

from math import pi

def area(r):
    areaC = pi*(r**2)
    return areaC

# creamos una lista con una serie de valores que vamos a pasar como parámetro 
# y vamos a ver el comportamiento que tiene esa función con esos valores.

valores = [1, 3, 0, -1, -3, 2+3j, True, 'hola']

# Lanzamos la función recorriendo los valores de la lista para ver qué resultados da

for v in valores:
    areaCalculada = area(v) 
    print('Para el valor', v, 'el áreaes', areaCalculada)

