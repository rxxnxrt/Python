#Escreva um programa que verifique se uma palavra ou frase digitada pelo usuário é um palíndromo.
#Um palíndromo é uma palavra ou frase que se lê da mesma forma de trás para frente

texto = input("Digite uma palavra ou frase: ")
texto_limpo = texto.replace(" ", "").lower()
texto_invertido = texto_limpo[::-1]

print(f"O inverso de {texto_limpo} é {texto_invertido}")

if texto_limpo == texto_invertido:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")