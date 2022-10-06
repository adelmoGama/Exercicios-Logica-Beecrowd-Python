N: int = int(input())
for i in range(N):
    valor: int = int(input())
    if valor % 2 == 0:
        if valor > 0:
            print("EVEN POSITIVE")
        elif valor < 0:
            print("EVEN NEGATIVE")
        elif valor == 0:
            print("NULL")
    else:
        if valor > 0:
            print("ODD POSITIVE")
        elif valor == 0:
            print("NULL")
        else:
            print("ODD NEGATIVE")
