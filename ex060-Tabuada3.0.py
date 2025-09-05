#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

soma = 0

print('=-=' * 3)
print('TABUADA')
print('=-=' * 3)
while True:
    n = int(input('Digite o número que deseja: '))
    if n < 0:
        break
    print('=-=' * 10)
    for cont in range(1, 11):
        print(f'{n} x {cont} = {n*cont}')
    print('=-=' * 10)
print("Programa tabuada encerrado.")



