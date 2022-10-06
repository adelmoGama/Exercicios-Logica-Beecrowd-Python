N: int = int(input())
for i in range(N):
    X, Y = input().split(" ")
    X: int = int(X)
    Y: int = int(Y)
    if Y != 0:
        divisao: float = float(X / Y)
        print("%.1f" % divisao)
    else:
        print("divisao impossivel")
