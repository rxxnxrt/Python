#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
#Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.

from random import randint
numero_secreto = randint(1, 10)
contador = 0
acertou = False
print("Sou seu computador e acabei de pensar em um número entre 0 e 10\nSera que você consegue advinhar qual foi?")

while not acertou:
    palpite = int(input("Qual o seu palpite: "))
    contador += 1
    if palpite == numero_secreto:
        print(f"Parabens, você descobriu que o número secreto é {numero_secreto}")
        acertou = True
    else:
        if palpite > numero_secreto:
            print("O número que estou pensando é menor hihihi, tente novamente")
        if palpite < numero_secreto:
            print("O número que estou pensando é maior hihihi, tente novamente")


print(f"Você tentou {contador} vezes até acertar meu pensamento!")