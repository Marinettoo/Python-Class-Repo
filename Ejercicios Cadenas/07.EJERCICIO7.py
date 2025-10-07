'''Escribir un programa que pregunte el correo electrónico del usuario en la consola y
muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante
de la arroba @) pero con dominio ceu.es.'''
email = input ('Escribe tu E-mail: ')
emaildiv = email.split('@')
nombre = emaildiv[0]

nuevo_email = nombre + '@ceu.es'
print(nuevo_email)
