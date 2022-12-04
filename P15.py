# 15.iterar una lista de elementos que contengan nombre y edad e imprimir solo los mayores de edad.
#Nota : cada elemento de la lista puede ser otra lista [[nombre,edad],.... ]

list=[["Andrea",19],["Ana",15],["Luna",34],["Aurora",65]]

for elemento in list:
    if elemento[1]>=18:
        print("LAS SIGUIENTE PERSONA ES MAYOR DE EDAD:",)
        print(elemento[0])