#Elabore um programa que calcule o valor a ser pago por um produto,
#considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal
#– 3x ou mais no cartão: 20% de juros

valor = float(input("Digite o valor a ser pago pelo produto: "))
opcao = int(input(""""Escolha o método de pagamento!
[1]Dinheiro/cheque - PAGAMENTO A VISTA
[2]Cartão - PAGAMENTO A VISTA
[3]Cartão - PARCELADO EM 2X
[4]Cartão - PARCELADO EM 3X
"""))
if opcao == 1:
    total = valor * 0.90
    print(f"Você recebeu 10% de desconto, o valor total ficou {total:.2f}")
elif opcao ==2:
    total = valor * 0.95
    print(f"Você recebeu 5% de desconto, o valor total ficou {total:.2f}")
elif opcao == 3:
    print(f"O valor total da compra ficou {valor}")
else:
    total = valor + (valor * 0.20)
    print(f'Devido o juros da maquininha o valor ficou em {total:.2f}')
