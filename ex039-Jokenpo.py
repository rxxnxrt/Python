from random import randint
from time import sleep

itens = ("pedra", "papel", "tesoura")
computador = randint(0, 2)
print("""SUAS OPCÔES SÃO:
[0] PEDRA
[1] PAPEL
[2] TESOURA
""")

jogador = int(input("Qual a sua jogada?"))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")
sleep(1)
print("-=" * 11)
print(f"O computador jogou {itens[computador]}")
print(f"O jogador jogou {itens[jogador]}")
print("-=" * 11)
if computador == 0:#COMPUTADOR PEDRA
    if jogador == 0:
        print("EMPATE")
    elif jogador == 1:
        print("JOGADOR VENCE")
    elif jogador == 2:
        print("COMPUTADOR VENCE")
    else:
        print("JOGADA INVALIDA!")
elif computador == 1: #COMPUTADOR PAPEL
    if jogador == 0:
        print("COMPUTADOR VENCE")
    elif jogador == 1:
        print("EMPATE")
    elif jogador == 2:
        print("JOGADOR VENCE")
    else:
        print("JOGADA INVALIDA!")
elif computador == 2: #COMPUTADOR TESOURA
    if jogador == 0:
        print("JOGADOR VENCE")
    elif jogador == 1:
        print("COMPUTADOR VENCE")
    elif jogador == 2:
        print("EMPATE")
    else:
        print("JOGADA INVALIDA!")