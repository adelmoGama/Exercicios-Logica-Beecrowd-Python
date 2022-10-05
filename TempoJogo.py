# ENTRADA:
inicio, fim = input().split(" ")
inicio: int = int(inicio)
fim: int = int(fim)
# PROCESSAMENTO:
if fim > inicio:
    print(f"O JOGO DUROU {fim - inicio} HORA(S)")
elif fim == inicio:
    print(f"O JOGO DUROU 24 HORA(S)")
else:
    print(f"O JOGO DUROU {24 + (fim - inicio)} HORA(S)")

