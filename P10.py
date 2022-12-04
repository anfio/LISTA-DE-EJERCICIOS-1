#10.Realizar un programa que calcule la penalidad por la mora de una deuda,sabiendo que si se
#demora de 1 día a 10 se le agrega el 5% , si se demora hasta 30 días se le agrega 8% y pasando
#el rango máximo se le agrega un 10%.

deuda=float(input("Ingrese el monto de su deuda: "))
demora=float(input("Ingrese la cantidad de dias que ha demorado en pagar su deuda: "))
penalidad=0.0
deuda_final=0.0

if demora>1 and demora<=10:
    penalidad=0.05
elif demora>10 and demora<=30:
    penalidad=0.08
else:
    penalidad=0.10

deuda_final=deuda+deuda*penalidad
print(f'Su penalidad es de {penalidad}, por lo cual su deuda asciende a {deuda_final} soles')

