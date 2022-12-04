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

#2.Calcule el área de un círculo con radio ingresado desde el teclado.
import math
radio=float(input("Ingrese el radio del circulo: "))
Area= 0.0
Area = math.pi*(radio*radio)
print("El area del circulo es: ", Area)

#3.Ingrese 3 valores y realice las operaciones de suma ,resta y multiplicación.
numero1=float(input("Ingrese su primer numero: "))
numero2=float(input("Ingrese su segundo numero: "))
numero3=float(input("Ingrese su tercer numero: "))
suma=0.0
resta=0.0
multiplicacion=0.0

suma=numero1+numero2+numero3
resta=numero1-numero2-numero3
multiplicacion=numero1*numero2*numero3

print(f'La suma de los valores ingresados es {suma}, su resta es {resta} y su multiplicacion {multiplicacion}')

#4). Ingrese un valor e imprima el tipo de dato.
a=int(input("Ingrese un valor: "))
print(type(a)) 

#5)> Realice un programa que imprima la ubicación de su carpeta donde se encuentra
#trabajando.
import sys
variable =sys.argv[0]

#6.Realice un programa que calcule la suma de los números hasta el valor ingresado.
#Ejemplo : si se ingresa 5 se tendrá que calcular 1+2+3+4+5

numero=int(input("Ingrese un numero: "))
suma=0
suma=numero*(1+numero)/2
print(f'El valor de la suma hasta {numero} es {suma}')

#7. Realiza un programa que lea 2 números por teclado y determine los siguientes aspectos:
    # Si los dos números son iguales
    # Si los dos números son diferentes
    # Si el primero es mayor que el segundo
    # Si el segundo es mayor o igual que el primero

num1=float(input("Ingrese un numero: "))
num2=float(input("Ingrese otro numero: "))

if num1==num2:
    print("Los numeros son iguales")
elif num1!=num2:
    print("Los numeros son diferentes y ")
    if num1>num2:
        print("el primer numero ingresado es mayor que el segundo")
    else:
        print("el segundo numero ingresado es mayor que el primero")

#8.Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
#pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el
#usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

contra="contraseña"
contra_usuario=input("Introduzca la contraseña: ")

if contra==contra_usuario:
    print("La contraseña coincide")
else:
    print("La contraseña no coincide")

#9.Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
numero=int(input("Ingrese un numero: "))

if numero%2==0:
    print("El numero ingresado es par")
else:
    print("El numero ingresado es impar")

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

#11a.Realiza un programa que lea dos números por teclado y permite elegir entre 3 opciones en un menú:
#Mostrar una suma de los dos números
# Mostrar una resta de los dos números (el primero menos el segundo)
# Mostrar una multiplicación de los dos números
# En caso de introducir una opción inválida, el programa informará de que no es correcta.

print("Programa para operaciones numericas")
num1=float(input("Ingrese su primer numero:"))
num2=float(input("Ingrese su segundo numero:"))
while True:
    print("""Escribe una opcion 
            1)Suma
            2)Restar
            3)Multiplicar""")
    opcion=input()

    if opcion == '1':
        print(f"La suma de los numeros ingresados es {num1+num2}")       
    elif opcion == '2':
        print(f"La resta de los numeros ingresados es {num1-num2}")         
    elif opcion == '3':
        print(f"La multiplicacion de los numeros ingresados es {num1*num2}")    
    else:
        print("ingrese un opcion valida")

#11(b).Escribí un programa que solicite al usuario una letra y, si es una vocal, muestre el mensaje “Es
#vocal”. Verificar si el usuario ingresó un string de más de un carácter y, en ese caso, informarle
#que no se puede procesar el dato.

letra=str(input("Ingrese una letra: "))

if len(letra) != 1:
    print(" ERROR: Ingrese solo 1 letra") 
else:
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        print("Es vocal")

#12.Defina una lista de 5 estudiantes realice lo siguiente :
# -el tamaño de la lista.
# -el ultimo elemento.
# -Revierta los elementos.

lista=["Andrea","Fiorely","Alejandra","Paola","Leady"]
print(lista)
print (f"El tamaño de la lista es: {len(lista)}")
print (f"El ultimo elemento de la lista es: {lista[-1]}")
lista.reverse()
print (f"La lista revertida es:{lista}")

#13.) Defina un diccionario con una tupla y una lista de elementos, modifique el ultimo elemento.
diccionario = {
    "tupla": ([1,2,3,4,5])
}
diccionario['tupla'][-1] = 10
print(diccionario)

# 14.Realice un Menú interactivo que tenga las opciones de saludar ,una operación matemática y salir.

print("MENU INTERACTIVO")

while True:
    print("""Elige una opcion 
            1)Saludar
            2)Multiplicacion 
            3)Salir""")
    opcion=input()

    if opcion == '1':
        print("hola mundo")
        
    elif opcion == '2':
        print("Ingrese 2 numeros")
        n1=float(input("Primer numero : \n"))
        n2=float(input("Segundo numero : \n"))
        print(f"RESULTADO DE LA OPERACION MATEMATICA: \n {n1*n2}")    
    elif opcion == '3':
        break;
    else:
        print("ingrese un opcion valida")

# 15.iterar una lista de elementos que contengan nombre y edad e imprimir solo los mayores de edad.
#Nota : cada elemento de la lista puede ser otra lista [[nombre,edad],.... ]

list=[["Andrea",19],["Ana",15],["Luna",34],["Aurora",65]]

for elemento in list:
    if elemento[1]>=18:
        print("LAS SIGUIENTE PERSONA ES MAYOR DE EDAD:",)
        print(elemento[0])