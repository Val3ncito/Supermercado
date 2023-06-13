#TRABAJO FINAL SUPERMERCADO
"""
✔Agregar un nuevo producto.
✔Eliminar un producto dado su código.
✔Listar todos los productos de una forma prolija.
• Actualizar el stock cuando se vende un producto.
• Actualizar el precio unitario de un producto determinado en un cierto procentaje.
✔Determinar la existencia de un producto para poder vender la cantidad solicitada.
• Reponer un producto cuando el stock está por debajo de un mínimo requerido.
• Pedir los datos de un cliente para hacer envío a domicilio.
• Determinar cuál es el artículo más vendido.
• Eliminar del supermercado (guardarlos en un otro diccionario) los artículos que estén
vencidos.
• Simular la venta a un cliente y emitir el ticket de venta.
• Agregar información adicional al producto para saber si un determinado producto tiene o no
descuento.
• Si el producto vence en una semana hacer un 10% de descuento.
• Determinar el producto más vendido dependiendo del tipo de producto.
"""


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
    stock = int(input("Ingrese el stock de producto: "))
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

def reponerProducto(diccionario):
    
    
    minimo = 10

    lista_claves = list(diccionario.keys())
    lista_valores = list(diccionario.values())
    
    for i in lista_valores:
        
        """recorriendo todos los valores del diccionario"""
        
        for j in i:
            
            """ recorriendo todos los datos dentro de la lista de cada uno de los valores"""

            if stock_producto == j:
                """  ya tengo el codigo del producto que quiero eliminar guardado en esa variable"""
                
                
                posicion = lista_valores.index(i)
                del lista_claves[posicion]

                """ devuelve la posicion en la que se encuentra el codigo del producto a eliminar y esta guardado en la variable posision"""
        














    



    

ingresarNuevoProducto()

#id_producto= int(input("Ingrese el id del producto existente: "))
#ingresarProductoExistente(productos,id_producto)
#eliminarProducto(productos)
determinarExistenciaDelProducto(productos)

    
