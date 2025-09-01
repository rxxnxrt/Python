#– Até 9 anos: MIRIM
#– Até 14 anos: INFANTIL
#– Até 19 anos: JÚNIOR
#– Até 25 anos: SÊNIOR
#– Acima de 25 anos: MASTER


idade = int(input("Idade: "))
if idade <= 9:
    print("MIRIM")
elif idade > 9 and idade <= 14:
    print("INFANTIL")
elif idade > 14 and idade <= 19:
    print("JUNIOR")
elif idade > 19 and idade <= 25:
    print("SENIOR")
else:
    print("MASTER")