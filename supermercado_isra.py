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
        
            
            
def eliminarProducto(diccionario,codigo_producto):
    
    lista_claves = list(diccionario.keys())
    lista_valores = list(diccionario.values())
    
    for i in lista_valores:
        
        """recorriendo todos los valores del diccionario"""
        
        for j in i:
            
            """ recorriendo todos los datos dentro de la lista de cada uno de los valores"""

            if codigo_producto == j:
                """  ya tengo el codigo del producto que quiero eliminar guardado en esa variable"""
                
                
                posicion = lista_valores.index(i)
                del lista_claves[posicion]

                """ devuelve la posicion en la que se encuentra el codigo del producto a eliminar y esta guardado en la variable posision"""
    print(lista_claves)            
    """ me equivoque y elimina la clave en la lista no en el diccionario"""   
    mostrarProductos()    


    

ingresarNuevoProducto()
#mostrarProductos()
#id_producto= int(input("Ingrese el id del producto existente: "))
#ingresarProductoExistente(productos,id_producto)
eliminarProducto(productos,56)

    
