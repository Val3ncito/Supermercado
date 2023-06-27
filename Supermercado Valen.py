#TRABAJO FINAL SUPERMERCADO
"""
✔Agregar un nuevo producto.
✔Eliminar un producto dado su código.
✔Listar todos los productos de una forma prolija.
✔ Actualizar el stock cuando se vende un producto.
✔ Actualizar el precio unitario de un producto determinado en un cierto porcentaje.
✔Determinar la existencia de un producto para poder vender la cantidad solicitada.
✔ Reponer un producto cuando el stock está por debajo de un mínimo requerido.
✔ Pedir los datos de un cliente para hacer envío a domicilio.
X Determinar cuál es el artículo más vendido.
•- Eliminar del supermercado (guardarlos en un otro diccionario) los artículos que estén vencidos.
X Simular la venta a un cliente y emitir el ticket de venta.
✔ Agregar información adicional al producto para saber si un determinado producto tiene o no descuento.
X Si el producto vence en una semana hacer un 10% de descuento.
X Determinar el producto más vendido dependiendo del tipo de producto.
"""

from datetime import datetime
productos={"1234":["Lechuga", "0001", "50", "Verdura", "2023/8/30", "10"],"5678":["Tomate", "0002", "4000", "Verdura", "2023-07-12]"]}
Usuarios={"123":["Valen", "Roque Saenz Peña"], "456":["Pepe", "Cabildo"]}


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
    from datetime import datetime
    fecha_de_vencimiento = "5/12/2023"
    
    
    valor.append(descripcion)
    valor.append(stock)
    valor.append(precio_unitario)
    valor.append(tipo_de_producto)
    valor.append(fecha_de_vencimiento)

    
    productos[codigo]=valor

    
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

    for i in diccionario:
        if diccionario[i][1]== 0:
            print("Producto sin stock")
        if diccionario[i][1] < minimo:
            print("Alerta!! Reponer stock")


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



def Descuento(productos):
    #FuncionISra
    Codigo=input("Ingresar Código del Producto: ")
    if len(productos.get(Codigo))==5:
        print("El producto no tiene descuento")
    elif len(productos.get(Codigo))!=5:
        print("El producto tiene un descuento del "+str(productos.get(Codigo)[5])+"%")
        Precio=int((int(productos.get(Codigo)[2]))*(int(productos.get(Codigo)[5])/100))
        print("Precio: "+str(Precio)+"$")




def ActualizarPrecio(productos):
    Clave=input("Ingresar Código de Producto: ")
    Porcentaje=int(input("Ingresar Porcentaje: "))
    Precio=int((productos.get(Clave)[2]))
    PrecioF=(Precio+(Precio*Porcentaje/100))
    productos.get(Clave)[2]=PrecioF





