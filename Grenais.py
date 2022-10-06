jogos: int = 0
vitoriaInter: int = 0
vitoriaGremio: int = 0
empates: int = 0
opcao: int = 1
while opcao == 1:
    golI, golG = input().split(" ")
    golI: int = int(golI)
    golG: int = int(golG)
    if golI > golG:
        vitoriaInter += 1
        jogos += 1
    elif golG > golI:
        vitoriaGremio += 1
        jogos += 1
    elif golI == golG:
        empates += 1
        jogos += 1
    print("Novo grenal (1-sim 2-nao)")
    opcao = int(input())
    while(opcao != 1) and (opcao != 2):
        print("Novo grenal (1-sim 2-nao)")
        opcao = int(input())
    if opcao == 2:
        break
print(f"{jogos} grenais")
print(f"Inter:{vitoriaInter}")
print(f"Gremio:{vitoriaGremio}")
print(f"Empates:{empates}")
if vitoriaInter > vitoriaGremio:
    print("Inter venceu mais")
elif vitoriaGremio > vitoriaInter:
    print("Gremio venceu mais")
