N: int = int(input())
X: int
for i in range(N):
    X: int = int(input())
    soma: int = 0
    for k in range(1, X):
        if X % k == 0:
            soma += k
    if soma == X:
        print(f"{X} eh perfeito")
    else:
        print(f"{X} nao eh perfeito")
