'''Escribir un programa que pregunte al usuario los números ganadores de la lotería
primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor
a mayor.'''

numeros = []
for i in range(6):
    n = int(input(f"Número {i+1}: "))
    numeros.append(n)

numeros.sort()
print()
print("Números ordenados de menor a mayor:")
for n in numeros:
    print(n)
