# Actividad 1
precios_frutas = {
"Banana": 1200, 
"Ananá": 2500, 
"Melón": 3000, 
"Uva": 1450
}
precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

# Actividad 2
precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

# Actividad 3
lista_frutas = list(precios_frutas.keys())

#Actividad 4
contactos = {}
for i in range(5):
    print(f"Contacto n° {i + 1}")
    clave = input("Ingrese su nombre: ").capitalize()
    valor = input(f"Ingrese el número para {clave}: ")
    contactos[clave] = valor
    print(f"{clave} añadido/a con éxito")
consulta = input("Ingrese el nombre que desea buscar: ").capitalize()
if consulta in contactos:
    numero_consultado = contactos[consulta]
    print(f"El número de {consulta} es: {numero_consultado}")
else:
    print("Nombre no encontrado")

#Actividad 5
frase = input("Escriba una frase: ")
palabras = frase.split()
set_palabras = set(palabras)
palabras_repetidas = {}
for palabra in palabras:
    if palabra in palabras_repetidas:
        palabras_repetidas[palabra] += 1
    else:
        palabras_repetidas[palabra] = 1
print("Palabras únicas:", set_palabras)
print("Palabras repetidas:", palabras_repetidas)

#Actividad 6
notas_alumnos = {}
for i in range(3):
    alumnos = input(f"Ingrese el nombre del alumno n° {i + 1}: ").capitalize()
    notas_actuales = []
    for j in range(3):
        notas = float(input(f"Ingrese la nota {j + 1} de {alumnos}: "))
        notas_actuales.append(notas)
    notas_alumnos[alumnos] = tuple(notas_actuales)
for nombre_alumno, tupla_notas in notas_alumnos.items():
    suma = sum(tupla_notas)
    prom = suma / len(tupla_notas)
    print(f"{nombre_alumno} tiene promedio: {prom}")

#Actividad 7
parcial1 = {1, 2, 3, 4, 5}
parcial2 = {3, 4, 6, 7, 8}
ambos = parcial1 & parcial2
uno = parcial1 ^ parcial2
uno_o_mas = parcial1 | parcial2
print("Aprobaron ambos:", ambos)
print("Aprobaron uno solo:", uno)
print("Aprobaron uno o más:", uno_o_mas)

#Actividad 8
tienda = {
    "Reglas": 20, 
    "Lápices": 0, 
    "Tijeras": 6, 
    "Resaltadores": 16
    }
producto_consultado = input("¿Qué producto desea consultar?: ").capitalize()
if producto_consultado in tienda:
    print(f"{producto_consultado} tiene {tienda[producto_consultado]} unidades disponibles")
    unidades_agregadas = int(input("¿Cuántas unidades desea agregar?: "))
    tienda[producto_consultado] += unidades_agregadas
    print(f"Ahora {producto_consultado} tiene {tienda[producto_consultado]} unidades")
else:
    print("El producto consultado no está en la tienda")
    unidades_nuevas = int(input("¿Con cuántas unidades desea ingresar el producto nuevo?: "))
    tienda[producto_consultado] = unidades_nuevas
    print(f"{producto_consultado} agregado a la tienda con {unidades_nuevas} unidades")

#Actividad 9
agenda = {
    ("Lunes", "10:00"): "Reunión",
    ("Martes", "15:00"): "Clase de inglés",
    ("Miercoles", "13:00"): "Almuerzo familiar",
    ("Miercoles", "21:00"): "Entrenamiento"
}
dia = input("¿Qué día desea consultar?: ").capitalize()
hora = input ("¿Qué horario desea consultar?(Ej: 15:00): ")
consulta = (dia, hora)
if consulta in agenda: 
    print(agenda[consulta])
else:
    print("No hay actividades para el momento consultado")

#Actividad 10
original = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Brasil": "Brasilia",
    "Uruguay": "Montevideo"
}
invertido = {}
for paises, capitales in original.items():
    invertido[capitales] = paises
print("Diccionario original: ", original)
print("Diccionario invertido: ", invertido)
