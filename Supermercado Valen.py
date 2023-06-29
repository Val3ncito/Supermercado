"""
1✔Agregar un nuevo producto.
2✔ Eliminar un producto dado su código.
3✔ Listar todos los productos de una forma prolija.
4✔ Actualizar el stock cuando se vende un producto.
5✔ Actualizar el precio unitario de un producto determinado en un cierto porcentaje.
6✔ Determinar la existencia de un producto para poder vender la cantidad solicitada.
7✔ Reponer un producto cuando el stock está por debajo de un mínimo requerido.
8✔ Pedir los datos de un cliente para hacer envío a domicilio.
9X Determinar cuál es el artículo más vendido.
10X Eliminar del supermercado (guardarlos en un otro diccionario) los artículos que estén vencidos.
11X Simular la venta a un cliente y emitir el ticket de venta.
12✔ Agregar información adicional al producto para saber si un determinado producto tiene o no descuento.
13✔ Si el producto vence en una semana hacer un 10% de descuento.
14X Determinar el producto más vendido dependiendo del tipo de producto.
"""

from datetime import datetime
productos={"1234":["Lechuga", "0001", "50", "Verdura", "2023/8/30", "10"],"5678":["Tomate", "0002", "4000", "Verdura", "2023-07-12]"]}
Usuarios={"123":["Valen", "Roque Saenz Peña"], "456":["Pepe", "Cabildo"]}

#1
def IngresarNuevoProducto():
    valor=[]
    codigo=int(input("Ingrese el código del nuevo producto: "))
    descripcion=input("Ingrese descripción del producto: ")
    stock=int(input("Ingrese el stock de producto: "))
    precio_unitario=float(input("Ingrese el precio del producto: "))
    tipo_de_producto="verdura"
    fecha_de_vencimiento=input("Ingrese fecha de vencimiento dd/mm/aa: ")
    fecha = datetime.strptime(fecha_de_vencimiento, "%d/%m/%Y")
    tiene_descuento = False
        
#2          
def EliminarProducto(diccionario):
    codigo = int(input("Ingrese el código del producto que desea a eliminar: "))
    del diccionario[codigo]
    print("El producto ha sido eliminado satisfactoriamente")

#3
def ListarProductos():
    claves=productos.keys()
    for c in claves:
        dato=productos[c]
        print(c,dato[0],dato[1],dato[2],dato[3],dato[4])

#4
def ActualizarStock(diccionario):
    descripcion = input("Ingrese descripción del producto que desea comprar: ")
    stock = int(input("Ingrese la cantidad deseada: "))
    for i in diccionario:
        if diccionario[i][0] == descripcion:
            stock_real = diccionario[i][1] - stock
            print("El stock real del producto es " + str(stock_real))

#5
def ActualizarPrecio(productos):
    Clave=input("Ingresar Código de Producto: ")
    Porcentaje=int(input("Ingresar Porcentaje: "))
    Precio=int((productos.get(Clave)[2]))
    PrecioF=(Precio+(Precio*Porcentaje/100))
    productos.get(Clave)[2]=PrecioF

#6
def DeterminarExistenciaDelProducto(diccionario):
    codigo = int(input("Ingrese el código del producto del cual desea saber su existencia: "))
    claves = diccionario.keys()
    for i in claves:
        if i == codigo:
            listarProductos()
        else:
            print("El producto no existe")

#7
def ReponerProducto(diccionario):
    minimo = 10
    for i in diccionario:
        if diccionario[i][1]== 0:
            print("Producto sin stock")
        if diccionario[i][1] < minimo:
            print("Alerta!! Reponer stock")

#8
def EnvioDomicilio(Usuarios):
    DNI=input("Ingresar DNI: ")
    valor=[]
    if DNI in Usuarios:
        fecha=input("Ingrese Cuando desea recibir su pedido: ")
        print("")
        print("El envio será el: ",fecha)
        print("Domicilio: ", Usuarios[DNI][1])
        print("A pedido de: ", Usuarios[DNI][0])
    else:
        Nombre=input("Ingrese su nombre completo: ")
        Direccion=input("Ingrese su direccion: ")
        fecha=input("Ingrese cuando desea recibir su pedido: ")
        valor.append(Nombre)
        valor.append(Direccion)
        Usuarios[DNI]=valor
        print("")
        print("El envio será el:", fecha)
        print("Domicilio: ", Usuarios[DNI][1])
        print("A pedido de: ",Usuarios[DNI][0])

#12
def TieneDescuento(diccionario):
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

#13
def DescuentoProducto(diccionario):
    fecha_actual = datetime.now()
    for i in diccionario:
        fecha_vencimiento = diccionario[i][4]
        prueba = fecha_vencimiento - fecha_actual
        
        if  int(prueba.days)<= 7 and (prueba.days)>0:
            precio = diccionario[i][2]
            descuento = precio * 0.1
            diccionario[i][2] = precio - descuento
            diccionario[i][5] = True


#9
#10
#11
#14








