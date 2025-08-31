#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário
#escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

numero = int(input("Digite um número inteiro: "))
print("""Escolha uma das base de bases:
[1] Converter para BINARIO:
[2] Converter para OCTAL:
[2] Converter para HEXADECIMAL:""")
opcao = int(input("Sua opção: "))
if opcao == 1:
    print(f"{numero} convertido para BINARIO É igual a {bin(numero)} ")
elif opcao == 2:
    print(f"{numero} convertido para OCTAL é igual a {oct(numero)} ")
elif opcao == 3:
    print(f"{numero} convertido para HEXADECIMAL é igual a {hex(numero)} ")
else:
    print("Opção Invalida")