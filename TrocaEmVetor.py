N: list = list(range(20))
aux: int = 0
aux2: int = 1
for i in range(len(N)):
    N[i] = int(input())
for i in range(int(len(N)/2)):
    aux = N[i]
    N[i] = N[len(N) - aux2]
    N[len(N) - aux2] = aux
    aux2 += 1
for i in range(len(N)):
    print(f"N[{i}] = {N[i]}")
