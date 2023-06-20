import tkinter

#Ventanas
ventana = tkinter.Tk()
ventana.title('Inicio')
ventana.geometry('900x640')

def AgrElim():
    ventanaAgrElim = tkinter.Toplevel()
    ventanaAgrElim.title('Agregar o Eliminar Producto')
    ventanaAgrElim.geometry('700x400')

    agregar = tkinter.Label(ventanaAgrElim, text='AGREGAR',bg='green',width=50,height=5).place(x=0,y=0)
    texto1 = tkinter.Entry(ventanaAgrElim).place(x=120,y=150)
    boton1 = tkinter.Button(ventanaAgrElim, text='Agregar').place(x=155,y=180)
    texto2 = tkinter.Entry(ventanaAgrElim).place(x=120,y=220)
    boton2 = tkinter.Button(ventanaAgrElim, text='Agregar').place(x=155,y=250)

    eliminar = tkinter.Label(ventanaAgrElim, text='ELIMINAR',bg='red',width=50,height=5).place(x=350,y=0)
    texto3 = tkinter.Entry(ventanaAgrElim).place(x=460,y=150)
    boton3 = tkinter.Button(ventanaAgrElim, text='Eliminar').place(x=495,y=180)

    cerrar = tkinter.Button(ventanaAgrElim, text='cerrar', command=ventanaAgrElim.destroy,width=5,height=1).place(x=655,y=360)

def Venta():
    ventanaAgrElim = tkinter.Toplevel()
    ventanaAgrElim.title('Venta')
    ventanaAgrElim.geometry('700x350')

def Listar():
    ventanaAgrElim = tkinter.Toplevel()
    ventanaAgrElim.title('Listar productos')
    ventanaAgrElim.geometry('700x350')


#imagen
img = tkinter.PhotoImage(file="super.png")
eti_img = tkinter.Label(ventana, image= img).place(x=310,y=200)


#Textos
titulo = tkinter.Label(ventana, text='BIENVENIDO AL SUPERMERCADO', bg='cyan',font='helvetica 13',width=100,height=9).place(x=0,y=0)


#Botones

buttonAgrElim = tkinter.Button(ventana, text= 'Agregar producto\n Eliminar Producto', command=AgrElim ,width=20,height=9).place(x=0,y=180)

buttonVenta = tkinter.Button(ventana, text= 'Vender Producto',command=Venta,width=20,height=9).place(x=0,y=330)

buttonListar = tkinter.Button(ventana, text= 'Listar productos',command=Listar,width=20,height=9).place(x=0,y=480)

buttonCerrar = tkinter.Button(ventana, text='cerrar', command=ventana.destroy,width=5,height=1).place(x=855,y=600)

ventana.mainloop()