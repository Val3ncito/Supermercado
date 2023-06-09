#TRABAJO FINAL SUPERMERCADO

productos={}

def mostrar():
    claves = productos.keys()
    for c in claves:
        dato = productos[c]
        print (dato[1],dato[2])


def ingresarNuevoProducto():
    id_producto = input("Ingrese el identificador del nuevo producto: ")
    valor = []
    almacen = {"V":"verduras","L":"lacteos","B": "bebidas","P":"panadería", "C":"carnes"}
    

    codigo = int(input("Ingrese el codigo del producto: "))
    descripcion = input("Ingrese descripción del producto: ")
    stock = int(input("Ingrese la cantidad de producto: "))
    precio_unitario = float(input("Ingrese el precio del producto: "))
    tipo_de_producto = "verdura"
    fecha_de_vencimiento = "5/1272023"
    
    

    valor.append(codigo)
    valor.append(descripcion)
    valor.append(stock)
    valor.append(precio_unitario)
    valor.append(tipo_de_producto)
    valor.append(fecha_de_vencimiento)

    
    productos[id_producto] = valor

ingresarNuevoProducto()
mostrar()
print(productos)
    
    
