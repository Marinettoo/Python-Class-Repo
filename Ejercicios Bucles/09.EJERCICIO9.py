'''Escribir un programa que almacene la cadena de caracteres contraseña en una
variable, pregzunte al usuario por la contraseña hasta que introduzca la contraseña
correcta.'''

contraseña = 'hola'
entrada = ''  

while entrada != contraseña:
    entrada = input("Introduce tu contraseña: ")

print("contraseña correcta")
