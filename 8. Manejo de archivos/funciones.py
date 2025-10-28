#Actividad 1
def creacion():
    with open("productos.txt", "w") as archivo_productos:
        archivo_productos.write("Silla,38000,35\n")
        archivo_productos.write("Mesa,220000,6\n")
        archivo_productos.write("Sillon,40000,0\n")

#Actividad 2
def mostrar_productos():
    with open ("productos.txt", "r") as archivo_leido:
        for linea in archivo_leido:
            linea_limpia = linea.strip()
            if linea_limpia:
                nombre, precio, cantidad = linea_limpia.split(",")
                print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

#Actividad 3
def agregar_producto():
    producto_agregado = input("Ingrese un nuevo producto: ").capitalize()
    precio_agregado = input("Ingrese su precio: ")
    stock_agregado = input("Ingrese su stock inicial: ")
    producto_nuevo = f"{producto_agregado},{precio_agregado},{stock_agregado}\n"
    with open ("productos.txt", "a") as archivo:
        archivo.write(producto_nuevo)
    print("El producto se agregó con éxito")

#Actividad 4
def productos_en_lista():
    productos = []
    with open ("productos.txt", "r") as archivo:
        for linea in archivo:
            nombre, valor, stock = linea.strip().split(",")
            producto = {
                "Nombre": nombre,
                "Precio": float(valor),
                "Cantidad": int(stock) 
                }
            productos.append(producto)
    return productos

#Actividad 5
def buscar_producto(productos):
    producto_buscado = input("Ingrese el nombre del producto que está buscando: ").capitalize()
    encontrado = False
    for producto in productos:
        if producto_buscado == producto["Nombre"]:
            print(producto)
            encontrado = True
            break
    if encontrado == False:
        print("El producto buscado no está en la lista")

#Actividad 6
def actualizacion_total(productos):
    with open ("productos.txt", "w") as archivo:
        for diccionario in productos:
            producto = diccionario["Nombre"]
            valor = diccionario["Precio"]
            cantidad = diccionario["Cantidad"]
            archivo.write(f"{producto},{valor},{cantidad}\n")
        print("Productos totalmente actualizados")