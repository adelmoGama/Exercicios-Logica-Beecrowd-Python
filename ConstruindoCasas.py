entrada = 1
while True:
    entrada = input().split(" ")
    if "0" in entrada:
        break
    A, B, C = entrada
    A, B, C = int(A), int(B), int(C)
    casa = A * B
    terreno = (casa * 100) / C
    terreno = terreno ** (1 / 2)
    print(int(terreno))
