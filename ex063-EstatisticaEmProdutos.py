#Crie um programa que leia o nome e o preço de vários produtos.
#O programa deverá perguntar se o usuário vai continuar ou não.
#No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.
tot = cont = soma = 0
barato = ''

while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço do produto: '))
    cont += 1
    soma += preco
    if preco > 1000:
        tot += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = nome
    else:
        if preco < menor:
            menor = preco
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]

    if continuar == 'N':
        break

print(f'O valor total gasto foi {soma:.2f}')
print(f'{tot} produtos custam mais de R$ 1000.00')
print(f'O produto de menor valor gasto foi com o produto: {barato}')