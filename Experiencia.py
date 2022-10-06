N: int = int(input())
sapos: int = 0
ratos: int = 0
coelhos: int = 0
total: int = 0
for i in range(N):
    quantidade, tipo = input().upper().split(" ")
    quantidade: int = int(quantidade)
    tipo: str = str(tipo)
    if tipo == "S":
        sapos += quantidade
        total += quantidade
    elif tipo == "R":
        ratos += quantidade
        total += quantidade
    elif tipo == "C":
        coelhos += quantidade
        total += quantidade
Pcoelhos: float = float(coelhos/total) * 100
Pratos: float = float(ratos/total) * 100
Psapos: float = float(sapos/total) * 100
print(f"Total: {total} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print("Percentual de coelhos: %.2f" % Pcoelhos, "%")
print("Percentual de ratos: %.2f" % Pratos, "%")
print("Percentual de sapos: %.2f" % Psapos, "%")
