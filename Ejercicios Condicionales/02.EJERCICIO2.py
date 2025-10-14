'''Escribir un programa que almacene la cadena de caracteres contraseña en una
variable, pregunte al usuario por la contraseña e imprima por pantalla si la
contraseña introducida por el usuario coincide con la guardada en la variable sin
tener en cuenta mayúsculas y minúsculas.'''
contraseña = input('¿Cuál es tu contraseña? ')
contraseña_chk = input('Confirma tu contraseña ')
if contraseña.lower() == contraseña_chk.lower():
    print ('Las contraseñas coinciden')
else:
    print ('Las contraseñas no coinciden, vuelve a intentarlo')