'''Escribir un programa que pregunte por consola por los productos de una cesta de la
compra, separados por comas, y muestre por pantalla cada uno de los productos en
una línea distinta.'''
productos = input('Escribe los productos que hay en la cesta: (x,x,x,x) ')
productosreemplazado = productos.replace(',','\n')
print (productosreemplazado)
