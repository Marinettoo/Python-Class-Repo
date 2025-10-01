'''Una panadería vende barras de pan a 3.49€ cada una. El pan
que no es del día tiene un descuento del 60%. Escribir un
programa que comience leyendo el número de barras vendidas
que no son del día. Después el programa debe mostrar el
precio habitual de una barra de pan, el descuento que se le
hace por no ser fresca y el coste final total.'''
barraPan = 3.49
barraPanNoDia = (60*3.49)/100
nro_BarrasVendidas = int(input('¿Cuantas barras que no son del dia se han vendido? '))
nro_BarrasDiaVendidas = int(input('¿Cuantas barras del dia se han vendido?  '))
barraPanNoDiaRed = round(barraPanNoDia,2)

print('Se han vendido ',nro_BarrasVendidas, 'que normalmente valen 3.49 pero como no son del dia, tienen un descuento del 60%. Actualmente cuestan', barraPanNoDiaRed)
print('En total, se han vendido ', nro_BarrasVendidas + nro_BarrasDiaVendidas,'barras, lo que supone un total de', (nro_BarrasDiaVendidas*barraPan + nro_BarrasVendidas * barraPanNoDia), '€')
