'''Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos
los años que ha cumplido (desde 1 hasta su edad).'''
edad = int(input('¿Que edad tienes? '))
n = 0
for i in range(edad):
    n = n+1
    print (n)
    