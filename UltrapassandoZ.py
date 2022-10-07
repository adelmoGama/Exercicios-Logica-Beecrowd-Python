X: int = int(input())
Z: int = int(input())
cont: int = 0
soma: int = 0
while Z <= X:
    Z = int(input())
while soma < Z:
    soma += X
    cont += 1
    X += 1
print(cont)
