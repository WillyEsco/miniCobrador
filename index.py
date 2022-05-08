

import sys
import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def mostrarProducto(lista, valores):
    clearConsole()
    print("+----------+--------------------+----------+")
    print("|    ID    |       NOMBRE       |  PRECIO  |")
    print("+----------+--------------------+----------+")
    indice = 0
    while indice < len(lista):
        nombre = lista[indice]
        precio = valores[indice]   
        print("|{:>10}|{:<20}|{:>10.2f}|".format(indice, nombre, precio))
        print("+----------+--------------------+----------+")
        indice = indice + 1


nombres = []
precios = []
cuenta = []
cuentaPrecio = []
 
while True:
    print("""
***************************************

          -- MINI COBRADOR --
         willyescobar@gmail.com

***************************************
""")
    eleccion = input("""
1 - Agregar un producto al inventario
2 - Remover un producto del inventario  
3 - Añadir a la cuenta
4 - Retirar de la cuenta
5 - Visulizar Inventario
6 - Visualizar cuenta
7 - Cobrar
8 - Salir
Seleccione: """)
    if eleccion == "1":
        clearConsole()
        nombre = input("Nombre del producto: ")
        precio = float(input("Precio del producto: "))
        nombres.append(nombre)
        precios.append(precio)
        mostrarProducto(nombres, precios)   
        continue

    if eleccion == "2":
        mostrarProducto(nombres, precios)   
        id = int(input("Ingresar ID del producto a eliminar: "))
        print( f"Remover {nombre}. id: {id}")
        if input("Seguro (s/n): ") == "s":
            if id < len(nombres):
                nombre = nombres[id]
                nombres.pop(id)
                precios.pop(id) 
                if id in cuenta:
                    cuenta.pop(id)
                    price = precios(id)
                    cuentaPrecio.remove(price)
                    mostrarProducto(nombres, precios)  
                    print( f"Se remueve  {nombre}. id: {id}")
                else:
                   continue

    if eleccion == "3":
        mostrarProducto(cuenta, cuentaPrecio)             
        id = int(input("Ingresar ID a añadir a la cuenta: "))
        if id not in cuenta:
            cuenta.append(id)
            elemento = precios(id)
            cuentaPrecio.append(elemento)
            print("Producto ingresado en la cuenta exitosamente")
        else:
            print("Producto previamente ingresado en la cuenta")
        continue

    if eleccion == "4":
        clearConsole()           
        id = int(input("Ingresar ID a retirar de la cuenta: "))
        if id in cuenta:
            del cuenta[id]
            print("Producto retirado de la cuenta exitosamente")
        else:
            print("Producto no existente en la cuenta")
        continue

    if eleccion == "5":
        clearConsole()  
        mostrarProducto(nombres, precios)   
        if input("Presione un tecla para continuar...") == "s":    
            continue  

    if eleccion == "6":
        clearConsole()  
        mostrarProducto(cuenta, cuentaPrecio) 
        if input("Continuar (s/n): ") == "s":    
            continue

    if eleccion == "7":
        clearConsole()
        if input("Seguro (s/n): ") == "s":
            suma = sum(cuentaPrecio) 
            print(f"¡Gracias por su compra! -- Su Total es: {float(suma)}")
            sys.exit()

    if eleccion == "8":
        if input("Seguro (s/n): ") == "s":
            sys.exit()