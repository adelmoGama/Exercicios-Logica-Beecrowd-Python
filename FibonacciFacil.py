N: int = int(input())
proximo: int = 0
anterior: int = 0
atual = 1
for i in range(1, N+1):
    if i == N:
        print(anterior)
    else:
        print(f"{anterior}", end=" ")
        prox = anterior + atual
        anterior = atual
        atual = prox
