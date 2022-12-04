#6.Realice un programa que calcule la suma de los números hasta el valor ingresado.
#Ejemplo : si se ingresa 5 se tendrá que calcular 1+2+3+4+5

numero=int(input("Ingrese un numero: "))
suma=0
suma=numero*(1+numero)/2
print(f'El valor de la suma hasta {numero} es {suma}')