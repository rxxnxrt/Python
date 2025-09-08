#Faça um programa que jogue par ou ímpar com o computador.
#O jogo só será interrompido quando o jogador perder,
#mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
import random

print('-=' * 15)
print('VAMOS JOGAR PAR OU IMPAR')
print('-=' * 15)

cont = 0


while True:
    valor = int(input('Digite um valor: '))
    numero_secreto = random.randint(0, 11)
    vt = valor + numero_secreto
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou impar? [P/I]: ')).strip().upper()[0]
    print(f'Voce jogou {valor} e o computador {numero_secreto}.Total de {vt} ', end='')
    print('deu PAR, ' if vt % 2 == 0 else 'deu IMPAR, ', end='')
    if tipo == 'P':
        if vt % 2 == 0:
            print('Voce venceu!')
            cont += 1
        else:
            print('Voce perdeu!')
            break
    elif tipo == 'I':
        if vt % 2 == 1:
            print('Voce venceu!')
        else:
            print('Voce perdeu!')
            break
    print('Vamos jogar novamente...')
    print('-=' * 15)
print('-=' * 15)
print(f'GAME OVER! Voce venceu {cont} vezes')
print('-=' * 15)
