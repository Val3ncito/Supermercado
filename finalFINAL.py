import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import copy
from datetime import datetime



productos = {
    'frutas': {},
    'verduras': {},
    'carnes': {}
}

vencidos = {
    'frutas': {
    },
    'verduras': {
    },
    'carnes': {
    }

}

ventas = {
    'frutas': {
    },
    'verduras': {
    },
    'carnes': {
    }
}
def Venta(aceptar_var,nombre_entry,apellido_entry,age_spinbox,dni_entry,dire_entry, codigo_Entry, cantidad_spinbox,tipo_Entry):
    accepted = aceptar_var.get()

    if accepted == "aceptados":
        # Usuario
        nombre = nombre_entry.get()
        apellido = apellido_entry.get()
        edad = age_spinbox.get()
        dirrecion = dire_entry.get()

        # compra
        tipo = tipo_Entry.get()
        codigo = codigo_Entry.get()
        cantidad = cantidad_spinbox.get()

        if nombre and apellido and edad and dirrecion and tipo and codigo and cantidad:
            aviso = VerificarCantidad(codigo_Entry, cantidad_spinbox,tipo_Entry)

            if (aviso == True):
                ventas[tipo][codigo] = productos[tipo][codigo].copy()
                ventas[tipo][codigo][1] = cantidad
                productos[tipo][codigo][1] = int(productos[tipo][codigo][1]) - int(cantidad)
                print(ventas)
                if (productos[tipo][codigo][1] == 0):
                    del productos[tipo][codigo]

                tk.messagebox.showinfo(title='Ticket', message='------------------------------------------\nNombre: ' + nombre + '/' + 'Apellido: ' + apellido + "\nEdad: " + edad + '/' + "Dirrecion: " + dirrecion + "\ncodigo del producto comprado: " + codigo + "# cantidad: " + cantidad + "\nSu producto sera enviado en dias habiles a la dirrecion " + dirrecion + '\nMuchas gracias por comprar' + '\n------------------------------------------')
            else:
                tk.messagebox.showwarning(title='Error', message='Hubo algun problema al realizar la compra, Porfavor vuelva a intentar.')
            print("------------------------------------------")
            print("Nombre: ", nombre, '/', "Apellido: ", apellido)
            print("Edad: ", edad, '/', "Dirrecion: ", dirrecion)
            print("codigo del producto comprado: ", codigo, "# cantidad: ", cantidad)
            print("Su producto sera enviado en dias habiles a la dirrecion", dirrecion)
            print('Muchas gracias por comprar')
            print("------------------------------------------")

        else:
            tk.messagebox.showwarning(title="Error", message="Los datos solicitados son requeridos.")
    else:
        tk.messagebox.showwarning(title="Error", message="No has aceptado los terminos y condiciones")
def VerificarCantidad(codigo, cant, tip):
    tipo = tip.get()
    clave = codigo.get()
    cantidad = cant.get()

    if tipo in productos:
        if clave in productos[tipo]:
            mon = int(productos[tipo][clave][1])
            if mon >= int(cantidad):
                tk.messagebox.showwarning(title='Aviso',message="Hay la cantidad de producto necesitado")
                return True
            else:
                tk.messagebox.showwarning(title='Aviso',message="No hay la cantidad de producto necesitado")
                return False
        else:
            tk.messagebox.showwarning(title='Error',message="No se encontró la clave {clave} en el diccionario de productos")
            return False
def descuentoProducto(diccionario):
    fecha_actual = datetime.now().date()

    for categoria in diccionario.values():
        for producto in categoria.values():
            fecha_vencimiento = producto[3].date()
            prueba = fecha_vencimiento - fecha_actual

            if 0 < prueba.days <= 7:
                precio_str = producto[2]
                precio = float(precio_str)
                descuento = precio * 0.1
                producto[2] = str(precio - descuento)
                producto[4] = True
def productosVencidos(diccionario):
    fecha_actual = datetime.now()
    lista_claves_a_eliminar = []
    copia_diccionario = diccionario.copy()

    for categoria, productos_categoria in copia_diccionario.items():
        claves_productos = productos_categoria.keys()
        for clave_producto in claves_productos:
            producto = productos_categoria[clave_producto]
            fecha_vencimiento = producto[3]
            if fecha_vencimiento < fecha_actual:
                vencidos.setdefault(categoria, {})[clave_producto] = producto
                lista_claves_a_eliminar.append((categoria, clave_producto))

    for categoria, clave_producto in lista_claves_a_eliminar:
        del diccionario[categoria][clave_producto]
def eliminarProducto(diccionario):
    tipo = caja_tipo_eliminar.get()
    codigo = caja_codigo_eliminar.get()
    if tipo and codigo:
        if tipo in diccionario:
            if codigo in diccionario[tipo]:
                del diccionario[tipo][codigo]
                tk.messagebox.showwarning(title='!!!', message="El producto fue eliminado correctamente")
            else:
                tk.messagebox.showwarning(title='Error',message="El producto con el código ingresado no existe")
        else:
            tk.messagebox.showwarning(title='Error', message="El tipo de producto ingresado no existe")
    else:
        tk.messagebox.showwarning(title='Error', message='Falto introducir alguno de los datos')
def listarProductos(productos, vencidos):
    productosVencidos(productos)
    ventana_listar = tk.Toplevel()
    ventana_listar.title("Listar productos")

    texto_resultado = tk.Text(ventana_listar)
    texto_resultado.pack()

    texto_resultado.insert(tk.END, "Productos disponibles:\n")

    claves = productos.keys()
    for categoria in claves:
        texto_resultado.insert(tk.END, f"\nCategoría: {categoria}\n")
        productos_categoria = productos[categoria]
        claves_productos = productos_categoria.keys()
        for c in claves_productos:
            dato = productos_categoria[c]
            texto = f"\nCódigo: {c}\nDescripción: {dato[0]}\nStock: {dato[1]}\nPrecio: {dato[2]}\nTipo: {dato[3]}\nFecha de vencimiento: {dato[4]}"
            texto += "\n" + "=" * 20
            texto_resultado.insert(tk.END, texto)

    texto_resultado.insert(tk.END, "================================================\n\nProductos vencidos:\n")

    claves_vencidos = vencidos.keys()
    for categoria_vencidos in claves_vencidos:
        texto_resultado.insert(tk.END, f'\nCategoria: {categoria_vencidos}\n')
        productos_vencidos = vencidos[categoria_vencidos]
        claves_productos_vencidos = productos_vencidos.keys()
        for clave_producto_vencido in claves_productos_vencidos:
            dato_vencido = productos_vencidos[clave_producto_vencido]
            texto_vencido = f"\nCódigo: {clave_producto_vencido}\nDescripción: {dato_vencido[0]}\nStock: {dato_vencido[1]}\nPrecio: {dato_vencido[2]}\nTipo: {dato_vencido[3]}\nFecha de vencimiento: {dato_vencido[4]}"
            texto_vencido += "\n" + "=" * 10
            texto_resultado.insert(tk.END, texto_vencido)

    texto_resultado.configure(state="disabled")
def ingresarNuevoProducto():
    tip = e_tipo.get()
    tipo = tip.lower()
    codigo = e_codigo.get()
    descripcion = e_descripcion.get()
    stock = 0
    precio_unitario = e_precio_unitario.get()

    if tipo and codigo and descripcion and stock and precio_unitario:
        stock = int(e_stock.get())
        while True:
            try:
                fecha_vencimiento = e_fecha_de_vencimiento.get()
                break
            except ValueError:
                print("No tiene el formato de fecha adecuado. Intente nuevamente")

        valor = []
        valor.append(descripcion)
        valor.append(stock)
        valor.append(precio_unitario)
        fecha = datetime.strptime(fecha_vencimiento, "%d/%m/%Y")
        valor.append(fecha)
        valor.append(False)

        productos[tipo][codigo] = valor

        descuentoProducto(productos)
        tk.messagebox.showwarning(title='!!!', message="El producto fue añadido")
    else:
        tk.messagebox.showwarning(title='Error', message='Falta alguno de los datos requeridos')
def abrir_agregar_eliminar():
    ventana_agregar_eliminar = tk.Toplevel()
    ventana_agregar_eliminar.geometry('300x300')
    ventana_agregar_eliminar.title("Agregar o Eliminar")

    #Agregar

    label_tipo = tk.Label(ventana_agregar_eliminar,text='Tipo de producto:')
    label_tipo.grid(row=0,column=0)
    global e_tipo
    e_tipo = tk.Entry(ventana_agregar_eliminar)
    e_tipo.grid(row=1,column=0)

    label_codigo = tk.Label(ventana_agregar_eliminar, text="Código:")
    label_codigo.grid(row=2,column=0)
    global e_codigo
    e_codigo = tk.Entry(ventana_agregar_eliminar)
    e_codigo.grid(row=3,column=0)

    label_descripcion = tk.Label(ventana_agregar_eliminar, text="Descripción:")
    label_descripcion.grid(row=4,column=0)
    global e_descripcion
    e_descripcion = tk.Entry(ventana_agregar_eliminar)
    e_descripcion.grid(row=5,column=0)

    label_stock = tk.Label(ventana_agregar_eliminar, text="Stock:")
    label_stock.grid(row=6,column=0)
    global e_stock
    e_stock = tk.Entry(ventana_agregar_eliminar)
    e_stock.grid(row=7,column=0)

    label_precio = tk.Label(ventana_agregar_eliminar, text="Precio Unitario:")
    label_precio.grid(row=8,column=0)
    global e_precio_unitario
    e_precio_unitario = tk.Entry(ventana_agregar_eliminar)
    e_precio_unitario.grid(row=9,column=0)

    label_fecha = tk.Label(ventana_agregar_eliminar, text="Fecha de Vencimiento:")
    label_fecha.grid(row=10,column=0)
    global e_fecha_de_vencimiento
    e_fecha_de_vencimiento = tk.Entry(ventana_agregar_eliminar)
    e_fecha_de_vencimiento.grid(row=11,column=0)

    boton_guardar = tk.Button(ventana_agregar_eliminar, text="Guardar", command=lambda :  ingresarNuevoProducto())
    boton_guardar.grid(row=12,column=0)

    #Eliminar

    label_tipo_eliminar = tk.Label(ventana_agregar_eliminar, text="Tipo de producto a eliminar")
    label_tipo_eliminar.grid(row=0,column=1)
    global caja_tipo_eliminar
    caja_tipo_eliminar = tk.Entry(ventana_agregar_eliminar)
    caja_tipo_eliminar.grid(row=1,column=1)

    label_codigo_eliminar = tk.Label(ventana_agregar_eliminar, text="Código del producto a eliminar:")
    label_codigo_eliminar.grid(row=2,column=1)
    global caja_codigo_eliminar
    caja_codigo_eliminar = tk.Entry(ventana_agregar_eliminar)
    caja_codigo_eliminar.grid(row=3,column=1)

    boton_eliminar = tk.Button(ventana_agregar_eliminar, text='Eliminar', command=lambda: eliminarProducto(productos))
    boton_eliminar.grid(row=4,column=1)
def abrir_venta():
    ventana_venta = tk.Toplevel()
    ventana_venta.title("Venta")

    frame = tk.Frame(ventana_venta)
    frame.pack()

    # usuario
    user_info_frame = tk.LabelFrame(frame, text="Informacion de usuario")
    user_info_frame.grid(row=0, column=0, padx=20, pady=10)

    nombre_label = tk.Label(user_info_frame, text="Nombre")
    nombre_label.grid(row=0, column=0)
    apellido_label = tk.Label(user_info_frame, text="Apellido")
    apellido_label.grid(row=0, column=1)
    dni_label = tk.Label(user_info_frame,text= 'DNI')
    dni_label.grid(row=2, column=1)
    dire_label = tk.Label(user_info_frame, text='Direccion de envio')
    dire_label.grid(row=2, column=2)

    nombre_entry = tk.Entry(user_info_frame)
    apellido_entry = tk.Entry(user_info_frame)
    dni_entry = tk.Entry(user_info_frame)
    dire_entry = tk.Entry(user_info_frame)

    nombre_entry.grid(row=1, column=0)
    apellido_entry.grid(row=1, column=1)
    dni_entry.grid(row=3,column=1)
    dire_entry.grid(row=3,column=2)



    age_label = tk.Label(user_info_frame, text="Edad")
    age_spinbox = tk.Spinbox(user_info_frame, from_=18, to=110)
    age_label.grid(row=2, column=0)
    age_spinbox.grid(row=3, column=0)


    for widget in user_info_frame.winfo_children():
        widget.grid_configure(padx=10, pady=5)


    # producto a comprar
    courses_frame = tk.LabelFrame(frame)
    courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

    tipo_label = tk.Label(courses_frame,text='#Tipo de producto')
    tipo_Entry = tk.Entry(courses_frame)
    tipo_label.grid(row=0, column=1)
    tipo_Entry.grid(row=1, column=1)

    codigo_label = tk.Label(courses_frame, text="# codigo del producto")
    codigo_Entry = tk.Entry(courses_frame)
    codigo_label.grid(row=0, column=2)
    codigo_Entry.grid(row=1, column=2)


    cantidad_label = tk.Label(courses_frame, text="# cantidad")
    cantidad_spinbox = tk.Spinbox(courses_frame, from_=0, to="infinity")
    cantidad_label.grid(row=0, column=3)
    cantidad_spinbox.grid(row=1, column=3)


    verificar_label = tk.Label(courses_frame, text='Verificar cantidad deseada')
    verificar_label.grid(row=0, column=4)
    verificar_button = tk.Button(courses_frame, text='Verificar', command=lambda: VerificarCantidad(codigo_Entry, cantidad_spinbox, tipo_Entry))
    verificar_button.grid(row=1, column=4)

    for widget in courses_frame.winfo_children():
        widget.grid_configure(padx=10, pady=5)

    # Terminos y condiciones
    terms_frame = tk.LabelFrame(frame, text="Terminos & Condiciones")
    terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

    aceptar_var = tk.StringVar(value="no aceptados")
    terms_check = tk.Checkbutton(terms_frame, text="acepto los terminos y condiciones.", variable=aceptar_var, onvalue="aceptados", offvalue="No aceptados")
    terms_check.grid(row=0, column=0)

    # Button
    button = tk.Button(frame, text="Continuar", command=lambda : Venta(aceptar_var,nombre_entry,apellido_entry,age_spinbox,dni_entry,dire_entry, codigo_Entry, cantidad_spinbox,tipo_Entry))
    button.grid(row=3, column=0, sticky="news", padx=20, pady=10)
def listarVentas(ventas):
    ventana_ventas = tk.Toplevel()
    ventana_ventas.title('Lista de Ventas')

    texto_resultado = tk.Text(ventana_ventas)
    texto_resultado.pack()

    texto_resultado.insert(tk.END, 'Productos Vendidos:\n')

    claves = ventas.keys()
    for categoria in claves:
        texto_resultado.insert(tk.END, f"\nCategoría: {categoria}\n")
        productos_categoria = ventas[categoria]
        claves_productos = productos_categoria.keys()
        for c in claves_productos:
            dato = productos_categoria[c]
            texto = f"\nCódigo: {c}\nDescripción: {dato[0]}\nCantidad: {dato[1]}\nCosto: {int(dato[2]) * int(dato[1])}\nTipo: {dato[3]}\nFecha de vencimiento: {dato[4]}"
            texto += "\n" + "=" * 20
            texto_resultado.insert(tk.END, texto)

    texto_resultado.insert(tk.END, "================================================\n")

    # mostrar productos más vendidos de cada sector
    productos_vendidos = {
        'frutas': {},
        'verduras': {},
        'carnes': {}
    }

    for categoria in ventas.keys():
        productos_categoria = ventas[categoria]
        for codigo, producto in productos_categoria.items():
            cantidad = producto[1]
            if codigo in productos_vendidos[categoria]:
                productos_vendidos[categoria][codigo] += cantidad
            else:
                productos_vendidos[categoria][codigo] = cantidad

    for categoria in productos_vendidos.keys():
        productos_categoria = productos_vendidos[categoria]
        productos_ordenados = sorted(productos_categoria.items(), key=lambda x: x[1], reverse=True)
        productos_vendidos[categoria] = productos_ordenados

    texto_resultado.insert(tk.END, "Productos más vendidos:\n")
    for categoria in productos_vendidos.keys():
        texto_resultado.insert(tk.END, f"\nCategoría: {categoria}\n")
        productos_categoria = productos_vendidos[categoria]
        for codigo, cantidad_vendida in productos_categoria:
            dato = ventas[categoria][codigo]
            texto = f"\nCódigo: {codigo}\nDescripción: {dato[0]}\nCantidad: {cantidad_vendida}\nCosto: {int(dato[2]) * cantidad_vendida}\nTipo: {dato[3]}\nFecha de vencimiento: {dato[4]}"
            texto += "\n" + "=" * 20
            texto_resultado.insert(tk.END, texto)

    # el producto más vendido en general
    productos_total_vendidos = {}

    for categoria in productos_vendidos.keys():
        productos_categoria = productos_vendidos[categoria]
        for codigo, cantidad_vendida in productos_categoria:
            if codigo in productos_total_vendidos:
                productos_total_vendidos[codigo] += cantidad_vendida
            else:
                productos_total_vendidos[codigo] = cantidad_vendida

    producto_mas_vendido = max(productos_total_vendidos, key=productos_total_vendidos.get)
    cantidad_mas_vendida = productos_total_vendidos[producto_mas_vendido]
    categoria_producto_mas_vendido = ''

    for categoria, productos_categoria in ventas.items():
        if producto_mas_vendido in productos_categoria:
            categoria_producto_mas_vendido = categoria
            break

    texto_resultado.insert(tk.END, f"\nProducto más vendido en general:\n")
    texto_resultado.insert(tk.END, f"\nCategoría: {categoria_producto_mas_vendido}\n")
    texto_resultado.insert(tk.END, f"Código: {producto_mas_vendido}\n")
    dato = ventas[categoria_producto_mas_vendido][producto_mas_vendido]
    texto_resultado.insert(tk.END, f"Descripción: {dato[0]}\n")
    texto_resultado.insert(tk.END, f"Cantidad vendida: {cantidad_mas_vendida}\n")
    texto_resultado.insert(tk.END, f"Costo total: {int(dato[2]) * cantidad_mas_vendida}\n")
    texto_resultado.insert(tk.END, f"Tipo: {dato[3]}\n")
    texto_resultado.insert(tk.END, f"Fecha de vencimiento: {dato[4]}\n")
    texto_resultado.insert(tk.END, "=" * 20)


# inicio
ventana_inicio = tk.Toplevel()
ventana_inicio.title("Inicio")
ventana_inicio.geometry("1000x700")

img = tk.PhotoImage(file="super.png")
eti_img = tk.Label(ventana_inicio, image=img)
eti_img.place(x=310, y=120)

titulo = tk.Label(ventana_inicio, text="La calidad que querés, al precio que buscás", font="helvetica 17",width=100, height=9)
titulo.place(x=-110, y=-50)

button_agr_elim = tk.Button(ventana_inicio, text="Agregar producto\nEliminar Producto",command=abrir_agregar_eliminar, width=20, height=9)
button_agr_elim.place(x=200, y=550)

button_venta = tk.Button(ventana_inicio, text="Vender Producto", command=abrir_venta, width=20, height=9)
button_venta.place(x=360, y=550)

button_listar = tk.Button(ventana_inicio, text="Listar productos", command=lambda: listarProductos(productos,vencidos),width=20, height=9)
button_listar.place(x=520, y=550)

button_listar_ventas = tk.Button(ventana_inicio, text='Listar Ventas', command=lambda: listarVentas(ventas),width=20,height=9)
button_listar_ventas.place(x=680, y=550)

ventana_inicio.mainloop()
