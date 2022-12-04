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