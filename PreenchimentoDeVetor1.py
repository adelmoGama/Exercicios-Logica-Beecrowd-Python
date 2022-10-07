N: list = list(range(10))
X: int = int(input())
for i in range(len(N)):
    N[i] = X
    X *= 2
for i in range(len(N)):
    print(f"N[{i}] = {N[i]}")
