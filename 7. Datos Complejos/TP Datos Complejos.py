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
print(lista_frutas)
#Actividad 4
contactos = {}
for i in range(5):
    print(f"Ingrese el contacto n° {i + 1}")
    clave = input("Ingrese su nombre: ").capitalize()
    valor = input(f"Ingrese el número para {clave}: ")
    contactos[clave] = valor
    print(f"{clave} añadido/a con éxito")
consulta = input("Ingrese el nombre que desea buscar: ").capitalize()
if consulta in contactos:
    numero_consultado = contactos[consulta]
    print(f"El número de {consulta} es: {numero_consultado}")
else:
    print("El nombre buscado no está en el diccionario")