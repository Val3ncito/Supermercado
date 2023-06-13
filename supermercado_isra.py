#TRABAJO FINAL SUPERMERCADO

productos={}

def listarProductos():
    
    claves = productos.keys()
    for c in claves:
        dato = productos[c]
        print (c,dato[0],dato[1],dato[2],dato[3],dato[4])


def ingresarNuevoProducto():
    
    codigo = int(input("Ingrese el código del nuevo producto: "))
    valor = []
    #almacen = {"V":"verduras","L":"lacteos","B": "bebidas","P":"panadería", "C":"carnes"}

    
    descripcion = input("Ingrese descripción del producto: ")
    stock = int(input("Ingrese la cantidad de producto: "))
    precio_unitario = float(input("Ingrese el precio del producto: "))
    tipo_de_producto = "verdura"
    fecha_de_vencimiento = "5/12/2023"
    
    
    valor.append(descripcion)
    valor.append(stock)
    valor.append(precio_unitario)
    valor.append(tipo_de_producto)
    valor.append(fecha_de_vencimiento)

    
    productos[codigo] = valor

    
    print("Su producto fue añadido satisfactoriamente")

    nuevo_producto = int(input("Ingrese 1 para añadir nuevo producto ó 2 para salir: "))

    if nuevo_producto == 1:
        ingresarNuevoProducto()
    else:
        listarProductos()
        
##def ingresarProductoExistente(diccionario, id):
##    for clave, valor in diccionario.items():
##        if clave == id:
##            
##            print(f"El valor para la clave {clave} es {valor}.")
##            break
##    else:
##        
##        print("No se encontró ningún ID que coincida con el ID proporcionado.")
##        
##            
            
def eliminarProducto(diccionario):
    codigo = int(input("Ingrese el código del producto que desea a eliminar: "))
    del diccionario[codigo]
    print("El producto ha sido eliminado satisfactoriamente")


def determinarExistenciaDelProducto(diccionario):
    codigo = int(input("Ingrese el código del producto del cual desea saber su existencia: "))

    claves = diccionario.keys()

    for i in claves:
        if i == codigo:
            listarProductos()
        else:
            print("El producto no existe")
    


    

ingresarNuevoProducto()

#id_producto= int(input("Ingrese el id del producto existente: "))
#ingresarProductoExistente(productos,id_producto)
#eliminarProducto(productos)
determinarExistenciaDelProducto(productos)

    
