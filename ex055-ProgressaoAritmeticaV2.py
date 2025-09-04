#Refaça o DESAFIO 45, lendo o primeiro termo e a razão de uma PA,
#mostrando os 10 primeiros termos da progressão usando a estrutura while.

print("    GERADOR DE PA")
print("-=" * 10)

primeiro_termo = int(input("Primeiro termo da PA: "))
razao = int(input("Razão da PA: "))
decimo = primeiro_termo + (10 - 1) * razao
termo = primeiro_termo
cont = 0

while cont <= 10:
    termo += razao
    cont += 1
    print(f"{termo} - ", end="")

print("Acabou")