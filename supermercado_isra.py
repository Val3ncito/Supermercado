#TRABAJO FINAL SUPERMERCADO
"""
✔Agregar un nuevo producto.
✔Eliminar un producto dado su código.
✔Listar todos los productos de una forma prolija.
✔Actualizar el stock cuando se vende un producto.
• Actualizar el precio unitario de un producto determinado en un cierto procentaje.
✔Determinar la existencia de un producto para poder vender la cantidad solicitada.
✔Reponer un producto cuando el stock está por debajo de un mínimo requerido.
✔Pedir los datos de un cliente para hacer envío a domicilio.
• Determinar cuál es el artículo más vendido.
• Eliminar del supermercado (guardarlos en un otro diccionario) los artículos que estén
vencidos.
• Simular la venta a un cliente y emitir el ticket de venta.
✔Agregar información adicional al producto para saber si un determinado producto tiene o no
descuento.
✔Si el producto vence en una semana hacer un 10% de descuento.
• Determinar el producto más vendido dependiendo del tipo de producto.
"""


from datetime import datetime, date
from time import strftime

productos = {}


def listarProductos():
    claves = productos.keys()
    for c in claves:
        dato = productos[c]
        print(c, dato[0], dato[1], dato[2], dato[3], dato[4])


def ingresarNuevoProducto():
    codigo = int(input("Ingrese el código del nuevo producto: "))
    valor = []

    descripcion = input("Ingrese descripción del producto: ")
    stock = int(input("Ingrese el stock de producto: "))
    precio_unitario = float(input("Ingrese el precio del producto: "))
    tipo_de_producto = "verdura"
    fecha_de_vencimiento = input("Ingrese fecha de vencimiento dd/mm/aa: ")
    fecha = datetime.strptime(fecha_de_vencimiento, "%d/%m/%Y")
    tiene_descuento = False


    valor.append(descripcion)
    valor.append(stock)
    valor.append(precio_unitario)
    valor.append(tipo_de_producto)
    valor.append(fecha)
    valor.append(tiene_descuento)


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


def ingresarProductoExistente(diccionario):
    codigo = int(input("Ingrese el código del producto: "))
    cantidad = int(input("Ingrese la cantidad que desea añadir: "))
    claves = diccionario.keys()

    for i in claves:
        if i == codigo:
            stock_anterior = diccionario[i][1]
            aux = stock_anterior + cantidad
            diccionario[i][1] = aux
    

def reponerProducto(diccionario):
    minimo = 10

    for i in diccionario:
        if diccionario[i][1] == 0:
            print("Producto sin stock")
        if diccionario[i][1] < minimo:
            print("Alerta!! Reponer stock")


def actualizarStock(diccionario):
    descripcion = input("Ingrese descripción del producto que desea comprar: ")
    stock = int(input("Ingrese la cantidad deseada: "))

    for i in diccionario:
        if diccionario[i][0] == descripcion:
            stock_real = diccionario[i][1] - stock
            print("El stock real del producto es " + str(stock_real))


def descuentoProducto(diccionario):
    fecha_actual = datetime.now()

    for i in diccionario:
        fecha_vencimiento = diccionario[i][4]
        prueba = fecha_vencimiento - fecha_actual
        
        if  int(prueba.days)<= 7 and (prueba.days)>0:
            precio = diccionario[i][2]
            descuento = precio * 0.1
            diccionario[i][2] = precio - descuento
            diccionario[i][5] = True

def tieneDescuento(diccionario):
    codigo = int(input("Ingrese el código del producto del cual desea saber si tiene descuento: "))
    claves = diccionario.keys()

    for i in claves:
        if i == codigo:
            aux = ""
            if diccionario[i][5]:
                aux = " El producto tiene descuento"
                print(aux)
            else:
                aux = "El producto no tiene descuento"
                print(aux)


ingresarNuevoProducto()
#ingresarProductoExistente(productos)
# eliminarProducto(productos)
# determinarExistenciaDelProducto(productos)
# reponerProducto(productos)
# actualizarStock(productos)
#descuentoProducto(productos)
#tieneDescuento(productos)
