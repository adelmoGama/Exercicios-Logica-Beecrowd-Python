X: int = int(input())
Y: int = int(input())
if X < Y:
    for i in range(X, Y):
        if(i % 5 == 2) or (i % 5 == 3):
            print(i)
elif Y < X:
    for i in range(Y, X):
        if(i % 5 == 2) or (i % 5 == 3):
            print(i)
