#Crie um programa que leia vários números inteiros pelo teclado.
#No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
#O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
resp = 'S'
cont = soma = media = maior = menor = 0

while True:
    n = int(input('Digite um número: '))
    cont += 1
    soma += n
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

    while resp not in 'SsNn':
        print('Opção Invalida, digite novamente.')
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

    if resp == 'N':
        break

media = soma / cont
print(f'A soma foi {soma} a média foi {media} o maior valor foi {maior} e o menor foi {menor}')


