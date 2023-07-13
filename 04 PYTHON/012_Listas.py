

#   LISTAS

"""
La lista es un tipo de colección ordenada y modificable. 
Es decir, una secuencia de valores de cualquier tipo, ordenados y de tamaño variable.
Se escriben entre corchetes. []
"""

miLista=["Angel", 43, 667767250] 
miLista2 = [22, True, "una lista", [1, 2]]

#   MÉTODOS DE LAS LISTAS

#   Hacer una lista de una cadena
miLista = list("PYTHON")
print(miLista)

#   Acceder a los elementos de una lista
# Indexing
miLista = [22, True, "una cadena", [1, 2]]
print(miLista[0])

# Slicing
miLista = ["text1", "text2", "text3", "text4", "text5"]

miVar1 = miLista[1:3]
print(miVar1)

miVar2 = miLista[:3]
print(miVar2)

miVar3 = miLista[1:]
print(miVar3)

# Stride
miLista = ["text1", "text2", "text3", "text4", "text5"]

miVar1 = miLista[0:5:2] # esto es: [ 'índice_inicial' : 'índice_final' : 'salto']
print(miVar1)

miVar2 = miLista[::-1] # para darle la vuelta a una lista
print(miVar2)



#   Función con una lista como parámetro

def miFunccion(listaFrutas):
      for x in listaFrutas:
        print(x)

frutas = ["Manzana", "banana", "cereza"]

miFunccion(frutas)

# Métodos de las listas

# append() -> Añade un elemento al final de la lista 
listaDavid = ["David", 40, True]
listaDavid.append("Casado")
print(listaDavid)

# clear() -> Borra los elementos de la lista.
listaDavid = ["David", 40, True]
listaDavid.clear()
print(listaDavid)

# copy() ->  Devuelve una copia de la lista. 
listaDavid = ["David", 40, True]
listaDavid_copia = listaDavid.copy()
print(listaDavid_copia)

# count() ->  Devuelve el número de veces que se encuentra un elemento en la lista 
listaDavid = ["David", 40, True]
listaDavid.count(40)

# extend() -> Añade los elementos de una lista a otra.
listaDavid = ["David", 40, True]
ListaBea = ["Bea", 36, False]
listaDavid.extend(ListaBea)
print(listaDavid)

# index() ->  Devuelve el índice del primer elemento cuyo valor es el especificado.
listaDavid = ["David", 40, True]
listaDavid.index("David")

# insert() ->  Añade un elemento en la posición especificada.
listaDavid = ["David", 40, True]
listaDavid.insert(1,"López")
print(listaDavid)

# pop() ->  Borra el elemento en la posición especificada y devuelve el elemento eliminado.
listaDavid = ["David", "López", 40, True]
listaDavid.pop(1)
print(listaDavid)

# remove() ->  Elimina el elemento con el valor especificado
listaDavid = ["David", "López", 40, True]
listaDavid.remove("López")
print(listaDavid)

# reverse() ->  Invierte el orden de la lista.
listaDavid = ["David", "López", 40, True]
listaDavid.reverse()
print(listaDavid)

# sort() ->  Ordena la lista (aparentemente no admite num + letras)
listaDavidNum = [1, 3, 2, 10, 8]
listaDavidNum.sort()
print(listaDavidNum)

listaDavidAlf = ["c", "a", "d", "e", "b"]
listaDavidAlf.sort()
print(listaDavidAlf)

# Operaciones con listas

# min() ->  Devuelve el mínimo
listaDavidNum = [1, 3, 2, 10, 8]
min(listaDavidNum)

# max() ->  Devuelve el máximo
listaDavidNum = [1, 3, 2, 10, 8]
max(listaDavidNum)

# len() ->  Devuelve el número de elementos de la lista
listaDavidNum = [1, 3, 2, 10, 8]
len(listaDavidNum)

# Creación de una llista mediante el constructor list()
thislist = list(("Cuky", "Katy", "Moka"))
print(thislist)


# Unir dos listas

# 1 Mediante +
listaDavidNum = [1, 3, 2, 10, 8]
listaDavidAlf = ["c", "a", "d", "e", "b"]

listaDavid_Unida = listaDavidNum + listaDavidAlf
print(listaDavid_Unida)

# 2 Mediante bucle for y el método append()
listaDavidNum = [1, 3, 2, 10, 8]
listaDavidAlf = ["c", "a", "d", "e", "b"]

for x in listaDavidAlf:
    listaDavidNum.append(x)
print(listaDavidNum)

# 3 Mediante el método extend()
listaDavidNum = [1, 3, 2, 10, 8]
listaDavidAlf = ["c", "a", "d", "e", "b"]

listaDavidNum.extend(listaDavidAlf)
print(listaDavidNum)

# Listas anidadas
listaAnidada = [[1,2,3],
                [4,5,6],
                [7,8,9]]

print(listaAnidada)

# Listas por comprensión

milista=[1,2,3,4,5,6,7]
print(milista)

## milista2 tiene los valores (2*elemento) siendo elemento los valores de la lista miLista

milista2 = [2*elemento for elemento in milista]
print (milista2)

## Crear una Lista solo con los elementos pares

listaPares = [elemento for elemento in milista if elemento%2==0]
print (listaPares)

## De la manera tradicional seria:

listaPares=[]
for i in milista:
  if i%2==0:
    listaPares.append(i)
print (listaPares)

## Anidar iteraciones dentro de la lista

a=["a", "b", "c"] 
b=[1,2,3]

## Para cada elemento de a me recorre todos Los elmentos de b 

c= [elemento1*elemento2 for elemento1 in a for elemento2 in b]
print (c)

##Puedo incluso poner alauna condicion

c=[elemento1*elemento2 for elemento1 in a for elemento2 in b if elemento2!=2]
print(c)


m = [["a1","a2","a3"],
     ["b1","b2","b3"],
     ["c1","c2","c3"]]
col2 = [row[1] for row in m]
col2 # o print(col2)

[m[i][i] for i in [0,1,2]] # Extrae la diagonal de la matriz m

# Extraemos la longitud de cada fila de la matriz
m = [["a1","a2","a3"],
     ["b1","b2","b3"],
     ["c1","c2","c3","c4"]]
[len(row) for row in m]

# Filtramos elementos por la longitud de cada fila de la matriz
m = [["a1","a2","a3"],
     ["b1","b2","b3"],
     ["c1","c2","c3","c4"]]
[len(row) for row in m if len(row)>3]

# Más expresiones dentro
squares = [n ** 2 for n in range(10)]
squares

# Copiar listas
la = [1,2,3]
lb = la[:]     # Forma 1
lc = list(la)  # Forma 2
print(la,lb,lc)

# Modificación de un elemento de la lista la pero lb y lc siguen igual
la[2] = 'z'
print(la,lb,lc)

# Aislar una variable (de camios externos)
import copy             # imporatmos copy
la = [1,2,[31,32,33]]   # lista anidada
lb = copy.copy(la)      # Copia 'plana' (igual que lb = la[:])
lc = copy.deepcopy(la)  # Copia profunda (por si hay elementos anidados)
la[1] = 'z'
la[2][2] = 'zz'

print(la)
print(lb)               # Copia plana sólo copia elementos de primer nivel
print(lc)               # Copia plana copia los elementos de todos los niveles