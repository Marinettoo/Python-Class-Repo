'''Escribir un programa que pida al usuario un número entero positivo y muestre por
pantalla la cuenta atrás desde ese número hasta cero separados por comas.'''
numero = int(input('Introduce un numero entero positivo: '))
n = numero

while n > 0:
    n = n - 1
    print (n, end=',')