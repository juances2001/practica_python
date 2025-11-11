# if - else

tengo_hambre = input("Tiene hambre? S/N: ") in {'s','S'}

print(f"El usuario dijo: {tengo_hambre}")

if tengo_hambre == True:
    print("vamos al descanso...")
else: 
    print("Seguimos en clase...")

print("Fin del programa.")