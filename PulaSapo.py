P, N = input().split(" ")
P, N = int(P), int(N)
negativo: int = P * (-1)
alturas = input().split()
for i in range(1, N):
    diferenca: int = int(alturas[i]) - int(alturas[i-1])
    if diferenca > P:
        print("GAME OVER")
        break
    elif diferenca < negativo:
        print("GAME OVER")
        break
else:
    print("YOU WIN")
