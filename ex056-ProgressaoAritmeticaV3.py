#Melhore o DESAFIO 55, perguntando para o usuário se ele quer mostrar mais alguns termos.
#O programa encerrará quando ele disser que quer mostrar 0 termos.
print("    GERADOR DE PA")
print("-=" * 10)

primeiro_termo = int(input("Primeiro termo da PA: "))
razao = int(input("Razão da PA: "))
decimo = primeiro_termo + (10 - 1) * razao
termo = primeiro_termo
cont = 0
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        termo += razao
        cont += 1
        print(f"{termo} - ", end="")
    print("Acabou")
    mais = int(input("Quantos termos você quer mostrar a mais? "))
print(f"Progressão finalizada com {total} termos mostrados.")
