

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
miLista = [22, True, "una cadena", [1, 2]]
print(miLista[0])

miLista = [[1,2] , [3,4] , [5,6]]
miVar = miLista[1,1]
print(miVar)

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
