import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from datetime import datetime

productos = {}

vencidos = {}

ventas = {}


# def DeterminarMasVendido(Ventas, Historial):
#     for i in Ventas:
#         if i[0] in Historial:
#             Suma=i[1]+Historial.get(i[0])
#             Historial.pop(i[0])
#             Historial[i[0]]=Suma
#         else:
#             Historial[i[0]]=i[1]
#     Mayor=-9999
#     MayorF=""
#     for i in Historial.items():
#         if i[1]>Mayor:
#             Mayor=i[1]
#             MayorF=i
#     global UltimasVentas
#     UltimasVentas=[]
#     print("El articulo más vendido es: ",MayorF)

def Venta(aceptar_var,nombre_entry,apellido_entry,age_spinbox,dni_entry,dire_entry, codigo_Entry, cantidad_spinbox):
    accepted = aceptar_var.get()

    if accepted == "aceptados":
        # Usuario
        nombre = nombre_entry.get()
        apellido = apellido_entry.get()

        if nombre and apellido:
            edad = age_spinbox.get()
            dirrecion = dire_entry.get()

            # compra
            codigo = codigo_Entry.get()
            cantidad = cantidad_spinbox.get()

            aviso = VerificarCantidad(codigo_Entry, cantidad_spinbox)

            if (aviso == True):
                ventas[codigo] = productos[codigo]
                ventas[codigo][1] = cantidad
                numero = int(productos[codigo][1]) - int(cantidad)
                
                if (productos[codigo][1] == 0):
                    del productos[codigo]

                tk.messagebox.showinfo(title='Ticket',
                                       message='------------------------------------------\nNombre: ' + nombre + '/' + 'Apellido: ' + apellido + "\nEdad: " + edad + '/' + "Dirrecion: " + dirrecion + "\ncodigo del producto comprado: " + codigo + "# cantidad: " + cantidad + "\nSu producto sera enviado en dias habiles a la dirrecion " + dirrecion + '\nMuchas gracias por comprar' + '\n------------------------------------------')

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
            tk.messagebox.showwarning(title="Error", message="Nombre y Apellido son requeridos.")
    else:
        tk.messagebox.showwarning(title="Error", message="No has aceptado los terminos y condiciones")


def VerificarCantidad(codigo, cant):
    clave = codigo.get()
    cantidad = cant.get()

    if clave in productos:
        mon = int(productos[clave][1])
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
    fecha_actual = datetime.now()

    for i in diccionario:
        fecha_vencimiento = diccionario[i][4]
        prueba = fecha_vencimiento - fecha_actual

        if int(prueba.days) <= 7 and prueba.days > 0:
            precio_str = diccionario[i][2]
            precio = float(precio_str)
            descuento = precio * 0.1
            diccionario[i][2] = precio - descuento
            diccionario[i][5] = True
def productosVencidos(diccionario):
    fecha_actual = datetime.now()
    lista_claves_a_eliminar = []
    copia_diccionario = diccionario.copy()

    for i in copia_diccionario:
        fecha_vencimiento = copia_diccionario[i][4]

        if fecha_vencimiento < fecha_actual:
            vencidos[i] = copia_diccionario[i]
            lista_claves_a_eliminar.append(i)

    for i in lista_claves_a_eliminar:
        del diccionario[i]
def eliminarProducto(diccionario):
    codigo = caja_codigo_eliminar.get()
    if codigo in diccionario:
        del diccionario[codigo]
        tk.messagebox.showwarning(title='!!!', message="El producto fue eliminado correctamente")
    else:
        tk.messagebox.showwarning(title='Error',message="El producto con el código ingresado no existe")
def listarProductos(diccionario, vencidos):
    productosVencidos(productos)
    ventana_listar = tk.Toplevel()
    ventana_listar.title("Listar productos")

    # Creamos un widget Text para mostrar los productos
    texto_resultado = tk.Text(ventana_listar)
    texto_resultado.pack()

    texto_resultado.insert(tk.END, "Productos disponibles:\n")

    claves = diccionario.keys()
    for c in claves:
        dato = diccionario[c]
        texto = f"\nCódigo: {c}\nDescripción: {dato[0]}\nStock: {dato[1]}\nPrecio: {dato[2]}\nTipo: {dato[3]}\nFecha de vencimiento: {dato[4]}"
        texto += "\n" + "=" * 20  # Separador entre productos
        texto_resultado.insert(tk.END, texto)

    texto_resultado.insert(tk.END, "\nProductos vencidos:\n")

    claves_vencidos = vencidos.keys()
    for c in claves_vencidos:
        dato_vencido = vencidos[c]
        texto_vencido = f"\nCódigo: {c}\nDescripción: {dato_vencido[0]}\nStock: {dato_vencido[1]}\nPrecio: {dato_vencido[2]}\nTipo: {dato_vencido[3]}\nFecha de vencimiento: {dato_vencido[4]}"
        texto_vencido += "\n" + "=" * 20  # Separador entre productos vencidos
        texto_resultado.insert(tk.END, texto_vencido)

    texto_resultado.configure(state="disabled")
def ingresarNuevoProducto():
    codigo = e_codigo.get()
    descripcion = e_descripcion.get()
    stock = int(e_stock.get())
    precio_unitario = e_precio_unitario.get()
    fecha_vencimiento = e_fecha_de_vencimiento.get()

    # Realiza las operaciones necesarias con los valores ingresados
    valor = []
    valor.append(descripcion)
    valor.append(stock)
    valor.append(precio_unitario)
    valor.append("verdura")
    fecha = datetime.strptime(fecha_vencimiento, "%d/%m/%Y")
    valor.append(fecha)
    valor.append(False)

    productos[codigo] = valor

    descuentoProducto(productos)

    tk.messagebox.showwarning(title='!!!', message="El producto fue añadido")
def abrir_agregar_eliminar():
    ventana_agregar_eliminar = tk.Toplevel()
    ventana_agregar_eliminar.geometry('300x300')
    ventana_agregar_eliminar.title("Agregar o Eliminar")

    label_codigo = tk.Label(ventana_agregar_eliminar, text="Código:")
    label_codigo.grid(row=0,column=0)
    global e_codigo
    e_codigo = tk.Entry(ventana_agregar_eliminar)
    e_codigo.grid(row=1,column=0)

    label_descripcion = tk.Label(ventana_agregar_eliminar, text="Descripción:")
    label_descripcion.grid(row=2,column=0)
    global e_descripcion
    e_descripcion = tk.Entry(ventana_agregar_eliminar)
    e_descripcion.grid(row=3,column=0)

    label_stock = tk.Label(ventana_agregar_eliminar, text="Stock:")
    label_stock.grid(row=4,column=0)
    global e_stock
    e_stock = tk.Entry(ventana_agregar_eliminar)
    e_stock.grid(row=5,column=0)

    label_precio = tk.Label(ventana_agregar_eliminar, text="Precio Unitario:")
    label_precio.grid(row=6,column=0)
    global e_precio_unitario
    e_precio_unitario = tk.Entry(ventana_agregar_eliminar)
    e_precio_unitario.grid(row=7,column=0)

    label_fecha = tk.Label(ventana_agregar_eliminar, text="Fecha de Vencimiento:")
    label_fecha.grid(row=8,column=0)
    global e_fecha_de_vencimiento
    e_fecha_de_vencimiento = tk.Entry(ventana_agregar_eliminar)
    e_fecha_de_vencimiento.grid(row=9,column=0)

    boton_guardar = tk.Button(ventana_agregar_eliminar, text="Guardar", command=ingresarNuevoProducto)
    boton_guardar.grid(row=10,column=0)

    label_codigo_eliminar = tk.Label(ventana_agregar_eliminar, text="Código del producto a eliminar:")
    label_codigo_eliminar.grid(row=0,column=1)
    global caja_codigo_eliminar
    caja_codigo_eliminar = tk.Entry(ventana_agregar_eliminar)
    caja_codigo_eliminar.grid(row=1,column=1)

    boton_eliminar = tk.Button(ventana_agregar_eliminar, text='Eliminar', command=lambda: eliminarProducto(productos))
    boton_eliminar.grid(row=2,column=1)
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


    codigo_label = tk.Label(courses_frame, text="# codigo del producto")
    codigo_Entry = tk.Entry(courses_frame)
    codigo_label.grid(row=0, column=1)
    codigo_Entry.grid(row=1, column=1)


    cantidad_label = tk.Label(courses_frame, text="# cantidad")
    cantidad_spinbox = tk.Spinbox(courses_frame, from_=0, to="infinity")
    cantidad_label.grid(row=0, column=2)
    cantidad_spinbox.grid(row=1, column=2)


    verificar_label = tk.Label(courses_frame, text='Verificar cantidad deseada')
    verificar_label.grid(row=0, column=3)
    verificar_button = tk.Button(courses_frame, text='Verificar', command=lambda: VerificarCantidad(codigo_Entry, cantidad_spinbox))
    verificar_button.grid(row=1, column=3)

    for widget in courses_frame.winfo_children():
        widget.grid_configure(padx=10, pady=5)

    # Terminos y condiciones
    terms_frame = tk.LabelFrame(frame, text="Terminos & Condiciones")
    terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

    aceptar_var = tk.StringVar(value="no aceptados")
    terms_check = tk.Checkbutton(terms_frame, text="acepto los terminos y condiciones.", variable=aceptar_var, onvalue="aceptados", offvalue="No aceptados")
    terms_check.grid(row=0, column=0)

    # Button
    button = tk.Button(frame, text="Continuar", command=lambda : Venta(aceptar_var,nombre_entry,apellido_entry,age_spinbox,dni_entry,dire_entry, codigo_Entry, cantidad_spinbox))
    button.grid(row=3, column=0, sticky="news", padx=20, pady=10)


# inicio
ventana_inicio = tk.Toplevel()
ventana_inicio.title("Inicio")
ventana_inicio.geometry("900x640")

img = tk.PhotoImage(file="super.png")
eti_img = tk.Label(ventana_inicio, image=img)
eti_img.place(x=270, y=100)

titulo = tk.Label(ventana_inicio, text="La calidad que querés, al precio que buscás", font="helvetica 17",
                      width=100, height=9)
titulo.place(x=-180, y=-50)

button_agr_elim = tk.Button(ventana_inicio, text="Agregar producto / Eliminar Producto",
                                command=abrir_agregar_eliminar, width=20, height=9)
button_agr_elim.place(x=200, y=480)

button_venta = tk.Button(ventana_inicio, text="Vender Producto", command=abrir_venta, width=20, height=9)
button_venta.place(x=360, y=480)

button_listar = tk.Button(ventana_inicio, text="Listar productos", command=lambda: listarProductos(productos,vencidos),
                              width=20, height=9)
button_listar.place(x=520, y=480)

button_cerrar = tk.Button(ventana_inicio, text="Cerrar", command=ventana_inicio.destroy, width=5, height=1)
button_cerrar.place(x=855, y=600)

ventana_inicio.mainloop()
