N: int = int(input())
for i in range(N):
    X, Y = input().split(" ")
    X: int = int(X)
    Y: int = int(Y)
    soma: int = 0
    if X < Y:
        for k in range(X+1, Y):
            if k % 2 != 0:
                soma += k
            else:
                soma += 0
        print(soma)
        soma = 0
    elif Y < X:
        for k in range(Y+1, X):
            if k % 2 != 0:
                soma += k
            else:
                soma += 0
        print(soma)
        soma = 0
    elif X == Y:
        soma = 0
        print(soma)
