#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input("Digite o valor da casa: "))
salario_comprador = float(input("Digite qual seu salário: "))
quantidade_parcela = int(input("Digite quantas parcelas: "))
prestacao = valor_casa / quantidade_parcela
emprestimo = salario_comprador * prestacao

if prestacao < salario_comprador * 0.30:
    print("Emprestimo foi aprovado")
else:
    print("Emprestimo nao foi aprovado")
