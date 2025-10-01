'''Escribir un programa que pregunte al usuario una cantidad a
invertir, el interés anual y el número de años, y muestre por
pantalla el capital obtenido en la inversión.'''

#Capital obtenido = Cantidad a invertir + (Interés anual * Número de años)

cantidadInvertir = float(input('¿Cuanto has invertido? '))
interesAnual = float(input('¿Cual es el interés anual de tu inversion? (%) '))
nroAños = float(input('¿Cuantos años dura tu inversión? '))

capital_final = cantidadInvertir * (1 + interesAnual / 100) ** nroAños
capitalRedondeado = round(capital_final, 2)

print  ("Después de ",nroAños, "años", " tendrás", capitalRedondeado, " €")