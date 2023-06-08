#TRABAJO FINAL SUPERMERCADO

productos={}



def ingresarNuevoProducto():
    id_producto = input("Ingrese el identificador del nuevo producto")
    valor = []

    codigo = int(input("Ingrese el codigo del producto"))
    descripcion = input("Ingrese descripción del producto")
    stock = int(input("Ingrese la cantidad de producto"))
    precio_unitario = float(input("Ingrese el precio del producto"))

    valor.append(codigo)
    valor.append(descripcion)
    valor.append(stock)
    valor.append(precio_unitario)

    
    productos[id_producto] = valor

ingresarNuevoProducto()
print(productos)
    
    
