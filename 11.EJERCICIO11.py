'''Imagina que acabas de abrir una nueva cuenta de ahorros que
te ofrece el 4% de interés al año. Estos ahorros debido a
intereses, que no se cobran hasta finales de año, se te añaden
al balance final de tu cuenta de ahorros. Escribir un programa
que comience leyendo la cantidad de dinero depositada en la
cuenta de ahorros, introducida por el usuario. Después el
programa debe calcular y mostrar por pantalla la cantidad de
ahorros tras el primer, segundo y tercer años. Redondear cada
cantidad a dos decimales.'''


deposito_inicial = float(input('¿Cuanto dinero has depositado? '))
interes = 0.04

balance_1 = deposito_inicial * (1 + interes)
balance_2 = balance_1 * (1 + interes)
balance_3 = balance_2 * (1 + interes)

print("Balance después del primer año: ", balance_1, "€")
print("Balance después del segundo año: ", balance_2, "€")
print("Balance después del tercer año: ", balance_3, "€")