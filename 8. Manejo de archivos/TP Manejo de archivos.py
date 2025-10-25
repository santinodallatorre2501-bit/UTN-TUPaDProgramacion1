#Actividad 1
nombre_archivo = "productos.txt"
with open(nombre_archivo, "w") as archivo_productos:
    archivo_productos.write("nombre,precio,cantidad\n")
    archivo_productos.write("silla,38000,35\n")
    archivo_productos.write("mesa,220000,6\n")
    archivo_productos.write("sillon,40000,0\n")

#Actividad 2

with open ("prodcutos.txt", "r") as archivo_leido:
    lineas = archivo_leido.readlines()
    for linea in lineas:
        lectura = linea.strip().split(",")
        print(lectura)