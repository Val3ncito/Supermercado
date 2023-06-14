Usuarios={}
def EnvioDomicilio(Usuarios):
    DNI=input("Ingresar DNI: ")
    valor = []
    if DNI in Usuarios:
        fecha = input('Cuando desea recibir su pedido: ')
        return fecha
    else:
        Nombre = input("Ingrese su nombre: ")
        Direccion = input("Ingrese su direccion: ")
    
        valor.append(Nombre)
        valor.append(Direccion)
        Usuarios[DNI] = valor
    
EnvioDomicilio(Usuarios)
