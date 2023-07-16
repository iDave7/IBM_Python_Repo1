

#	WHILE

#   Imprime edad cuando el contador llegue a 18

edad = 0
while edad < 18: 
    edad=edad+1
print("Tienes "+str(edad))

#   Pregunta la edad mientras sea negativa

edad=int(input("Introduce edad: "))

while edad<0:
    print("Edad incorrecta")
    edad=int(input("Introduce edad: "))

print("tu edad es: "+str(edad))

#   Calcula la raiz cuadrada de un número. Tenemos tres intentos y el número no puede ser negativo.

import math;
intentos=0;
num = int(input("Introduce numero: "))

while num<0:
    intentos=intentos+1
    print("Incorrecto")
    num=int(input("Introduce numero: "))

    if intentos==2:
        print("Demasiados intentos")
        break;

if intentos<2:
    intentos=intentos+1
    solucion=math.sqrt(num)
    print("la raiz cuadrada de "+str(num)+ " es: "+str(solucion))

#   Bucle while con un if anidado y un break
#   Salga del bucle cuando num sea 3:

num = 1
while num < 6:
  print(num)
  if num == 3:
    break
  num += 1
  
# Otro ejemplo de sentencia break

a = 5
while a:
   print(a, end=' ')
   a-=1
   if a==2:
       break

print('\nFuera del bucle')
print('Valor de "a": {}'.format(a))



# Sentencia continue: nos permite interrumpir la iteración actual y saltar una vuelta de bucle

a = 7
while bool(a):
   a-=1
   if a % 2 == 0:
      continue
   print(a, end='\n')
print('\nFuera del bucle')

# Sentencia pass: no hace absolutamente nada. Es un marcador de posición para dejar bucles vacíos.
a = 5 
while a:
   pass # Presiona Ctrl-C en Win o Interrumpir en la consola para abortar la ejecución

# Bloques else al finalizar bucles
# evaluamos si un número es primo o no 

a = int(input("Introduce un número entero"))
b = a // 2
while b>1:
   if a % b == 0:
      print('{1} es factor de {0}'.format(b,a))
      break
   
else:
   print('{} es primo'.format(a))
print('\nFuera del bucle')