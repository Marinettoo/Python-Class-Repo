'''Escribir un programa que pida al usuario una palabra y muestre por pantalla el
número de veces que contiene cada vocal.'''
word = input("Introduce una palabra: ")
word_lower = word.lower()
for vocal in ['a', 'e', 'i', 'o', 'u']:
    print(f"La vocal {vocal} aparece {word_lower.count(vocal)} veces")