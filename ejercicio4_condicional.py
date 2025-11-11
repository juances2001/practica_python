# Solicitar un número, y averiguar si es negativo, cero o positivo.
# Si es positivo, averiguar si es par o impar

num = int(input("Digite un num: "))

if num <0:
    print(f"Es negativo...")
elif num ==0:
    print("Es cero...")
else:
    print("Es positivo...")
    if num % 2 == 0:
        print("Es par...")
    else:
        print("Es impar...")
    