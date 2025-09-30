'''Escribir un programa que pregunte al usuario por el número de
horas trabajadas y el coste por hora. Después debe mostrar
por pantalla la paga que le corresponde.'''
horasTrabajadas = float(input('¿Cuantas horas has trabajado? '))
costeHora = float(input('¿Cual es el coste por hora de tu trabajo? '))
paga = horasTrabajadas * costeHora
print ("Te corresponden:", paga, "€")
