'''Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta
que el usuario escriba “salir” que terminará.'''

texto =''


while texto != ('salir'):
    texto = str(input('Escribe lo que quieras, o escribe "salir" para salir: '))
    print (texto)


else:
    print ('Has salido')