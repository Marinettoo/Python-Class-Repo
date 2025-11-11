'''Escribir un programa que almacene las asignaturas de un curso (por ejemplo
Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la
nota que ha sacado en cada asignatura y elimine de la lista las asignaturas
aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el
usuario tiene que repetir'''
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

suspender = []
for asignatura in asignaturas:
    try:
        nota = float(input(f"Nota de {asignatura}: "))
    except ValueError:
        nota = 0.0
    if nota < 5:
        suspender.append(asignatura)

print()
if suspender:
    print("Tienes que repetir estas asignaturas:")
    for a in suspender:
        print(a)
else:
    print("No tienes que repetir ninguna asignatura.")