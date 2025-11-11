# Desarrolle un algoritmo que permita leer tres valores y almacenarlos en las variables A, B y C respectivamente. El algoritmo debe imprimir cual es el mayor y cual es el menor. Recuerde constatar que los tres valores introducidos por el teclado sean valores distintos. Presente un mensaje de alerta en caso de que se detecte la introducción de valores iguales.

A = int(input("Digite un numero: "))
B = int(input("Digite un numero: "))
C = int(input("Digite un numero: "))

if A == B or A == C or B == C:
    print(f"Error, valores repetidos")

else: 
    if A > B and A > C:
        mayor = A
    elif B > A and B > C:
        mayor = B
    else:
        mayor = C

    if A < B and A < C:
        menor = A
    elif B < A and B < C:
        menor = B
    else:
        menor = C

print(f"El menor es:{menor}")
print(f"El mayor es:{mayor}")