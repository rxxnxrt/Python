#Desenvolva um programa que leia seis números inteiros
#e mostre a soma apenas daqueles que forem pares.
#Se o valor digitado for ímpar, desconsidere-o.
soma = 0
contador = 0

for n in range(1,7):
    numero = int(input(f"Digite o {n} valor: "))
    if numero % 2 == 0:
        soma += numero
        contador += 1

print(f"Você informou {contador} números pares e a soma foi {soma}")