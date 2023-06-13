#TRABAJO FINAL SUPERMERCADO
"""
✔Agregar un nuevo producto.
✔Eliminar un producto dado su código.
✔Listar todos los productos de una forma prolija.
• Actualizar el stock cuando se vende un producto.
• Actualizar el precio unitario de un producto determinado en un cierto procentaje.
✔Determinar la existencia de un producto para poder vender la cantidad solicitada.
✔Reponer un producto cuando el stock está por debajo de un mínimo requerido.
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

    for i in diccionario:
        if diccionario[i][1]== 0:
            print("Producto sin stock")
        if diccionario[i][1] < minimo:
            print("Alerta!! Reponer stock")
 

#ingresarNuevoProducto()
#ingresarProductoExistente(productos,id_producto)
#eliminarProducto(productos)
#determinarExistenciaDelProducto(productos)
#reponerProducto(productos)
    
