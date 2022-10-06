X, Y = input().split(" ")
X: int = int(X)
Y: int = int(Y)
while True:
    if(X == 0) or (Y == 0):
        break
    if(X > 0) and (Y > 0):
        print("primeiro")
    elif(X > 0) and (Y < 0):
        print("quarto")
    elif(X < 0) and (Y > 0):
        print("segundo")
    elif(X < 0) and (Y < 0):
        print("terceiro")
    X, Y = input().split(" ")
    X: int = int(X)
    Y: int = int(Y)
