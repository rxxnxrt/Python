r1 = float(input("R1: "))
r2 = float(input("R2: "))
r3 = float(input("R3: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos podem formar um triangulo!")
    if r1 == r2 == r3:
        print("EQUILATERO")
    elif r1 != r2 != r3 != r1:
        print("ESCALENO")
    else
        print("ISÓCELES")
else:
    print("Os segmentos não podem formar um triangulo!")

