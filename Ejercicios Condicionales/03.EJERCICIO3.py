'''Escribir un programa que pida al usuario dos números y muestre por pantalla su
división. Si el divisor es cero el programa debe mostrar un error.'''

dividendo = int(input('¿Cual es el dividendo de tu división? ' ))
divisor = int(input('¿Cual es el divisor de tu división? '))


if divisor == 0:
    print ('No se puede dividir entre 0')
else:
    resultado = dividendo/divisor
    print (f'el resultado es:  {resultado}')

