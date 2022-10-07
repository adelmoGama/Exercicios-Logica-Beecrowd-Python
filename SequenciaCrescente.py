while True:
    X: int = int(input())
    if X == 0:
        break
    for i in range(1, X+1):
        if i == X:
            print(i)
        else:
            print(f"{i}", end=" ")
