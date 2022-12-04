#1. Realizar un programa que ingrese sus datos personales e imprimirlos.

Nombres=str(input("Ingrese sus nombres: "))
Apellidos=str(input("Ingrese sus apellidos: "))
Celular=int(input("Ingrese su numero telefonico: "))
DNI=int(input("Ingrese su numero de DNI: "))
Direccion=str(input("Ingrese su direccion: "))

print('Nombre Completo: {},{}'.format(Apellidos, Nombres))
print("Celular: ", Celular)
print('DNI: ',DNI)
print(f'Direccion: {Direccion}')

