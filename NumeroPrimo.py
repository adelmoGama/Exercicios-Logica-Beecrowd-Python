N: int = int(input())
for i in range(N):
    X: int = int(input())
    soma: int = 0
    for k in range(1, X+1):
        if X % k == 0:
            soma += k
    if soma == (X+1):
        print(f"{X} eh primo")
    else:
        print(f"{X} nao eh primo")
