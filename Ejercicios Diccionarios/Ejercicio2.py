'''Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono
y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje
<nombre> tiene <edad> años, vive en <dirección> y su número de
teléfono es <teléfono>.'''

nombre = input('Cual es tu nombre? ')
edad = input('Cual es tu edad? ')
direccion = input('Indicanos tu direccion ')
edad = input('Cuantos años tienes ')
telefono = input('Facilitanos tu telefono ')

diccionario = {
    'nombre': nombre,
    'edad': edad,
    'direccion': direccion,
    'telefono': telefono
}

print (diccionario['nombre'], ', tienes', diccionario['edad'], 'años. Vives en la direccion', diccionario['direccion'], ' y tu numero de teléfono es: ', diccionario['telefono'])

