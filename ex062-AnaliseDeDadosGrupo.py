#Crie um programa que leia a idade e o sexo de várias pessoas.
#A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
#No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados
#C) quantas mulheres tem menos de 20 anos.
print('-=' * 10)
print('CADASTRE UMA PESSOA')
print('-=' * 10)

maior = homi = muie = 0

while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        homi += 1
    if sexo == 'F' and idade < 20:
        muie += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'{maior} pessoas com mais de 18 anos cadastrados.')
print(f'{homi} homens cadastrados')
print(f'{muie} mulheres com menos de 20 anos cadastrados.')