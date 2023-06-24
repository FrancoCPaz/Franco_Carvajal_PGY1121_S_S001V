import funciones as fn
import numpy as np
import pdb
#pdb.set_trace()
nombre= ''
edad= 0
n_nif = 0
dv_nif = ''
op= 0 
datos =np.array([nombre,edad,n_nif,dv_nif])
while op != 4:
    try:
        print('1. grabar \n2. buscar\n3. imprimir\n4. salir')
        op= (int(input('ingrese su opcion\n: ')))
        if op == 1:
                nombre, edad,n_nif,dv_nif = (fn.datosusuario(nombre, edad,n_nif,dv_nif))
                if len(n_nif)<8:
                       print('vuelva a ingresar su numero nif')
        if op == 2:
                print(datos([0]))

        if op == 3:
                fn.impresion
        if op ==4:
                print(fn.salida(nombre, edad,n_nif,dv_nif))
                print('saliste')
                break

    except ValueError:
                print('debe ingresar un numero ')