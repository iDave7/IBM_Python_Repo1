


#   DICCIONARIOS

"""Los diccionarios, también llamados matrices asociativas, deben su nombre a que son 
colecciones que relacionan una clave y un valor.
Un diccionario es una colección desordenada, modificable e indexada. 
En Python, los diccionarios se escriben entre llaves y tienen claves y valores.
"""

#   Declaración de un diccionario

miDiccionario = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(miDiccionario)

#   Declaración de un diccionario mediante el constructor dict

miDiccionario = dict(
      brand= "Ford",
      model= "Mustang",
      year= 1964
)
print(miDiccionario)

# Daclaración de un diccionario partiendo de uno vacío
miDiccionario = {}
miDiccionario["brand"] = "Ford"
miDiccionario["model"] = "Mustang"
miDiccionario["year"] = 1994
miDiccionario

#   A los valores almacenados en un diccionario se accede por su clave

peliculas = {"Love Actually": "Richard Curtis", 
"Kill Bill": "Tarantino",
"Amélie": "Jean-Pierre Jeunet"}

peliculas["Love Actually"] 

# Reasignar valores a un diccionario

peliculas["Kill Bill"] = "Quentin Tarantino"
print(peliculas)

#   Usar una tupla dentro de un diccionario:

miDiccionario3={"nombre":"Jordan", "Equipo":"Bulls", "Anillos":[1991, 1992, 1993, 1996, 1997, 1998]}
print(miDiccionario3["Anillos"])

#   Quitar valores de un diccionario

peliculas = {"Love Actually": "Richard Curtis", 
"Kill Bill": "Tarantino",
"Amélie": "Jean-Pierre Jeunet"}

peliculas.pop("Love Actually")	

print(peliculas)

#   Crear un diccionario a partir de dos listas:

lista_claves=["nombre", "edad"]
lista_valores=["Angel", 43]
diccionario = dict(zip(lista_claves , lista_valores))
print(diccionario)

# también se puede convertir en una lista
lista=list(zip(lista_claves, lista_valores))

#   Para comprobar si una clave está en el diccionario:

"nombre" in diccionario		#Devuelve true o false

#   Imprima las claves (no los valores):

peliculas = {"Love Actually": "Richard Curtis", 
"Kill Bill": "Tarantino",
"Amélie": "Jean-Pierre Jeunet"}
for x in peliculas:
      print(x)
# o lo que sería lo mismo:     
for x in peliculas.keys():
      print(x)  

#   Imprima los valores del diccionario (no sus claves):

peliculas = {"Love Actually": "Richard Curtis", 
"Kill Bill": "Tarantino",
"Amélie": "Jean-Pierre Jeunet"}
for x in peliculas:
      print(peliculas[x])
# o lo que sería lo mismo:     
for x in peliculas.values():
      print(x)   

 # Imprime claves y valores

peliculas = {"Love Actually": "Richard Curtis", 
"Kill Bill": "Tarantino",
"Amélie": "Jean-Pierre Jeunet"}
for x,y in peliculas.items():
      print(x,y)       

#   Longitud de un diccionario:

peliculas = {"Love Actually": "Richard Curtis", 
"Kill Bill": "Tarantino",
"Amélie": "Jean-Pierre Jeunet"}

print(len(peliculas))

#   Agregar elementos a un diccionario:

miDiccionario = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
miDiccionario["color"] = "red"
print(miDiccionario)

#   Eliminar el último elemento:

miDiccionario = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
miDiccionario.popitem()
print(miDiccionario)


#   La palabra clave del elimina el elemento con el nombre de clave especificado:

miDiccionario = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del miDiccionario["model"]
print(miDiccionario)


#   La palabra clave del también puede eliminar completamente el diccionario:

miDiccionario = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del miDiccionario
print(miDiccionario)

#   La palabra clave clear() vacía el diccionario:

miDiccionario = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
miDiccionario.clear()
print(miDiccionario)


      
#   Copiar un diccionario

miDiccionario = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
midict = miDiccionario.copy()
print(midict)


#   Otra forma de copiar un diccionario

miDiccionario = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
midict = dict(miDiccionario)
print(midict)

#   Diccionarios anidados

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily["child1"])
print(myfamily)

# Métodos de los diccionarios

# clear() -> Borra todos los elementos de un diccionario
miDiccionario = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
miDiccionario.clear()
print(miDiccionario)

# copy() -> Devuelve una copia de un diccionario 

# fromkeys() -> Devuelve un diccionario con las claves y valores especificados

# get() -> Devuelve el valor de una clave

# items() -> Devuelve una lista que contiene una tupla por cada par clave-valor

# keys() -> Devuelve una lista que contiene las claves del diccionario

# pop() -> Borra el elemento con la clave especificada
miDiccionario = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
miDiccionario.pop("year")
print(miDiccionario)

# También se puede elimiinar con del
miDiccionario = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del miDiccionario["year"]
print(miDiccionario)


# popitem() -> Borra el último par clave-valor insertado (existente)
miDiccionario = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
miDiccionario.popitem()
print(miDiccionario)


# setdefault() -> Devuelve el valor de la clave especificada. 
# Si no existe, insertta la clave con el valor especificado. 
 
# update() -> Actualiza el diccionario con el par clave-valor que se especifique 

# values() -> Devuelve una lista con los valores del diccionario


# Operaciones con diccionarios

dict1 = {
      "key1": "Value1",
      "key2": "Value2"
}

dict2 = {
      "key3": "Value3",
      "key4": "Value4"
}

dict1 is dict1

dict1 == dict1

dict1 is dict2

dict1 == dict2

# Eliminar valores de un diccionario

dict1 = {
      "key1": "Value1",
      "key2": "Value2"
}

dict1.pop("key2")
dict1

# Meter un diccionario dentro de otro

miDiccionario3={"nombre":"Jordan", "Equipo":"Bulls", "Anillos":[1991, 1992, 1993, 1996, 1997, 1998]}
print(miDiccionario3)
print(miDiccionario3.keys())
print(miDiccionario3.values())
print(len(miDiccionario3))
print(miDiccionario3["nombre"])

#   Comprobar que existe una clave en el diccionario

peliculas = {
      "Love Actually": "Richard Curtis", 
      "Kill Bill": "Tarantino",
      "Amélie": "Jean-Pierre Jeunet"
      }

if "Kill Bill" in peliculas:
      print("Yes!")

# Eliminación completa de un diccionario

dict1 = {
      "key1": "Value1",
      "key2": "Value2"
}

del dict1
print(dict1)