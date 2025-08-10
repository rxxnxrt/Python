#Solicita a idade do usuario. Se for menor que 5 anos deve aparecer a mensagem "idade a partir de 5 anos". 
#Se for entre 5 e 7 deve aparecer "Infantil", entre 8 e 10 deve #aparecer "Iniciar"
#se for entre 11 e 13 deve aparecer "Juvenil", entre 14 a 17 deve #aparecer "Junior"
#maiores de 18 deve aparecer "Senior"

idade = int(input("Digite a idade do atleta: "))

if idade < 5:
    print("Idade apartir de 5 anos!")
elif idade >= 5 and idade <= 7:
    print("Infantil!")
elif idade >= 8 and idade <= 10:
    print("Iniciado!")
elif idade >= 11 and idade <= 13:
    print("Juvenil!")
elif idade >= 14 and idade <= 17:
    print("Junior!")
else:
    print("Senior!")
