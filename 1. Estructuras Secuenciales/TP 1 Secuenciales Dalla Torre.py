#Actividad 1
print("Hola mundo!")

#Actividad 2
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}! ") 

#Actividad 3 
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#Actividad 4
import math
radio = float(input("Ingrese el radio de un círculo: "))
area = round (math.pi * (radio)**2, 2)
perimetro = round(2 * math.pi * radio, 2)
print(f"El área del círculo es de {area} y el perímetro es de {perimetro}")

#Actividad 5
segundos = float(input("Ingrese los segundos que desea calcular: "))
horas = round (segundos / 3600, 2)
print(f"Los segundos ingresados equivalen a {horas} horas")

#Actividad 6
num = int(input("Ingrese un número: "))
print(f"""
{num} x 0 = {num *0}
{num} x 1 = {num *1}
{num} x 2 = {num *2}
{num} x 3 = {num *3}
{num} x 4 = {num *4}
{num} x 5 = {num *5}
{num} x 6 = {num *6}
{num} x 7 = {num *7}
{num} x 8 = {num *8}
{num} x 9 = {num *9}
{num} x 10 = {num *10}
""")

#Actividad 7
num1 = float(input("Ingrese el primer número (debe ser distinto a 0): "))
num2 = float(input("Ingrese el segundo número (debe ser distinto a 0): "))
print(f"""
    La suma de ambos números es de: {num1 + num2}
    La división de ambos números es de: {num1 / num2}
    La multiplicación de ambos números es de: {num1 * num2}
    La resta de ambos números es de: {num1 - num2}
    """)

#Actividad 8
altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kg: "))
imc = round(peso / altura**2, 2)
print(f"Su índice de masa corporal es de: {imc}.")

#Actividad 9
celsius = float(input("Ingrese una temperatura en grados celsius: "))
fahrenheit = round((9/5)*celsius+32, 2)
print(f"{celsius} °C equivalen a {fahrenheit} °F.")

#Actividad 10
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
promedio = round ((num1+num2+num3)/3, 2)
print(f"El promedio de los 3 números es de: {promedio}")
