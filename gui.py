import tkinter

#Ventanas
ventana = tkinter.Tk()
ventana.title('Inicio')
ventana.geometry('900x640')


productos={"1234":["Lechuga", "0001", "50", "Verdura", "5/12/2023", "10"],"5678":["Tomate", "0002", "75", "Verdura", "7/12/2023]"]}

def listarProductos(diccionario):
    claves = diccionario.keys()
    for c in claves:
        dato = diccionario[c]
        return(c, dato[0], dato[1], dato[2], dato[3], dato[4], dato[5])

def AgrElim():
    ventanaAgrElim = tkinter.Toplevel()
    ventanaAgrElim.title('Agregar o Eliminar Producto')
    ventanaAgrElim.geometry('700x400')

    agregar = tkinter.Label(ventanaAgrElim, text='AGREGAR',bg='green',width=50,height=5).place(x=0,y=0)
    texto1 = tkinter.Entry(ventanaAgrElim).place(x=120,y=150)
    textoFecha = tkinter.Label(ventanaAgrElim, text="XXXX/XX/XX").place(x=144,y=129)
    boton1 = tkinter.Button(ventanaAgrElim, text='Agregar').place(x=155,y=180)
    texto2 = tkinter.Entry(ventanaAgrElim).place(x=120,y=220)
    boton2 = tkinter.Button(ventanaAgrElim, text='Agregar').place(x=155,y=250)

    eliminar = tkinter.Label(ventanaAgrElim, text='ELIMINAR',bg='red',width=50,height=5).place(x=350,y=0)
    texto3 = tkinter.Entry(ventanaAgrElim).place(x=460,y=150)
    boton3 = tkinter.Button(ventanaAgrElim, text='Eliminar').place(x=495,y=180)

    cerrar = tkinter.Button(ventanaAgrElim, text='cerrar', command=ventanaAgrElim.destroy,width=5,height=1).place(x=655,y=360)

def Venta():
    ventanaVenta = tkinter.Toplevel()
    ventanaVenta.title('Venta')
    ventanaVenta.geometry('700x350')

def Listar():
    ventanaListar = tkinter.Toplevel()
    ventanaListar.title('Listar productos')
    ventanaListar.geometry('700x350')
    label = tkinter.Label(ventanaListar,text = listarProductos(productos)).place(x=0,y=0)


#imagen
img = tkinter.PhotoImage(file="super.png")
eti_img = tkinter.Label(ventana, image= img).place(x=270,y=100)


#Textos
titulo = tkinter.Label(ventana, text='La calidad que querés, al precio que buscás',font='helvetica 17',width=100,height=9).place(x=-180,y=-50)


#Botones

buttonAgrElim = tkinter.Button(ventana, text= 'Agregar producto\n Eliminar Producto', command=AgrElim ,width=20,height=9).place(x=200,y=480)

buttonVenta = tkinter.Button(ventana, text= 'Vender Producto',command=Venta,width=20,height=9).place(x=360,y=480)

buttonListar = tkinter.Button(ventana, text= 'Listar productos',command=Listar,width=20,height=9).place(x=520,y=480)

buttonCerrar = tkinter.Button(ventana, text='cerrar', command=ventana.destroy,width=5,height=1).place(x=855,y=600)

ventana.mainloop()