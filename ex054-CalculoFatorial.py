#Faça um programa que leia um número qualquer e mostre o seu fatorial.
#Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120
from math import factorial
n = int(input("Digite um número: "))
c = n
f = factorial(n)
print(f"Calculando {n}! = ")
while c > 0:
    print(f"{c}", end="")
    print(f" x " if c > 1 else " = ", end="")
    c -= 1

print(f"{f}")