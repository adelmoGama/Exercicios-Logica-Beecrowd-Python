X, Y = input().split(" ")
X: int = int(X)
Y: int = int(Y)
while True:
    if X == Y:
        break
    if X < Y:
        print("Crescente")
    elif X > Y:
        print("Decrescente")
    X, Y = input().split(" ")
    X: int = int(X)
    Y: int = int(Y)
