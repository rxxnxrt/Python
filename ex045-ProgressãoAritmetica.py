#Desenvolva um programa que leia o primeiro termo
#e a razão de uma PA.
#No final, mostre os 10 primeiros termos dessa progressão.

primeiro_termo = int(input("Primeiro termo da PA: "))
razao = int(input("Razão da PA: "))
decimo = primeiro_termo + (10 - 1) * razao
for numero in range(primeiro_termo, decimo + razao  , razao):
    print(numero, end=" ")

print("Acabou")