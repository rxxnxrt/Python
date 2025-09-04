#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
#No final do programa, mostre: a média de idade do grupo,
#qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_velho = ""
totmulher20 = 0

for p in range(1, 5):
    print(f"----- {p}ª Pessoa -----" )
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo[M/F]: "))
    soma_idade += idade
    if p == 1 and sexo in "Mm":
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in "Mm" and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in "Ff" and idade < 20:
        totmulher20 += 1

media_idade = soma_idade / 4
print(f"A media da idade do grupo é {media_idade}")
print(f"O homem mais velho tem {maior_idade_homem} anos e seu nome é {nome_velho}")
print(f"A quantidade de mulheres com menos de 20 anos é: {totmulher20}")


