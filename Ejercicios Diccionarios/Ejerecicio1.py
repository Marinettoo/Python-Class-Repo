'''
Escribir un programa que guarde en una variable el diccionario {'Euro':'€',
'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su
símbolo o un mensaje de aviso si la divisa no está en el diccionario.
'''
pregunta = input('Que divisa vas a usar? Euro, Dolar, Yen: ')

divisa = pregunta.lower()

simbolo = {
    'euro': '€',
    'dollar': '$',
    'yen': '¥'
}

if divisa in simbolo:
    print(f'El símbolo de {divisa} es: {simbolo[divisa]}')
else:
    print('La divisa no está en el diccionario')


