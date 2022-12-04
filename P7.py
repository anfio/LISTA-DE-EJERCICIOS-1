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
