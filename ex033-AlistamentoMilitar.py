#Faça um programa que leia o ano de nascimento de um jovem e informe,
#de acordo com a sua idade se ele ainda vai se alistar ao serviço militar,
#se é a hora exata de se alistar
#ou se já passou do tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date

nascimento = int(input("Digite o ano de nascimento: "))
atual = date.today().year
idade = atual - nascimento
print(f"Quem nasceu em {nascimento} tem {idade} anos em {atual}. ")

if idade == 18:
    print(f"Faça o alistamento IMEDIATAMENTE!")
elif idade < 18:
    saldo = 18 - idade
    print(f"Ainda falta {saldo} anos!")
    ano = atual + saldo
    print(f"Seu alistamento será em {ano}")
else:
    saldo = idade - 18
    print(f"Você deveria ter se alistado há {saldo} anos!")
    ano = atual - saldo
    print(f"Seu alistamento foi em {ano}")