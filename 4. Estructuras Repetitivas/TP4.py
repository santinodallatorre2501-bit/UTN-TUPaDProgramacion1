# 1 Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
cont = 0
for cont in range (101):
 print(cont)
# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.
numero = int(input("Ingrese un número entero: "))
cont = 0
if numero == 0:
 print("El número tiene 1 dígito")
else:
    numero = abs(numero)
    while numero >= 1:
        numero = numero/10
        cont += 1
    print("El número ingresado tiene",(cont),"dígitos")
# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.
numero_1 = int(input("Ingrese el primer número: "))
numero_2 = int(input("Ingrese el segundo número: "))
cont = 0
suma = 0
for cont in range(numero_1 + 1, numero_2):
  suma+=cont
print("La suma de los números comprendidos entre los que ingresó (excluyendo los ingresados) es: ",suma)
# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.
numero = int(input("Ingrese un número: "))
suma = 0
if numero != 0:
  while numero != 0:
    suma += numero
    numero = int(input("Ingrese otro número: "))
  print("La suma de todos los nùmeros ingresados es: ",suma)
else:
  print("No se ingresó ningún número")
# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
from random import randint
num_random = randint(0,9)
numero = int(input("Adivina el número entre 0 y 9: "))
intento = 1
while numero != num_random:
  intento+=1
  numero = int(input("No adivinaste, intenta con otro: "))
print("Adivinaste en ",intento,"intentos")
# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.
cont=0
for cont in range(100,0,-2):
  print(cont)
# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.
numero_1 = int(0)
numero_2 = int(input("Ingrese un número positivo: "))
cont = 0
suma = 0
if numero_2 > 0:
  for cont in range(numero_1, numero_2+1):
    suma+=cont
  print("La suma de los números comprendidos entre el 0 y el que ingresó es: ",suma)
else:
  print("El número ingresado no es positivo")
# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).
cont = 0
pares = 0
impares = 0
negativos = 0
positivos = 0
for cont in range(100):
  numero = int(input("Ingrese un número: "))
  if numero % 2 == 0 and numero != 0:
    pares +=1
  elif numero % 2 != 0:
    impares +=1
  if numero < 0:
    negativos +=1
  elif numero > 0:
    positivos +=1
print(pares,"fueron pares,", impares,"fueron impares,",negativos,"fueron negativos y",positivos,"fueron positivos.")
# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).
cont = 0
suma = 0
cant_num = 100
for cont in range(cant_num):
  numero = int(input("Ingrese un número entero: "))
  suma += numero
media = float(suma / cant_num)
print("La media de todos los números ingresados es: ",media)
# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
numero = int(input("Ingrese un número: "))
invertido = 0
while numero > 0:
    aux = numero % 10
    invertido = (invertido * 10) + aux
    numero = numero // 10
print("El número invertido es: ",invertido)
    