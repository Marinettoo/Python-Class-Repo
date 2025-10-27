'''Escribir un programa en el que se pregunte al usuario por una frase y una letra, y
muestre por pantalla el número de veces que aparece la letra en la frase.'''

frase = str(input('Introduce una frase: '))
letra = str(input('¿Que letra quieres contear?: '))
num_veces = frase.count(letra)

print (num_veces)