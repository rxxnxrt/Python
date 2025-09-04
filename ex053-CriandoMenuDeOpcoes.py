#Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

while True:
    print("""    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [6] Menor
    [5] Sair do programa""")
    opcao = int(input(">>>> Qual é a sua opção: "))
    if opcao == 1:
        soma = valor1 + valor2
        print(f"O resultado de {valor1} + {valor2} é {soma}")
    elif opcao == 2:
        multiplicacao = valor1 * valor2
        print(f"O resultado de {valor1} x {valor2} é {multiplicacao}")
    elif opcao == 3:
        maior = max(valor1, valor2)
        print(f"O maior valor entre {valor1} e {valor2} é {maior}")
    elif opcao == 4:
        print("Digite os novos números.")
        valor1 = int(input("Digite o primeiro valor: "))
        valor2 = int(input("Digite o segundo valor: "))
    elif opcao == 5:
        print("Saindo do programa...")
        sleep(1)
        break
    elif opcao == 6:
        menor = min(valor1, valor2)
        print(f"O menor valor entre {valor1} e {valor2} é {menor}")
    else:
        print("Opção invalida, tente novamente")
    print("-=" * 15)