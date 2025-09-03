numero = int(input("Digite um número: "))
tot = 0
for numeros in range (1, numero + 1):
    if numero % numeros == 0:
        print("\033[34m", end=" ")
        tot += 1
    else:
        print(f'\033[31m', end="")
    print(f"{numeros}", end=" ")

print(f"\n\033[mO numero {numero} foi divisivel {tot}")
if tot == 2:
    print("Por isso ele é primo!")
else:
    print("Ele não é primo!")

