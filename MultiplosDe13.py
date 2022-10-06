X: int = int(input())
Y: int = int(input())
soma: int = 0
if X < Y:
    for i in range(X, Y+1):
        if i % 13 != 0:
            soma += i
    print(soma)
elif Y < X:
    for i in range(Y, X+1):
        if i % 13 != 0:
            soma += i
    print(soma)
