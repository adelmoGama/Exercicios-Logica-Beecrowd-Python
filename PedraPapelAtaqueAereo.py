N: int = int(input())
for i in range(N):
    escolha1 = str(input())
    escolha2 = str(input())
    if escolha1 == "ataque":
        if escolha2 == "ataque":
            print("Aniquilacao mutua")
        elif escolha2 == "pedra":
            print("Jogador 1 venceu")
        else:
            print("Jogador 1 venceu")
    elif escolha1 == "pedra":
        if escolha2 == "ataque":
            print("Jogador 2 venceu")
        elif escolha2 == "pedra":
            print("Sem ganhador")
        elif escolha2 == "papel":
            print("Jogador 1 venceu")
    elif escolha1 == "papel":
        if escolha2 == "ataque":
            print("Jogador 2 venceu")
        elif escolha2 == "pedra":
            print("Jogador 2 venceu")
        elif escolha2 == "papel":
            print("Ambos venceram")
