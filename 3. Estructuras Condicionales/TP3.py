#Actividad 1
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad")
#Actividad 2
ota=int(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else: 
    print("Desaprobado")
#Actividad 3
num=int(input("Escriba un número par: "))
if num%2==0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")
#Actividad 4
edad=int(input("Ingrese su edad: "))
if edad<12:
    print("Sos un niño")
elif edad>=12 and edad<18:
    print("Sos un adolescente")
elif edad>=18 and edad<30:
    print("Sos un adulto joven")
elif edad>=30:
    print("Sos un adulto")
#Actividad 5
clave=input("Ingrese una contraseña: ")
if len(clave)>=8 and len(clave)<=14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 a 14 caracteres")
#Actividad 6
from statistics import mode, median, mean
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
print(numeros_aleatorios)
print(mean(numeros_aleatorios))
print(median(numeros_aleatorios))
print(mode(numeros_aleatorios))
if mean(numeros_aleatorios)>median(numeros_aleatorios) and median(numeros_aleatorios)>mode(numeros_aleatorios):
    print("Hay sesgo positivo o a la derecha")
elif mean(numeros_aleatorios)<median(numeros_aleatorios) and median(numeros_aleatorios)<mode(numeros_aleatorios):
    print("Hay sesgo negativo o a la izquierda")
elif mean(numeros_aleatorios)==median(numeros_aleatorios) and median(numeros_aleatorios)==mode(numeros_aleatorios):
    print("Sin sesgo")
#Actividad 7
texto=input("Escriba una frase o palabra: ")
ultima_letra=texto[len(texto) - 1]
if ultima_letra in "aeiou":
    texto=texto+"!"
    print(texto)
else:
    print(texto)
#Actividad 8
nombre=input("Ingrese su nombre: ")
numero=int(input("""Elija una opción:
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro 
"""))
if numero==1:
    nombre=(nombre.upper())
    print(nombre)
elif numero==2:
    nombre=(nombre.lower())
    print(nombre)
elif numero==3:
    nombre=(nombre.title())
    print(nombre)
#Actividad 9
grado=float(input("Ingrese la magnitud del terremoto: "))
if grado<3:
    print("Muy leve")
elif grado>=3 and grado<4:
    print("Leve")
elif grado>=4 and grado<5:
    print("Moderado")
elif grado>=5 and grado<6:
    print("Fuerte")
elif grado>=6 and grado<7:
    print("Muy fuerte")
elif grado>=7:
    print("Extremo")
#Actividad 10
hemisferio=input("¿En que hemisferio está? (N/S): ")
mes=int(input("¿En qué mes se encuentra? (1/12): "))
dia=int(input("¿Qué día es? (1/31): "))
if hemisferio=="N":
    if (mes==12 and dia>=21) or mes==1 or mes==2 or (mes==3 and dia<=20):
        print("Se encuentra en invierno")
    elif (mes==3 and dia>=21) or mes==4 or mes==5 or (mes==6 and dia<=20):
        print("Se encuentra en primavera")
    elif (mes==6 and dia>=21) or mes==7 or mes==8 or (mes==9 and dia<=20):
       print("Se encuentra en verano")
    elif (mes==9 and dia>=21) or mes==10 or mes==11 or (mes==12 and dia<=20):
        print("Se encuentra en otoño")
else:
    if (mes==12 and dia>=21) or mes==1 or mes==2 or (mes==3 and dia<=20):
        print("Se encuentra en verano")
    elif (mes==3 and dia>=21) or mes==4 or mes==5 or (mes==6 and dia<=20):
        print("Se encuentra en otoño")
    elif (mes==6 and dia>=21) or mes==7 or mes==8 or (mes==9 and dia<=20):
        print("Se encuentra en invierno")
    elif (mes==9 and dia>=21) or mes==10 or mes==11 or (mes==12 and dia<=20):
        print("Se encuentra en primavera")