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