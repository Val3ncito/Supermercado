#TRABAJO FINAL SUPERMERCADO

productos={}

def mostrarProductos():
    
    claves = productos.keys()
    for c in claves:
        dato = productos[c]
        print (c,dato[0],dato[1],dato[2],dato[3],dato[4],dato[5])


def ingresarNuevoProducto():
    
    id_producto = input("Ingrese el identificador del nuevo producto: ")
    valor = []
    almacen = {"V":"verduras","L":"lacteos","B": "bebidas","P":"panadería", "C":"carnes"}
    

    codigo = int(input("Ingrese el codigo del producto: "))
    descripcion = input("Ingrese descripción del producto: ")
    stock = int(input("Ingrese la cantidad de producto: "))
    precio_unitario = float(input("Ingrese el precio del producto: "))
    tipo_de_producto = "verdura"
    fecha_de_vencimiento = "5/12/2023"
    
    

    valor.append(codigo)
    valor.append(descripcion)
    valor.append(stock)
    valor.append(precio_unitario)
    valor.append(tipo_de_producto)
    valor.append(fecha_de_vencimiento)

    
    productos[id_producto] = valor

    
    print("Su producto fue añadido satisfactoriamente")

    nuevo_producto = int(input("Ingrese 1 para añadir nuevo producto ó 2 para salir: "))

    if nuevo_producto == 1:
        ingresarNuevoProducto()
    else:
        mostrarProductos()
        
def ingresarProductoExistente(diccionario, id):
    for clave, valor in diccionario.items():
        if clave == id:
            
            print(f"El valor para la clave {clave} es {valor}.")
            break
    else:
        
        print("No se encontró ningún ID que coincida con el ID proporcionado.")
        
            
            
            
        
        


    

ingresarNuevoProducto()
#mostrar()
id_producto= int(input("Ingrese el id del producto existente: "))
ingresarProductoExistente(productos,id_producto)
    
    
