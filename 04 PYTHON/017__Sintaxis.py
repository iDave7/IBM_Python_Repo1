# Solicitando elementos de List uno por uno
List = list()
l = int(input("Introduzca el tamaño de la lista: "))
print("Introduzca los elementos de la lista:")
for i in range(0, l):
    List.append(input())
print(List)

# Solicitando elementos del Set uno por uno
Set = set()
s = int(input("Introduzca el tamaño del conjunto: "))
print("Introduzca los elementos del conjunto:")
for i in range(0, s):
    Set.add(int(input())) 
print(Set)

# Solicitando elementos de List todos a la vez separados por espacios
List = list(map(int, input("Introduzca los elementos de la lista separados por espacios:").split()))
print(List)

# Solicitando elementos del Set todos a la vez separados por espacios
Set = set(map(int, input("Introduzca los elementos del Set separados por espacios: ").split()))
print(Set)

# Para agregar un nuevo elemento a una tupla, primero deberemos convertir 
# la tupla en lista, luego agregaremos el elemento a la lista y nuevamente 
# convertiremos la lista en una tupla.

T = (2, 3, 4, 5, 6)  #Tupla inicial
print("Tupla inicial")
print(T)
L = list(T)
L.append(int(input("Introduzca el nuevo elemento: ")))
T = tuple(L)
print("Tupla final")
print(T)

# Modificación de print()

print("ABC")
print("A","B","C")

print("A","B","C", sep = "@")
print("ABC", end ="@")

# Salida de datos con formato

# Usando f o F
# Declaramos una variable
name = "David"
# Salida
print(f'Hola {name}!. Qué tal?')

# Usando format()
# Declaramos de variables
a = 20 
b = 10
# Suma
sum = a+b
# Resta
sub = a-b
# Salida
print('El valor de a es {} y b es {}'.format(a,b))
print('{2} es la suma de {0} y {1}'.format(a, b, sum))
print('{sub_value} es la resta de {value_a} y {value_b}'.format(value_a=a,value_b=b,sub_value=sub))

# Usando el operador %
# Entrada de datos
num = int(input("Introduzca un número:"))
add = num+5
# Salida
print("La suma es %d" %add) # %d – entero
print("La suma es %f" %add) # %f – flotante
print("La suma es %s" %add) # %s - cadena
print("La suma es %x" %add) # %x - hexadecimal 
print("La suma es %o" %add) # %o – octal
