#Crie um programa que leia o ano de nascimento de sete pessoas
#No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date

atual = date.today().year
cont_maior = 0
cont_menor = 0

for pessoa in range(1, 8):
    nasc = int(input("Digite o ano de nascimento: "))
    idade = atual - nasc

    if idade >= 18:
        cont_maior += 1
    else:
        cont_menor += 1

print(f"A quantidade de maiores de idade foi: {cont_maior}!")
print(f"A quantidade de menores de idade foi: {cont_menor}!")