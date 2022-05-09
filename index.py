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
        precio = precios[indice]   
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

        while True:
            try:
                precio = float(input("Precio del producto: "))            
            except ValueError:
                print("Debes escribir un número.")
                continue

            if precio < 0:
                print("El precio debe ser un número positivo.")
                continue
            else:
                nombres.append(nombre)
                precios.append(precio)
                mostrarProducto(nombres, precios)   
                break

    if eleccion == "2":
        if len(nombres)==0:
            input("""
            
            ***************************************
            *  No existen productos en invetario  *
            ***************************************

Presione una tecla para continuar...""")  
            continue
        else:          
            mostrarProducto(nombres, precio)   
            id = input("Ingresar ID del producto a eliminar: ")
            if id=="":
                continue
            else:
                id = int(id)
                if not id in range(0,len(nombres)):
                    mostrarProducto(nombres, precio) 
                    id = input("Debe Ingresar ID de producto EXISTENTE para eliminar: ")
            if id=="" or (not int(id) in range(0,len(nombres))):
                continue            
            print( f"El producto {nombre}, (id: {id}) ha sido eliminado del inventario")
            nombre = nombres[id]
            nombres.pop(id)
            precios.pop(id) 


    if eleccion == "3":  
        if len(nombres)==0:
            input("""
            
            ***************************************
            *  No existen productos en invetario  *
            ***************************************

Presione una tecla para continuar...""")  
            continue
        else:
            mostrarProducto(nombres, precio)     
#
        while True:
            try:
                id = int(input("Ingresar ID a añadir a la cuenta: "))         
            except ValueError:
                print("Debes escribir un número.")
                continue     
            if id in range(0,len(nombres)):
                break
            else:
                print("Debes ingresar un id existente en el inventario.")
                continue

        if id not in cuenta:
            cuenta.append(nombres[id])
            cuentaPrecio.append(precios[id])

            print("Producto ingresado en la cuenta exitosamente")
        else:
            print("Producto previamente ingresado en la cuenta")
            

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