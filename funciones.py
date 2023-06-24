

def datosusuario(nombre, edad,n_nif,dv_nif):
    nombre = str(input('ingrese su nombre : '))
    edad = int(input('indique su edad: '))
    n_nif= str(input('ingrese los primeros 8 digitos de su NIF : '))
    if len(n_nif)<8:
        try:
            n_nif = str(input('tiene que ser de 8 digitos: '))
        except: 
            len(n_nif) >8
    dv_nif = str(input('ingrese los ultimos 3 digitos de su NIF: '))
    return nombre, edad,n_nif,dv_nif


def impresion(edad):
    print('certficado de nacimiento:')
    print('certficado de nacimiento:')
    print('certficado de nacimiento:')
    print('certficado de nacimiento:')
    print('edad =',edad)




def salida(nombre, edad,n_nif,dv_nif):
    print('hasta luego\n----------------')
    print(f'nombre = {nombre}')
    print(f'edad = {edad}')
    print(f'nif = {n_nif}-{dv_nif}')
    return nombre, edad,n_nif,dv_nif
  

