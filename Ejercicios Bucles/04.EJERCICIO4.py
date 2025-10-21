'''Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual
y el número de años, y muestre por pantalla el capital obtenido en la inversión cada
año que dura la inversión.'''

''''''

cantidad = float(input('¿Cuanto vas a invertir? '))
interes = float(input('¿Cual es el interes anual? '))
años = float(input('¿Cuantos años fura tu inversión?'))

final= cantidad * (1+interes/100)**años

print (final)