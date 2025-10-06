# Ejercicio 1
def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()
# Ejercicio 2
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

nombre2 = input("Ingrese su nombre: ")
saludar_usuario(nombre2)
# Ejercicio 3
def informacion_persona(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre3 = input("Ingrese su nombre: ")
apellido3 = input("Ingrese su apellido: ")
edad3 = input("Ingrese su edad: ")
residencia3 = input("Ingrese su lugar de residencia: ")
informacion_persona(nombre3, apellido3, edad3, residencia3)
# Ejercicio 4
def calcular_area_circulo(radio):
    return 3.14 * (radio ** 2)
def calcular_perimetro_circulo(radio):
    return 2 * 3.14 * radio

radio = float(input("Ingrese el radio de un círculo: "))
print("Área:", calcular_area_circulo(radio))
print("Perímetro:", calcular_perimetro_circulo(radio))
# Ejercicio 5
def segundos_a_horas(segundos):
    minutos = segundos / 60
    horas = minutos / 60
    print(horas)

segundos = int(input("Ingrese una cantidad de segundos: "))
segundos_a_horas(segundos)
# Ejercicio 6
def tabla_multiplicar(numero):
    for i in range(1,11):
        print(numero,"x", i,"=",(numero * i))

numero_multiplicar = int(input("Ingrese el número que desea multiplicar: "))
tabla_multiplicar(numero_multiplicar)
# Ejercicio 7
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    print(a, "+", b, "=", suma)
    print(a, "-", b, "=", resta)
    print(a, "x", b, "=", multiplicacion)
    print(a, "/", b, "=", division)

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
operaciones_basicas(num1, num2)
# Ejercicio 8
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = calcular_imc(peso, altura)
print("Su IMC es: ",round(imc, 2))
# Ejercicio 9
def celsius_a_farenheit(celsius):
    return celsius * 9/5 + 32

celsius = float(input("Ingrese una temperatura en grados celsius: "))
farenheit = celsius_a_farenheit(celsius)
print(celsius, "grados celsius equivalen a", farenheit, "grados farenheit")
# Ejercicio 10
def calcular_promedio(a, b, c): 
    promedio = (a + b + c) / 3
    return promedio

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))
promedio = calcular_promedio(num1, num2, num3)
print("El promedio de los números ingresados es:", promedio)