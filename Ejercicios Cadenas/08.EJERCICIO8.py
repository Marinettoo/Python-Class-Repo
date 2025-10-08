'''Escribir un programa que pregunte por consola el precio de un producto en euros
con dos decimales y muestre por pantalla el número de euros y el número de
céntimos del precio introducido.'''
precio = input('Introduce el precio de un producto con 2 decimales: ')
preciodiv = precio.split('.')

print (preciodiv[0]+' euros'+' y '+preciodiv[1]+' centimos')
