'''
Escribir un programa que pida al usuario un número entero y muestre por pantalla
un triángulo rectángulo como el de más abajo.
1
3 1
5 3 1
7 5 3 1
9 7 5 3 1

'''
altura = int(input("Inserta la altura del triángulo: "))

num = 1

for i in range(altura):
   
    for j in range(num, 0, -2):
        print(j, end=" ")
    print()  
    num += 2  
