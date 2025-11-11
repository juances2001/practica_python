# Desarrolle un algoritmo que permita leer dos valores distintos, determinar cuál de los dos valores es el mayor y escribirlo (imprimirlo)

num1 = int(input("Digite un numero entero: "))
num2 = int(input("Digite un numero entero: "))

if num1 > num2:
    print(f"El mayor es el: {num1}")
else:
    print(f"El mayor es el: {num2}")