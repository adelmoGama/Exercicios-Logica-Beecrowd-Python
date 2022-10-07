T: int = int(input())
for i in range(T):
    PA, PB, G1, G2 = input().split(" ")
    PA, PB = int(PA), int(PB)
    G1, G2 = float(G1), float(G2)
    ano = 0
    while True:
        if PA > PB:
            break
        else:
            PA += PA * (G1//100)
            PB += PB * (G2//100)
            ano += 1
    if ano > 100:
        print("Mais de 1 seculo.")
    else:
        print("%d anos." % ano)
