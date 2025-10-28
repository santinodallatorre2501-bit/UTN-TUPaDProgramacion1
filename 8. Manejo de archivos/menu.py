import funciones as opciones

opciones.creacion()

menu = True
while menu:
    print("""
APLICACIÓN DE PRODUCTOS
1. Ver productos
2. Agregar producto
3. Buscar producto
4. Salir    
          """)
    opcion = input("Elija una opción: ")
    if opcion == "1":
        opciones.mostrar_productos()
    elif opcion == "2":
        opciones.agregar_producto()
    elif opcion == "3":
        lista_productos = opciones.productos_en_lista()
        opciones.buscar_producto(lista_productos)
    elif opcion == "4":
        menu = False
    else: 
        print("Escoja una opción correcta")
