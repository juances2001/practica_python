# condicional simple: if

tengo_hambre = input("Tiene hambre? S/N: ") in {'s','S'}

print(f"El usuario dijo: {tengo_hambre}")

if tengo_hambre == True:
    
    print("vamos al descanso...")

print("Fin del programa.")