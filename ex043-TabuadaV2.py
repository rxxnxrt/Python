#Refaça o DESAFIO 9, mostrando a tabuada de um número que
# o usuário escolher, só que agora utilizando um laço for.

tabuada = int(input("Digite o número que deseja saber a tabuada: "))
print("-=" * 6)
print(f"Tabuada do {tabuada}")
print("-=" * 6)
for numero in range(1,11):
    print(f"{numero} x {tabuada} = {numero*tabuada}")

print("-=" * 6)