'''Escribir un programa que pregunte el nombre el un producto, su precio y un número
de unidades y muestre por pantalla una cadena con el nombre del producto seguido
de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con
tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.'''
nombre = input('¿Como se llama el producto?')
precio = float(input('¿Cuanto cuesta?'))
numUniddades = int(input('¿Cuantas unidades has coprado?'))
costeTotal = (precio*numUniddades)

print (f'Producto: {nombre}')
print (f'precio: {precio:06.2f} €')
print (f'numero de unidades: {numUniddades:03d}')
print (f'coste total: {costeTotal:08.02f} € ')