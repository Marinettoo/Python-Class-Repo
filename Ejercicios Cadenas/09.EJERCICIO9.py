'''Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato
dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa
anterior para que también funcione cuando el día o el mes se introduzcan con un
solo carácter.'''
fechaNac = (input('¿Cuando naciste? (dd/mm/aaaa)'))

fechaSplit = fechaNac.split('/')

print ('Naciste el dia: '+fechaSplit[0]+ ' del mes: '+ fechaSplit[1]+ ' del año: '+fechaSplit[2])
