'''Escribir un programa que pida al usuario que introduzca una frase en la consola y
muestre por pantalla la frase invertida.'''
frase = input('Introduce la frase, para mostrarla al revés: ')

reves = frase[::-1] #[::]Significa 'coge toda la cadena de texto desde la primera hasta la ultima letra y [-1] significa 'en orden inverso


print (reves)