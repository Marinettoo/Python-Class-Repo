'''Escribir un programa que pida al usuario un número entero y muestre por pantalla si
es un número primo o no.'''

numero = int(input('Introduce un número entero'))

if numero > 1:
    for i in range (2, numero):
        if numero % i == 0:
            print ('No es un número primo')
            
    else:
        print ('Es un numero primo')
else:
     print ('Es un numero primo')